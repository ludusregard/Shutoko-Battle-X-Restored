This script is to be used for Import Tuner Challenge or Shutoko Battle X to do bitmap extraction/importation.

You will need an install of Python to run the scripts | https://www.python.org/downloads/
You will also need the Bundler and Unbundler | https://www.mediafire.com/file/a82lkgkgqie435r/SBX_Bitmap_Tools.zip/file

## Description

The script can extract XPR2 bitmaps into TGA images and also build TGA images into XPR2 files. XPR2 is a format for packing 
files for the Xbox 360 (Xbox Packed Resource 2). In the case of ITC/SBX, XPR2 files are exclusively used for bitmaps that
aren't already loose TGA images like the car decals are. Multiple bitmaps tend to be stored in a single XPR2 file.

## IMPORTANT

The Bundler and Unbundler executables need to be placed into the folder named "temp" for the python script to work properly!

## How to use

Simply either run the Python script directly with something like PowerShell/CMD or run the .bat file. The script will prompt
you on whether your are dumping or building an XPR2 file. After that it checks the folders below:

** Bitmap Tool\old_in\

XPR2 files you want to extract from go into here.

** Bitmap Tool\old_out\

When extracting from an XPR2 file, the contents are dumped into a folder of the same name within here.
*Example:
Bitmap Tool\old_in\00022657.xpr
*Gets dumped into:
Bitmap Tool\old_in\00022657\0022557.rdf
Bitmap Tool\old_in\00022657\menu_com_bg_grid00.tga
Bitmap Tool\old_in\00022657\menu_com_bg_sphere00.tga
Bitmap Tool\old_in\00022657\menu_com_menucursor00.tga
Bitmap Tool\old_in\00022657\menu_mai_bg00.tga
Bitmap Tool\old_in\00022657\menu_mai_effect00.tga
Bitmap Tool\old_in\00022657\menu_mai_logo00.tga
Bitmap Tool\old_in\00022657\menu_mai_logo01.tga
Bitmap Tool\old_in\00022657\menu_mai_logo02.tga
Bitmap Tool\old_in\00022657\menu_mai_logo03.tga
Bitmap Tool\old_in\00022657\menu_mai_start00.tga
Bitmap Tool\old_in\00022657\menu_mai_start01.tga

** Bitmap Tool\new_in\

Compiling the bitmaps likewise works the same way as above just in reverse. In this folder you will want to have a folder
with the name you want the final XPR2 file to be called. This folder should contain any TGA files you would like to pack into
the XPR2 file. You will need an RDF file to reference any of these bitmaps. When extracting an XPR2 file, an RDF file is also
dumped in the extraction. The RDF file is an XML file that references every TGA image that will be processed, their dimensions,
what kind of compression alogirithm should be used, etc. For nor the best practice is to reuse RDF files from extraction for
when you want to reimport modified bitmaps. Modifying the RDF file can however allow you to export XPR2 files with larger res or
uncompressed bitmaps however reimporting these bitmaps into ITC/SBX can result in bad scaling, game crashes, or a failure to
load the desired bitmap.
*Example:
Bitmap Tool\new_in\001337\001337.rdf
Bitmap Tool\new_in\001337\cool_image.tga
*Gets compiled into:
Bitmap Tool\new_out\001337.xpr

** Bitmap Tool\new_in\
As demonstrated by the above example, this is where your newly compiled XPR2 files will be. Some XPR2 bitmap collections are
nested within other files like XMD files. You will want to hex edit these new bitmaps in for those cases.