import os
import time

# Constants
SCREEN_WIDTH = 80
TRAIN_WIDTH = len("""
   _______
  /        \\
 /          \\
|   _____  |
 _| |       |_
  | |       |
  | |_____  |
  |_________|
""")

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the train at a given position
def print_train(position):
    clear_screen()
    print(" " * position + """
   _______
  /        \\
 /          \\
|   _____  |
 _| |       |_
  | |       |
  | |_____  |
  |_________|
""")

# Simulate the train passing on the screen from left to right and back
for i in range(2):
    for position in range(SCREEN_WIDTH + TRAIN_WIDTH):
        print_train(position)
        time.sleep(0.1)
    for position in range(SCREEN_WIDTH + TRAIN_WIDTH - 1, -1, -1):
        print_train(position)
        time.sleep(0.1)
