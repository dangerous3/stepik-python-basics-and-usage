'''В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
равное days.'''

import datetime

year, month, day = list(map(int, input().split()))
days_delta = int(input())

initial_date =  datetime.date(year, month, day)
final_date = initial_date + datetime.timedelta(days = days_delta)

print(final_date.year, final_date.month, final_date.day)