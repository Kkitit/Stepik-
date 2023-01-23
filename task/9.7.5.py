import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))
st = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант',
        'капитан', 'майор', 'подполковник', 'полковник']
lst = sorted(list([i.split("=") for i in lst_in]),key=lambda x: st.index(x[1]))





