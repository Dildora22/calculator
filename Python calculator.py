def qoshish(a, b):
    return a + b
def ayirish(a, b):
    return a - b
def kopaytirish(a, b):
    return a * b
def bolish(a, b):
    if b != 0:
        return a / b
    else:
        return "0 ga bolish mumkin emas!"

print("Operatsiyalar: 1-Qoshish, 2-Ayirish, 3-Kopaytirish, 4-Bolish")
tanlov = int(input("Operatsiyani tanlang (1-4): "))


son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))


if tanlov == 1:
    print("Natija:", qoshish(son1, son2))
elif tanlov == 2:
    print("Natija:", ayirish(son1, son2))
elif tanlov == 3:
    print("Natija:", kopaytirish(son1, son2))
elif tanlov == 4:
    print("Natija:", bolish(son1, son2))
else:
    print("Noto'g'ri tanlov!")


print("Dastur yakunlandi.")
