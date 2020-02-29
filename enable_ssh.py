import time
import telnetlib

#my_device = ['192.168.118.131']
my_device = ['192.168.118.132', '192.168.118.133']

for device in my_device:
#ip = '192.168.118.132'
    user = 'veru'
    password = 'veru'
    tnt = telnetlib.Telnet(device)

    tnt.read_until(b'Username: ')
    tnt.write(user.encode() + b'\n')
    tnt.read_until(b'Password: ')
    tnt.write(password.encode() + b'\n')

    tnt.write(b'terminal length 0\n')
    tnt.write(b'conf t\n')
    tnt.write(b'ip domain name veru.com\n')
    tnt.write(b'line vty 0 4\n')
    tnt.write(b'login local\n')
    tnt.write(b'trans input all\n')
    tnt.write(b'exit\n')
    tnt.write(b'crypto key gene rsa\n')
    time.sleep(3)
    tnt.write(b'yes\n')
    time.sleep(3)
    tnt.write(b'1024\n')
    tnt.write(b'end\n')
    time.sleep(3)
    result = tnt.read_all().decode()
    print(result)


