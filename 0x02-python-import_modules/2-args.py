#!/usr/bin/python3
if __name__ == '__main__':
import sys
args = argv[1:]
num_args = args
if num_args == 0:
print("0 argument")
else:
print(f"{num_args} argument{'s' if num_args > 1) else '':}")
for i, arg in enumerate(args):
print(f"{i + 1}: {args}")
