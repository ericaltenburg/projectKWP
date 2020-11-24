import os, sys

def main(argv):
	for opt in argv: 
		found = os.system("python grabber.py | grep " + opt + " > .temp.txt")
		if os.path.isfile(".temp.txt") > 0:
			print("In stock")
		else:
			print("Not in stock")

if __name__ == "__main__":
   main(sys.argv[1:])