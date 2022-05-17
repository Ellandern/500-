#Date import
from datetime import date

#Current yeat and month
a = date.today().year
e = date.today().month
#Number of childern
if 1+1 < 3:
    children_sum = int(input('Input number of children, that are below 18 years old: '))
    while children_sum < 0:
        children_sum = int(input('Input number of children, that are below 18 years old: '))
        if children_sum >= 0:
            break

#Children number less than 2
    if children_sum <= 1:
        print('You wont get any money if you have less than 2 children below 18 years old')
        more_children = str(input('Do you have more than 2 children? (Yes/No)'))
        #Any other answer than Yes/No
        while more_children != 'Yes' and more_children != 'No':
            more_children = str(input('Do you have more than 2 children? (Yes/No)'))
            if more_children == 'Yes':
                children_sum = int(input('Input number of children: '))
                if children_sum > 1:
                    break
                while children_sum <= 1:
                    print('You must enter a number greater than or equal to 2')
                    children_sum = int(input('Input number of children: '))
                if children_sum > 1:
                    break
            elif more_children == 'No':
                input('Close the program')
                break
        #If Yes
        while more_children == 'Yes':
            children_sum = int(input('Input number of children: '))
            if children_sum > 1:
                break
            while children_sum <= 1:
                print('You must enter a number greater than or equal to 2')
                children_sum = int(input('Input number of children: '))
            if children_sum > 1:
                break
        #If No
        while more_children == 'No':
            input('Close the program')
            break
    #Number of children greater/equal 2
    years_sum = []
    month_sum = []
    for i in range(children_sum):
        print('Input child year of birth', i + 1, ':')
        birth_year = int(input())
        while (a - birth_year) < 0 or (a - birth_year) >= 18:
            print('The childs age is off the 18 year scale. Enter a valid date or reduce the number of children.')
            birth_year = int(input('Enter the childs year of birth: '))
            if (a - birth_year) > 0 and (a - birth_year) < 18:
                break
        print('Enter the childs month of birth', i + 1, '(from 1 to 12):')
        month = int(input())
        while month < 1 or month > 12:
            print('!Value outside the range was entered!')
            print('Enter the childs month of birth', i + 1, '(from 1 to 12):')
            month = int(input())
            if month >= 1 and month <= 12:
                break
        years_sum.append(birth_year)
        month_sum.append(month)
    print('You gonna get ~', (18 * (i + 1) - (a * (i + 1) - sum(years_sum))) * 12 * 500 -
          (e * (i + 1) * 500 + sum(month_sum) * (i + 1) * 500), 'zł more')
    input()
