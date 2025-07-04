import time
import random
from actors import Hero, Opponent

def main():
    print_welcome()
    play_game()

def print_welcome():
     print("""
----------------------------------------------------------
---------- Welcome to the RPG: The Legend of PyLink -------
----------------------------------------------------------

A dark force has infected the servers of cyberspace.
You are the chosen one who must restore peace to the web.
Prepare to face the most annoying digital enemies ever...

Good luck, brave warrior!
""")
     
def play_game():
     opponents = [
          Opponent('Slow Wifi', 1),
          Opponent('Pop-up Ad', 3),
          Opponent('Infinite Captcha', 5),
          Opponent('Error 404', 7),
          Opponent('Blue Screen', 10),
          Opponent('Grumpy Virus', 15),
          Opponent('Forced Update', 20),
          Opponent('Terms & Conditions', 30)
     ]

     hero = Hero("Sir Python", 5)

     while opponents:
          current_opponent = random.choice(opponents)
          print(f"A wild {current_opponent.name} (Level {current_opponent.level}) appears!")

          cmd = input("What will you do? [a]ttack, [r]un, [l]ook around, [q]uit: ").lower()

          while cmd not in ['a', 'r', 'l', 'q']:
            cmd = input("Please enter a valid command [a/r/l/q]: ").lower()

          if cmd == 'a':
            if hero.attack(current_opponent):
                opponents.remove(current_opponent)
                print(f"{len(opponents)} opponents remaining.\n")
            else:
                print(f"{hero.name} needs a moment to recover...")
                time.sleep(3)
                print("Back online and ready to fight!\n")

          elif cmd == 'r':
            print("You ran away safely...\n")

          elif cmd == 'l':
            print("\n👁️ You scan the digital battlefield. Remaining threats:")
            for op in opponents:
                print(f" - {op}")
            print()

          elif cmd == 'q':
            print("\nThanks for playing! See you next time, digital hero.")
            break

     if not opponents:
        print("🎉 You’ve defeated all digital threats! The web is safe again. 🎉")

if __name__ == '__main__':
    main()