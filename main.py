import pyautogui
import time
from pynput import keyboard

# Define the list of coordinates and actions as dictionaries
coordinates = [
    {"x": 638, "y": 192, "action": "left"},
    {"x": 637, "y": 304, "action": "left"},
    {"x": 800, "y": 270, "action": "left", "double_click": True},
    {"x": 636, "y": 224, "action": "left"},
    {"x": 850, "y": 380, "action": "left"},
    {"x": 850, "y": 359, "action": "left"},
    {"x": 638, "y": 192, "action": "right"},
    {"x": 636, "y": 296, "action": "right"},
    {"x": 850, "y": 359, "action": "left"}
]

# Define a variable to keep track of whether automation is on or off
automation_on = False


# Function to toggle automation on and off
def toggle_automation():
    global automation_on
    automation_on = not automation_on


# Create a listener for the hotkey
hotkey_listener = keyboard.GlobalHotKeys({
    'o': toggle_automation
})

# Start listening for the hotkey
hotkey_listener.start()

print("Press the 'o' key to toggle automation on and off.")

# Loop through the coordinates and actions
while True:
    if automation_on:
        for coord in coordinates:
            x, y = coord["x"], coord["y"]
            action = coord["action"]

            # Click or right click
            if action == "left":
                pyautogui.click(x, y)
            elif action == "right":
                pyautogui.rightClick(x, y)

            # Double click if specified
            if "double_click" in coord and coord["double_click"]:
                pyautogui.click(x, y)

            # Wait for 0.1 seconds
            time.sleep(0.3)
    else:
        # Wait for 0.1 seconds before checking again
        time.sleep(0.1)
