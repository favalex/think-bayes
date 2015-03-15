from bayes import Bayes, DictModel

cookies_likelihoods = {
	'Bowl 1': { 'vanilla': 0.75, 'chocolate': 0.25 },
	'Bowl 2': { 'vanilla': 0.50, 'chocolate': 0.50 },
}

cookies = Bayes(DictModel(cookies_likelihoods))
cookies.print()
cookies.update('vanilla')
cookies.print()
cookies.update('vanilla')
cookies.print()
cookies.update('vanilla')
cookies.print()
