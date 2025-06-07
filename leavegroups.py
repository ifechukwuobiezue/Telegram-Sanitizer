from telethon.sync import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import DeleteChatUserRequest
from telethon.tl.types import Channel, Chat
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
        if dialog.is_group:
            try:
                print(f"Leaving group: {dialog.name}")
                if isinstance(dialog.entity, Channel):
                    # For supergroups and channels
                    client(LeaveChannelRequest(dialog.entity))
                elif isinstance(dialog.entity, Chat):
                    # For basic groups
                    client(DeleteChatUserRequest(dialog.entity.id, 'me'))
                else:
                    print(f"Unknown group type for {dialog.name}, skipping.")
                    continue
                left_count += 1
            except Exception as e:
                print(f"Failed to leave {dialog.name}: {e}")

    print(f"\n✅ Done. Left {left_count} groups.")
