# for i in range(1, 11):
#     res = ''
#     for j in range(1, 6):
#         res += f'{i:^2} x {j:^2} = {i*j:^2}\t'
#
#     print(res)
# print('\n')
# for i in range(1, 11):
#     res = ''
#     for j in range(6, 11):
#         res += f'{i:^2} x {j:^2} = {i * j:^2}\t'
#
#     print(res)

# OR

for k in [0, 4]:
    for i in range(2, 11):
        res = ''
        for j in range(2+k, 6+k):
            res += f'{j:^2} x {i:^2} = {i * j:^2}\t'

        print(res)
    print('\n')
