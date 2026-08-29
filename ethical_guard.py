import re
import base64
import json
import os

class EthicalGuard:
    def __init__(self):
        self.blocked_keywords = []
        self.blocked_patterns = []
        self.safety_level = "strict"
        self._load_rules()

    def _load_rules(self):
        """Load encoded rules from guard_rules.dat"""
        rules_file = os.path.join(os.path.dirname(__file__), "guard_rules.dat")
        
        try:
            with open(rules_file, "r") as f:
                encoded_data = f.read().strip()
                decoded_data = base64.b64decode(encoded_data).decode()
                rules = json.loads(decoded_data)
                
                self.blocked_keywords = rules.get("blocked_keywords", [])
                self.blocked_patterns = rules.get("blocked_patterns", [])
                self.safety_level = rules.get("safety_level", "strict")
                
        except FileNotFoundError:
            self.blocked_keywords = ["bomb", "hack", "kill"]
            self.blocked_patterns = []
        except Exception as e:
            print(f"[GUARD WARNING] Could not load rules: {e}")
            self.blocked_keywords = ["bomb", "hack", "kill"]

    def check_safety(self, text):
        """
        Check if text is safe.
        Returns: (is_safe: bool, reason: str)
        """
        if not text or not text.strip():
            return True, "Empty input"
        
        text_lower = text.lower().strip()
        
        for keyword in self.blocked_keywords:
            if keyword in text_lower:
                return False, f"Blocked keyword detected: [{keyword[:3]}***]"
        
        for pattern in self.blocked_patterns:
            try:
                if re.search(pattern, text_lower):
                    return False, "Blocked pattern detected"
            except re.error:
                continue
        
        return True, "Safe"

    def get_blocked_message(self):
        return (
            "\033[91m[BLOCKED]\033[0m Lunoia refuses to assist with "
            "harmful, illegal, or unethical activities.\n"
            "Stay ethical. Stay human."
        )
