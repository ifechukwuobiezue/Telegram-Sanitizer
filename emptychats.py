from telethon.sync import TelegramClient
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.types import MessageService
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
        # Fetch the first 5 messages (to avoid rate limits and for efficiency)
        messages = list(client.iter_messages(dialog.entity, limit=5))
        if not messages:
            # No messages at all
            should_delete = True
        else:
            # Only delete if all messages are MessageService (system messages)
            should_delete = all(isinstance(m, MessageService) for m in messages)
        if should_delete:
            try:
                print(f"Deleting empty/system-only chat: {dialog.name}")
                client(DeleteHistoryRequest(peer=dialog.entity, max_id=0, revoke=True))
                deleted_count += 1
            except Exception as e:
                print(f"Failed to delete chat {dialog.name}: {e}")

    print(f"\n✅ Done. Deleted {deleted_count} empty/system-only chats.")

# Instructions for users:
# 1. Create a file named .env in the same directory as this script.
# 2. Add the following lines to your .env file (replace with your own values):
#    API_ID=your_api_id
#    API_HASH=your_api_hash
