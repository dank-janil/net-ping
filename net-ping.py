from functions import  *
from pyfiglet import Figlet
import sys


f = Figlet(font='slant')
print(f.renderText('net-ping'))
try:
    str(sys.argv[1])
    print('Network : ' + str(sys.argv[1]))
    scan_multi(str(sys.argv[1]))
except IndexError:
    print("==============Penggunaan Salah=================")
    print("Penggunaan : python net-ping.py network/netmask")
    print("Contoh : python net-ping.py 192.168.1.0/24")
    print("===============================================")


