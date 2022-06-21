if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = sum (student_marks[query_name])/len (student_marks[query_name])
    result = '{:.{prec}f}'.format(result,prec=2)
    print (result) 
    #  ints = [56, 56, 45.5]
    # ints[0]
    # [
    #   "uczen1": [ 56, 56, 45.5 ],
#        "uczen2": []
    # ]