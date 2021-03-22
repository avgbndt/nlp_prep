import re
import csv

class Normalize(object):

	def __init__(self, route):
		self.route = route
		self.contents = []
		self.new = []

	def load(self):
		if ".csv" in self.route:
			with open(self.route, encoding='utf-8',newline='') as file:
				reader = csv.reader(file, delimiter=',', quotechar='"')
				for row in reader:
					self.contents.append(row[0])
		else:
			pass

	def show(self):
		x = [print(f"{i} \n") for i in self.contents[:20]]

	def clean(self, text):
		
		subs = {
			"https?:\S*" : "",
			"\." : "ENDOFSENTENCE",
			"\W+" : " ",
			"ENDOFSENTENCE" : "."
		}

		output_text = text
		
		for regex, sub in subs.items():
			output_text = re.sub(regex, sub, output_text)
		
		return output_text

	def clean_contents(self):
		self.contents = [self.clean(i).strip() for i in self.contents]