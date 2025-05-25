Hunger=0
Thirst=0
Dirt=0
def Cat(*f):
    global Hunger
    global Thirst
    global Dirt
    if str(type(f))=="<class 'tuple'>":
        act=list(*f)
        for i in act:
            if i=='feed':
                Hunger-=1
            if i=='water':
                Thirst-=1
            if i=='bath':
                Dirt=0
            if i=='comb':
                Dirt-=1
    else:
        act=[str(f),'']
    print(act)

    if Hunger<0:
        Hunger=0
    if Thirst<0:
        Thirst=0
    if Dirt<0:
        Dirt=0

#Testing the Cat()
Hunger=2
Cat('feed')
print(Hunger)