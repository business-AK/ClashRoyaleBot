import subprocess
import time
import pyautogui
import pyscreeze 
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

#launch CR
def launchGame():
    subprocess.Popen(r'"C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance Pie64 --cmd launchApp --package com.supercell.clashroyale --source desktop_shortcut', shell=True)
    print("Launched the game")

#start battle
def startBattle():
    battle_x = 967
    battle_y=842
    pyautogui.click(battle_x, battle_y)
    print("Battle Started")
    time.sleep(1)
    last_check = time.time()

    while True:
        playCard()
        time.sleep(5)

        if (time.time() - last_check >= 30):
            if not inBattle():
                break
            last_check = time.time()

#check for battle in progress
def safeLocate(img, confidence=0.8):
    try:
        return pyautogui.locateOnScreen(img, confidence=confidence)
    except pyscreeze.ImageNotFoundException:
        return None

def inBattle():
    if safeLocate('victory.png') is not None:
        print("Battle ended: victory")
        return False
    if safeLocate('defeat.png') is not None:
        print("Battle ended: defeat")
        return False
    return True



#play game
def playCard():
    cardx, cardy = random.choice(cards)

    dropx = random.randint(arena_bounds["x_min"], arena_bounds["x_max"])
    dropy = random.randint(arena_bounds["y_min"], arena_bounds["y_max"])

    print("Playing card: ")
    pyautogui.moveTo(cardx, cardy, duration=0.2)
    pyautogui.dragTo(dropx, dropy, duration=0.5, button='left')

launchGame()
time.sleep(30)
startBattle()