# Shutokō Battle X Restored
A relocalization/undub project for the game Shutokō Battle X by Genki for the Xbox 360.

Import Tuner Challenge has numerous minor gameplay and changes from SBX while also containing  multiple errors in its localized
script by Ubisoft. This project seeks to rectify those issues by patching the original Japanese release of SBX to be in English.
Currently the SBXR is a modified version of the ITC release but with numerous fixes to the script.
i.e. correcting dialog errors like "Nissan 80 Supra" to "Toyota 80 Supra"

# Installation
Reminder, use the .toml patch for Xenia for the game to prevent the load hang after the first race regardless of installation method.
If you want to run this on an Xbox 360, it should work without issue as long as you are familiar with console modding.
Method 1 is for if you have an iso and want to mod that copy. Method 2 is for if you have loose files + xex.
The two methods are separated in the tag releases by "iso" and "xex" accordingly.

Both methods of installation are Xdelta patches to not infringe on copyright by distributing assets illegally.

Grab any Xdelta patcher of choice, I recommend the latest version of Delta Patcher: https://github.com/marco-calautti/DeltaPatcher

## Method 1: iso
**Requires an unmodified iso of *Shutokō Battle X* (*首都高バトルＸ*) NOT *Import Tuner Challenge*.**

**MD5:** *7FC78018C68A2f73E703E1679AC4051E* **|** http://redump.org/disc/86493/

Grab the latest iso Xdelta patch: https://github.com/ludusregard/Shutoko-Battle-X-Restored/releases/tag/iso

Patch your iso (make a backup of the original too) and it should just work in Xenia. The iso size will shrink nearly in half.

## Method 2: xex with loose game files
Requires your dump of the game to be unmodified, MD5 hashes provided of the unmodified files extracted from SBX.

Grab the latest xex Xdelta patches: https://github.com/ludusregard/Shutoko-Battle-X-Restored/releases/tag/xex

All Xdelta patches have their name matched to the file they patch. See the list below for file names and paths + MD5 hash.

#### Example: ***BUILD.DAT*** is patched by ***build-dat.xdelta***

### Main Game Files
- **MD5:** *E1EA991DDF75BAF4B218B39921A5F50C* **|** DATA\BUILD\TXR\\**BUILD.DAT**

- **MD5:** *7AFBDB24E11A34BDC61A14F7BC1C365D* **|** DATA\BUILD\TXR\\**BUILD.TOC**

### Optional Video Files
- **MD5:** *BE4C013AC9B61895E7F351C845B26FB7* **|** DATA\TXR\MOVIE\\**OPENING.wmv**

- **MD5:** *F73940D1D5F0E4BB9E06F613D6A6EC4C* **|** DATA\TXR\MOVIE\\**ENDING.wmv**

- **MD5:** *2F1A5539FCB9238B7375E5BD6D982460* **|** DATA\TXR\MOVIE\\**PERFECT_ENDING.wmv**

- **MD5:** *AB3AB9D78AD99D67854A9179226180CD* **|** DATA\TXR\MOVIE\\**STAGE1_OPENING.wmv**

- **MD5:** *17260E9DD9CEBAEB7AF8EF98FD7B7399* **|** DATA\TXR\MOVIE\\**STAGE2_OPENING.wmv**

- **MD5:** *F83E4901D58648247F95E56C646D249B* **|** DATA\TXR\MOVIE\\**STAGE3_OPENING.wmv**

### Notes
- The "optional" video file patches can be substituted by replacing the .wmv files with their ***Import Tuner Challenge*** equivalents

- If you want the ***Import Tuner Challenge*** map changes, replacing the files **BUILD_CRS.DAT** and **BUILD_CRS.TOC** with their ITC equivalents should work

- Many of the files aren't actually used in the game as they have duplicates baked into **BUILD.DAT** so deleting many of the loose files can save space

## Future Plans
- Replace more of the Import Tuner Challenge localization with fresh translations

- Release python scripts and tutorials to enable others to translate SBX to other languages

- If possible, reenable the half-cut content like the Corollas that can only be used with a 100% save

- If possible, look into the feasabillity of any sort of 60fps patch

# Special Thanks
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
