north= "n"
south = "s"
west  = "w"
east = "e"

def direction (n, s, w, e):
    message= "You can travel:"
    if n==1:
        message +="(N)orth"
    elif s==1:
        message += "(S)outh"
    elif w==1:
        message += "(W)est"
    elif e==1:
        message += "(E)ast"
        


print("You can travel: (N)orth.")

print ("change")
print("Not a valid direction!")