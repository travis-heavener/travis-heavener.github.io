#!/usr/bin/env bash
DOWNLOAD_URL=$(curl -s https://api.github.com/repos/ai-robots-txt/ai.robots.txt/releases/latest | grep -Po "(?<=\"browser_download_url\": \")(.*?)(?=\")")
curl -Ls "$DOWNLOAD_URL" > docs/robots.txt