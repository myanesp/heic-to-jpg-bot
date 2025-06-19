# HEIC to JPG Telegram Bot

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/myanesp/heic-to-jpg-bot)
[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://hub.docker.com/r/myanesp/heic-to-jpg-bot)
[![Docker Pulls](https://badgen.net/docker/pulls/myanesp/heic-to-jpg-bot?icon=docker&label=pulls)](https://hub.docker.com/r/myanesp/heic-to-jpg-bot)
![Last Commit](https://img.shields.io/github/last-commit/myanesp/heic-to-jpg-bot)
[![License](https://badgen.net/github/license/myanesp/heic-to-jpg-bot)](LICENSE)
[![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

## Why?

This Docker container runs a Telegram bot that automatically converts HEIC images (commonly used by iOS devices) sent to the bot into the widely supported JPG format. This is handy when you (or your family/friends) receive HEIC images on Telegram and want to easily get a JPG version for sharing, storing, or uploading elsewhere.

## Features

- ✅ Converts HEIC images sent to the bot into JPG format
- ✅ Sends the JPG version back to the user automatically
- ✅ Lightweight Docker image

## How to Run

### 1. Set up your Telegram bot

- Create a new bot using [@BotFather](https://t.me/BotFather)
- Note down your bot token
- Start a chat with your new bot

### 2. Run the container

The image is available on both [Docker Hub](https://hub.docker.com/r/myanesp/heic-to-jpg-bot) and GitHub Container Registry. Use whichever you prefer.

#### Run with Docker Compose

```yaml
services:
  heic-to-jpg-bot:
    image: ghcr.io/myanesp/heic-to-jpg-bot:latest # or myanesp/heic-to-jpg-bot
    container_name: heic-to-jpg-bot
    restart: unless-stopped
    environment:
      - TELEGRAM_BOT_TOKEN=your_telegram_bot_token
      - TZ=Europe/Madrid # optional
```

#### Run with Docker

```bash
docker run -d \
  --name heic-to-jpg-bot \
  --restart unless-stopped \
  -e TELEGRAM_BOT_TOKEN=your_telegram_bot_token \
  -e TZ=Europe/Madrid \
  ghcr.io/myanesp/heic-to-jpg-bot:latest # or myanesp/heic-to-jpg-bot
```

## Environment Variables

| VARIABLE           | MANDATORY | DESCRIPTION                                                         | DEFAULT          |
|--------------------|:---------:|---------------------------------------------------------------------|------------------|
| TELEGRAM_BOT_TOKEN |    ✅     | Your Telegram bot token from @BotFather                            | -                |
| TZ                 |    ❌     | Timezone (for logging, etc)                                        | UTC              |

## Planned Features

- [ ] Select other output formats (PNG, WEBP, etc)
- [ ] Multiarch support
- [ ] Allow batch/bulk conversion of multiple images
- [ ] Custom JPG quality settings
- [ ] Multilingual support
