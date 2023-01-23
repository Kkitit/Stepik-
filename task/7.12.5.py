from functools import wraps

# здесь продолжайте программу
def decoratos_sum(func):
    @wraps(func)
    def wrapper(*args):
        return sum(func(*args))
    return wrapper


@decoratos_sum
def get_list(s):
    '''Функция для формирования списка целых значений'''
    return list(map(int, s.split()))




