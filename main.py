import sys
import time
import zipfile
import itertools
from concurrent.futures import ProcessPoolExecutor


class Crack:
    def __init__(self):
        self.max_num = int(input("Max num: "))
        self.filename = input("Filename: ")
        self.pwd = []
        start_t = time.time()
        print("Init ~~~")
        init_pool = ProcessPoolExecutor(8)
        for i in range(self.max_num):
            i += 1
            init_pool.submit(self.pre_guess_pwd(i))
        init_pool.shutdown(True)
        self.len_pwd = len(self.pwd)
        print("Cracking ~~~")
        pwd_list = [self.pwd[i:i + 20] for i in range(0, len(self.pwd), 20)]
        crack_pool = ProcessPoolExecutor(8)
        for i in pwd_list:
            crack_pool.submit(self.guess(i))
        crack_pool.shutdown(True)
        end_t = time.time()
        print("Cost :" + str(end_t - start_t))
        sys.exit(0)

    def pre_guess_pwd(self, guess_num: int):
        tmp = itertools.combinations("1234567890!@#$%^&*()-=_+~`qwertyuiop\\|asdfghjkl;zxcvbnm,./:<>?", guess_num)
        tmp_pwd = []
        for i in tmp:
            tmp_pwd.append("".join(i))

        self.pwd += tmp_pwd

    def unzip(self):
        file = zipfile.ZipFile(self.filename)
        file.extractall("./")

    def guess(self, pwd):
        file = zipfile.ZipFile(self.filename)
        for i in pwd:
            file.extractall(pwd=bytes(i.encode()))


if __name__ == '__main__':
    crack = Crack()
