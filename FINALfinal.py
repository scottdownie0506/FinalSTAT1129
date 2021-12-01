import turtle as tur
 
# need to create a screen with a background color and a title
screen = tur.getscreen()
screen.screensize(2000, 2000, 'white')
screen.bgcolor('white')
screen.title('U.S. Flag')
 
# specifying the drawing tool and its speed
pen = tur.Turtle() 
pen.speed(9)
 
# so the pen does not draw until directed:
pen.pu()
 
# the drawing tool will be shaped like a turtle
pen.shape('turtle')
 
# what we will plug in to the draw_flag function to get all the other values
flag_height = 500
 
# starting point
start_x = 0
start_y = 0
 
def get_color(color):
    if color == "red":
        r = 1
        g = 0
        b = 0
        return r, g, b
 
    elif color == "blue":
        r = 0
        g = 0
        b = 1
        return r, g, b
 
    elif color == "white":
        r = 1
        g = 1
        b = 1
        return r, g, b
 
    else:
        r = 0
        g = 0
        b = 0
        return r, g, b
 
def draw_rectangle(length, height, color):
    pen.pd()
    pen.fillcolor(get_color(color))
    pen.begin_fill()
    pen.forward(length)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.forward(length)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.end_fill()
    pen.pu()
    return
 
 
# takes in a radius of the star and its color to draw a star
def draw_star(size, color):
 
    # to set the star drawing at the correct position, it will always start centered and then go to the top of the star
    side_size = size / 0.8507
    pen.left(90)
    pen.forward(size)
    pen.right(180)
 
    # then the pen will start drawing and end back where it started 
    pen.pd()
    pen.fillcolor(get_color(color))
    pen.begin_fill()
    pen.left(18)
    for i in range(5):
        pen.forward(side_size)
        pen.left(72)
        pen.forward(side_size)
        pen.right(144)
    pen.end_fill()
    pen.pu()
    pen.right(18)
    pen.forward(size)
    pen.forward(size)
    pen.left(90)
    return
 
def draw_flag(height):
 
    pen.goto(start_x, start_y)
 
    # start by drawing the border
    length = height * 1.9
    draw_rectangle(length, height, "white")
 
    # then draw the stripes
    stripe_height = height / 13
    stripe_y = start_y
    for i in range(13):
        stripe_y = stripe_y - stripe_height
        if (i % 2) == 1:
            draw_rectangle(length, stripe_height, "white")
        else:
            draw_rectangle(length, stripe_height, "red")
        if i == 12:
            pen.sety(start_y)
            break
        pen.sety(stripe_y)
 
 
    # then draw over the stripes to set up the canton
    canton_height = height * (7 / 13)
    canton_length = length * (2 / 5)
    draw_rectangle(canton_length, canton_height, "blue")
 
    # now for the rows of stars
    star_radius = stripe_height * 0.4
    star_centerx = canton_length / 12    
    star_centery = canton_height / 10 
    y = star_centery
    for i in range(9):
        if i % 2 == 0:
            x = star_centerx
            pen.goto(x, -y)
            for n in range(6):
                draw_star(star_radius, "white")
                x += (star_centerx * 2)
                pen.goto(x, -y)
        else:
            x = star_centerx * 2
            pen.goto(x, -y)
            for n in range(5):
                draw_star(star_radius, "white")
                x += (star_centerx * 2)
                pen.goto(x, -y)
        y += (star_centery)
    return

def main():
    draw_flag(flag_height)

if __name__ == '__main__':
    main()
