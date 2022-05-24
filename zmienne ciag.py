from multiprocessing.sharedctypes import Value

if __name__ == '__main__':
    #n = int(input())
    n = 100
    for item in range(1,n+1,2):
        print(item, end="\r")