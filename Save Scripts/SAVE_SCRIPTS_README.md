These are Python scripts that are to be used with Import Tuner Challenge or Shutoko Battle X save files.

You will need an install of Python to run the scripts | https://www.python.org/downloads/

To use the scripts, drag the .py file and .bat into the save file directory of the game you'd like to modify the save of. Below are the Xenia file paths for each game.

## Import Tuner Challenge | XeniaRootFolder\content\555307EE\00000001\SystemData.bin\

## Shutoko Battle X | XeniaRootFolder\content\474507D1\00000001\SystemData.bin\

Read below to see what each script does with additional instructions:

## unlock_cars.py

Place the .bat and .py in the folder of your save for ITC or SBX, run the .bat and follow the prompts to unlock the cut cars as buyable options in the shop. This does not give you the cars for free in your garage and only adds the cars as buyable options. You might need to rerun the script on your save after unlocking the Devil Z and/or Skull Bullet.

## save_convert.py

This script is to convert save files between games, *PLEASE NOTE* the only thing not transferable between games is the license plates for cars as the license plate system is different between games. You can edit the license plate in the garage. I recommend taking notes of your original license plates and keeping it with your backup original save file somewhere save. 

Place the .bat and .py in the folder of the save you'd wish to convert and run the .bat file. The script should automatically detect which game it is converting from and to but if there are issues, just follow the prompts. When the conversion is done, the file named "TXR_DATA_1" will be your new converted save while your original save will be backed up with either an "OLD_SBX_" or "OLD_ITC_" prefix depending on which game your input save is from. *PLEASE NOTE* that once you make a save in game, anything that isnt named "TXR_DATA_1" will be deleted from the "SystemData.bin" folder so just in case place your backup save somewhere safe.