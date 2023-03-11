#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    num_args = len(args) - 1
    if num_args == 0:
        print("0 arguments")
    else:
        print(f"{num_args} argument{'s' if num_args>1 else''}")
        for i in range(num_args):
            print("{}: {}".format(i + 1, args[i + 1]))
