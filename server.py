import sys
import glob
import serial
PORT = "COM4"
# position values
arm_pos = 30
base_pos = 200
# cred https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python#14224477
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
s = serial.Serial(PORT,baudrate = 9600, timeout=1)

def send_commands_motor(val,val2):
	positions = '{},{}\n'.format(val,val2).encode('ascii')
	s.write(positions)

try:
	

	while 1:

		arduino_output = s.readline().decode("ascii")
		print(arduino_output)
		send_commands_motor(arm_pos,base_pos)
		

except KeyboardInterrupt as e:
	print("Program Closed")
	exit()

if __name__ == '__main__':
	print("Wifi camera Motor Server\n\n")
	print(serial_ports())
	s = serial.Serial(PORT)
	
	acc = ""
	
	for i in range(0,20):
		acc += s.read().decode("ascii")
	print(acc)
	string = '{},{}\n'.format(arm_pos,base_pos)


	s.write(string.encode('ascii'))
	
	for i in range(0,100):
		acc += s.read().decode("ascii")
		print(acc, end="")
	print()
	s.close()
	print(s.is_open)
	print(("port closed", "port open")[s.is_open == True])
	
	if s.is_open == True:
		s.close()

