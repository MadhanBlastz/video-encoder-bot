import os
from pyrogram import Client
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')

# Directly set the API ID
api_id = 7211200915

# Print the API ID (or use it in your application)
print(f"API ID is: {api_id}")

api_hash = os.environ.get("79612bc71908f95372808520a7eeee74")
bot_token = os.environ.get("7211200915:AAHYmpFqwjyhvVqdXZzjQuBBn7HaJna1gfs")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = list(set(int(x) for x in os.environ.get("2021408974").split()))

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
