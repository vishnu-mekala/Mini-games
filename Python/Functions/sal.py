def sal():
    sal = int(input('Enter the Salary:'))
    no_of_days = int(input('Enter the Number of days:'))
    sal_per_day = sal//30
    if (no_of_days > 22):
        ot_days = no_of_days - 22
        ot = ot_days * 2
        ot_sal = sal_per_day * ot
        total_sal = sal + ot_sal
    elif (no_of_days < 22):
        ot1_days = 22 - no_of_days
        ot1_sal = sal_per_day * ot1_days
        total_sal = sal_per_day - ot1_sal
    else:
        total_sal = sal
    print(total_sal)
sal()