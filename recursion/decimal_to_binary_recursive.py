def binary_conversion(number:int) -> int:    
        if number==0:
            return 0
        else:
            return number%2 +10*binary_conversion(number//2)
        
if __name__=="__main__":
   number= int(input("Enter the number:"))
   print(binary_conversion(number))
