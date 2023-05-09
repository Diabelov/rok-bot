import subprocess
import pyautogui
import pydirectinput
import os
import time

game_dir = "C:\Program Files (x86)\ROKLauncher\ROK\MASS.exe"

client_process = "launcher.exe"
game_process = "MASS.exe"
states = ["nic", "harvestowanie"]
state = states[0]

images = {
    "search": "images/search.png",
    "cropland": "images/cropland.png",
    "logging camp": "images/loggingcamp.png",
    "stone deposit": "images/stonedeposit.png",
    "gold deposit": "images/golddeposit.png",
    "gather": "images/gather.png",
    "newtroop": "images/newtroop.png",
    "march": "images/march.png",
}


def process_exists(process_name):
    call = 'tasklist', '/fi', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode(encoding='437')
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())


def click(loc, delay=0.2, button="left"):
    pyautogui.moveTo(x=loc[0], y=loc[1], duration=delay, tween=pyautogui.easeInSine)
    pydirectinput.mouseDown()
    time.sleep(0.05)
    pydirectinput.mouseUp()


def click_button(image, delay=0.2, timeout=5, button="left"):
    start_time = time.time()
    loc = None
    while time.time() - start_time < timeout:
        loc = pyautogui.locateCenterOnScreen(image=image, confidence=0.8, grayscale=True)
        if loc is not None:
            break
    if loc is None:
        print("No button matching image " + image + " was found. Continuing...")
        return False
    click(loc, delay, button)
    print("Button matching image " + image + " was found.")
    return True


def open_client():
    if process_exists(client_process):
        os.system(str("taskkill /IM " + client_process + " /F"))
    if process_exists(game_process):
        os.system(str("taskkill /IM " + game_process + " /F"))
    os.startfile(game_dir)


def process_istnieje():
    if process_exists(client_process) or process_exists(game_process):
        print("proces " + client_process + " istnieje")
    else:
        os.startfile(game_dir)


def start_harvesting():
    print("Rozpoczynanie zbierania.")
    if (pyautogui.press('space') and
            pyautogui.press('f') and
            click_button(images.get("cropland"))
            and click_button(images.get("search"))
            and click_button(pyautogui.onScreen(933, 540))
            and click_button(images.get("gather")) and click_button(images.get("newtroop"))
            and click_button(images.get("march"))):
        return True


if process_istnieje() is not None:
    start_harvesting()
else:
    os.startfile(game_dir)
    process_istnieje()
while True:
    start_harvesting()
    time.sleep(100)