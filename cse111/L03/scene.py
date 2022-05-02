# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_grid(canvas, scene_width, scene_height, 50)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
                   scene_width, scene_height, width=0, fill="midnightBlue")

    draw_polygon(canvas, 150, 150, 200, 100, 150, 50, 100, 100, fill='black')

    for i in range(20):
        random_clouds = random.random()
        if random_clouds > .5:
            random_color = f'gray{random.randint(25,51)}'
            random_x = random.randint(200, 800)
            random_y = random.randint(250, 500)
            draw_oval(canvas, random_x, random_y, random_x -
                      150, random_y-50, fill=random_color)

    for i in range(18):
        colors = f'gray{71-i}'
        draw_oval(canvas, 150+i, 500+i, 0-i, 350 -
                  i, fill=colors, outline=colors)
    draw_oval(canvas, 150, 500, 0, 350, fill='gray80')
    for i in range(50):
        random_crater = random.random()
        if random_crater > .5:
            random_color = f'gray{random.randint(25,51)}'
            random_x = random.randint(50, 125)
            random_y = random.randint(375, 475)
            draw_oval(canvas, random_x, random_y, random_x -
                      10, random_y-10, fill=random_color)
            draw_oval(canvas, random_x, random_y, random_x -
                      10, random_y-10, fill=random_color)


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
                   scene_width, scene_height / 3, width=0, fill="saddleBrown")
    for i in range(50):
        random_star = random.random()
        if random_star > .5:
            random_x = random.randint(50, 775)
            random_y = random.randint(200, 475)
            draw_polygon(canvas, random_x, random_y, random_x+5, random_y-5,
                         random_x, random_y-10, random_x-5, random_y-5, fill='gold1')

    # draw_polygon(canvas, 150, 150, 200, 100, 150, 50, 100, 100, fill='black')


def draw_grid(canvas, width, height, interval, color="snow1"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)


# Call the main function so that
# this program will start executing.
main()
