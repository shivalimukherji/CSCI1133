# Shivali Mukherji
# mukhe105
# CSCI 1133 Section 070
# Assignment 3

import images
import turtle

def draw_pixel(x, y, color, pixel_size):

    '''Uses the turtle module to find the x and y coordinates for each pixel and colors them in. The x and y coordinates, color, and pixel size are all taken as arguments.'''

    t = turtle.Turtle()
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.setheading(0)	# set the pen in the +ve x direction
    t.pendown()
    for iter in range (4):
        t.forward(pixel_size)
        t.right(90)
    t.penup()
    t.end_fill()
    t.hideturtle()

def draw_image(img):

    '''Uses the x and y coordinates to pinpoint each location on the image that needs to be drawn, and uses rgb values to fill color for each invidual pixel on the image. Also uses a nested for loop to repeat this process for each individual pixel.'''

    turtle.colormode(255)
    turtle.setup(450,450)
    turtle.setworldcoordinates(0,0,450,450)
    rows = len(img)
    cols = len(img[0])
    #print('rows=',rows,'cols=',cols)
    pix_size = 450//rows
    #print('pixel size', pix_size)
    #Set initial position
    xpos = 0
    ypos = 450
    for i in range(0,rows):
        for j in range(0,cols):
            #print('i=',i,'j=',j,'xpos=', xpos, 'ypos=', ypos)
            draw_pixel(xpos,ypos,img[i][j],pix_size)
            xpos = xpos + pix_size
            #print('xpos and ypos after draw',xpos,ypos)
            if j == cols - 1:    # Move y-position to the next row and reset x-position to 0
                ypos = ypos - pix_size
                xpos = 0
    # persist drawing
    turtle.done()
    
def grayscale_conversion(img):

    '''Uses the x and y coordinates to pinpoint the location of each pixel and uses rgb values to fill color for each individual pixel on the image. Also uses a nested for loop with integer division of the rgb values to obtain the values for printing a grayscale image.'''

    turtle.colormode(255)
    turtle.setup(450,450)
    turtle.setworldcoordinates(0,0,450,450)
    rows = len(img)
    cols = len(img[0])
    #print('rows=',rows,'cols=',cols)
    pix_size = 450//rows    # Use integer division
    #print('pixel size', pix_size)
    #Set initial position
    xpos = 0
    ypos = 450
    for i in range(0,rows):
        for j in range(0,cols):
            #print('i=',i,'j=',j,'xpos=', xpos, 'ypos=', ypos)
            gray_scale = [sum(img[i][j])//3,sum(img[i][j])//3,sum(img[i][j])//3]    # Use integer division
            #print('i=',i,'j=',j,gray_scale)
            draw_pixel(xpos,ypos,gray_scale,pix_size)
            xpos = xpos + pix_size
            #print('xpos and ypos after draw',xpos,ypos)
            if j == cols - 1:    # Move y-position to the next row and reset x-position to 0
                ypos = ypos - pix_size
                xpos = 0
    # persist drawing
    turtle.done()

def main():

    '''Driver function that takes an input of which image the user would like to print so that the program could draw the corresponding image. If the user's input does not match one of the given options, the program will return "invalid input."'''

    print('Whish image should I print (image 1, image 1 gs, image 2, image 2 gs, image 3, image 3 gs, image 4, image 4 gs or bonus or bonus gs)?')
    image_name = input()
    if image_name == 'image 1':
        draw_image(images.img1)
    elif image_name == 'image 1 gs':
        grayscale_conversion(images.img1)
    elif image_name == 'image 2':
        draw_image(images.img2)
    elif image_name == 'image 2 gs':
        grayscale_conversion(images.img2)
    elif image_name == 'image 3':
        draw_image(images.img3)
    elif image_name == 'image 3 gs':
        grayscale_conversion(images.img3)
    elif image_name == 'image 4':
        draw_image(images.img4)
    elif image_name == 'image 4 gs':
        grayscale_conversion(images.img4)
    elif image_name == 'bonus':
        draw_image(images.bonus)
    elif image_name == 'bonus gs':
        grayscale_conversion(images.bonus)
    else:
        print('Invalid input')
        exit()


main()