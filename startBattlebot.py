import time
import numpy as np
import pyautogui
import random


cards = [
    (840, 950),  # card1
    (950, 950),  # card2
    (1080, 950), # card3
    (1180, 950)  # card4
]

arena_bounds = {
    "x_min": 720,
    "x_max": 1200,
    "y_min": 490,
    "y_max": 790
}

elixer_avg_value = 171.56
elixir_region = (795, 1055, 5, 5)

#start battle
def startBattle():
    battle_x = 967
    battle_y=842
    pyautogui.click(battle_x, battle_y)
    time.sleep(7)
    print("Battle Started")
    last_check = time.time()

    while True:
        playCard()
        time.sleep(5)

        if (time.time() - last_check >= 10):
            if not inBattle():
                print("Battle ended")
                break
            last_check = time.time()

#check for battle in progress
def avg_brightness(region):
    screenshot = pyautogui.screenshot(region=region)
    img = np.array(screenshot)  # convert to numpy
    return img.mean()  # average pixel intensity

def inBattle():
    val = avg_brightness(elixir_region)
    if val >= 170 and val <= 175:
        return True
    else :
        return False



#play game
def playCard():
    cardx, cardy = random.choice(cards)

    dropx = random.randint(arena_bounds["x_min"], arena_bounds["x_max"])
    dropy = random.randint(arena_bounds["y_min"], arena_bounds["y_max"])

    print("Playing card: ")
    pyautogui.moveTo(cardx, cardy, duration=0.2)
    pyautogui.dragTo(dropx, dropy, duration=0.5, button='left')

time.sleep(3)
startBattle()