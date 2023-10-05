import pyautogui
import time
import random


time.sleep(5)


numberOfVideos = 100
hamburgerbutton = 1859, 290
removeWL = 1762,402


def randomFloat():
    return random.uniform(0.7, 2)


for i in range(numberOfVideos):
    x = randomFloat()
    
    pyautogui.moveTo(hamburgerbutton)
    pyautogui.click()

    time.sleep(x)

    pyautogui.moveTo(removeWL)
    pyautogui.click()

    time.sleep(x)