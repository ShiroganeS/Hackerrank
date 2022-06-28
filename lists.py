if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        name, *line = input().split()
        if name == "insert":
               index = int(line[0])
               object = int(line[1])
               list.insert(index,object)
        elif name == "print":
                print (list)  
        elif name == "remove":
                list.remove(int(line[0]))
        elif name == "append":
                list.append(int(line[0])) 
        elif name == "sort":
                list.sort()
        elif name == "pop": 
                list.pop()
        elif name == "reverse":
                 list.reverse()