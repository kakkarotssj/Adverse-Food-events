import csv


class Database:
	def __init__(self):
		filepath = "/Users/sid/Downloads/adverse-food-events/CAERS_ASCII_2004_2017Q2.csv"

		self.d = {}

		with open(filepath, 'r') as f:
			mycsv = list(csv.reader(f))

			for row in mycsv:
				column11 = row[11].split(',')
				for item in column11:
					if item in iter(self.d):
						if not row[4] in self.d and self.d[item][0] != 0:
							self.d[item].append(row[4])
							self.d[item][0] -= 1
					else:
						self.d[item] = []
						self.d[item].append(5)
						self.d[item].append(row[4])


	def get_data(self):
		return self.d

