# -*- coding: utf-8 -*-
# 整数の入力//1行目
a = int(input())
# スペース区切りの整数の入力//2行目//split()空白で分割されるが両端の空白も削除
b, c = map(int, input().split()) 
# 文字列の入力//3行目
s = input()
# 出力
print("{} {}".format(a+b+c, s))