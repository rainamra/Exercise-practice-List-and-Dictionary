#number 2
prices = {
"banana": [4, 7],
"apple": [2, 1],
"orange": [1.5, 2],
"pear": [3, 2]}

total = 0.0

for key, item in prices.items():
    print(key)
    print('price: ', item[0])
    print('stock: ', item[1], '\n')
    total = total + item[0]*item[1]

print('\ntotal: ', str(total))