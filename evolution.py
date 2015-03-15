# Using pmf module directly

from pmf import Pmf
from pprint import pprint

pmf = Pmf()

# Prior
pmf.set('Bowl 1', 0.5)
pmf.set('Bowl 2', 0.5)

# Likelihood
pmf.mult('Bowl 1', 0.75)
pmf.mult('Bowl 2', 0.5)
pmf.normalize()

pprint(pmf.probs)

# Factoring out update()

class Cookies(Pmf):
	def __init__(self):
		Pmf.__init__(self)
		self.set('Bowl 1', 1)
		self.set('Bowl 2', 1)
		self.normalize()

	def update(self, data):
		for hypo in self.values():
			self.mult(hypo, self.likelihood(data, hypo))
		self.normalize()

	def likelihood(self, data, hypo):
		return {
				'Bowl 1': { 'vanilla': 0.75, 'chocolate': 0.25 },
				'Bowl 2': { 'vanilla': 0.50, 'chocolate': 0.50 },
			}[hypo][data]

cookies = Cookies()
print(cookies['Bowl 1'])
cookies.update('vanilla')
print(cookies['Bowl 1'])
cookies.update('vanilla')
print(cookies['Bowl 1'])
cookies.update('vanilla')
print(cookies['Bowl 1'])
cookies.update('vanilla')
print(cookies['Bowl 1'])
cookies.update('vanilla')
print(cookies['Bowl 1'])

# Using bayes module

from bayes import Bayes, DictModel

cookies_likelihoods = {
	'Bowl 1': { 'vanilla': 0.75, 'chocolate': 0.25 },
	'Bowl 2': { 'vanilla': 0.50, 'chocolate': 0.50 },
}

cookies = Bayes(DictModel(cookies_likelihoods))
print(cookies['Bowl 1'])
cookies.update('vanilla')
print(cookies['Bowl 1'])
