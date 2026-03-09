max_row,max_col=map(int,input().split())

move={"N" :(0,1),"W":(-1,0),"E":(1,0),"S":(0,-1)}
right_turn={"N":"E","E":"S","S":"W","W":"N"}
left_turn={"N":"W","W":"S","S":"E","E":"N"}
res=[]
while True:
    coordinates=input().split()
    if(not coordinates):
        break
    x_axis=int(coordinates[0])
    y_axis=int(coordinates[1])
    direction=coordinates[2]
    
    instructions=input()
    for i in instructions:
        if(i=="L"):
            direction=left_turn[direction]
        elif(i=="R"):
            direction=right_turn[direction]
        else:
            x_move,y_move=move[direction]
            new_x=x_axis+x_move
            new_y=y_axis+y_move
            if(0<=new_x<=max_row and 0<=new_y<=max_col):
                x_axis=new_x
                y_axis=new_y
            else:
                continue
            
    res.append(f"{x_axis} {y_axis} {direction}")
for j in res:
    print(j)