# Gui-Automator

This is a GUI automation tool which opens a new tab in a browser to open a new URL for a Google Drive folder, and then it automatically selects the n number of random files or folders and then downloads them, This is made possible by pyautogui library.
It then extracts the zip at the specified location and then assuming that we have downloaded all the zip files from Google Drive.
Then it extracts all the downloaded zip files, it then copies 1 file from each of the zip files in incremental order like copies file 1 from 1st zip then 2 from second zip, this continues till the nth zip file.
After that, it also renames all the files in Pascal Case and deletes all the zip files.
