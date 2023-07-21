students={'Aex':{'class':'V',
                 'roll_id':2},
          'Puja':{'class':'V',
                  'roll_id':3}}
for a in students:
     print(a)
     for b in students[a]:
          print(b,':',students[a][b])
