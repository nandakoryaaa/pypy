class UserData:
	def __init__(self, str = None):
		self.name = ''
		self.score = 0
		self.level = 0
		self.apples = 0
		self.length = 0
		self.flags = 0
		if str is not None:
			self.from_string(str)

	def from_string(self, str):
		values = str.split(',')
		self.name = values[0]
		self.score = int(values[1])
		self.level = int(values[2])
		self.apples = int(values[3])
		self.length = int(values[4])
		self.flags = int(values[5])

	def to_string(self):
		return ','.join((self.name, str(self.score), str(self.level),
				str(self.apples), str(self.length), str(self.flags)))