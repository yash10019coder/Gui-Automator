#!/bin/bash

downloadedZipFilePath="/home/ubuntu/Downloads/temp/"

destinationFolderPath="/home/ubuntu/Documents/college/semester4/cp/week4/"

#rm -r $destinationFolderPath/*

# move the downloaded zip file to the destination folder
cp $downloadedZipFilePath/drive*.zip $destinationFolderPath

unzip $destinationFolderPath/drive*.zip -d $destinationFolderPath

#rm $destinationFolderPath/drive*.zip

i=1
for file in $(ls $destinationFolderPath); do
  unzip $destinationFolderPath/$file -d $destinationFolderPath/$i
  rm $destinationFolderPath/$file
done

unzip $(ls $destinationFolderPath) -d $destinationFolderPath

rm $destinationFolderPath/*.zip

allFilesFolders=$(ls $destinationFolderPath)

echo $allFilesFolders
