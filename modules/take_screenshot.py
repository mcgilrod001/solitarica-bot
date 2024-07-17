# takes screenshot and saves it in screenshot folder
def screenshot():
    import pyautogui
    screenshot = pyautogui.screenshot('screenshot.png')
    screenshot.save('solitarica-bot/images/screenshot.png')
    
if __name__ == "__main__":
    screenshot()