def recursion(n:int) -> None:
    if n<1:
        print('n is less than 1')
    else:
        recursion(n-1)
        print(n)


#recursion brings a extra overhead(memory or time)
#use a loop(iteration) instead if there is a limiting factor in time or space 

#stack of the following program in memory 

'''
3 - recursion(1)
2 - recursion(2)
1 - recursion(3)
0 - recursion(4)
'''

#output 
'''
-> n is less than 1
    -> 1 (stack.pop(3))->(recursion(1))
        -> 2(stack.pop(2))->(recursion(2))
            -> 3(stack.pop(1))->(recursion(3))
                -> 4(stack.pop(0))->(recursion(4))
'''

from sys import setrecursionlimit


setrecursionlimit(100)

def factorial(n:int) -> int  :
    try:
        if n in [0,1]:
                return 1                 #base condition
        else :
                return n*factorial(n-1)  
    except RecursionError:
        print("Stack overflow")
        exit()      


def febo(number: int)-> int :
    try:
            
        if number in [0,1]:
            return number
        else:
            return febo(number-1)+febo(number-2)
    except RecursionError:
        print("Stack overflow")
        exit()    
    
    
    
    
    
    
    
if __name__== '__main__':
    try:
        number = int(input("Enter the number:"))
        # if number<1 :
        #     print("The factorial of negative number was given which doesn't exit ") 
        # else:
        #     print(factorial(number))
        print(febo(n=number))
    except BaseException:
        print("Value of n must be positive integer ")
# recursion use extra overhead call stack




''' when to use recursion:
when the problems can be easily break down into similar sub problems
when to transverse a tree








'''


''' when now to use recurion 
when time and space complexity matters 
recursion occupies more space in stack 
recursive can be slow when the time complexity is high 


'''




# x=0
# assert x==2 ,"x is 2 "


# assert is used to raise the flags for the error with the given message