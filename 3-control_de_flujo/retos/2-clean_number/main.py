def clean_number (posible_number):
    number_result = ''
    is_decimal = False
    for char in posible_number:
        if char in '0123456789':
            number_result += char
        elif (char == '.') and (not is_decimal):
            number_result += char
            is_decimal = True
        elif (char == ',') and (is_decimal):
            return None
            break
        elif char in ', ':
            continue
        else:
            return None
            break
    else:
        return float(num) if is_decimal else int(num)
