
x = 0
while x < 101:
    print(x)
    x = x + 1

print('acabou')


x = 0
while x < 10:
    if x == 3:
      x = x + 1
      continue

    print(x)
    x = x + 1

print('acabou')



x = 0 #coluna
while x < 10:
      y = 0  # linha

      while y < 5:
        print('x vale {} e y vale {}'.format(x,y))
        y += 1

      x += 1

print('o programa foi finalizado')

