

class Polynomial:
	def __init__(*coefs):
		self.coefs = coefs

	def get_degree():
		l = len(self.coefs)

		for i in range(l - 1, -1, -1):
			if self.coefs[i] != 0:
				return i

		return 1
