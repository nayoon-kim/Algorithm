print('[{:d}]'.format(777))
print('[{:10}]'.format(777)) # 10칸 띄고 777
print('[{:>10}]'.format(777)) # 10칸 이후에
print('[{:<10}]'.format("dkljaf")) # 글자쓰고 10칸 띄우기
print('[{:^10}]'.format(777)) # 5칸 띄고 글자쓰고 다시 5칸 띄우

for i in range(5):
    print('*' * (i+1))
