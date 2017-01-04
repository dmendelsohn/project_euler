# How many different ways can $2.00 be made using any number of coins?
def compute():
	COINS = [1,2,5,10,20,50,100,200]
	def num_ways(num_coin_types, amount):
		if num_coin_types == 1:
			return 1
		else:
			biggest = COINS[num_coin_types-1]
			num_fit = amount/biggest
			return sum(num_ways(num_coin_types-1,amount-i*biggest) for i in range(num_fit+1))
	return num_ways(8, 200), "Number of ways to make $2.00 with the given coins"