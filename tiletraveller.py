

x, y = 1 , 1

location = [x, y]

def direction (n, e, w, s):
    message = "You can travel: "
    if n==1:
        message += "(N)orth"
    if e == 1 and n == 1:
        message += " or (E)ast"
    elif e == 1 and n !=1:
        message +="(E)ast"
    if s== 1 and (n==1 or e==1):
        message += " or (S)outh"
    elif s == 1 and not (n==1 or e==1):
        message += "(S)outh"
    if w == 1 and (n==1 or e==1 or s==1):
        message += " or (W)est"
    elif w==1 and not (n==1 or e==1 or s==1):
        message += "(W)est"
    print (message + ".")
    
def userinput():
    move_in_grid= input("Direction: ")

    move_in_grid = move_in_grid.lower()

    return move_in_grid




def move (z, q, x, y):
    z = z.lower()
    if z == "n" and n ==1:
        y +=1
    elif z == "s" and s ==1:
        y -=1
    elif z == "w" and w ==1:
        x -=1
    elif z == "e" and e ==1:
        x +=1
    else:
        print("Not a valid direction!")
    q = [x, y]
    return q, x, y

def movement(th , sj, ak, uh, x, y, xy):
    direction(n, e, w, s)
    location2 = xy
    while location2 == xy:
        way = userinput()
        xy , x, y = move(way, xy, x, y)
    return xy,x,y 

victory = [3,1]

while location != victory:
    if location == [1,1] or location == [2,1]:
        n, e, w, s = 1, 0, 0, 0
        location,x,y = movement(n,e,w,s,x,y,location)
    if location == [1,2]:
        n, e, w, s = 1, 1, 0, 1
        location,x,y = movement(n,e,w,s,x,y,location)
    if location ==[2,2] or location == [3,2]:
        n, e, w, s = 0, 0, 1, 1
        location,x,y = movement(n,e,w,s,x,y,location)
    if location == [1,3]:
        n, e, w, s = 0, 1, 0, 1
        location,x,y = movement(n,e,w,s,x,y,location)
    if location ==  [2,3]:
        n, e, w, s = 0, 1, 1, 0
        location,x,y = movement(n,e,w,s,x,y,location)
    if location ==  [3,3]:
        n, e, w, s = 0, 0, 1, 1
        location,x,y = movement(n,e,w,s,x,y,location)
    
print("Victory!")





