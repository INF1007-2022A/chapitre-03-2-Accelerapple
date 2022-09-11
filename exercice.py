#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2/resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	prod_scalaire = v1[0]*v2[0] + v1[1]*v2[1]
	if prod_scalaire == 0:
		return True
	else:
		return False

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	output = []
	for v in values:  # La variable v contient une valeur de la liste.
		if v >= 0:
			output.append(v)
	return sum(output)/len(output)

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = tens = fives = ones = 0
	while value != 0:
		if value >= 20:
			twenties += 1
			value -= 20
		elif value >= 10:
			tens += 1
			value -= 10
		elif value >= 5:
			fives += 1
			value -= 5
		elif value >= 1:
			ones += 1
			value -= 1

	return (twenties, tens, fives, ones);

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	i = 0
	j = 0
	while True:
		if abs_value - base**i >= 0:
			i += 1
		elif abs_value - base**i < 0:
			i -= 1
			if i < 0:
				i = 0
			# print("i 1: ", i)
			break
		else:
			print("how")

	while abs_value != 0:
		if abs_value - j*base**i >= 0 and j <= base:
			j += 1
			# print("j: ", j)
		else:
			j -= 1
			abs_value = abs_value - j*base**i
			result += digit_letters[j]
			if abs_value == 0 and i != 0:
				while i != 0:
					result += digit_letters[0]
					i -= 1
			i -= 1
			# print("i: ", abs_value, j)
			j = 0



		# 64 32 16 8 4 2 1
		#  6  5  4 3 2 1 0
		# 2* 2* 2* 2*

	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result = "-" + result

	if result == "":
		result += "0"
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(123, 16, "0123456789ABCDEF"))
