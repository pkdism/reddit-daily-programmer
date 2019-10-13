az = list(map(lambda x: chr(ord('a')+x%26), range(0,26)))

lookup = {}
j = 0
for i in az:
    lookup[i] = list(map(lambda x: chr(ord('a')+(x+j)%26), range(0,26)))
    j += 1


def decipher(keyword, msg):
    n = len(msg)
    l = len(keyword)
    key_string = ""
    for i in range(n):
        key_string +=  keyword[i%l]

    deciphered_msg = ''
    for i in range(n):
        deciphered_msg += lookup[key_string[i]][ord(msg[i]) - ord('a')]

    return deciphered_msg

print(decipher("snitch", "thepackagehasbeendelivered"))
print(decipher("bond", "theredfoxtrotsquietlyatmidnight"))
print(decipher("train", "murderontheorientexpress"))
print(decipher("garden", "themolessnuckintothegardenlastnight"))
