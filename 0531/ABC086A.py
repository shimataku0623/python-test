#入力
a, b = map(int, input().split())

#奇数と奇数のみodd
if a%2!=0 and b%2!=0 :
  print('Odd')
else:
  print('Even')