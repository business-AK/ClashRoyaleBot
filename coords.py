import pyautogui
import numpy as np
import time
from PIL import Image

# Define a very small region where elixir number appears (adjust coords)
elixir_region = (1200, 950, 5, 5)  # (x, y, width, height)

def avg_brightness(region):
    screenshot = pyautogui.screenshot(region=region)
    img = np.array(screenshot)  # convert to numpy
    return img.mean()  # average pixel intensity

# First, capture baseline while in-game
baseline = avg_brightness(elixir_region)
print("Baseline brightness:", baseline)

while True:
    current = avg_brightness(elixir_region)
    print("Current:", current)
    
    if abs(current - baseline) > 50:  # threshold, tweak as needed
        print("⚠️ Battle likely ended!")
        break
    
    time.sleep(2)
