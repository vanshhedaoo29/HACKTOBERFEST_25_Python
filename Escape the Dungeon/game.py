from inputimeout import inputimeout, TimeoutOccurred

def start_game():
    """Starts the 'Escape the Dungeon' game."""
    print("🧙 Welcome to 'Escape the Dungeon'!")
    print("You wake up in a dark dungeon. There are two doors: one to your LEFT and one to your RIGHT.")

    try:
        # Ask for input with a 5-second timeout.
        choice1 = inputimeout(prompt="Which door do you choose? (left/right): ", timeout=5).lower()
    except TimeoutOccurred:
        # If the timer runs out, treat it as no input.
        choice1 = ""

    if choice1 == "left":
        left_room()
    elif choice1 == "right":
        right_room()
    else:
        print("😵 You stand still too long... a trapdoor opens beneath you. Game Over.")

def left_room():
    """The room to the left."""
    print("\nYou enter a room filled with treasure! 💰 But there's a sleeping dragon. 🐉")
    
    try:
        choice = inputimeout(prompt="Do you try to STEAL the treasure or SNEAK past the dragon? (steal/sneak): ", timeout=5).lower()
    except TimeoutOccurred:
        choice = ""

    if choice == "steal":
        print("🔥 The dragon wakes up and burns you to ashes. Game Over.")
    elif choice == "sneak":
        print("😮‍💨 You sneak past the dragon and find a ladder leading out. You escaped! 🎉")
    else:
        print("❓ You hesitate and the dragon wakes up. Game Over.")

def right_room():
    """The room to the right."""
    print("\nYou enter a dark hallway with two things: a SWORD and a SHIELD.")
    
    try:
        choice = inputimeout(prompt="Which do you take? (sword/shield): ", timeout=5).lower()
    except TimeoutOccurred:
        choice = ""

    if choice == "sword":
        print("⚔️ You bravely walk forward but run into a heavily-armored guard. Your sword is useless. Game Over.")
    elif choice == "shield":
        print("🛡️ You block the guard's attack and run past him. There's a trapdoor. You open it and escape! 🎉")
    else:
        print("⏳ You took too long to decide. The guard finds you. Game Over.")

if __name__ == "__main__":
    start_game()