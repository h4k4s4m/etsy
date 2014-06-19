#Author: Sahm Samarghandi
#Created 12/28/13
#License: Free to use, distrubute, change, profit off of


import os


#this is my proof of concept try and catch error for input error checking

diditwork=False
while diditwork==False:
        diditwork=True
        try:
                a=raw_input("enter a number")
                a=int(a)
                b=(a+2)/2
        except ValueError:
                print("that didn't work, did it?")
                diditwork=False
                continue

#this is the end of the proof of concept thingy part
        
again=True
while again==True:
        def convert_temp(a, b):
                
                if b[0]=='c' or b[0]=='C':
                        x=((a*9)/5)+32
                        return x
                        
                elif b[0]=='f' or b[0]=='F':
                        x= ((a-32)*5)/9
                        return x
                else:
                        print("You typed something wrong\n\n\n")
                        return "bacon"

        def main():
                Dank="bacon"	
                while Dank =="bacon":
                        a=input("Please Enter Temperature to convert:   ")
                        print("\n")
                        b=raw_input("Please enter F or C for farenheit or celcius:   ")
                        print("\n")
                        Dank = convert_temp(a,b)

                while Dank !="bacon":
                        return Dank
        
        print(main())

        print("\n")
        test=raw_input("Do you want to convert another number?    ")

        if test[0]=="y" or test[0]=="Y":
                again=True

        else:
                again=False

        os.system('cls')


