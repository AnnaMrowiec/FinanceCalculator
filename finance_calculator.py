import sys
import xlsxwriter


# Food calculator 
this_month_food = int(input('How much did you spent on food this month?   '))
last_month_food = int(input('How much did you spent on food last month?   '))
difference_food = this_month_food - last_month_food
percent_food = round((this_month_food/last_month_food*100)-100, 2)

if difference_food > 0:
    print('This month you have spent {} more money'.format(difference_food))
elif difference_food < 0:
    print('This month you have spent {} less money'.format(difference_food))
else:
    print("This month you have spent exactly the same amount of money as last month")

if last_month_food > this_month_food:
    print('This is {} percent less than last month'.format(percent_food))
elif this_month_food > last_month_food:
    print('This is{} percent more than last month'.format(percent_food))
else:
    print('There is no different percent in the amount of money you have spent on food')

print('\n')

# Apartment calculator
this_month_apartment = int(input('How much did you spent on apartment this month?   '))
last_month_apartment = int(input('How much did you spent on apartment last month?   '))
difference_apartment = this_month_apartment - last_month_apartment
percent_apartment= round((this_month_apartment/last_month_apartment*100)-100, 2)

if difference_apartment > 0:
    print('This month you have spent {} more money'.format(difference_apartment))
elif difference_apartment< 0:
    print('This month you have spent {} less money'.format(difference_apartment))
else:
    print("This month you have spent exactly the same amount of money as last month")

if last_month_apartment > this_month_apartment:
    print('This month you have spent {} percent less than last month'.format(percent_apartment))
elif this_month_apartment> last_month_apartment:
    print('This month you have spent {} percent more than last month'.format(percent_apartment))
else:
    print('There is no different percent in the amount of money you have spent on apartment')

print('\n')

# Eat-out calculator
this_month_gastro= int(input('How much did you spent on eating out this month?   '))
last_month_gastro = int(input('How much did you spent on eating out last month?   '))
difference_gastro = this_month_gastro - last_month_gastro
percent_gastro = round((this_month_gastro/last_month_gastro*100)-100, 2)

if difference_gastro > 0:
    print('This month you have spent {} more money'.format(difference_gastro))
elif difference_gastro< 0:
    print('This month you have spent {} less money'.format(difference_gastro))
else:
    print("This month you have spent exactly the same amount of money as last month")

if last_month_gastro> this_month_gastro:
    print('This is {} percent less than last month'.format(percent_gastro))
elif this_month_gastro> last_month_gastro:
    print('This is {} percent more than last month'.format(percent_gastro))
else:
    print('There is no different percent in the amount of money you have spent on eating out')

print('\n')

# Sum of monthly expenses
this_month_sum = this_month_food + this_month_apartment + this_month_gastro
last_month_sum = last_month_food + last_month_apartment + last_month_gastro
percent_sum = round((this_month_sum/last_month_sum*100)-100, 2)
if this_month_sum == last_month_sum:
    print('You have spent this month exactly the same amount of money as last month')
elif this_month_sum > last_month_sum:
    print('This month you have spent {} instead of {}. That is {} percent more than the last month'.format(this_month_sum, last_month_sum, percent_sum))
elif last_month_sum > this_month_sum:
    print('This month you have spent {} instead of {}. That is {} percent less than the last month'.format(this_month_sum, last_month_sum, percent_sum))

#Getting permission to saave it to Excel file
permission = str(input('Do you wish to save your calculations in the XLS file? Y/N   '))
if permission == 'n':
    exit
elif permission == 'y':
    str(input('Confirm creating XLS file. Y/N   '))

# # Creating an Excel document summing up the calculator
#  wb = xlsxwriter.Workbook('Finance.xlsx')

#  sheet_1 = wb.add_worksheet()
#  sheet_1.write(0, 0, this_month_food)
#  sheet_1.write(0, 1, last_month_food)
#  sheet_1.write(0, 2, difference_food)
#  sheet_1.write(0, 3, percent_food)

#  sheet_2 = wb.add_worksheet()
#  sheet_2.write(0, 0, this_month_apartment)
#  sheet_2.write(0, 1, last_month_apartment)
#  sheet_2.write(0, 2, difference_apartment)
#  sheet_2.write(0, 3, percent_apartment)

#  sheet_3 = wb.add_worksheet()
#  sheet_3.write(0, 0, this_month_gastro)
#  sheet_3.write(0, 1, last_month_gastro)
#  sheet_3.write(0, 2, difference_gastro)
#  sheet_3.write(0, 3, percent_gastro)

 