import os
from termcolor import *


class main:
    def __init__(self):
        self.path = './'
        self.file = ''

    def mkdir(self, name):
        filename = self.path + name
        isExists = os.path.exists(filename)
        if not isExists:
            os.makedirs(filename)
            print(filename)
            return True
        else:
            print(filename, '目录已存在')
            return False

    def rmdir(self, name):
        filename = self.path + name
        if os.path.isdir(filename):
            for p in os.listdir(filename):
                self.rmdir(os.path.join(name,p))
            if os.path.exists(filename):
                os.rmdir(filename)
        else:
            print(filename, "不是文件夹")

    def rm(self, name):
        filename = self.path + name
        if os.path.isfile(filename):
            os.remove(filename)
        else:
            print(filename, '是文件目录')

    def touch(self, name):
        filename = self.path + name
        isExists = os.path.exists(filename)
        if not isExists:
            os.mknod(filename)
            print(filename, '创建成功')
            return True
        else:
            print(filename, '文件已存在')
            return False

    def ls(self, name = ''):
        filename = self.path + name
        color = 'green'
        for index, file in enumerate(os.listdir(filename)):
            if os.path.isfile(filename + '/' + file):
                color = "blue"
            else:
                color = "green"
            if (int(index) < len(os.listdir(filename)) - 1):
                print(colored(file, color), end='  ')
            else:
                print(colored(file, color))

    def open(self, name):
        filename = self.path + name
        isExists = os.path.exists(filename)
        if isExists:
            self.file = os.open(filename, os.O_RDWR | os.O_APPEND)
            print(filename, "opened")
        else:
            print(filename, 'not exists')

    def write(self, text):
        os.write(self.file, text.encode())
        print('写入成功')
        os.close(self.file)

    def cd(self, path):
        filepath = self.path + path
        isExists = os.path.exists(filepath)
        if isExists:
            self.path = filepath + '/'
        else:
            print(filepath, 'not exists')

    def read(self, name):
        filename = self.path + name
        isExists = os.path.exists(filename)
        if isExists:
            # 读取文本
            fd = os.open(filename, os.O_RDWR)
            ret = os.read(fd,200)
            print(
                colored(ret.decode(encoding='UTF-8', errors='strict'), 'red'))
        else:
            print(filename, "not exit")


def formcmd(system, commond):
    commond = commond.split()
    cmd1 = commond[0]
    if cmd1 == 'exit':
        pass
    else:
        if cmd1 == 'ls':
            try:
                cmd2 = commond[1]
            except:
                cmd2 = ''
        else:
            try:
                cmd2 = commond[1]
            except:
                print('请输入操作的对象')

        getattr(system, cmd1)(cmd2)


if __name__ == '__main__':
    system = main()
    print('当前目录为', os.getcwd(), '请选择操作')
    print('\n')
    print("exit :安全退出该文件系统,保存信息.")
    print("mkdir dirname :创建子目录.")
    print("rmdir dirname :删除子目录.")
    print("ls dirname :显示当前目录下信息.")
    print("cd dirname :更改当前目录.")
    print("touch filename :创建一个新文件.")
    print("write filename :选择一个打开的文件写入信息.")
    print("read filename :选择一个打开的文件读取信息.")
    print("rm filename :删除文件.")
    print("open filename :打开文件.")
    commond = ''
    while commond != 'exit':
        commond = input(os.getcwd() + system.path.replace('.', '') + ': ')
        formcmd(system, commond)
