import telnetlib
import getpass
my_device = ['192.168.118.131', '192.168.118.132', '192.168.118.133']
for device in my_device:
    user = 'veru'
    password = getpass.getpass()
#    password = 'veru'
    tn = telnetlib.Telnet(device)

    tn.read_until(b'Username: ')
    tn.write(user.encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')
    tn.write(b'terminal length 0\n')
    tn.write(b'terminal length 0\n')
    tn.write(b'conf t\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 192.168.118.2\n')
    tn.write(b'exit\n')
    tn.write(b'sh ip int bri\n')

    tn.write(b'exit\n')

    result = tn.read_all().decode()
    print(result)
    print('++======++========++========++========')

