conditional_message ='Number must be positive integer'
def sum(number: int) -> int :
    try:
        assert number >= 0 , conditional_message   
        if number == 0:
            return number
        else:
            return number+sum(number-1)
    except AssertionError as error:
        print(error)
        exit() 
    
    
if __name__=="__main__":
    try:
        number = int(input("Enter a number: "))
        print(sum(number))
    except ValueError as error:
        print(conditional_message)