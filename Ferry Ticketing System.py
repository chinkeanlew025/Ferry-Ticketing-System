import sys
import os
import datetime

def clear():
    os.system('cls')

def menu():
    clear()
    print("\n*********************************  Main Menu  **********************************")
    print("""\n\t\t\t\tFerry Ticketing System
        \t\tP-to Purchase Ticket
        \t\tV-to View Seating Arrangement
        \t\tQ-to Quit the system""")
    
    choice=input("\n\t\t\tEnter Your Choice:")

    if((choice=="p") or (choice=="P")):
        submenuP()
    elif((choice=="v") or (choice=="V")):
        submenuV()
    elif((choice=="q") or (choice=="Q")):
        submenuQ()
    else:
        print("\nInvalid choice. Please choose another one")
        print("\nPlease choose again from p.v.q")
        menu()

def submenuP():
    clear()
    print("\n*****************************  Purchasing Module  *****************************")
    print("""
    \t\tB–to purchase ticket for Business class
    \t\tE–to purchase ticket for Economy class
    \t\tM–to return to Main Menu""")
    
    choice=input("\n\t\tEnter Your Choice:")
    
    if ((choice=="B") or (choice=="b")): #choice.lower()
        B_class()
    elif((choice=="E") or (choice=="e")):
        E_class()
    elif((choice=="M") or (choice=="m")):
        menu()
    else:
        print("\nInvalid choice. Please choose another one")
        print("\nPlease choose again from b,e,m")
        submenuP()

def submenuQ():
    print("Thank You. Please choose us again!")
    sys.exit()


Bus_Ferry10 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry10=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry101 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry101=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry11 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry11=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry111 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry111=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry12 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry12=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry121 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry121=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry13 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry13=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry131 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry131=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry14 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry14=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry141 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry141=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry15 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry15=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry151 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry151=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry16 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry16=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry161 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry161=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry17 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry17=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]
Bus_Ferry171 = [0,0,0,0,0,0,0,0,0,0]
Eco_Ferry171=[0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0]


##FerryID,Business,Economy
##Ferry_List10=['0001',0,0] # 10 pl
Ferry_List10=['0001',0,0]
Ferry_List101=['0002',0,0] #101 lp
Ferry_List11=['0003',0,0] 
Ferry_List111=['0004',0,0]
Ferry_List12=['0005',0,0]
Ferry_List121=['0006',0,0]
Ferry_List13=['0007',0,0]
Ferry_List131=['0008',0,0]
Ferry_List14=['0009',0,0]
Ferry_List141=['0010',0,0]
Ferry_List15=['0011',0,0]
Ferry_List151=['0012',0,0]
Ferry_List16=['0013',0,0]
Ferry_List161=['0014',0,0]
Ferry_List17=['0015',0,0]
Ferry_List171=['0016',0,0]

    
def B_class():
    clear()
    zone="Business"
    now = datetime.datetime.now()
    date=now.strftime("%d/%m/%Y")
    for no in range (10,18):
        print (no,":00")
        no+=1
    time=float(input("\nEnter Your Booking Time:"))
    if((time<=17) and (time>=10)):
        name=input("\nEnter Your Name:")
        print("""\nSource and Destination
    PL-from Penang to Langkawi
    LP-from Langkawi to Penang""")
        choice=input("\nEnter Your Choice:")
        check_availB(name,zone,date,time,choice)
    else:
        print('\nInvalid Booking Time')
        B_class()
    
    
def E_class():
    clear()
    zone="Economy"
    now = datetime.datetime.now()
    date=now.strftime("%d/%m/%Y")
    for no in range (10,18):
        print (no,":00")
        no+=1
    time=float(input("\nEnter Your Booking Time:"))
    if((time<=17) and (time>=10)):
        name=input("\nEnter Your Name:")
        print("""\nSource and Destination
    PL-from Penang to Langkawi
    LP-from Langkawi to Penang""")
        choice=input("\nEnter Your Choice:")
        check_availE(name,zone,date,time,choice)
    else:
        print('\nInvalid Booking Time')
        E_class()

