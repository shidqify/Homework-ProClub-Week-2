A = input('Klub A : ')
B = input('Klub B : ')

list_hasil = []
pertandingan = 1
while True:
    hasilA, hasilB = map(int, input(f'Pertandingan {pertandingan} : ').split('\t'))
    if hasilA < 0 or hasilB < 0:
        break

    if hasilA > hasilB:
        list_hasil.append(A)
    elif hasilA < hasilB:
        list_hasil.append(B)
    else:
        list_hasil.append('Draw')
    pertandingan += 1

for i in range(len(list_hasil)):
    print(f'Hasil {i+1} : {list_hasil[i]}')

print('Pertandingan selesai')   