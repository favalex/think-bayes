from pmf import Pmf
from functools import reduce

class Die(Pmf):
	def __init__(self, sides):
		Pmf.__init__(self)
		for side in range(1, 1+sides):
			self.set(side, 1.0 / sides)

three = Die(6) + Die(6) + Die(6)
three.plot()

print()

reduce(Pmf.max, (three for _ in range(6))).plot()
