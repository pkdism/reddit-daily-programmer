def balanced(string):
    count = {'x' : 0, 'y' : 0}
    for i in string:
        count[i] += 1
    if count['x'] == count['y']:
        return True
    else:
        return False

def balanced_bonus(string):
    hash = [0]*26
    for i in string:
        hash[ord(i)-ord('a')] += 1
    for i in string:
        if hash[ord(i) - ord('a')] != hash[ord(string[0]) - ord('a')]:
            return False
    return True

print(balanced("xxxyyy"))# => true
print(balanced("yyyxxx"))# => true
print(balanced("xxxyyyy"))# => false
print(balanced("yyxyxxyxxyyyyxxxyxyx"))# => true
print(balanced("xyxxxxyyyxyxxyxxyy"))# => false
print(balanced(""))# => true
print(balanced("x"))# => false
print("\nBonus")
print(balanced_bonus("xxxyyyzzz"))# => true
print(balanced_bonus("abccbaabccba"))# => true
print(balanced_bonus("xxxyyyzzzz"))# => false
print(balanced_bonus("abcdefghijklmnopqrstuvwxyz"))# => true
print(balanced_bonus("pqq"))# => false
print(balanced_bonus("fdedfdeffeddefeeeefddf"))# => false
print(balanced_bonus("www"))# => true
print(balanced_bonus("x"))# => true
print(balanced_bonus(""))# => true
