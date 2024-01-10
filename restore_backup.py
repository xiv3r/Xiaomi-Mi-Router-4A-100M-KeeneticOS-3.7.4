import os
import sys
import time
import telnetlib
import ftplib
import gateway

router_ip_address=gateway.get_ip_address()

print()
print()

try:	
	tn = telnetlib.Telnet(router_ip_address)
except:
	print ("telnet сервер не запущен")
	time.sleep(10)
	os.system('!Start.bat')

tn.read_until(b"XiaoQiang login:")
tn.write(b"root\n")
tn.read_until(b"Password:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"wifi down\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"rmmod mt7628\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"rmmod mt7613\n")
tn.read_until(b"root@XiaoQiang:~#",20)
tn.write(b"exit\n")

try:	
	ftp=ftplib.FTP(router_ip_address)
except:
	print ()
	print ("ftp сервер не запущен")
	print ()
	print ("Выполните ещё раз пункт [11] - Connect to router")
	print ()
	sys.exit(1)

try:	
	file1=open('data/backup.bin', 'rb')
except:
	print ("backup.bin не найден")
	sys.exit(1)


try:	
	file2=open('flashall.sh', 'rb')
except:
	print ("Не найден скрипт")
	sys.exit(1)



print ("Загружаем данные на Xiaomi.")
ftp.storbinary(f'STOR /tmp/backup.bin', file1)
ftp.storbinary(f'STOR /tmp/flashall.sh', file2)
file1.close()
file2.close()
ftp.quit()

#############################################

try:	
	tn = telnetlib.Telnet(router_ip_address)
except:
	print ("telnet сервер не запущен")
	time.sleep(10)
	os.system('!Start.bat')

tn.read_until(b"XiaoQiang login:")
tn.write(b"root\n")
tn.read_until(b"Password:")
tn.write(b"root\n")
tn.read_until(b"root@XiaoQiang:~#")
tn.write(b"sh /tmp/flashall.sh >/dev/null 2>&1 &\n")
tn.read_until(b"root@XiaoQiang:~#",240)
tn.write(b"exit\n")
tn.close()
time.sleep(20)

os.system('cls')
print ("Записываю прошивку.")
print ('')

#############################################

print ("Ждите ~4-5 минут.")
print ("Не выключайте роутер!!!")
time.sleep(240)
print ('')
print ('Роутер перезагружается, ждем ~60 секунд.')
print ('')
print ('')
time.sleep(50)

os.system('cls')
print ('Заходим в браузере по адресу 192.168.31.1')


print ('')
print ('')
print ('')
print ('')
sys.exit(1)
