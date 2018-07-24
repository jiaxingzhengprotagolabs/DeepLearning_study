import sys 
import getopt

def main(argv):
	if argv == None:
		print("world@")
	else:
		print(argv)

print("hello")

if __name__ == '__main__':
	main(sys.argv)