#! /usr/local/bin/python3
import os

def CreateProcess(func,lparam):
	pid = os.fork()
	if pid == 0:
		func(lparam)
	return 0


if __name__ == '__main__':
	pid = os.fork()
	if pid == 0:
		print("I am Child")
	else:
		print("I am Parent")

print("END")

