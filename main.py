import threading
import itertools
import zipfile


class Crack:
    def __init__(self):
        self.max_num = int(input("Max num: "))
        self.filename = input("Filename: ")
        self.pwd = []
        for i in range(self.max_num):
            i += 1
            threading.Thread(target=self.pre_guess_pwd(i)).run()
        for i in range(int(input()))

    def unzip(self):
        file = zipfile.ZipFile(self.filename)
        file.extractall("./")

    def pre_guess_pwd(self, guess_num: int):
        tmp = itertools.combinations("1234567890!@#$%^&*()-=_+~`qwertyuiop\\|asdfghjkl;zxcvbnm,./:<>?", guess_num)
        for it in tmp:
            self.pwd.append("".join(it))

    def guess(self, pwd):
        file = zipfile.ZipFile(self.filename)
        for i in pwd:
            file.extractall(pwd=pwd)


if __name__ == '__main__':
    crack = Crack()
