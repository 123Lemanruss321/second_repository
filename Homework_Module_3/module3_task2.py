from random import randint
def get_numbers_ticket (min_value, max_value, quantity) -> int:
    try:
        result_array = set()
        if min_value >= 1 and max_value <= 1000 and max_value-min_value >= quantity:
            while len(result_array) != quantity:
                result_array.add(randint(min_value, max_value))
        else:
            return list(result_array)
        result_array = sorted(list(result_array))
        return result_array
    except TypeError:
        return (print("Every Values must be only int. digits"))
    
    
    
    
lottery_numbers = get_numbers_ticket(8, 40, 30)
print("Ваші лотерейні числа:", lottery_numbers)