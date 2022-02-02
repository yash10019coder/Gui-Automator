import pyautogui
import time
import random


def clickImage(image):
    x, y = pyautogui.locateCenterOnScreen(image)
    pyautogui.click(x, y)


def downloadAssingment():
    time.sleep(.1)
    clickImage('options_menu_google_drive.png')
    pyautogui.press('up')
    pyautogui.press('enter')
    time.sleep(25)
    clickImage('save_button_nautilus.png')


def randomlySelectAssignmetsAndDownloadThem(count):
    for i in range(count):
        pyautogui.keyDown('ctrl')
        for j in range(random.randint(1, 5)):
            pyautogui.press('right')
        pyautogui.press('space')
        pyautogui.keyUp('ctrl')
    downloadAssingment()


def main():
    assignmentLink = 'https://drive.google.com/drive/u/1/folders/1VlkehHj-3pM1dxEURCJnutve27tblrxz'

    pyautogui.hotkey('alt', '1')
    time.sleep(.5)
    # opening the link in a new tab
    clickImage('new_tab_browser_button.png')
    pyautogui.typewrite(assignmentLink)
    pyautogui.press('enter')
    time.sleep(5)
    # focussing on the files
    pyautogui.press('alt')
    randomlySelectAssignmetsAndDownloadThem(10)


main()
