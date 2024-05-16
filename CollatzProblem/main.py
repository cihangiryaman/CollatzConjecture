import matplotlib.pyplot as plt

plt.figure(figsize=(11,6))
numbers = str(input("Sayıların arasına boşluk bırakmadan yalnızca virgül(,) koyunuz.\nCollatz formülü sonuç grafiklerini çizmek istediğiniz sayıları giriniz:")).split(",")

for number in numbers:
    results = []
    number = int(number)
    while number != 1:
        if number % 2 == 0:
            number /= 2
            results.append(number)
        else:
            number *= 3
            number += 1
            results.append(number)
    plt.plot(results)

plt.ylabel("Ara Sonuçlar")
plt.xlabel("Adımlar")
if len(numbers) == 1:
    plt.title(f"{numbers[0]} Sayısının Collatz Formülü Ara Sonuçları Grafiği")
else:
    plt.title(f"{numbers} Sayılarının Collatz Formülü Ara Sonuçları Grafiği")
plt.show()
