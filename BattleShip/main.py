bcount = 54
def db(b):
  print("--------------------------------------------")
  print("      0   1   2   3   4   5   6   7   8   9")
  for i in range(0, 10, 1):
      print(i," ", end=" ")
      for j in range(0, 10, 1):
          print(" ",b[i][j],end=" ")
      print()
  print("--------------------------------------------")
  return

gb = []
for i in range(0,10, 1):
  gb.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
db(gb)

map = [[5,5,5,5,5,0,0,0,0,2] ,
      [4,4,4,4,0,0,0,0,0,2] ,
      [3,3,3,0,0,0,0,0,0,0] ,
      [0,0,0,0,0,0,0,0,0,0] ,
      [0,0,0,0,0,0,0,0,0,0] ,
      [0,0,0,0,0,0,0,0,0,0] ,
      [0,0,0,0,0,0,0,0,0,0] ,
      [0,0,0,0,0,0,0,0,0,0] ,
      [0,0,0,0,0,0,0,0,0,0] ,
      [0,0,0,0,0,0,0,0,0,0]    ]
while bcount > 0:
   y = int(input('please enter your row of your shot:'))
   x = int(input('please enter your column of your shot:'))
   if gb[y][x] == 'X' or gb[y][x] == 'O':
       db(gb)
       print('you already hit that area, Commander!!')
       print('-------------------------------------------')
   elif map[y][x] != 0:
       gb[y][x] = 'X'
       db(gb)
       print('You HIT!!!!, Commander')
       print('--------------------------------------------')
       ship = map[y][x]
       map[y][x] = 0
       bcount -= ship
       if any(5 in sublist for sublist in map) == False:
           print('You sunk the Carrier!!')
       if any(4 in sublist for sublist in map) == False:
           print('You sunk the Battleship!!')
       if any(3 in sublist for sublist in map) == False:
           print('You sunk the Cruiser!!')
       if any(2 in sublist for sublist in map) == False:
           print('you sunk the Destroyer')
   elif map[y][x] == 0:
       gb[y][x] = 'O'
       db(gb)
       print('You MISS!!!!, Commander')
       print('--------------------------------------------')
if bcount <= 0:
   print('You Win, Commander. Great job')
   print('--------------------------------------------')