import subprocess
import pyautogui
import time

game_dir = "C:\Program Files (x86)\ROKLauncher\ROK\MASS.exe"

client_process = "launcher.exe"
game_process = "MASS.exe"


def process_exists(process_name):
    call = 'tasklist', '/fi', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode(encoding='437')
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())


def start_harvesting():
    print("Rozpoczynanie zbierania.")
    time.sleep(2)
    pyautogui.click(1800, 1012), time.sleep(2), pyautogui.click(1800, 900), time.sleep(2),
    pyautogui.click(730, 1012), time.sleep(2),
    pyautogui.click(740, 853), time.sleep(2),
    pyautogui.click(933, 540), time.sleep(2),
    pyautogui.click(615, 680), time.sleep(1)
    pyautogui.click(1600, 330), time.sleep(1)
    pyautogui.click(1200, 830), time.sleep(1)
    pyautogui.click(1800, 1012),


def procex():
    if process_exists(game_process):
        return True
    else:
        return False


while True:
    if procex():
        print("proces istnieje")
        start_harvesting()
        time.sleep(3600)
    else:
        print("proces nieistnieje")
        time.sleep(480)
