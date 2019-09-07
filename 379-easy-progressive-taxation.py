hundred_k = 100000
thirty_k = 30000
ten_k = 10000

tax_on_10k = 0
tax_on_30k = int((30000 - 10000)*0.1)
tax_on_100k = int((100000 - 30000)*0.25 + (30000 - 10000)*0.1)

def tax(num):
	tax_amount = 0

	if num > hundred_k:
		tax_amount += int((num - hundred_k)*0.4 + tax_on_100k)
	elif num > thirty_k:
		tax_amount += int((num - thirty_k)*0.25 + tax_on_30k)
	elif num > ten_k:
		tax_amount += int((num - ten_k)*0.1 + tax_on_10k)

	return(tax_amount)

print(tax(0))
print(tax(10000))
print(tax(10009))
print(tax(10010))
print(tax(12000))
print(tax(56789))
print(tax(1234567))
