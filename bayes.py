from pmf import Pmf

class Suite(Pmf):
	def __init__(self, likelihoods):
		self.likelihoods = likelihoods
		Pmf.__init__(self)
		for hypo in self.likelihoods.keys():
			self.set(hypo, 1)
		self.normalize()

	def update(self, *data):
		for hypo in self.values():
			self.mult(hypo, self.likelihood(data, hypo))
		self.normalize()

	def likelihood(self, data, hypo):
		result = self.likelihoods[hypo]
		for d in data:
			result = result[d]
		return result
