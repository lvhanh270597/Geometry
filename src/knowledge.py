

typeOfObjects = ['diem', 'doan thang', 'duong thang', 'tam giac']

class Function(object):
	""" """
	def __init__(self, description, function, typeOfArguments):
		self.des = description
		self.func = function
		self.num = len(typeOfArguments)
		self.typeOfArgs = typeOfArguments
	def getDescription(self, ListOfArguments):
		for i in range(self.num - len(ListOfArguments)):
			ListOfArguments.append('___')
		res = ''
		for i in range(self.num):
			res += self.des[i] \
                               + ' ' + str(ListOfArguments[i]) + ' '
		print(res)
		return res

def getType(x):	
	if len(x) == 1:
		if x.isupper():
			return typeOfObjects[0]
		else:
			return typeOfObjects[2]
	if len(x) == 2: 
		if x.isupper():
			return typeOfObjects[1]
		else:
			if x.startswith('d'):
                                return typeOfObjects[2]
	if len(x) == 3:
		if x.isupper():
			return typeOfObjects[3]
	return None

