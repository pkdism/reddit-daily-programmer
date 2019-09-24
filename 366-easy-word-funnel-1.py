# --- Functions ---

def funnel(s1, s2):
    diff = 0
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            i += 1
            diff += 1
            if diff > 1:
                return False
        else:
            i += 1
            j += 1
    return diff == 1 and i == len(s1) and j == len(s2)

def bonus1(word):
    res = []
    for j in range(0, len(word)):
        x = ""
        for i in range(0, len(word)):
            if i == j:
                continue
            x += word[i]
        res.append(x)
    return res

# --- Tests ---

# Main
print("Main")
print(funnel("leave", "eave"))
print(funnel("reset", "rest"))
print(funnel("dragoon", "dragon"))
print(funnel("eave", "leave"))
print(funnel("sleet", "lets"))
print(funnel("skiff", "ski"))

print("Bonus1")
print(bonus1("dragon"))
