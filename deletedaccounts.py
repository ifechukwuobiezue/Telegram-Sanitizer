from telethon.sync import TelegramClient
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.types import User
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

with TelegramClient('session_name', api_id, api_hash) as client:
    deleted_count = 0

    for dialog in client.iter_dialogs():
        entity = dialog.entity
        # Check if the dialog is a deleted user
        if isinstance(entity, User) and entity.deleted:
            try:
                print(f"Deleting chat with deleted account: {dialog.name}")
                client(DeleteHistoryRequest(peer=entity, max_id=0, revoke=True))
                deleted_count += 1
            except Exception as e:
                print(f"Failed to delete chat with {dialog.name}: {e}")

    print(f"\n✅ Done. Deleted {deleted_count} deleted account chats.")
