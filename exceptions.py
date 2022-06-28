if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = (input().split())
        try:
            print (int(int(n) / int(m)))
        except ZeroDivisionError as e:
            print ("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print ("Error Code:", e)