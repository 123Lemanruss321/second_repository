from random import randint
def get_numbers_ticket (min_value, max_value, quantity) -> int:
    try:
        result_array = set()
        if min_value >= 1 and max_value <= 1000:
            while len(result_array) != quantity:
                result_array.add(randint(min_value, max_value))
        elif min_value < 1 and max_value > 1000:
            print ("Minimal Value must be >=1 and Maximal Value must be <=1000")
        elif max_value > 1000:
            print ("Maximal Value must be <=1000")
        elif min_value < 1:
            print ("Minimal Value must be >=1")
        result_array = sorted(list(result_array))
        return result_array
    except TypeError:
        return (print("Every Values must be only int. digits"))
    
    
lottery_numbers = get_numbers_ticket(1, 100, 30)
print("Ваші лотерейні числа:", lottery_numbers)