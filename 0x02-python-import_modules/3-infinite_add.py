#!/usr/bin/python
if __name__=='__main__':
    
    import sys
    
    args = sys.argv[1:]
    
    total = 0
    
    for arg in args:
    
        total += int(arg)
    
    print(total)
