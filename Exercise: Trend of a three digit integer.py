n = input()
d100, d10, d1 = n[0], n[1], n[2]

if d100 == d10 == d1:
     print("repeating")
elif d100 > d10 > d1:
     print("decreasing")
elif d100 < d10 < d1:
     print("increasing")
else:
     print("mixed")