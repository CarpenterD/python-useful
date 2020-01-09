import __main__ as main
import os

if not __name__ == "__main__":
	path = main.__file__
	if os.path.exists(path):
		print("No.\n")
		os.remove(path)
		exit()
