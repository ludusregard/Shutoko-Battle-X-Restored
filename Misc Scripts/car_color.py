import struct
import math

def hex_to_sbx_hsv(hex_color):
    # Remove the '#' from the hex color if present
    hex_color = hex_color.lstrip('#')

    # Convert the HEX color to RGB values
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # Normalize RGB values to the range [0, 1]
    r_normalized, g_normalized, b_normalized = r / 255.0, g / 255.0, b / 255.0

    # Convert RGB to HSV using colorsys module
    import colorsys
    h, s, v = colorsys.rgb_to_hsv(r_normalized, g_normalized, b_normalized)

    # Convert HSV values to the required format
    hue = math.ceil(h * 360)  # Hue in degrees
    saturation = math.ceil(s * 255)  # Saturation on 0-255 scale
    value = math.ceil(v * 255)  # Value on 0-255 scale

    # Convert Hue to little-endian format (2 bytes)
    hue_little_endian = struct.pack('<H', hue)

    # Combine the bytes into the desired 4-byte format
    sbx_hsv = hue_little_endian + bytes([saturation, value])

    # Convert to hexadecimal string for display
    sbx_hsv_hex = ' '.join(f'{byte:02X}' for byte in sbx_hsv)

    return sbx_hsv_hex

# Prompt the user for input
hex_color = input("Enter a HEX color code #RRGGBB: ")
result = hex_to_sbx_hsv(hex_color)
print(f"HEX Color: {hex_color}")
print(f"SBX HSV: {result}")
