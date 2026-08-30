import os
import sys
import platform
import requests

try:
    from lunoia_core import LunoiaBrain
except ImportError:
    print("\033[91m[CRITICAL] lunoia_core.py not found.\033[0m")
    sys.exit(1)

class LunoiaCLI:
    def __init__(self):
        self.brain = LunoiaBrain()
        self.os_name = platform.system()
        self.user = os.getenv('USER') or os.getenv('USERNAME') or 'user'
        self.noia_url = "http://localhost:8765/hook" # Alamat .noia hook

    def print_banner(self):
        print("\033[92m  EsotericArtificial | Lunoia v0.1-alpha\033[0m")
        print("  Status: \033[93mEXPERIMENTAL\033[0m | Hybrid (Online/Offline)")
        print(f"  OS: {self.os_name} | User: {self.user}\n")

    def search_online(self, query):
        """Manggil .noia hook buat ngesearch di browser"""
        print("  \033[93m[ONLINE] Connecting to .noia browser hook...\033[0m")
        try:
            payload = {"url": f"https://duckduckgo.com/html/?q={query}"}
            res = requests.post(self.noia_url, json=payload, timeout=15)
            
            if res.status_code == 200:
                data = res.json().get("data")
                return f"Web Result:\n{data[:500]}..."
            else:
                return "[ERROR] .noia hook returned an error."
        except requests.exceptions.ConnectionError:
            return "\033[91m[OFFLINE FALLBACK]\033[0m .noia hook is not running. Using local brain."
        except Exception as e:
            return f"[ERROR] {e}"

    def run(self):
        self.print_banner()
        print("  Type '/search [query]' to browse the web.")
        print("  Type anything else to chat with local brain.\n")
        
        while True:
            try:
                user_input = input(f"\033[94m{self.user}@lunoia:~$\033[0m ")
                if not user_input.strip(): continue
                
                cmd = user_input.lower().strip()
                
                if cmd in ['exit', 'quit', 'q']:
                    print("  Goodbye.\n"); break
                elif cmd == 'clear':
                    os.system('cls' if self.os_name == 'Windows' else 'clear')
                    self.print_banner(); continue
                
                elif cmd.startswith('/search ') or cmd.startswith('/online '):
                    query = user_input.split(' ', 1)[1]
                    result = self.search_online(query)
                    print(f"\n  \033[96mLunoia (Web):\033[0m {result}\n")
                    continue

                else:
                    response = self.brain.process_command(user_input)
                    print(f"\n  \033[92mLunoia (Local):\033[0m {response}\n")

            except KeyboardInterrupt:
                print("\n  Shutting down...\n"); break
            except Exception as e:
                print(f"  \033[91m[ERROR]\033[0m {e}\n")

if __name__ == "__main__":
    app = LunoiaCLI()
    app.run()
