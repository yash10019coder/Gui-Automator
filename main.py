import pyautogui
import time


def clickImage(image):
    x, y = pyautogui.locateCenterOnScreen(image)
    pyautogui.click(x, y)


def downloadAssingment():
    time.sleep(.1)
    clickImage('options_menu_google_drive.png')
    pyautogui.press('up')
    pyautogui.press('enter')
    time.sleep(.5)


def randomlySelectAssignmetsAndDownloadThem(count):
    for i in range(count):
        downloadAssingment()
        time.sleep(.5)


assignmentLink = 'https://drive.google.com/drive/u/1/folders/1VlkehHj-3pM1dxEURCJnutve27tblrxz'

pyautogui.hotkey('alt', '1')
time.sleep(.5)
try:
    # opening the link in a new tab
    clickImage('new_tab_browser_button.png')
    pyautogui.typewrite(assignmentLink)
    pyautogui.press('enter')
    time.sleep(5)
    # focussing on the files
    clickImage('files_google_drive.png')
    pyautogui.press('right')
    downloadAssingment()


except Exception as e:
    print(e)