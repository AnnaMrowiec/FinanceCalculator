import sys

# Food calculator 
this_month_food = int(input('How much did you spent on food this month?   '))
print('This month you have spent {}'.format(this_month_food))
last_month_food = int(input('How much did you spent on food last month?   '))
print('Last month you have spent {}'.format(last_month_food))
difference_food = this_month_food - last_month_food
if difference_food > 0:
    print('This month you have spent {} more money'.format(difference_food))
elif difference_food < 0:
    print('This month you have spent {} less money'.format(difference_food))
else:
    print("This month you have spent exactly the same amount of money as last month")

precent_food = round((this_month_food/last_month_food*100)-100, 2)
if last_month_food > this_month_food:
    print('This month you have spent {} percent less last month'.format(precent_food))
elif this_month_food > last_month_food:
    print('This month you have spent {} percent more than last month'.format(precent_food))
else:
    print('There is no different percent in the amount of money you have spent on food')

print('\n')

# Apartment calculator
this_month_apartment = int(input('How much did you spent on apartment this month?   '))
print('This month you have spent {}'.format(this_month_apartment))
last_month_apartment = int(input('How much did you spent on apartment last month?   '))
print('Last month you have spent {}'.format(last_month_apartment))
difference_apartment = this_month_apartment - last_month_apartment
if difference_apartment > 0:
    print('This month you have spent {} more money'.format(difference_apartment))
elif difference_apartment< 0:
    print('This month you have spent {} less money'.format(difference_apartment))
else:
    print("This month you have spent exactly the same amount of money as last month")

precent_apartment= round((this_month_apartment/last_month_apartment*100)-100, 2)
if last_month_apartment > this_month_apartment:
    print('This month you have spent {} percent less than last month'.format(precent_apartment))
elif this_month_apartment> last_month_apartment:
    print('This month you have spent {} percent more than last month'.format(precent_apartment))
else:
    print('There is no different percent in the amount of money you have spent on food')

print('\n')
# Sum of monthly expenses
this_month_sum = this_month_food + this_month_apartment
last_month_sum = last_month_food + last_month_apartment
percent_sum = round((this_month_sum/last_month_sum*100)-100, 2)
if this_month_sum == last_month_sum:
    print('You have spent this month exactly the same amount of money as last month')
elif this_month_sum > last_month_sum:
    print('This month you have spent {} instead of {}. That is {} percent more than the last month'.format(this_month_sum, last_month_sum, percent_sum))
elif last_month_sum > this_month_sum:
    print('This month you have spent {} instead of {}. That is {} percent less than the last month'.format(this_month_sum, last_month_sum, percent_sum))