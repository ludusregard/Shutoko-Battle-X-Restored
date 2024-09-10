# Shutokō Battle X Restored
A relocalization/undub project for the game Shutokō Battle X by Genki for the Xbox 360.

Import Tuner Challenge has numerous minor gameplay and changes from SBX while also containing  multiple errors in its localized
script by Ubisoft. This project seeks to rectify those issues by patching the original Japanese release of SBX to be in English.
Currently the SBXR is a modified version of the ITC release but with numerous fixes to the script.
i.e. correcting dialog errors like "Nissan 80 Supra" to "Toyota 80 Supra"

## Installation
Requires an unmodified iso dump of Shutokō Battle X (首都高バトルＸ) NOT Import Tuner Challenge:

MD5: 7fc78018c68a2f73e703e1679ac4051e | http://redump.org/disc/86493/

Grab the latest Xdelta patch here:

https://github.com/ludusregard/Shutoko-Battle-X-Restored/releases/tag/Xdelta

Grab any Xdelta patcher of choice, I recommend the latest version of Delta Patcher:

https://github.com/marco-calautti/DeltaPatcher

Patch your iso (make a backup of the original too) and it should just work in Xenia. The iso size will shrink nearly in half.
Reminder, use the .toml patch for Xenia for the game to prevent the load hang after the first race. If you want to run this on
an Xbox 360, it should work without issue as long as you are familiar with modding. After patching the iso you can either dump
to xex and loose files or convert to games on demand in the typical fashion. This patch has been tested on an Xbox 360 dev kit
and causes no issues. Achievements and game Title are not localized.

## Future Plans
- Replace more of the Import Tuner Challenge localization with fresh translations
- Release python scripts and tutorials to enable others to translate SBX to other languages
- If possible, reenable the half-cut content like the Corollas that can only be used with a 100% save
- If possible, look into the feasabillity of any sort of 60fps patch

## Special Thanks
- [**igorciz777**] None of this could have been possible without the use of GUTArchive

  https://github.com/igorciz777/GUTArchiveTools

  
- [**JakeMR2**] Helpful initial research into ITC

  https://github.com/JakeMR2/Jake-s-TXR-Resources-and-Research

  
- [**Shutokō Battle Rival Database Wiki**] Invaluable datamined info for all the games

  https://genkirivalproject.fandom.com/wiki/

  
- [**Shutokou Battle Discord**] Quick support, feedback, etc. Cool community in general

  https://discord.gg/n4FvF3VkHQ

  
- [**Sean T**] Testing builds and testing on actual Xbox 360 hardware

  https://x.com/DogbrainSean

- [**Genki and Ubisoft**] For the game and the initial localization much of this is currently based off of

  https://store.steampowered.com/developer/genki
