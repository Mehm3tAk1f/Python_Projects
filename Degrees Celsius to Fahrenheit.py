def main():
    print('°C to °F')
    celsius = is_number('°C: ')
    fahrenheit = celsius * 9/5 + 32
    print(f'{celsius}°C is {fahrenheit}°F')

def is_number(text, user_input=None):
    while user_input is not int or user_input is not float:
        try:
            user_input = float(input(text))
            return user_input
        except ValueError:
            continue

if __name__ == "__main__":
    main()