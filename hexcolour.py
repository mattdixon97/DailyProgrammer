'''
Given three integers between 0 and 255, corresponding to the red, green,
and blue channel values of a colour, find the hex string for that colour.

https://www.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/
'''

# One-liner

hexcolour = '#{:02X}{:02X}{:02X}'.format


# Implementing my own dec to hex

def hex(n):
    dict = {10:'A', 11:'B', 12:'C', 13:'D', 14: 'E', 15:'F'}
    return dict.get(n // 16, str(n // 16)) + dict.get(n % 16, str(n % 16))

def hexcolour2(r, g, b):
    return "#" + hex(r) + hex(g) + hex(b)


# Bonus: colour blending

def blend(colours):
    r = g = b = 0
    for colour in colours:
        r += int(colour[1:3], 16)
        g += int(colour[3:5], 16)
        b += int(colour[5:7], 16)
    return "#" + hex(r // len(colours)) + hex(g // len(colours)) + hex(b // len(colours))
