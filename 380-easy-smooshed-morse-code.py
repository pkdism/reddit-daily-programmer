a_z_codes = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split(" ")

decoding = {}

for i in range(97, 122, 1):
	decoding[a_z_codes[i-97]] = chr(i)

encoding = dict((k, v) for v, k in decoding.items())

def encode_morse_code(word):
	print("Encoding morse code : ", word)
	for i in word:
		print(encoding[i], end = "")
	print("")

encode_morse_code("teete")
