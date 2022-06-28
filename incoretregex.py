import re
if __name__ == '__main__':
    for _ in range(int(input())):
        x = input ()
        try:
            re.compile (x)
            print ("True")
        except:
            print ("False")