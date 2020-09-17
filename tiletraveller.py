
x = 1 
y = 1 
location = [x, y]



def direction (n, s, w, e):
    message= "You can travel:"
    if n==1:
        message +="(N)orth"
    if e== 1 and n==1:
        message += " or (E)ast"
    if w==1 and e==1 :
        message += "or (W)est"
    elif s==1:
        message += "(S)outh"
    elif e==1:
        message += "(E)ast"
        

# x = 2
# y= 2 
#  n e w s
# (0,0,0,1,)
def userinput():

while location != [3,1]:
    if location [1,1] or location[2,1]:
        n,e,w,s = (1,0,0,0)
    elif location [1,2]:
        n,e,w,s = (1,1,0,1)
    elif location [2,2] or location[3,2]:
        n,e,w,s = (0,0,1,1)
    elif location [1,3]:
        n,e,w,s = (0,1,0,1)
    elif location [2,3]:
        n,e,w,s = (0,1,1,0)
    elif location [3,3]:
        n,e,w,s = (0,0,1,1)
    elif location [3,1]:
        print("Victory!")
