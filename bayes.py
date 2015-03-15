from pmf import Pmf

class Model:
	def prior(self, hypo):
		return 1

class DictModel(Model):
	def __init__(self, likelihoods):
		self.likelihoods = likelihoods

	def hypos(self):
		return self.likelihoods.keys()

	def likelihood(self, data, hypo):
		result = self.likelihoods[hypo]
		for d in data:
			result = result[d]
		return result

class Bayes(Pmf):
	def __init__(self, model):
		self.model = model
		Pmf.__init__(self)
		for hypo in self.model.hypos():
			self.set(hypo, self.model.prior(hypo))
		self.normalize()

	def update(self, *data):
		self.update_unnormalized(data)
		self.normalize()

	def update_set(self, dataset):
		for data in dataset:
			self.update_unnormalized([data])
		self.normalize()

	def update_unnormalized(self, data):
		for hypo in self.values():
			self.mult(hypo, self.model.likelihood(data, hypo))
