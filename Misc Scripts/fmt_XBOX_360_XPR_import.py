
from inc_noesis import *

import noesis

#rapi methods should only be used during handler callbacks
import rapi

def registerNoesisTypes():
    handle = noesis.register("XPR2 Textures", ".xpr")
    noesis.setHandlerTypeCheck(handle, XPRCheckType)
    noesis.setHandlerLoadRGBA(handle, XPRLoadRGBA)
    noesis.logPopup()
    return 1

def XPRCheckType(data):
    bs = NoeBitStream(data)
    Header = bs.readBytes(4).decode("ASCII")
    if Header != 'XPR2':
        return 0
    return 1

def XPRLoadRGBA(data, texList):
    bs = NoeBitStream(data)
    Header = bs.read(">iiii")
    Tex = []
    TexNames = []
    TexData = []
    TexSize = []

    # Loop through the textures
    for i in range(0, Header[3]):
        Data = bs.read(">iiii")
        Tex.append([Data[1], Data[2], Data[3]])

    # Reading texture names safely
    for i in range(0, Header[3]):
        bs.seek(Tex[i][2] + 12, NOESEEK_ABS)
        try:
            TexNames.append(bs.readString())
        except UnicodeDecodeError:
            TexNames.append("unknown_texture_name_" + str(i))

    # Reading texture data
    for i in range(0, Header[3]):
        bs.seek(Tex[i][0] + 12, NOESEEK_ABS)
        bs.seek(33, NOESEEK_REL)
        Data = bs.read(">HBHHiii")
        TexData.append([Data[0], Data[1], Data[2], Data[3]])

    # Calculate texture sizes
    for i in range(0, Header[3] - 1):
        TexSize.append((TexData[i + 1][0] - TexData[i][0]))
    TexSize.append(Header[2] / 0x100 - TexData[Header[3] - 1][0])

    # Process and append textures
    for i in range(0, Header[3]):
        bs.seek(TexData[i][0] * 0x100 + (Header[1] + 12), NOESEEK_ABS)
        data = bs.readBytes(int(TexSize[i] * 0x100))
        imgHeight = (TexData[i][2] + 1) * 8
        imgWidth  = (TexData[i][3] + 1) & 0x1FFF
        texFmt = 0

        print(TexNames[i])

        # Handle different texture formats
        if TexData[i][1] == 0x52:  # DXT1
            data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 8)
            texFmt = noesis.NOESISTEX_DXT1
        elif TexData[i][1] == 0x53:  # DXT3
            data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 16)
            texFmt = noesis.NOESISTEX_DXT3
        elif TexData[i][1] == 0x54:  # DXT5
            data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 16)
            texFmt = noesis.NOESISTEX_DXT5
        elif TexData[i][1] == 0x71:  # DXT5 packed normal map
            data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 16)
            data = rapi.imageDecodeDXT(data, imgWidth, imgHeight, noesis.FOURCC_ATI2)
            texFmt = noesis.NOESISTEX_RGBA32
        elif TexData[i][1] == 0x7C:  # DXT1 packed normal map
            data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 8)
            data = rapi.imageDecodeDXT(data, imgWidth, imgHeight, noesis.FOURCC_DXT1NORMAL)
            texFmt = noesis.NOESISTEX_RGBA32
        elif TexData[i][1] == 0x86:  # Raw
            data = rapi.imageUntile360Raw(data, imgWidth, imgHeight, 4)
            data = rapi.imageDecodeRaw(data, imgWidth, imgHeight, "a8r8g8b8")
            texFmt = noesis.NOESISTEX_RGBA32
        else:
            print("WARNING: Unhandled image format " + repr(imgFmt) + " - " + repr(imgWidth) + "x" + repr(imgHeight) + " - " + repr(len(data)))
            return None

        tex1 = NoeTexture(TexNames[i], imgWidth, imgHeight, data, texFmt)
        texList.append(tex1)

    return 1
