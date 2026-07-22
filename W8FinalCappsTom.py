import re

print('\nWhat would you like to do with your BillsCMU.txt?')
print('Enter "a" to add new bills to the record.')
print('Enter "b" to calculate bills to be paid for each of your roommates.')
print('To exit hit "enter".')

exit = 'n'
while exit =='n': #loop for exiting
    Choice = input('\nEnter "a" or "b":')
    if Choice=='a':
        class myclassa(): #User entered data.
            month = input('Enter a 2 digit value of the month the utility bills are due.')
            year = input('Now enter a 2 digit value of the year.') #This could also be a 4 digit value, just make sure you stay consistent.
            utilities = input('Please enter the bill value for your standard utilities this month: ')
            gas = input('Now enter the value of your gas bill: ')
        class myclassb():
            def m1(self, month, year, utilities, gas):
                with open('BillsCMU.txt', 'a') as ofile: #Creates and/or Appends the txt file with new bills.
                    ofile.write(f"\n\nRent\t\t\tpayment due {month}/1/{year}\t$1150") #Rent is a constant $1150
                    ofile.write(f"\nUtilities\t\tpayment due {month}/20/{year}\t${utilities}")
                    ofile.write(f"\nGas\t\t\tpayment due {month}/20/{year}\t${gas}")
        a=myclassa()
        b=myclassb()
        b.m1(a.month, a.year, a.utilities, a.gas)
        exit = input('Would you like to exit the program? If no enter "n".')

    elif Choice=='b':
        month = input('Enter the 2 digit value of the month you want to look up:')
        year = input('Enter the 2 digit value for the year:') #This could also be a 4 digit value, just make sure you stay consistent.
        rm = input('Number of roommates to split bills with?')
        frm = float(rm)
        total_sum = 0.0
        with open('BillsCMU.txt','r') as file: #Reading the txt file.
            for line in file: #for every line in the file
                pattern = month + '(/\S*./)' + year 
                match = re.search(pattern, line) #search for correct date in the line
                if match:                       #If the correct date is found in a line
                    money = re.findall ('\$([0-9.]+)',line) #heres the number to sum in that line
                    for amount_str in money: #This loops is 100% necessary for the float casting
                        total_sum += float(amount_str) #This casts the string to a float value and sums it.
                    portion = total_sum / frm #Heres what each roommate owes.
        print(f"You and your roommates each owe ${portion:.2f} for the month of {month}")
        exit = input('Would you like to exit the program? If no enter "n".')     
    else:
        exit = 'y'

print('Exiting program, thank you.')