import os
import sys
import platform

try:
    from lunoia_core import LunoiaBrain
except ImportError:
    print("\033[91m[CRITICAL] lunoia_core.py not found. Ensure it's in the same directory.\033[0m")
    sys.exit(1)

class LunoiaCLI:
    def __init__(self):
        self.brain = LunoiaBrain()
        self.os_name = platform.system()
        self.user = os.getenv('USER') or os.getenv('USERNAME') or 'user'

    def print_banner(self):
        print("\033[92m  EsotericArtificial | Lunoia v0.1-alpha\033[0m")
        print("  Status: \033[93mEXPERIMENTAL\033[0m | 100% Local | Bilingual (EN/ID)")
        print(f"  OS: {self.os_name} | User: {self.user}\n")

    def run(self):
        self.print_banner()
        
        print("  Type 'help' or 'bantuan' for commands. Just chat!\n")
        
        while True:
            try:
                user_input = input(f"\033[94m{self.user}@lunoia:~$\033[0m ")
                
                if not user_input.strip():
                    continue
                
                cmd = user_input.lower().strip()
                
                if cmd in ['keluar', 'exit', 'quit', 'q']:
                    print("\n  Goodbye. / Sampai jumpa.\n")
                    break
                
                elif cmd in ['help', 'bantuan']:
                    print("""
  \033[96mCOMMANDS:\033[0m
    help / bantuan   - Show this menu
    clear            - Clear terminal
    about            - About EsoArtificial
    ajar [q] [a]     - Teach Lunoia (ID)
    teach [q] [a]    - Teach Lunoia (EN)
    exit             - Quit
                    """)
                    continue

                elif cmd in ['about', 'tentang']:
                    print("\n  \033[95mABOUT ESOTERIC ARTIFICIAL:\033[0m")
                    print("  - thanks to Corde.")
                    print("  - i hope Runs 100% locally. <512MB RAM.")
                    print("  - free and custom Model.\n")
                    continue

                elif cmd == 'clear':
                    os.system('cls' if self.os_name == 'Windows' else 'clear')
                    self.print_banner()
                    continue
                
                elif cmd.startswith('ajar ') or cmd.startswith('teach '):
                    print("  \033[93mLearning module processing... / Memproses...\033[0m\n")
                    continue

                # Default: Chat with AI
                else:
                    response = self.brain.process_command(user_input)
                    print(f"\n  \033[92mLunoia:\033[0m {response}\n")

            except KeyboardInterrupt:
                print("\n\n  Interrupt detected. Shutting down...\n")
                break
            except Exception as e:
                print(f"\n  \033[91m[ERROR]\033[0m {e}\n")

if __name__ == "__main__":
    app = LunoiaCLI()
    app.run()
