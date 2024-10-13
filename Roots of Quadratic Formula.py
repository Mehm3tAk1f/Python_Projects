def main():
    print('ax² + bx + c = 0')
    a = is_number('a: ')
    b = is_number('b: ')
    c = is_number('c: ')

    disc = b**2 - 4*a*c

    if disc > 0:    # if the discriminant is positive, we have two real roots
        x_1 = (-b + disc**0.5) / (2*a)
        x_2 = (-b - disc**0.5) / (2*a)
        print(f"x1 = {x_1} and x2 = {x_2}")
    elif disc == 0: # if the discriminant is zero, we have one real root
        x = -b / (2*a)
        print(f"The root is {x}")
    else:          # if the discriminant is negative, we have two complex roots
        real = -b / (2*a)
        imaginary = (-disc)**0.5 / (2*a)
        print(f"x1 = {real} + {imaginary}i and x2 = {real} - {imaginary}i")

def is_number(text, user_input=None):
    while user_input is not int or user_input is not float:
        try:
            user_input = float(input(text))
            return user_input
        except ValueError:
            continue

if __name__ == "__main__":
    main()