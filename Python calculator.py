gymimport math



def addition(a,b):
   return a + b
def subtract(a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide (a,b):
    return a/b
def remainder (a,b):
    return a%b
def sqrRoot (a):
    return math.sqrt(a)
    if(a<0):
        print("You have entered a negative number for square root!")
def square (a,b):
    i=1
    while(i<b):
        a=a*a
        i+=1
    return a
    if(b==0):

        a=a
    elif b<0:
        print("Please make a correct input!")

def ifLoops(a,b,decision):
    if decision=="+":
        return addition(a,b)
    elif decision=="-":
        return subtract(a,b)
    elif decision=="*":
        return multiply(a,b)
    elif decision=="^":
        return square(a,b)
    elif decision=="%":
        return remainder(a,b)
    elif decision=="s":
        return sqrRoot(a,b)




print ("These are the allowed operations.")    
print ("+ | Add")    
print ("- | Subtract")    
print ("* | Multiply")    
print ("/ | Divide")
print ("^ | Exponential")
print ("s | Square Root")
print ("% | Remainder")





while True:
    
    number1=input()
    try:
        number1=float(number1)
        decision=input()
        if decision=="+" or decision=="-" or decision=="/" or decision=="*" or decision=="%" or decision=="^":
            number2=float()
            number2=input()
            equals=input()
            if(equals!="="):
                print("Please make a correct input!")
            elif(equals=="="):
                final=ifLoops(float(number1),float(number2),decision)
                print(final)


        elif decision=="s":
                equals=input()
                if(equals!="="):
                    print("Please make a correct input!")
                elif (equals=="="):
                    final=sqrRoot(number1,number2)
                    print(final(number1,number2))
                    
    except:
        if number1=="+" or number1=="*" or number1=="-" or number1=="/" or number1=="^" or number1=="%":
            decision=number1
            number1=final
            
            number2=input()
            number2=float(number2)
            equals=input()
            if (equals!="="):
                print("Please make a correct input!")
            elif (equals=="="):
                final=ifLoops(float(number1),float(number2),decision)
                print(final)
        elif number1=="s":
            decision=number1
            number1=final
            equals=input()
            if(equals!="="):
                print("Please make a correct input!")
            elif(equals=="="):
                final=ifLoops(float(number1),float(number2),decision)
                print(final)
        elif number1=="Q" or number1=="q":
            break
        else:
            print("Please make a correct input!") 
    



                    






  
 
 
 
 

 


 