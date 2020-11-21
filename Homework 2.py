A = input('Klub A : ')
B = input('Klub B : ')

list_result = []
match = 1

while True:
    resultA, resultB = map(int, input(f'Pertandingan {match} : ').split('\t'))
    if resultA < 0 or resultB < 0:
        break
        
    if resultA > resultB:
        list_result.append(A)
    elif resultA < resultB:
        list_result.append(B)
    else:
        list_result.append('Draw')
    match += 1

for i in range(len(list_result)):
    print(f'Hasil {i+1} : {list_result[i]}')

print('Pertandingan selesai')   
