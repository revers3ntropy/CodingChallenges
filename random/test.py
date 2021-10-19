n = int(input())

cups = [0] * n
  
cups[n-1] = 1

number_of_swaps = int(input())

def swap (args):
  a = int(args[0])
  b = int(args[1])
  
  temp = cups[a]
  cups[a] = cups[b]
  cups[b] = temp
  
for _ in range(number_of_swaps):
  swap_ = input()
  swap_ = swap_.split()
  swap(swap_)
  
  
for i in range(n):
  if (cups[i] == 1):
    print(i)
