arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax

    arrBerat.sort()
    bMin += arrBerat[0]
    bMax += arrBerat[-1]
    
    print('''Berat balita minimum : {:.2f} kg
Berat balita maksimum : {:.2f} kg'''.format(bMin, bMax))


def rerata(arrBerat):
    total = 0

    for i in arrBerat:
        total += i
    
    rata = total / len(arrBerat)
    print('Rerata berat balita: {:.2f}'.format(rata))


print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    arrBerat.append(float(input()))

hitungMinMax(arrBerat)
rerata(arrBerat)