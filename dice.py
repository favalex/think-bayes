from bayes import Bayes, Model

class DiceModel(Model):
	def hypos(self):
		return [4, 6, 8, 12, 20]

	def likelihood(self, data, hypo):
		data = data[0]
		if data > hypo:
			return 0

		return 1.0 / hypo

dice = Bayes(DiceModel())
dice.print()
for roll in [6, 6, 8, 7, 7, 5, 4]:
	dice.update(roll)
dice.print()
