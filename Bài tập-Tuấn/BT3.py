class inforSV():
    def __init__(self,hoten = "" , namsinh =0, quequan ="",noio="",truong="",khoa="",chuyennganh=""):
        self.ten = hoten
        self.namsinh = namsinh
        self.quequan = quequan
        self.noio = noio
        self.truong = truong
        self.khoa = khoa
        self.chuyenN = chuyennganh
    def input(self):
        while True:
            self.ten = input("Nhập tên : ").strip()
            if self.ten != "" : break
        while True:
            self.namsinh = input("Nhập năm sinh : ").strip()
            if self.namsinh != "" and self.namsinh != 0 : break
        while True:
            self.quequan = input("Nhập quê quán : ").strip()
            if self.quequan != "" : break
        while True:
            self.noio = input("Nhập nơi ở hiện tại : ").strip()
            if self.noio != "" : break
        while True:
            self.truong = input("Nhập trường : ").strip()
            if self.truong != "" : break
        while True:
            self.khoa = input("Nhập khoa : ").strip()
            if self.khoa != "" : break
        while True:
            self.chuyenN = input("Nhập chuyên ngành : ").strip()
            if self.chuyenN != "" : break
    def show(self):
        print("Thông tin vừa nhập:")
        print("Họ tên:",self.ten)
        print("Năm sinh:",self.namsinh)
        print("Quê quán:",self.quequan)
        print("Nơi ở hiện tại:",self.noio)
        print("Trường:",self.truong)
        print("Khoa:",self.khoa)
        print("Chuyên ngành:",self.chuyenN)
info = inforSV()
info.input()
info.show()
