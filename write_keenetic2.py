import os
import sys
import telnetlib
import ftplib
import time
import gateway

router_ip_address=gateway.get_ip_address()
print ("")

try:	
	tn = telnetlib.Telnet(router_ip_address)
except:
	print ("telnet сервер не запущен")
	time.sleep(10)
	os.system('!Start.bat')
#=============================================



try:	
	ftp=ftplib.FTP(router_ip_address)
except:
	print ("ftp сервер не запущен.")
	time.sleep(10)
	os.system('!Start.bat')

try:	
	file1=open('keenetic/full_keenetic.bin', 'rb')
except:
	print ("Не найден full_keenetic.bin")
	time.sleep(10)
	os.system('!Start.bat')

try:	
	file2=open('keenetic/flashall_kn.sh', 'rb')
except:
	print ("Не найден flashall_kn.sh")
	time.sleep(10)
	os.system('!Start.bat')


print ('')
print ("Загружаю файлы в Xiaomi...")
ftp.storbinary(f'STOR /tmp/full_keenetic.bin', file1)
ftp.storbinary(f'STOR /tmp/flashall_kn.sh', file2)
time.sleep(3)
file1.close()
file2.close()
ftp.quit()
print ("Загрузка завершена")


#################################################
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
tn.write(b"sh /tmp/flashall_kn.sh >/dev/null 2>&1 &\n")
tn.read_until(b"root@XiaoQiang:~#",240)
tn.write(b"exit\n")
tn.close()
time.sleep(20)

os.system('cls')
print ("Записываю загрузчик и прошивку...")
print ('')
###########################################


print ("Ждите перезагрузку роутера. Примерно 5 минут.")
print ("Не выключайте роутер!!!")
time.sleep(300)
os.system('cls')

print ('')
os.system('cls')
print ('Заходим в браузере по адресу 192.168.1.1')


print ('')
print ('')
print ('')
print ('')
sys.exit(1)