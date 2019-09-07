#include <iostream>
using namespace std;

int k100 = 100000;
int k30 = 30000;
int k10 = 10000;

float tax_on_100k = (k100 - k30)*0.25 + (k30 - k10)*0.1;
float tax_on_30k = (k30 - k10)*0.1;

int tax(int num) {
	int tax_amount = 0;
	if (num > k100) {
		tax_amount += int((num - k100)*0.4 + tax_on_100k);
	} else if (num > k30) {
		tax_amount += int((num - k30)*0.25 + tax_on_30k);
	} else if (num > k10) {
		tax_amount += int((num - k10)*0.1);
	}
	return tax_amount;
}

int main() {
	int nums[] = {0, 10000, 10009, 10010, 12000, 56789, 1234567};
	for (int i = 0; i < 7; i++) {
		cout << tax(nums[i]) << endl;
	}
	return 0;
}