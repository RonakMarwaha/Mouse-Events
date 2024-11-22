import pgzrun
HEIGHT=480
WIDTH=500
points=[]
clicked=False
def draw():
    screen.clear()
    screen.fill('grey')
    for i in range(len(points)-1):
        screen.draw.line(points[i],points[i+1],'blue')

def on_mouse_down():
    global clicked
    clicked=True
    
def on_mouse_up():
    global clicked
    clicked=False 

def on_mouse_move(pos):
    global clicked
    if clicked:
        points.append(pos)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
pgzrun.go()