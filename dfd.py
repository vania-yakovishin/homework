def can_split_chocolate(n, m, k):
    total_pieces = n * m
    if total_pieces == k:
        return True
    else:
        return False
n = int(input("Введіть кількість рядків шоколадки: "))
m = int(input("Введіть кількість стовпців шоколадки: "))
k = int(input("Введіть бажану кількість частинок: "))
if can_split_chocolate(n, m, k):
    print("Так, можна розламати шоколадку на рівно", k, "частинок.")
else:
    print("Ні, не можна розламати шоколадку на рівно", k, "частинок.")