import pyautogui
import time

print("Move your mouse over a spot in the game window...")
time.sleep(3)

while True:
    x, y = pyautogui.position()
    print(f"X: {x}, Y: {y}", end="\r")  # overwrite same line
    time.sleep(0.1)
