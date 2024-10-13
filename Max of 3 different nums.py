def main():
    print('Enter 3 different numbers.')
    num1 = is_number('1st number: ')
    max = num1
    num2 = is_number('2nd number: ')
    while is_distinct(num1, num2) == False:
        num2 = is_number('2nd number: ')
    if num2 > max:
        max = num2
    num3 = is_number('3rd number: ')
    while is_distinct(num1, num2, num3) == False:
        num3 = is_number('3rd number: ')
    if num3 > max:
        max = num3
    print(f'Out of {num1}, {num2} and {num3}, {max} is the largest number.')


def is_distinct(*nums):
    for num in nums:
        if nums.count(num) > 1:
            return False
    return True

def is_number(text, user_input=None):
    while user_input is not int or user_input is not float:
        try:
            user_input = float(input(text))
            return user_input
        except ValueError:
            continue

if __name__ == "__main__":
    main()