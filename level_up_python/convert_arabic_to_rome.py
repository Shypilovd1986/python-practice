rome_num_digits = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
rome_num_decimal = {'1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XL'}
rome_num_hundred = {'1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}


def convert_to_rome():
    input_number = int(input('Input your arabic number\n'))
    rome_converted_number = ''
    if input_number > 1000:
        print('Your number more then 1000, please pick another number')
    elif input_number < 0:
        print('Your number is negative , pick between 0 to 1000')
    elif input_number == 1000:
        print('Rome equivalent: M')
    else:
        hundred_category = input_number//100
        if hundred_category != 0:
            rome_converted_number = rome_converted_number + rome_num_hundred[str(hundred_category)]
        decimal_category = (input_number - hundred_category * 100)//10
        if decimal_category != 0:
            rome_converted_number = rome_converted_number + rome_num_decimal[str(decimal_category)]
        digit_category = (input_number - hundred_category * 100 - decimal_category * 10)//1
        if digit_category != 0:
            rome_converted_number = rome_converted_number + rome_num_digits[str(digit_category)]
    return rome_converted_number


if __name__ == '__main__':
    print(convert_to_rome())
