#country_codes = {'Finland': 'fi','South Africa':'za','Nepal':'np'}
#
#country_codes.clear()
#if country_codes:
#    print('country_codes is not empty')
#else:
#    print('country_codes is empty')
#
#print(len(country_codes))
#
#
#days_per_month = {'January': 31,'February': 28, 'March': 31}
#for month, days in days_per_month.items():
#    print(f'{month} has {days} days')
#
#
#roman_numerals = {'I': 1,'II': 2,'III': 3,'IV':10}
#roman_numerals['IV'] = 4
#
#print(roman_numerals)
#print(roman_numerals.get('x'))

grades_book = {
    'Susan': [65,89,76],
    'Tope': [56,97,68],
    'Christiana': [67,88,99]

    }
all_grades_total = 0
all_grades_count = 0

for name, grades in grades_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades):.2f} ')
    all_grades_total += total
    all_grades_count += len(grades)
print(f"class's average is: {all_grades_total / all_grades_count:.2f}")
