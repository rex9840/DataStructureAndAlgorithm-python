def gcd( dividend :int,divisor :int  ) ->  int:
    if divisor==0:
         return dividend 
    else:
        reminder:int = dividend % divisor
        return gcd(divisor,reminder)



if __name__=="__main__":
    try:
        number1,number2= [int(input("enter a number:")),int(input("enter another number:"))]
        if number1>number2:
            print(gcd(dividend=number1,divisor=number2))
        else:
            print(gcd(dividend=number2,divisor=number1))
    except ValueError:
        print("Value must be integer")    
        
        
        
    
    
    
    
    
    
    
    
    

