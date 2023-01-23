t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def decorator(chars=" !?"):
    def s_l(fn):
        def wrapper(*args):
            yt = ""
            s = fn(*args)
            for i in s:
                if i in chars:
                    yt += '-'
                else:
                    yt += i

            while '--' in yt:
                yt = yt.replace('--', '-')
            return yt

        return wrapper

    return s_l


@decorator(chars="?!:;,. ")
def get_list(s):
    s = s.lower()
    s = [t[key] if key in t else key for key in s]
    return ''.join(s)


s = input()
print(get_list(s))