def check_availB(name,zone,date,time,choice):
    if(choice.upper()=='PL'):
        choice='From Penang To Langkawi'
        if(time=='10.00') or (time==10):
            if(Ferry_List10[1]!=10):
                B_seat=Ferry_List10[1]
                Ferry_ID=Ferry_List10[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List10[2]!=40):  #if both classes are full
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='11.00') or (time==11):
            if(Ferry_List11[1]!=10): #if using <= will face the limit problem
                B_seat=Ferry_List11[1]
                Ferry_ID=Ferry_List11[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List11[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='12.00') or (time==12):
            if(Ferry_List12[1]!=10):
                B_seat=Ferry_List12[1]
                Ferry_ID=Ferry_List12[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List12[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='13.00') or (time==13):
            if(Ferry_List13[1]!=10):
                B_seat=Ferry_List13[1]
                Ferry_ID=Ferry_List13[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List13[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='14.00') or (time==14):
            if(Ferry_List14[1]!=10):
                B_seat=Ferry_List14[1]
                Ferry_ID=Ferry_List14[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List14[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='15.00') or (time==15):
            if(Ferry_List15[1]!=10):
                B_seat=Ferry_List15[1]
                Ferry_ID=Ferry_List15[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List15[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='16.00') or (time==16):
            if(Ferry_List16[1]!=10):
                B_seat=Ferry_List16[1]
                Ferry_ID=Ferry_List16[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List16[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='17.00') or (time==17):
            if(Ferry_List17[1]!=10):
                B_seat=Ferry_List17[1]
                Ferry_ID=Ferry_List17[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List17[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        else:
            print('Invalid time.Please try again')
            B_class()
            
    elif(choice.upper()=='LP'):
        choice='From Langkawi To Penang'
        if(time=='10.00') or (time==10):
            if(Ferry_List101[1]!=10):
                B_seat=Ferry_List101[1]
                Ferry_ID=Ferry_List101[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List101[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='11.00') or (time==11):
            if(Ferry_List111[1]!=10):
                B_seat=Ferry_List111[1]
                Ferry_ID=Ferry_List111[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List111[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='12.00') or (time==12):
            if(Ferry_List121[1]!=10):
                B_seat=Ferry_List121[1]
                Ferry_ID=Ferry_List121[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List121[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='13.00') or (time==13):
            if(Ferry_List131[1]!=10):
                B_seat=Ferry_List131[1]
                Ferry_ID=Ferry_List131[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List131[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='14.00') or (time==14):
            if(Ferry_List141[1]!=10):
                B_seat=Ferry_List141[1]
                Ferry_ID=Ferry_List141[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List141[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='15.00') or (time==15):
            if(Ferry_List151[1]!=10):
                B_seat=Ferry_List151[1]
                Ferry_ID=Ferry_List151[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List151[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='16.00') or (time==16):
            if(Ferry_List161[1]!=10):
                B_seat=Ferry_List161[1]
                Ferry_ID=Ferry_List161[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List161[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        elif(time=='17.00') or (time==17):
            if(Ferry_List171[1]!=10):
                B_seat=Ferry_List171[1]
                Ferry_ID=Ferry_List171[0]
                UpdateSeatStatus(B_seat,zone,Ferry_ID)
                B_seat=1+B_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,B_seat)
            elif(Ferry_List171[2]!=40):
                change_classB()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                B_class()
        else:
            print('Invalid time.Please try again')
            B_class()
    else:
        print('Invalid choice.')
        B_class()


def check_availE(name,zone,date,time,choice):
    if(choice.upper()=='PL'):
        choice='From Penang To Langkawi'
        if(time=='10.00') or (time==10):
            if(Ferry_List10[2]!=40):
                E_seat=Ferry_List10[2]
                Ferry_ID=Ferry_List10[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List10[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='11.00') or (time==11):
            if(Ferry_List11[2]!=40):
                E_seat=Ferry_List11[2]
                Ferry_ID=Ferry_List11[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List11[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='12.00') or (time==12):
            if(Ferry_List12[2]!=40):
                E_seat=Ferry_List12[2]
                Ferry_ID=Ferry_List12[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List12[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='13.00') or (time==13):
            if(Ferry_List13[2]!=40):
                E_seat=Ferry_List13[2]
                Ferry_ID=Ferry_List13[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List13[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='14.00') or (time==14):
            if(Ferry_List14[2]!=40):
                E_seat=Ferry_List14[2]
                Ferry_ID=Ferry_List14[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List14[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='15.00') or (time==15):
            if(Ferry_List15[2]!=40):
                E_seat=Ferry_List15[2]
                Ferry_ID=Ferry_List15[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List15[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='16.00') or (time==16):
            if(Ferry_List16[2]!=40):
                E_seat=Ferry_List16[2]
                Ferry_ID=Ferry_List16[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List16[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='17.00') or (time==17):
            if(Ferry_List17[2]!=40):
                E_seat=Ferry_List17[2]
                Ferry_ID=Ferry_List17[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List17[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        else:
            print('Invalid time.Please try again')
            E_class()
            
    elif(choice.upper()=='LP'):
        choice='From Langkawi To Penang'
        if(time=='10.00') or (time==10):
            if(Ferry_List101[2]!=40):
                E_seat=Ferry_List101[2]
                Ferry_ID=Ferry_List101[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List101[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='11.00') or (time==11):
            if(Ferry_List111[2]!=40):
                E_seat=Ferry_List111[2]
                Ferry_ID=Ferry_List111[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List111[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='12.00') or (time==12):
            if(Ferry_List121[2]!=40):
                E_seat=Ferry_List121[2]
                Ferry_ID=Ferry_List121[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List121[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='13.00') or (time==13):
            if(Ferry_List131[2]!=40):
                E_seat=Ferry_List131[2]
                Ferry_ID=Ferry_List131[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List131[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='14.00') or (time==14):
            if(Ferry_List141[2]!=40):
                E_seat=Ferry_List141[2]
                Ferry_ID=Ferry_List141[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List141[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='15.00') or (time==15):
            if(Ferry_List151[2]!=40):
                E_seat=Ferry_List151[2]
                Ferry_ID=Ferry_List151[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List151[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='16.00') or (time==16):
            if(Ferry_List161[2]!=40):
                E_seat=Ferry_List161[2]
                Ferry_ID=Ferry_List161[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List161[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        elif(time=='17.00') or (time==17):
            if(Ferry_List171[2]!=40):
                E_seat=Ferry_List171[2]
                Ferry_ID=Ferry_List171[0]
                UpdateSeatStatus(E_seat,zone,Ferry_ID)
                E_seat=1+E_seat
                print_ticket(name,zone,date,time,choice,Ferry_ID,E_seat)
            elif(Ferry_List171[1]!=10):
                change_classE()
            else:
                print("Business Class and Economy Class are full.Please choose another time")
                E_class()
        else:
            print('Invalid time.Please try again')
            E_class()
    else:
        print('Invalid choice')
        E_class()
        
def change_classB():
    print("Is it acceptable to be placed in economy class?")
    choice=input("""
    \t\t\t1.Yes
    \t\t\t2.No
    \n\t\t\tEnter Your Choice  :""")
    if (choice==1):
        E_class()
    elif(choice==2):
        print("Next trip will be leaving in 1 hour.Thank You!")
    else:
        print("Invalid choice. Please try again!")
        B_class()
    
def change_classE():
    print("Is it acceptable to be placed in business class?")
    choice=input("""
    \t\t\t1.Yes
    \t\t\t2.No
    \n\t\t\tEnter Your Choice  :""")
    if (choice==1):
        B_class()
    elif(choice==2):
        print("Next trip will be leaving in 1 hour.Thank You!")
    else:
        print("Invalid choice. Please try again!")
        E_class()

def print_ticket(name,zone,date,time,choice,Ferry_ID,SeatNumber):
    clear()
    print("*******************************************************************************")
    print("\n\t\tBoarding Ticket")
    print("\n\t\tName:",name)
    print("\n\t\tFerry ID:",Ferry_ID)
    print("\n\t\tZone:",zone)
    print('\n\t\tSeat Number:',SeatNumber)
    print("\n\t\tDate:",date)
    print("\n\t\tTime:","{:.2f}".format(time))
    print("\n\t\tSource and Destination:",choice)
    print("\n*******************************************************************************")
    save_data(name,Ferry_ID,zone,SeatNumber,date,time,choice)
    os.system("pause")
    menu()
            


def UpdateSeatStatus(SeatNumber,zone,Ferry_ID): #Ferry_ID is added, need to add check into 
    if(Ferry_ID=='0001'):
        if(zone=='Business'):
            Bus_Ferry10[SeatNumber]=1 
            Ferry_List10[1]=Ferry_List10[1]+1
        elif(zone=='Economy'):
            Eco_Ferry10[SeatNumber]=1
            Ferry_List10[2]=Ferry_List10[2]+1    
    elif(Ferry_ID=='0002'):
        if(zone=='Business'):
            Bus_Ferry101[SeatNumber]=1 
            Ferry_List101[1]=Ferry_List101[1]+1
        elif(zone=='Economy'):
            Eco_Ferry101[SeatNumber]=1
            Ferry_List101[2]=Ferry_List101[2]+1          
    elif(Ferry_ID=='0003'):
        if(zone=='Business'):
            Bus_Ferry11[SeatNumber]=1 
            Ferry_List11[1]=Ferry_List11[1]+1
        elif(zone=='Economy'):
            Eco_Ferry11[SeatNumber]=1
            Ferry_List11[2]=Ferry_List11[2]+1
    elif(Ferry_ID=='0004'):
        if(zone=='Business'):
            Bus_Ferry111[SeatNumber]=1 
            Ferry_List111[1]=Ferry_List111[1]+1
        elif(zone=='Economy'):
            Eco_Ferry111[SeatNumber]=1
            Ferry_List111[2]=Ferry_List111[2]+1
    elif(Ferry_ID=='0005'):
        if(zone=='Business'):
            Bus_Ferry12[SeatNumber]=1 
            Ferry_List12[1]=Ferry_List12[1]+1
        elif(zone=='Economy'):
            Eco_Ferry12[SeatNumber]=1
            Ferry_List12[2]=Ferry_List12[2]+1
    elif(Ferry_ID=='0006'):
        if(zone=='Business'):
            Bus_Ferry121[SeatNumber]=1 
            Ferry_List121[1]=Ferry_List121[1]+1
        elif(zone=='Economy'):
            Eco_Ferry121[SeatNumber]=1
            Ferry_List121[2]=Ferry_List121[2]+1
    elif(Ferry_ID=='0007'):
        if(zone=='Business'):
            Bus_Ferry13[SeatNumber]=1 
            Ferry_List13[1]=Ferry_List13[1]+1
        elif(zone=='Economy'):
            Eco_Ferry13[SeatNumber]=1
            Ferry_List13[2]=Ferry_List13[2]+1
    elif(Ferry_ID=='0008'):
        if(zone=='Business'):
            Bus_Ferry131[SeatNumber]=1 
            Ferry_List131[1]=Ferry_List131[1]+1
        elif(zone=='Economy'):
            Eco_Ferry131[SeatNumber]=1
            Ferry_List131[2]=Ferry_List131[2]+1
    elif(Ferry_ID=='0009'):
        if(zone=='Business'):
            Bus_Ferry14[SeatNumber]=1 
            Ferry_List14[1]=Ferry_List14[1]+1
        elif(zone=='Economy'):
            Eco_Ferry14[SeatNumber]=1
            Ferry_List14[2]=Ferry_List14[2]+1
    elif(Ferry_ID=='0010'):
        if(zone=='Business'):
            Bus_Ferry141[SeatNumber]=1 
            Ferry_List141[1]=Ferry_List141[1]+1
        elif(zone=='Economy'):
            Eco_Ferry141[SeatNumber]=1
            Ferry_List141[2]=Ferry_List141[2]+1
    elif(Ferry_ID=='0011'):
        if(zone=='Business'):
            Bus_Ferry15[SeatNumber]=1 
            Ferry_List15[1]=Ferry_List15[1]+1
        elif(zone=='Economy'):
            Eco_Ferry15[SeatNumber]=1
            Ferry_List15[2]=Ferry_List15[2]+1
    elif(Ferry_ID=='0012'):
        if(zone=='Business'):
            Bus_Ferry151[SeatNumber]=1 
            Ferry_List151[1]=Ferry_List151[1]+1
        elif(zone=='Economy'):
            Eco_Ferry151[SeatNumber]=1
            Ferry_List151[2]=Ferry_List151[2]+1
    elif(Ferry_ID=='0013'):
        if(zone=='Business'):
            Bus_Ferry16[SeatNumber]=1 
            Ferry_List16[1]=Ferry_List16[1]+1
        elif(zone=='Economy'):
            Eco_Ferry[SeatNumber]=1
            Ferry_List16[2]=Ferry_List16[2]+1
    elif(Ferry_ID=='0014'):
        if(zone=='Business'):
            Bus_Ferry161[SeatNumber]=1 
            Ferry_List161[1]=Ferry_List161[1]+1
        elif(zone=='Economy'):
            Eco_Ferry161[SeatNumber]=1
            Ferry_List161[2]=Ferry_List161[2]+1
    elif(Ferry_ID=='0015'):
        if(zone=='Business'):
            Bus_Ferry17[SeatNumber]=1 
            Ferry_List17[1]=Ferry_List17[1]+1
        elif(zone=='Economy'):
            Eco_Ferry17[SeatNumber]=1
            Ferry_List17[2]=Ferry_List17[2]+1
    elif(Ferry_ID=='0016'):
        if(zone=='Business'):
            Bus_Ferry171[SeatNumber]=1 
            Ferry_List171[1]=Ferry_List171[1]+1
        elif(zone=='Economy'):
            Eco_Ferry171[SeatNumber]=1
            Ferry_List171[2]=Ferry_List171[2]+1

            

def submenuV():
    print("*************************  Seating Arrangement Module  *************************")
    print("""
    \t\t\tF-to select Ferry ID
    \n\t\t\tT-to select Trip Time""")
    choice=input("\n\t\t\tEnter Your Choice:")
    if((choice=='F') or (choice=='f')):
        Ferry_ID=input("\n\t\t\tEnter Your Ferry ID:")
        ViewFerry(Ferry_ID)
    elif((choice=='T') or (choice=='t')):
        time=input("\n\t\t\tEnter Your Time:")
        place=input('\n\t\t\tEnter Your Source & Destination:')
        ViewFerryT(time,place)
    else:
        print("Invalid choice")
        submenuV()
        

def ViewFerry(Ferry_ID):
    clear()
    if(Ferry_ID=='0001'):
        print("Business Class")
        print(*Bus_Ferry10,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry10,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0002'):
        print("Business Class")
        print(*Bus_Ferry101,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry101,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0003'):
        print("Business Class")
        print(*Bus_Ferry11,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry11,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0004'):
        print("Business Class")
        print(*Bus_Ferry111,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry111,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0005'):
        print("Business Class")
        print(*Bus_Ferry12,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry12,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0006'):
        print("Business Class")
        print(*Bus_Ferry121,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry121,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0007'):
        print("Business Class")
        print(*Bus_Ferry13,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry13,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0008'):
        print("Business Class")
        print(*Bus_Ferry131,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry131,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0009'):
        print("Business Class")
        print(*Bus_Ferry14,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry14,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0010'):
        print("Business Class")
        print(*Bus_Ferry141,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry141,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0011'):
        print("Business Class")
        print(*Bus_Ferry15,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry15,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0012'):
        print("Business Class")
        print(*Bus_Ferry151,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry151,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0013'):
        print("Business Class")
        print(*Bus_Ferry16,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry16,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0014'):
        print("Business Class")
        print(*Bus_Ferry161,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry161,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0015'):
        print("Business Class")
        print(*Bus_Ferry17,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry17,sep='\t\t')
        os.system("pause")
        menu()
    elif(Ferry_ID=='0016'):
        print("Business Class")
        print(*Bus_Ferry171,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry171,sep='\t\t')
        os.system("pause")
        menu()
    else:
        print('\nInvalid Ferry ID. Please re-enter\n')
        submenuV()

def ViewFerryT(time,place):
    clear()
    if(time==10) and (place.upper()=='PL'): 
        print("Business Class")
        print(*Bus_Ferry10,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry10,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==10) and (place.upper()=="LP"):
        print("Business Class")
        print(*Bus_Ferry101,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry101,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==11) and (place.upper()=='PL'):
        print("Business Class")
        print(*Bus_Ferry11,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry11,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==11) and (place.upper()=="LP"):
        print("Business Class")
        print(*Bus_Ferry111,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry111,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==12) and (place.upper()=='PL'): 
        print("Business Class")
        print(*Bus_Ferry12,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry12,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==12) and (place.upper()=="LP"):
        print("Business Class")
        print(*Bus_Ferry121,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry121,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==13) and (place.upper()=='PL'): 
        print("Business Class")
        print(*Bus_Ferry13,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry13,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==13) and (place.upper()=="LP"):
        print("Business Class")
        print(*Bus_Ferry131,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry131,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==14) and (place.upper()=='PL'):
        print("Business Class")
        print(*Bus_Ferry14,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry14,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==14) and (place.upper()=="LP"):
        print("Business Class")
        print(*Bus_Ferry141,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry141,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==15) and (place.upper()=='PL'):
        print("Business Class")
        print(*Bus_Ferry15,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry15,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==15) and (place.upper()=="LP"):
        print("Business Class")
        print(*Bus_Ferry151,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry151,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==16) and (place.upper()=='PL'):
        print("Business Class")
        print(*Bus_Ferry16,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry16,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==16) and (place.upper()=="LP"):
        print("Business Class")
        print(*Bus_Ferry161,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry161,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==17) and (place.upper()=="PL"):
        print("Business Class")
        print(*Bus_Ferry17,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry17,sep='\t\t')
        os.system("pause")
        menu()
    elif(time==17) and (place.upper()=="LP"):
        print("Business Class")
        print(*Bus_Ferry171,sep='\t\t')
        print("Economy Class")
        print(*Eco_Ferry171,sep='\t\t')
        os.system("pause")
        menu()
    else:
        print('Invalid Ferry ID. Please re-enter')
        submenuV()

def save_data(name,Ferry_ID,zone,SeatNumber,date,time,choice):
    myfile=open('customers.txt','a')
    myfile.write('\n')
    myfile.write("{}\t".format(name)+'{}\t'.format(Ferry_ID)+'{}\t'.format(zone)+'{}\t'.format(SeatNumber)+'{}\t'.format(date)+'{}\t'.format(time)+'{}\t'.format(choice))
    myfile.close()


menu()



















