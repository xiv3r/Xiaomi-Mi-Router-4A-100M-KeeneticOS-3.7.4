mount -o remount,size=100% /tmp

echo -1000 > /proc/$$/oom_score_adj
sync

if [ -f "/etc/init.d/sysapihttpd" ] ;then
    /etc/init.d/sysapihttpd stop
fi


ifdown wan

wifi down
rmmod mt7628
rmmod mt7613

sleep 10
cd /tmp
dd if=/dev/mtd3 of=1.bin
dd if=1.bin of=x1.bin bs=1 count=1024
dd if=1.bin of=2.bin ibs=1 skip=32768
dd if=2.bin of=x2.bin bs=1 count=1536
dd if=1.bin of=x3.bin ibs=1 skip=2560
cat x*.bin > eeprom_mod.bin
rm 1.bin 2.bin x*.bin
dd if=/dev/mtd0 of=backup.bin
sleep 10

gpio 1 1
gpio 2 0
