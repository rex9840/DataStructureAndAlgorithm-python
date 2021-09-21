import sys 
sys.setrecursionlimit(100)


def fibonacci(number:int) -> int: 
    try:
        assert number>=0 , "index postion number must be non negative "    #acts as an throw statement 
        if number in [0,1]:
            return number 
        else:
            return fibonacci(number-1)+fibonacci(number-2)
    except AssertionError as error:   # it catches the error and prints it
        print(error)
        exit()
    except RecursionError as error:
        print("Stack overflow ")
        exit()
        
        
if __name__ == "__main__":
    try:
        num= int(input("Enter the term number :"))
        print(fibonacci(number=num))
    except ValueError as error:
        print("index postion number must be non negative ")
    
    