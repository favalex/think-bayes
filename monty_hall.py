from bayes import Bayes, DictModel

monty_hall_likelihoods = {
	'Car A': { 'Picks A, Opens B': .5 },
	'Car B': { 'Picks A, Opens B': 0 },
	'Car C': { 'Picks A, Opens B': 1 },
}

monty_hall = Bayes(DictModel(monty_hall_likelihoods))
monty_hall.print()
monty_hall.update('Picks A, Opens B')
monty_hall.print()
