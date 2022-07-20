# own modules
import Zfmath
from Zfmath import add, substract

Zfmath.add(10,30)
add(10,20)
substract(80,50)

print("\n")
# Thirdy prty modules Internet
import ipaddress

Id_red= "192.168.36.0/24"
ip=ipaddress.IPv4Network(Id_red)
print("La mascara de Subred es:",ip.netmask)

print("\n")
# Python modules
import datetime
from datetime import timedelta, date

print(datetime.date.today())
print(datetime.timedelta(minutes=70))
print(timedelta(seconds=365))
print(date.today())
