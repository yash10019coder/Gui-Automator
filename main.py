import pyautogui
import time
import random
import os
import shutil


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


def unzipFile(path):
    os.system('unzip ' + path)


def moveDownloadedFile(path1, path2):
    for file in os.listdir(path1):
        if file.endswith(".zip"):
            shutil.move(path1 + file, path2 + file)
            break


def unzipAllFilesInFolder(path):
    for file in os.listdir(path):
        if file.endswith(".zip"):
            unzipFile(path + file)
    for file in os.listdir(path):
        if file.endswith(".zip"):
            os.remove(path + file)


def anyCaseToPascalCase(string):
    return ''.join(x.capitalize() or '_' for x in string.split('_'))


assignmentLink = 'https://drive.google.com/drive/u/1/folders/1VlkehHj-3pM1dxEURCJnutve27tblrxz'
downloadsFolder = '/home/ubuntu/Downloads/temp/'
destinationFolder = '/home/ubuntu/Documents/college/cp/semester4/week2auto/'


def main():
    os.system('brave-browser')
    time.sleep(.5)
    # opening the link in a new tab
    clickImage('new_tab_browserster4/week2auto/LCS2020044.zip or /home/ubuntu/Documents/college/cp/semester4/week2auto_button.png')
    pyautogui.typewrite(assignmentLink)
    pyautogui.press('enter')
    time.sleep(5)
    # focussing on the files
    pyautogui.press('alt')
    randomlySelectAssignmetsAndDownloadThem(10)
    # moveDownloadedFile(downloadsFolder, destinationFolder)
    # file = os.listdir(destinationFolder)
    # unzipFile(destinationFolder + file[0])
    # os.remove(destinationFolder + file[0])
    # unzipAllFilesInFolder(destinationFolder)
    # for folder in os.listdir(destinationFolder):
    #     for programs in os.listdir(destinationFolder + folder):
    #         os.rename(destinationFolder + folder + programs, destinationFolder + folder + anyCaseToPascalCase(programs))


main()
