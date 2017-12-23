

import functions as fc
import knowledge as know
import nlp

ListOfFunctions = [
	fc.Doan,
	fc.Duong,
	fc.DuongTrungTruc,
	fc.DoanTrungBinh,
	fc.TamGiac,
	fc.TamGiacVuong,
	fc.TamGiacCan,
	fc.TamGiacVuongCan,
	fc.TamGiacDeu,
	fc.TrungTuyen,
	fc.DuongTronNgoaiTiep,
	fc.DoanPhanGiac,
	fc.QuaMotDiemVaSongSongVoiDuong,
	fc.QuaMotDiemVaSongSongVoiDoan,
	fc.QuaMotDiemVuongGocVoiDuong,
	fc.QuaMotDiemVuongGocVoiDoan,
	fc.TrungDiem,
	fc.NamGiua,
	fc.GiaoDiemDoan,
	fc.DiemTrongTamGiac,
	fc.DiemNgoaiTamGiac,
	fc.DiemThuocDuongThang,
	fc.HaiDoanThangSongSong,
	fc.HaiDoanThangVuongGoc,
	fc.TrongTam,
	fc.DuongCaoTamGiac,
	fc.TrucTam,
	fc.GiaoDiemDuongDoan,
	fc.GiaoDiemHaiDuong,
	fc.DoiXungQuaCanh,
	fc.DoiXungQuaDiem,
	fc.TuGiac,
	fc.Tia,
	fc.TiaNamGiuaHaiTia,
	fc.HaiTiaDoiNhau,
	fc.ThuocDuongTron,
	fc.NgoaiDuongTron,
	fc.HinhThang,
	fc.HinhThangCan,
	fc.HinhThangVuong,
	fc.HinhBinhHanh,
	fc.HinhThoi,
	fc.HinhVuong,
	fc.HinhChuNhat,
	fc.TiaPhanGiac,
	fc.DiemThuocTia,
	fc.GiaoDiemHaiTia,
	fc.GiaoDiemTiaDoan,
	fc.GiaoDiemHaiDuongCheoTuGiac
]


class Knowledge(object):
	def __init__(self):
		self.num = 0
		self.funcs = []
	

class ChatBot(object):

	def loadData(self):

		print("Đang nạp kiến thức...", end=' ')

		self.knowl = Knowledge()
		f = open('../data/cstt.txt')		
		num = int(f.readline())

		self.knowl.num = num
		self.knowl.funcs = []
		for i in range(num):
			n_des = int(f.readline())
			des = []
			for j in range(n_des):
				s = f.readline()
				des.append(s[ : len(s) - 1])			
			tys = []
			for j in range(n_des):
				s = f.readline()
				tys.append(s[ : len(s) - 1])
			self.knowl.funcs.append(know.Function(des, ListOfFunctions[i], tys))

		print("OK")

		print("Đang tạo từ điển...", end=' ')
		nlp.loadData()
		nlp.learnData()
		print("OK")


	def __init__(self):
		print('Chatbot đang được khởi tạo...')
		self.loadData()		
		print('OK')

	def process(self):
		print('Xin chào! Tôi là Bot siêu thông minh =)) ')
		print('Hãy tin tưởng ở tôi, tôi hứa sẽ luôn làm bạn thất vọng.')
		print('Bạn hãy nhập vào một câu để vẽ hình bạn muốn :D')
		print("Hãy gõ thứ gì đó...")
		while True:
			sentence = input('Nhập một câu (không dấu): ')
			L = nlp.getTheSame(sentence)
			# khong tim thay
			if L == None:
				print('Tôi chưa hiểu ý bạn. Xin thử lại với câu khác.')
				continue
			args = nlp.getNames(sentence)
			found = -1
			func = None
			for index in L:
				print('Có phải ý của bạn là: ', end =' ')
				func = self.knowl.funcs[index[1]]
				func.getDescription(args)
				
				if not Enter():
					continue
				else:
					found = index[1]
					break
			if found == -1:
				print('Tôi chưa hiểu ý bạn. Xin hãy tiếp tục...')
				continue
			# pass mind
			# Kiem tra tham so
			typeOfargs = [know.getType(a) for a in args]
			
			again = False
			if typeOfargs.count(None) > 0:
				print('Vậy thì hãy điền lại các tham số cho đầy đủ nào...')
				again = True
			if not again and typeOfargs != func.typeOfArgs:
				print('Tham số bạn nhập chưa khớp!')
				again = True			
			if again:				
				print('Ví dụ: ', nlp.sentences[found])
				args = EnterInput(func.typeOfArgs).split()			
				typeOfargs = [know.getType(a) for a in args]				

				while typeOfargs != func.typeOfArgs:
					print('Xin hãy thử lại...')
					args = EnterInput(func.typeOfArgs).split()			
					typeOfargs = [know.getType(a) for a in args]					

			# pass tham so
			# Ve
			func.func(args)


def EnterInput(typeOfArgs):	
	print('Bạn cần nhập theo thứ tự:', end=' ')
	for tys in typeOfArgs:
		print(tys, end=', ')
	print()
	s = input('Ngăn cách nhau bởi dấu cách: ')	
	return s


def Enter():
	while True:
		select = input("Yes or No? ")
		if select.upper() == 'NO':						
			return False
		if select.upper() == 'YES':				
			return True
