#! /usr/bin/python3

from collections import defaultdict

class Pmf:
	def __init__(self):
		self.probs = defaultdict(int)

	def __add__(self, other):
		pmf = Pmf()
		for sv, sp in self.probs.items():
			for ov, op in other.probs.items():
				pmf.incr(sv+ov, sp*op)
		return pmf

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

	def print(self):
		for value, prob in sorted(self.probs.items()):
			print("{}: {}".format(value, prob))

	def mean(self):
		return sum(value*prob for value, prob in self.probs.items())

	def percentile(self, percentage):
		p = percentage / 100.0
		total = 0
		for value, prob in sorted(self.probs.items()):
			total += prob
			if total >= p:
				return value

	def median(self):
		return self.percentile(50)

	def credible_interval(self, percentage):
		half = percentage / 2
		return self.percentile(50 - half), self.percentile(50 + half)

	def maximum_likelihood(self):
		_, value = max((prob, value) for value, prob in self.probs.items())
		return value

	def plot(self):
		scale = 80 / max(self.probs.values())
		for value, prob in sorted(self.probs.items()):
			print("{:2d}: {}".format(value, '#'*int(prob*scale)))

if __name__ == '__main__':
	from pprint import pprint
	pmf = Pmf()
	pmf.set('a', 1)
	pmf.set('b', 2)
	pmf.set('c', 3)
	pmf.normalize()
	pprint(pmf.probs)
