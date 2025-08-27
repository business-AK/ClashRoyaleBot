# ClashRoyaleBot

A Python bot that automates **Clash Royale** gameplay on **BlueStacks**.

## Features

- Launches Clash Royale automatically in BlueStacks  
- Starts battles and plays cards without manual input  
- Randomized card positions and drop locations for more natural gameplay  
- Detects battle status using on-screen templates (Victory, Defeat, or Time Left)  
- Plays continuously until the battle ends  

## Requirements

- Python 3.x  
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)  
- BlueStacks installed with Clash Royale  
- Screenshots of `timeLeft.png`, `victory.png`, and `defeat.png` for battle detection  

## Usage

1. Clone this repository:

git clone https://github.com/your-username/ClashRoyaleBot.git


2. Install required packages:

pip install pyautogui


3. Place the template images (timeLeft.png, victory.png, defeat.png) in the project folder.
4. Run the bot:

python bot.py

5. Done
(Note : Adjust the card coordinates and arena bounds in bot.py if your BlueStacks window has a different resolution.)