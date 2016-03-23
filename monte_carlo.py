"""This script demonstrates simulations of coin flipping"""

import random

# Create virtual fair coin object that can be flipped
class Coin(object):
	sides = ("Heads", "Tails")
	last_result = None

	def flip(self):
		"""Call coin.flip() to flip the coin and record it as the last result"""
		self.last_result = result = random.choice(self.sides)
		return result

# Create auxillary functions to manipulate the coin
def create_coins(number):
	"""Create a list of a number of coin objects"""
	return [Coin() for _ in xrange(number)]

def flip_coins(coins):
	"""Side effect function, modifies object in place, returns None"""
	for coin in coins:
		coin.flip()

def count_heads(flipped_coins):
	return sum(coin.last_result == "Heads" for coin in flipped_coins)

def count_tailss(flipped_coins):
	return sum(coin.last_result == "Tails" for coin in flipped_coins)

def main():
	coins = create_coins(1000)
	for i in xrange(100):
		flip_coins(coins)
		print(count_heads(coins))

if __name__ == "__main__":
	main()