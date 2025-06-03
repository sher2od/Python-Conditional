age = int(input())

summa  = 100
if age < 7:
    summa *= 0.5
    print(summa)

if 7 < age < 17:
    summa *= 0.8
    print(summa)

if age < 60:
    summa *= 0.7
    print(summa)

else:
    print("chegirma yoq afsus")