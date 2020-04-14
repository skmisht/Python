Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
Enter your 6 numbers, separated by commas: 1,2,3,4,5,6
Traceback (most recent call last):
  File "C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py", line 31, in <module>
    main()
  File "C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py", line 9, in main
    matched_numbers = user_numbers.intersection(lottery_numbers)
AttributeError: 'list' object has no attribute 'intersection'
>>> 
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
Enter your 6 numbers, separated by commas: 1,2,3,4,5,6
Traceback (most recent call last):
  File "C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py", line 31, in <module>
    main()
  File "C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py", line 9, in main
    matched_numbers = user_numbers.intersection(lottery_numbers)
AttributeError: 'list' object has no attribute 'intersection'
>>> 
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
Enter your 6 numbers, separated by commas: 1,2,3,4,5,6
Traceback (most recent call last):
  File "C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py", line 31, in <module>
    lottery_main()
  File "C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py", line 9, in lottery_main
    matched_numbers = user_numbers.intersection(lottery_numbers)
AttributeError: 'list' object has no attribute 'intersection'
>>> 
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
['Enter your 6 numbers', ' separated by commas: ']
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
Enter your 6 numbers
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
 separated by commas: 
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
Traceback (most recent call last):
  File "C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py", line 32, in <module>
    lottery_main()
  File "C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py", line 5, in lottery_main
    user_numbers = get_player_numbers()
  File "C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py", line 15, in get_player_numbers
    input_csv = input("Enter your 6 numbers, separated by commas: ".split(",")[4])
IndexError: list index out of range
>>> 
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
Enter your 6 numbers, separated by commas: 1,2,3,4,5,6
You matched {1, 5}. you won $10000!
>>> 
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
Enter your 6 numbers, separated by commas: 1,2,3,4,5,6
You matched {2, 3, 5}. you won $1000000!
>>> 
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
Enter your 6 numbers, separated by commas: 1,2,3,4,5,6
You matched {1, 5}. you won $10000!
>>> 
 RESTART: C:\Users\Surender\Documents\Python & PostgreSQL Developer\lottery_app.py 
Enter your 6 numbers, separated by commas: 2,3,6,5,7,8
You matched {8, 2}. you won $10000!
>>> 
