#! /usr/bin/python3

from collections import defaultdict

class Pmf:
	def __init__(self):
		self.probs = defaultdict(int)

	def set(self, value, prob):
		self.probs[value] = prob

	def incr(self, value, incr=1):
		self.probs[value] += incr

	def mult(self, value, mult):
		self.probs[value] *= mult

	def __getitem__(self, value):
		return self.probs[value]

	def normalize(self):
		total = sum(self.probs.values())
		for value, prob in self.probs.items():
			self.probs[value] /= total
	
	def values(self):
		return self.probs.keys()

if __name__ == '__main__':
	from pprint import pprint
	pmf = Pmf()
	pmf.set('a', 1)
	pmf.set('b', 2)
	pmf.set('c', 3)
	pmf.normalize()
	pprint(pmf.probs)
