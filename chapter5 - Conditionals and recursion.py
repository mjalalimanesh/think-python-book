
####################  5_1  #################### 
import time

total_seconds = round(time.time())

total_seconds_in_this_day = (total_seconds % (3600*24)) + 4*3600 + 30*60
days_before = total_seconds // (3600*24)


hours_in_this_day = (total_seconds_in_this_day // 3600)
minutes_in_this_day =  (total_seconds_in_this_day % 3600) // 60
seconds_in_this_day = (total_seconds_in_this_day % 3600) % 60

####################  5_2  #################### 

def check_fermat(a, b, c, n):
    if n < 3:
        print('n must be greater than 2')
        return
    
    if a**n + b**n == c**n:
        print("Fermat was wrong")
    else:
        print("No, that doesn't work")

a = int(input("enter a  :  "))
b = int(input("enter b  :  "))
c = int(input("enter c  :  "))
n = 3

#check_fermat(a, b, c, n)

####################  5_9  #################### 
def do_n(func, n):
    if n <= 0:
        return
    func()
    do_n(func, n-1)
    
def myfunc():
    print("Hello")

#do_n(myfunc, 3)
