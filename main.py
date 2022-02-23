import pyautogui
import time
import random
import os
import shutil
import zipfile


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


def unzipFile(file_path, dest_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(dest_path)


def copyDownloadedFile(path1, path2):
    for file in os.listdir(path1):
        if file.endswith(".zip"):
            shutil.copy(path1 + file, path2 + file)
            break


def unzipAllFilesInFolder(path):
    for file in os.listdir(path):
        if file.endswith(".zip"):
            os.mkdir(path + file[:-4])
            unzipFile(path + file, path + file[:-4])
    for file in os.listdir(path):
        if file.endswith(".zip"):
            os.remove(path + file)


def anyCaseToPascalCase(string):
    return ''.join(x.capitalize() or '_' for x in string.split('_'))


def removeStartNumerals(string):
    if string[2].isdigit():
        return string[3:]
    elif string[1].isdigit():
        return string[2:]
    elif string[0] == '.' and string[1].isdigit():
        return string[1:]
    else:
        return string


def renameFilesAndFoldersAccordingToPascalCase(path):
    for folder in os.listdir(path):
        if folder.startswith('.'):
            continue
        arr = os.listdir(path + folder)
        if len(os.listdir(path + folder)) > 2:
            for program in os.listdir(path + folder):
                os.rename(path + '' + folder + '/' + program,
                          path + '' + folder + '/' + anyCaseToPascalCase(program))
                os.rename(path + '' + folder + '/' + anyCaseToPascalCase(program),
                          path + '' + folder + '/' + removeStartNumerals(program))
        else:
            while True:
                if len(os.listdir(path + folder)) == 2:
                    folder = folder + '/' + os.listdir(path + folder)[1]
                    if len(os.listdir(path + folder)) >= 2:
                        break
                else:
                    folder = folder + '/' + os.listdir(path + folder)[0]
                    if len(os.listdir(path + folder)) >= 2:
                        break
            for program in os.listdir(path + folder):
                os.rename(path + '' + folder + '/' + program,
                          path + '' + folder + '/' + anyCaseToPascalCase(program))
                os.rename(path + '' + folder + '/' + anyCaseToPascalCase(program),
                          path + '' + folder + '/' + removeStartNumerals(program))


def copyAFileFromEachDirectory(path, copyPath):
    count = 0
    for folder in os.listdir(path):
        if folder.startswith('.'):
            continue
        arr = os.listdir(path + folder)
        if len(os.listdir(path + folder)) > 2:
            programs = os.listdir(path + folder)
            shutil.copy(path + folder + '/' + programs[count], copyPath)
            count += 1
        else:
            while True:
                if len(os.listdir(path + folder)) == 2:
                    folder = folder + '/' + os.listdir(path + folder)[1]
                    if len(os.listdir(path + folder)) >= 2:
                        break
                else:
                    folder = folder + '/' + os.listdir(path + folder)[0]
                    if len(os.listdir(path + folder)) >= 2:
                        break
            programs = os.listdir(path + folder)
            shutil.copy(path + folder + '/' + programs[count], copyPath)
            count += 1


assignmentLink = 'https://drive.google.com/drive/u/1/folders/1ZmDG9pAzMqdamGRfqumqrc_SS9lAEwdl?usp=sharing'
downloadsFolder = '/home/ubuntu/Downloads/'
destinationFolder = '/home/ubuntu/Documents/college/semester4/cp/week4/'
solutionsFolderInDestination = '.lit2020066 yash verma cp assignment week4'


def main():
    os.system('brave-browser ' + assignmentLink)
    time.sleep(5)
    pyautogui.press('alt')
    randomlySelectAssignmetsAndDownloadThem(10)
    copyDownloadedFile(downloadsFolder, destinationFolder)
    file = os.listdir(destinationFolder)
    unzipFile(destinationFolder + file[0], destinationFolder)
    os.remove(destinationFolder + file[0])
    unzipAllFilesInFolder(destinationFolder)
    renameFilesAndFoldersAccordingToPascalCase(destinationFolder)
    os.mkdir(destinationFolder + solutionsFolderInDestination)
    copyAFileFromEachDirectory(destinationFolder, destinationFolder + '/' + solutionsFolderInDestination)
    renameFilesAndFoldersAccordingToPascalCase(destinationFolder + solutionsFolderInDestination)


main()
