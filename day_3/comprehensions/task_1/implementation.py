from math import sqrt


def great_comprehension(list1, list2, list3):
    """
    Возвращает список с перемноженными элементами списков list1, list2 и list3 согласно условию
    """
    return [x*y*z
            for x in [i%10 + int(str(i)[0]) for i in list1 if i%10 == int(str(i)[0]) and len(str(i)) > 1]
            for y in [sqrt(j) for j in list2 if (j//10)//10 != 0 and ((j//10)//10)//10 == 0 and j%2 == 0]
            for z in [k for k in list3 if k % 2 != 0 or k == 4]
            ]


list1 = [12, 2, 17, 44, 131]
list2 = [127, 69, 144, 0, 1024]
list3 = [8, 6, 5, 4, 7]

print(great_comprehension(list1,list2,list3))
