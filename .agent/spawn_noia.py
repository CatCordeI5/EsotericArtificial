import json
import os

class SpawnNoia:
    def __init__(self):
        base = os.path.dirname(__file__)
        self.roles_file = os.path.join(base, "roles.json")
        self.roles = self._load_roles()
        self.active_agents = []

    def _load_roles(self):
        try:
            with open(self.roles_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def spawn(self, role, task, lang="en"):
        role = role.lower()
        
        if role not in self.roles:
            if lang == "id":
                return f"[SARANG] Peran '{role}' gak ada. Coba: {', '.join(self.roles.keys())}"
            return f"[HIVE] Role '{role}' not found. Try: {', '.join(self.roles.keys())}"

        info = self.roles[role]
        name = info.get(f"name_{lang}", role)
        focus = info.get(f"focus_{lang}", "")

        self.active_agents.append({
            "role": role, "task": task, "lang": lang
        })

        if lang == "id":
            return f"\033[95m[SARANG]\033[0m {name}-noia lahir! Fokus: {focus}. Tugas: {task}"
        return f"\033[95m[HIVE]\033[0m {name}-noia spawned! Focus: {focus}. Task: {task}"
