def raised(number:float , power:int ) -> float:
    if power==0:
        return 1
    else:
        return number*raised(number,power-1)



if __name__=="__main__":    
        number,power=[float(input("enter number:")),int(input("enter power:"))]
        answer=raised(number,power)
        if answer.__str__()[-2]=='.':
           print(int(answer))
        else :
            print('%.2f' %answer )                      #place value



    