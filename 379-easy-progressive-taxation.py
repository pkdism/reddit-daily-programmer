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

# Optional Bonus
print("\nOptional Bonus\n")

overall_tax_rate_on_10k = 0
overall_tax_rate_on_30k = tax_on_30k/thirty_k
overall_tax_rate_on_100k = tax_on_100k/hundred_k

def get_income(overall_tax_rate):

	if overall_tax_rate >= 0.4:
		return None

	income = 0
	if overall_tax_rate > overall_tax_rate_on_100k:
		income = int((tax_on_100k - hundred_k*0.4)/(overall_tax_rate - 0.4))
	elif overall_tax_rate > overall_tax_rate_on_30k:
		income = int((tax_on_30k - thirty_k*0.25)/(overall_tax_rate - 0.25))
	elif overall_tax_rate > overall_tax_rate_on_10k:
		income = int((tax_on_10k - ten_k*0.1)/(overall_tax_rate - 0.1))
	return income

print(get_income(0))
print(get_income(0.06))
print(get_income(0.09))
print(get_income(0.32))
print(get_income(0.40))
