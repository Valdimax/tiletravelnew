
x = 1 
y = 1 
location = [x, y]

def move (x, y, z, q):
    z = z.lower()
    if z == "n" and n ==1:
        y +=1
    elif z == "s" and s==1:
        y-=1
    elif z == "w" and w==1:
        x -=1
    elif e == "e" and e==1:
        x +=1
    else:
        print("Not a valid direction!")
    q=[x, y]
    return q, x, y



def direction (n, s, w, e):
    message= "You can travel:"
    if n==1:
        message +="(N)orth"
    if n==1 and e==1 and s==1:
        message +="or (E)ast or (S)outh"
    if s== 1 and e==1:
        message += "(E)ast or (S)outh"
    if w==1 and e==1 :
        message += "(E)ast or (W)est"
    if w==1 and s==1 :
        message += "(S)outh or (W)est"
    if n==1 and s==1 :
        message += "or (S)outh"
    
def userinput():
    move_in_grid= input("direction: ")
    move_in_grid = move_in_grid.lower()
    return move_in_grid

# x = 2
# y= 2 
#  n e w s
# (0,0,0,1,)

while location != [3,1]:
    if location == [1,1] or location == [2,1]:
        n,e,w,s = (1,0,0,0)
    elif location == [1,2]:
        n,e,w,s = (1,1,0,1)
    elif location ==[2,2] or location == [3,2]:
        n,e,w,s = (0,0,1,1)
    elif location == [1,3]:
        n,e,w,s = (0,1,0,1)
    elif location ==  [2,3]:
        n,e,w,s = (0,1,1,0)
    elif location ==  [3,3]:
        n,e,w,s = (0,0,1,1)
    elif location == [3,1]:
        print("Victory!")





