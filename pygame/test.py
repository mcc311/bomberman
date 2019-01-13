import json

box_loc = []
for i in range(13):
    if i%2:
        for j in range(15):
            if j%2:
                box_loc.append([j,i])
print(box_loc)