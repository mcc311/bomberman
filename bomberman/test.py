import json

a = "Body\\\\Object\\\\Bomb\\\\bomb_img\\\\"
for i in range(60):
    print('"', end = '')
    print(i,end = '')
    print('"', end = '')
    print(':', end = '')
    print('"', end = '')

    print(a,end = '')

    if i < 10:
        print('00',end = '')
    elif i < 100:
        print('0', end = '')
    print(i, end = '') 
    print('.jpg',end = '')
    print('",')

