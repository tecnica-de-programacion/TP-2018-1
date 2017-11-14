class Formater():
    def clean_number (posible_number):
        sanitize_number = posible_number.replace(' ', '')
        number_of_dots = sanitize_number.count('.')

        if number_of_dots > 1:
            return None
        if number_of_dots == 1:
            dot_position = sanitize_number.index('.')
            try:
                sanitize_number.index(',', dot_position)
            except Exception:
                sanitize_number = sanitize_number.replace(',', '')
            else:
                return None
            finally:
                try:
                    return float(sanitize_number)
                except Exception:
                    return None
        if number_of_dots == 0:
            sanitize_number = sanitize_number.replace(',', '')
            try:
                return int(sanitize_number)
            except Exception:
                return None
