a = input()
n = int(a, 16)
  
for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i),sep='')