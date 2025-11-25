import os
import json
import logging
import uuid
from datetime import datetime

class ConversationMemory:
    USER_ID = "Hamid_22"
    MESSAGE_PREFIX = "HD_"
    
    def __init__(self, user_id=None):
        self.user_id = user_id or self.USER_ID
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.conv_dir = os.path.join(self.base_dir, "conversations")
        self.memory_file = os.path.join(self.conv_dir, f"{self.user_id}_memory.json")
        os.makedirs(self.conv_dir, exist_ok=True)
        
        # Configure logging
        self.logger = logging.getLogger("memory_store")
    
    def save_conversation(self, conversation_data):
        try:
            # Convert existing message IDs to new format
            if isinstance(conversation_data, dict) and "messages" in conversation_data:
                for msg in conversation_data["messages"]:
                    if "id" in msg and msg["id"].startswith("GR_"):
                        new_id = f"{self.MESSAGE_PREFIX}{msg['id'][3:]}"
                        msg["id"] = new_id
            
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump(conversation_data, f, indent=2)
            
            self.logger.info(f"File saved at: {self.memory_file}")
            return True
        except Exception as e:
            self.logger.error(f"Error saving conversation: {e}")
            return False
    
    def generate_message_id(self):
        """Generate new message ID with HD_ prefix"""
        return f"{self.MESSAGE_PREFIX}{uuid.uuid4().hex[:12]}"

# Backward compatibility
MemoryStore = ConversationMemory