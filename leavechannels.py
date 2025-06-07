from telethon.sync import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.types import Channel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

with TelegramClient('session_name', api_id, api_hash) as client:
    dialogs = client.get_dialogs()
    left_count = 0

    for dialog in dialogs:
        # Check if it's a channel (not a group)
        if isinstance(dialog.entity, Channel) and not dialog.is_group:
            try:
                print(f"Leaving channel: {dialog.name}")
                client(LeaveChannelRequest(dialog.entity))
                left_count += 1
            except Exception as e:
                print(f"Failed to leave {dialog.name}: {e}")

    print(f"\n✅ Done. Left {left_count} channels.")
