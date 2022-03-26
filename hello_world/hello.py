class Text:
	def __init__(self, str1, str2):
		self.str1 = str1
		self.str2 = str2

	def hello_world(self):
		str = f"{self.str1} {self.str2}!"
		return str.title()

hw = Text("hello", "world")
print(hw.hello_world())