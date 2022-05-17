
def is_leap(year):
    leap = False
    #The year can be evenly divided by 4, is a leap year, unless:
    if year% 4 == 0:
       leap= True   
    #The year can be evenly divided by 100, it is NOT a leap year, unless:
    if year%100==0 and year%400 != 0:
        leap=False
    #The year is also evenly divisible by 400. Then it is a leap year.
  
    #Write your logic here
    
    return leap

year = int(raw_input())
result=is_leap(year)
print (result)
#my_list=[ 1800, 1900, 2100, 2200, 2300,2000, 2400]
#for year in my_list:
  # result= is_leap (year)
   #print(result)


