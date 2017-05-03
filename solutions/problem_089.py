import utils

# How many digits can we save by writing the given Roman numerals in minimal form
def compute(verbose=False):
	VALUES = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	def to_roman(n): # Outputs minimal roman numeral representation, as string
		def to_roman_digit(digit, symbol_set):  # Outputs a single roman numeral digit (0-9)
			(sym1, sym5, sym10) = symbol_set
			if digit == 0:
				return ''
			elif digit <= 3:
				return sym1 * digit
			elif digit == 4:
				return sym1 + sym5
			elif digit <= 8:
				return sym5 + sym1 * (digit-5)
			else: # digit == 9:
				return sym1 + sym10
		# Index i is symbol set to translate 10**i place
		symbol_sets = [('I','V','X'), ('X','L','C'), ('C','D','M')]
		roman = 'M' * (n//1000)  # However many Ms are required
		for i in range(2, -1, -1): # process 10**i place
			n %= 10**(i+1)
			roman += to_roman_digit(n//10**i, symbol_sets[i])
		return roman
	def from_roman(r): # Interpret valid (but not necessarily minimal) roman numeral string
		if len(r) == 0:  # Base case for recursive solution
			return 0
		subtractives = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
		if r[:2] in subtractives:  # This works fine even if len(r) == 1
			return VALUES[r[1]] - VALUES[r[0]] + from_roman(r[2:])
		else:
			return VALUES[r[0]] + from_roman(r[1:])
	nums = open(utils.INPUT_PATH + 'p089_roman.txt').read().strip().split('\n')
	min_nums = map(lambda r: to_roman(from_roman(r)), nums)
	digits_saved = sum(map(len, nums)) - sum(map(len, min_nums))
	return digits_saved, 'Digits saved by writing roman numerals in minimal form'
