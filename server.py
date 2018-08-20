import sys
import glob
import serial
import json
from pprint import pprint
PORT = "COM4"
# position values
arm_pos = 30
base_pos = 200
filename = "serial_data.json"
sensor = {"data":[]}
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
	



if __name__ == '__main__':
	print("Wifi camera Motor Server\n\n")
	print(serial_ports())
	exit = True
	i = 0
	try:
		while exit:
			arduino_output = s.readline().decode("ascii")
			if '\n' in arduino_output:
				arduino_output = arduino_output.replace(',\n','')
				sensor["data"].append(arduino_output.split(","))
				pprint(sensor)
			elif 'end' in arduino_output:
				exit = False
				if s.is_open == True:
					s.close()
				with open(filename, 'w') as file:
				 	file.write(json.dumps(sensor))
				print("Exit loop")
			# if 'end' in arduino_output:
			# 	removeEND = arduino_output.replace(",","")
			# 	splitData = removeEND.split(",")
			# 	sensor["data"][0] = splitData
			# 	print(str(sensor) )

			# 	with open(filename, 'w') as file:
			# 	 	file.write(json.dumps(sensor))
			# 	exit = False
			# 	if s.is_open == True:
			# 		s.close()
			# 	print("Exit loop")
		print("exited")
			# send_commands_motor(arm_pos,base_pos)
	except KeyboardInterrupt as e:
		print("Program Closed")
		if s.is_open == True:
			s.close()
		exit()
	# s = serial.Serial(PORT)
	
	# acc = ""
	
	# for i in range(0,20):
	# 	acc += s.read().decode("ascii")
	# print(acc)
	# string = '{},{}\n'.format(arm_pos,base_pos)


	# s.write(string.encode('ascii'))
	
	# for i in range(0,100):
	# 	acc += s.read().decode("ascii")
	# 	print(acc, end="")
	# print()
	# s.close()
	# print(s.is_open)
	# print(("port closed", "port open")[s.is_open == True])
	
	# if s.is_open == True:
	# 	s.close()

