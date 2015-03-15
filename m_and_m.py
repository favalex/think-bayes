from collections import defaultdict
from bayes import Bayes, DictModel

mix94 = defaultdict(int, yellow=20, red=20, green=10, orange=10, tan=10)
mix96 = defaultdict(int, blue=24, green=20, orange=16, yellow=14, red=13, brown=13)

m_and_m_likelihoods = {
	'A': dict(bag1=mix94, bag2=mix96),
	'B': dict(bag1=mix96, bag2=mix94),
}

m_and_m = Bayes(DictModel(m_and_m_likelihoods))
m_and_m.print()
m_and_m.update('bag1', 'yellow')
m_and_m.update('bag2', 'green')
m_and_m.print()
m_and_m.update('bag1', 'tan')
m_and_m.update('bag2', 'green')
m_and_m.print()
m_and_m.update('bag2', 'tan')
m_and_m.print()
