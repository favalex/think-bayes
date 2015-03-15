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

pmf_dice = Pmf()
pmf_dice.set(Die(4), 2)
pmf_dice.set(Die(6), 3)
pmf_dice.set(Die(8), 2)
pmf_dice.set(Die(12), 1)
pmf_dice.set(Die(20), 1)
pmf_dice.normalize()
Pmf.make_mixture(pmf_dice).plot()
