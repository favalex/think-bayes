from bayes import Bayes, Model

class TrainModel(Model):
	def __init__(self, num_trains):
		self.num_trains = num_trains

	def prior(self, hypo):
		return hypo**(-1.0)

	def hypos(self):
		return range(1, 1 + self.num_trains)

	def likelihood(self, data, hypo):
		data = data[0]
		if data > hypo:
			return 0

		return 1.0 / hypo

for n in [500, 1000, 2000]:
	train = Bayes(TrainModel(n))
	for t in [60, 30, 90]:
		train.update(t)
	print("Mean: {}".format(train.mean()))
	print("90% credible interval: {} {}".format(train.percentile(5), train.percentile(95)))
