import os
from pyrogram import Client
from dotenv import load_dotenv

# Load environment variables from a file if it exists
if os.path.exists('config.env'):
    load_dotenv('config.env')

# Directly set the API ID
api_id = 7211200915

# Directly set the API Hash and Bot Token
api_hash = "79612bc71908f95372808520a7eeee74"
bot_token = "7211200915:AAHYmpFqwjyhvVqdXZzjQuBBn7HaJna1gfs"

# Default download directory
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")

# Retrieve the environment variable for sudo users
env_var = os.environ.get("SUDO_USERS")

# Check if the environment variable is set and not None
if env_var is None:
    # Provide a default value or handle the missing variable case
    env_var = ""  # Or you could set a default list of users, e.g., "1 2 3"

# Process the environment variable
try:
    sudo_users = list(set(int(x) for x in env_var.split() if x))
except ValueError as e:
    raise ValueError(f"Error processing environment variable 'SUDO_USERS': {e}")

# Example usage
print(f"Sudo users: {sudo_users}")

# Initialize the Pyrogram Client
app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Ensure download directory exists
if not download_dir.endswith("/"):
    download_dir += "/"
if not os.path.isdir(download_dir):
    os.makedirs(download_dir)
