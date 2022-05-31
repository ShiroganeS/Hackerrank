if __name__ == '__main__':
    n = int(input())
    arr = [int (i) for i in input().split()]
    fir_max = max (arr[0],arr[1])
    sec_max = min (arr[0],arr[1])
    for i in range(0,n):
        if arr[i] > fir_max:
            sec_max = fir_max
            fir_max = arr[i]
        elif arr[i] > sec_max and fir_max != arr[i]:
            sec_max = arr[i]
        elif arr[i] < fir_max and fir_max == sec_max:
            sec_max = arr[i] 
    print (sec_max)