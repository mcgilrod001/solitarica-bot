
# deletes screenshots in screenshot folder
def delete_screenshot():
    import os
    for file in os.listdir("solitarica-bot/images"):
        os.remove(f'solitarica-bot/images/{file}')

if __name__ == "__main__":
    delete_screenshot()