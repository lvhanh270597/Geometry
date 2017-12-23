

typeOfObjects = ['diem', 'doan thang', 'duong thang', 'tam giac', 'tu giac', 'tia', 'duong tron']

class Function(object):
	""" """
	def __init__(self, description, function, typeOfArguments):
		self.des = description
		self.func = function
		self.num = len(typeOfArguments)
		self.typeOfArgs = typeOfArguments
	def getDescription(self, ListOfArguments):
		len_args = len(ListOfArguments)
		checkIndex = [False] * len_args
		typeOfargs = [getType(a) for a in ListOfArguments]
		
		new_args = []
		for i in range(self.num):
			for j in range(len_args):
				if (typeOfargs[j] == self.typeOfArgs[i]) and (not checkIndex[j]):
					new_args.append(ListOfArguments[j])
					checkIndex[j] = True

		############################################################################
		if len(new_args) != len(self.typeOfArgs):
			ListOfArguments = []

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
			if x.startswith('d') and x[1].isnumeric(): return typeOfObjects[2]
			if x[0].isupper() and x[1].islower(): return typeOfObjects[5]
	if len(x) == 3:		
		if (x[0] == '(') and (x[2] == ')'):
			return typeOfObjects[6]
		if x.isupper():
			return typeOfObjects[3]
	if len(x) == 4:
		if x.isupper():
			return typeOfObjects[4]	
	return None

