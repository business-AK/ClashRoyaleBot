# ClashRoyaleBot

A Python bot that automates Clash Royale gameplay on BlueStacks.

## Features
- Automatically launches Clash Royale in BlueStacks
- Starts battles and plays cards without manual input
- Randomized card positions and drop locations for more natural gameplay
- Detects battle state by checking the elixir bar brightness (disappears when battle ends)
- Stops automatically once the battle is over

## Requirements
- Python 3.x
- PyAutoGUI
- NumPy
- BlueStacks installed with Clash Royale

## Usage
1. Clone this repository:
   git clone https://github.com/your-username/ClashRoyaleBot.git
   cd ClashRoyaleBot

2. Install required packages:
   pip install pyautogui numpy

3. Adjust coordinates in bot.py (card positions, arena bounds, and elixir region) if your BlueStacks window resolution differs.

4. Run the bot:
   python bot.py

The bot will launch Clash Royale, start a battle, drop cards every few seconds, and automatically stop once the game is over.
