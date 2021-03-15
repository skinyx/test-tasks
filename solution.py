def friendship(candy_list) -> int:
    from math import gcd
    from collections import Counter

    if len(candy_list) == 0:
        return 0

    candy_counter = Counter(candy_list)
    #Чтобы не считать НОД попарно для всех комбинаций количества конфет, отсортируем значения по убыванию и найдём его итеративно, ведь: a % b = b % c = 0 -> a % c = 0
    #Оставлю только уникальные значения количества конфет: итоговый НОД от этого не изменится
    unique_counts = sorted(set(candy_counter.values()), reverse=True)
    #Если попадутся два взаимно простых числа - объявляю 1 НОД'ом 
    gcd_ = unique_counts.pop()
    while unique_counts:
        gcd_ = gcd(gcd_, unique_counts.pop())
        if gcd_ == 1:
            return 1
    return gcd_


if __name__ == '__main__':
    print('answer:', friendship(['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c']), 'correct:', 1)
    print('answer:', friendship(['a', 'b', 'c', 'a', 'b', 'c', 'c', 'c']), 'correct:', 2)
    print('answer:', friendship([]), 'correct:', 0)
    print('answer:', friendship(['a']), 'correct:', 1)
    print('answer:', friendship(['a', 'a', 'a']), 'correct:', 3)
    print('answer:', friendship(['a', 'a', 'a', 'a', 'a', 'b']), 'correct:', 1)