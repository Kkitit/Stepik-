t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def sort_list(func):
    def wr(*args):
        return func(*args).replace(' - ', '-').replace(' ', '-')

    return wr


@sort_list
def get_list(s):
    lst = s
    lst = lst.replace(':', '-').replace('.', '-').replace(',', '-').replace('_', '-').replace(';', '-')
    lst = [t[key] if key in t else key for key in lst]

    return ''.join(lst)


s = input().lower()
print(get_list(s))