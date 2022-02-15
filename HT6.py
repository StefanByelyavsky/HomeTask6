lst_bs = list(input('Задайте список:'))
a = len(lst_bs)
if a == 0:
    lst_bs = list()
else:
    b = lst_bs.pop(-1)
    lst_bs.insert(0, b)
print(lst_bs)
