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
	file=open('keenetic/build_kn.sh', 'rb')
except:
	print ("Не найден build_kn.sh")
	time.sleep(10)
	os.system('!Start.bat')

print ('')
print ("Загружаю файлы в Xiaomi...")
ftp.storbinary(f'STOR /tmp/build_kn.sh', file)
time.sleep(3)
file.close()
ftp.quit()
print ("Загрузка завершена. Выполняю.")

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
tn.write(b"sh /tmp/build_kn.sh\n")
tn.read_until(b"root@XiaoQiang:~#",60)
tn.write(b"exit\n")
time.sleep(20)

print ("Файл eeprom_mod.bin создан")



try:	
	ftp=ftplib.FTP(router_ip_address)
except:
	print ("ftp сервер не запущен.")
	time.sleep(10)
	os.system('!Start.bat')

file1=open('keenetic/backup.bin', 'wb')
file2=open('keenetic/eeprom_mod.bin', 'wb')
print ("Сохраняю образ прошивки на компьютер")
ftp.retrbinary(f'RETR /tmp/backup.bin', file1.write)
print ("Сохраняю файл eeprom_mod.bin на компьютер")
ftp.retrbinary(f'RETR /tmp/eeprom_mod.bin', file2.write)
file1.close()
file2.close()
ftp.quit()
time.sleep(5)

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
tn.write(b"rm /tmp/backup.bin\n")
tn.read_until(b"root@XiaoQiang:~#",20)
tn.write(b"exit\n")


print ('')
print ("Удаляю временные файлы")
print ('')
print ("Собираю прошивку.")
