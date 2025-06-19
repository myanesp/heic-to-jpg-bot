import os
import subprocess
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.getLogger("httpx").setLevel(logging.WARNING)

async def handle_heic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document
    filename = document.file_name

    if filename.lower().endswith(".heic"):
        logging.info(f"Received file: {filename}")
        file = await context.bot.get_file(document.file_id)

        base_name = os.path.splitext(filename)[0]
        output_filename = base_name + ".jpg"
        input_path = f"/tmp/{filename}"
        output_path = f"/tmp/{output_filename}"

        await update.message.reply_text(f"📥 Received `{filename}`, converting...", parse_mode="Markdown")
        await file.download_to_drive(input_path)
        logging.info(f"Downloaded to {input_path}")

        try:
            subprocess.run(["heif-convert", input_path, output_path], check=True)
            logging.info(f"Conversion successful: {output_filename}")

            with open(output_path, "rb") as jpg_file:
                await update.message.reply_document(document=jpg_file, filename=output_filename)
                await update.message.reply_text("✅ Conversion successful.")

        except subprocess.CalledProcessError as e:
            logging.error(f"Conversion failed: {e}")
            await update.message.reply_text("❌ Failed to convert HEIC to JPG.")

        finally:
            for f in [input_path, output_path]:
                if os.path.exists(f):
                    os.remove(f)
            logging.info("Cleaned up temp files.")

    else:
        logging.info(f"Ignored non-HEIC file: {filename}")
        await update.message.reply_text("❌ Failed to convert. That's not a HEIC file.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.Document.ALL, handle_heic))
    logging.info("Bot is running...")
    app.run_polling()