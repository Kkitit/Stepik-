# put your python code here
n = int(input()) * 1000
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
new_dct = {}
for key, value in things.items():
    new_dct.setdefault(value, key)

for i in sorted(new_dct.keys(), reverse=True):
    if n >= i:
        n -= i
        print(new_dct.get(i), end=' ')
    if n < i:
        continue