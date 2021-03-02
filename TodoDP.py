#追記2021/03/02
#このコードは2019年末に書いたはてブの戯言に使ったコードです。
#https://perarduaadastra.hatenablog.com/entry/2019/12/24/055250


import sys
input = sys.stdin.readline
N = int(input())
todo = []
time = 12 * 3600
for _ in range(N):
  name, sec, ukiuki = input().split(", ")
  name = name[1: -1]
  sec = int(sec)
  ukiuki = int(ukiuki)
  todo.append((name, sec, ukiuki))
dp = [[0] * (time + 1) for _ in range(N + 1)]
prev = [[(-1, -1)] * (time + 1) for _ in range(N + 1)]
for i in range(N):
  for j in range(time + 1):
    if dp[i + 1][j] < dp[i][j]:
      dp[i + 1][j] = dp[i][j]
      prev[i + 1][j] = prev[i][j]
    if j + todo[i][1] <= time:
      if dp[i + 1][j + todo[i][1]] < dp[i][j] + todo[i][2]:
        dp[i + 1][j + todo[i][1]] = dp[i][j] + todo[i][2]
        prev[i + 1][j + todo[i][1]] = (i, j)
res = []
x = 0
i = N - 1
j = 0
for k in range(time + 1): 
  if dp[-1][k] > x:
    x = dp[-1][k]
    j = k
for _ in range(N + 1):
  p = prev[i][j]
  if p != (-1, -1):
    i = p[0]
    j = p[1]
  else: break
  res.append(todo[p[0]])
res = res[: : -1]
sumsec = 0
sumukiuki = 0
for do in res:
  print(do[0], "予想時間：", do[1], "予想快楽：", do[2])
  sumsec += do[1]
  sumukiuki += do[2]
print("合計予想時間：", sumsec)
print("合計予想快楽：", sumukiuki)
