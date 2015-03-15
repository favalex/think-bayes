from bayes import Bayes, Model

class Bowl:
	def __init__(self, **cookies):
		self.cookies = cookies

	def __getitem__(self, flavor):
		return self.cookies[flavor]

	def total(self):
		return sum(self.cookies.values())

	def remove(self, flavor):
		self.cookies[flavor] -= 1

class DiceModel(Model):
	def __init__(self):
		self.bowls = {
			'Bowl 1': Bowl(vanilla=30, chocolate=10),
			'Bowl 2': Bowl(vanilla=20, chocolate=20),
		}

	def hypos(self):
		return self.bowls.keys()

	def likelihood(self, data, hypo):
		data = data[0]
		bowl = self.bowls[hypo]
		like = bowl[data] / bowl.total()
		bowl.remove(data)
		return like
		
cookies = Bayes(DiceModel())
cookies.print()
cookies.update('vanilla')
cookies.print()
cookies.update('vanilla')
cookies.print()
cookies.update('vanilla')
cookies.print()
cookies.update('vanilla')
cookies.print()
cookies.update('vanilla')
cookies.print()
