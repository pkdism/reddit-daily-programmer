from itertools import permutations

s = input()
words = s.split(" + ")
n = len(words)
final = words[n-1].split(" == ")[1]
words[n-1] = words[n-1].split(" == ")[0]

letters = set(s)
letters.remove('+')
letters.remove("=")
letters.remove(" ")
letters_list = list(letters)
l = len(letters_list)

nums = list(range(10))

mapping = {}

for per in list(permutations(nums, l)):
    for j in range(len(per)):
        mapping[letters_list[j]] = str(per[j])

        words_sum = 0
        for word in words:
            word_num = int(''.join([mapping[i] for i in word]))
            words_sum += word_num

        final_sum = int(''.join(mapping[i] for i in final))
        if final_sum == words_sum:
            print(mapping)
