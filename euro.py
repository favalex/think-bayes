from bayes import Bayes, Model

class EuroModel(Model):
	def prior(self, hypo):
		if hypo <= 50:
			return hypo
		else:
			return 100 - hypo

	def hypos(self):
		return range(100)

	def likelihood(self, data, hypo):
		p = hypo / 100.0
		heads, tails = data[0]
		return p**heads * (1-p)**tails

euro = Bayes(EuroModel())

euro.update((140, 110))

print("Mean:", euro.mean())
print("Median:", euro.median())
print("Maximum likelihood:", euro.maximum_likelihood())
print("90% credible interval:", euro.credible_interval(90))
