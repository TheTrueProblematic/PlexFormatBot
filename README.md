# PlexFormatBot

## Goal
The goal of this bot is to reformat entire seasons at a time to be compatible with Plex.

## Explination
I have been reluctant to put TV shows into my Plex library due to the time it takes to transcode all of the episodes and rename them properly. This is designed to specifically cut down on that. It will properly name all of your files and transcode them for playing on Plex. 

## Usage
To use the PlexFormatBot simply place one season of any TV show in the folder labled In. They can be in seperate folders (such as sorting them by disk) or just put in as loose files.  
![image](https://user-images.githubusercontent.com/58759972/137047637-cd482f2c-1e87-4192-b3ec-87ea4c6a60be.png)
![image](https://user-images.githubusercontent.com/58759972/137047933-8889927f-26f9-4122-96a6-5bac76995da4.png)
The files themselves do not have to be named anything in particular all that matters is that they are in the correct order. You should have the files such that they look as if they go from the first episode to the last from the perspective of you in file explorer. Once all the files are in the In folder, just double click on the file that is named the same as your opperating system (Windows.bat for example). Give the program a while to run and the new files will appear in the folder labled Out. Throw them into your Plex TV library and your all done!
Note: This program will not delete the origional files in the in folder so make sure to clear them before doing a new season! 

## CAUTION
If you do not have an NVidia GPU this will not work as configured. (See Advanced Users Below)

## Advanced Users
I am using a tool called HandBrake to transcode the footage. My settings for transcoding are ones that I have found to be best for my settup, however, if you don't have a NVidia GPU or would like to configure the settings yourself this is very possible. The eaisiest way is to open the GUI version of HandBrake and configure the settings the way you want them in there. Then save your settings as a preset and name the preset "NVEnc". After this click Presets in the top right, click custom presets, click NVEnc, click options in the bottom left, and then click Export to File. Name the file "preset.json" and replace the file located in the Common folder of the PlexFormatBot with this new file. 
