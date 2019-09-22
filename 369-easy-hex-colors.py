map = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
hex_mapping = {**{x : str(x) for x in range(10)}, **map}
dec_mapping = {x : y for y,x in hex_mapping.items()}

def hexcolor(red, green, blue):
    hex = "#"
    for color in [red, green, blue]:
        hex += hex_mapping[color//16] + hex_mapping[color%16]
    return hex

def blend(hex_colors):
    l = len(hex_colors)
    r_avg, g_avg, b_avg = 0, 0, 0
    for color in hex_colors:
        r_avg += dec_mapping[color[1]]*16 + dec_mapping[color[2]]
        g_avg += dec_mapping[color[3]]*16 + dec_mapping[color[4]]
        b_avg += dec_mapping[color[5]]*16 + dec_mapping[color[6]]
    r_avg //= l
    g_avg //= l
    b_avg //= l
    return(hexcolor(r_avg, g_avg, b_avg))


print(hexcolor(255, 99, 71))# => "#FF6347"  (Tomato)
print(hexcolor(184, 134, 11))# => "#B8860B"  (DarkGoldenrod)
print(hexcolor(189, 183, 107))# => "#BDB76B"  (DarkKhaki)
print(hexcolor(0, 0, 205))# => "#0000CD"  (MediumBlue)

print("\nBonus")
print(blend({"#000000", "#778899"}))# => "#3C444C"
print(blend({"#E6E6FA", "#FF69B4", "#B0C4DE"}))# => "#DCB1D9"
