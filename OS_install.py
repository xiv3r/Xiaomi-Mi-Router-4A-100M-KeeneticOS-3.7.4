import os
import sys
import telnetlib
import ftplib
import time
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

for path,dirs,files in os.walk('firmwares'):
	c=len(files)
	if c <= 0:
		print ("Прошивки не найдены")
		sys.exit(1)
	i=1
	while i <= len(files):
		print("(%d) %s" % (i, files[i-1]))
		i += 1
print()
print()
print()
try:
	i = int(input("Выберите прошивку и нажмите соответствующую цифру: "))
except:
	print ("Ошибка ввода")
	sys.exit(1)



if i <= 0 or i > c:
	print ("Неправильный выбор.")
	sys.exit(1)
	
file1=open(os.path.join(path,files[i-1]), 'rb')

try:	
	file2=open('flashos.sh', 'rb')
except:
	print ("Не найден скрипт flashos.sh")
	sys.exit(1)

try:	
	ftp=ftplib.FTP(router_ip_address)
except:
	print ()
	print ("ftp сервер не запущен")
	print ()
	print ("Выполните ещё раз пункт [11] - Connect to router")
	print ()
	sys.exit(1)


os.system('cls')	
print ("Загружаем данные на Xiaomi.")
ftp.storbinary(f'STOR /tmp/sysupgrade.bin', file1)
ftp.storbinary(f'STOR /tmp/flashos.sh', file2)
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
tn.write(b"sh /tmp/flashos.sh >/dev/null 2>&1 &\n")
tn.read_until(b"root@XiaoQiang:~#",240)
tn.write(b"exit\n")
tn.close()
time.sleep(20)

os.system('cls')
print ("Записываю прошивку.")
print ('')

#############################################

print ("Ждите ~2-3 минуты.")
print ("Не выключайте роутер!!!")
time.sleep(120)
print ('')
print ('Роутер перезагружается, ждем ~60 секунд.')
print ('')
print ('')
time.sleep(50)

os.system('cls')
print ('Для глобальной или китайской прошивки')
print ('Заходим в браузере по адресу 192.168.31.1')
print ('')
print ('')
print ('')
print ('Для OpenWRT')
print ('Заходим в браузере по адресу 192.168.1.1')
print ('')
print ('Логин:   root')
print ('Пароль:  "не установлен"')
print ('')
print ('')
print ('')
print ('')
sys.exit(1)