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
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
                   scene_width, scene_height, width=0, fill="midnightBlue")
    draw_stars(canvas)
    draw_clouds(canvas)
    draw_moon(canvas)


def draw_moon(canvas):
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


def draw_clouds(canvas):
    for i in range(20):
        random_clouds = random.random()
        if random_clouds > .5:
            random_color = f'gray{random.randint(25,51)}'
            random_x = random.randint(200, 800)
            random_y = random.randint(250, 500)
            draw_oval(canvas, random_x, random_y, random_x -
                      150, random_y-50, fill=random_color)


def draw_stars(canvas):
    for i in range(50):
        random_star = random.random()
        if random_star > .5:
            random_x = random.randint(50, 775)
            random_y = random.randint(200, 475)
            draw_polygon(canvas, random_x, random_y, random_x+5, random_y-5,
                         random_x, random_y-10, random_x-5, random_y-5, fill='gold1')


def draw_pine_tree(canvas):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    for x in range(200):
        # tree_center_x = 100
        # tree_bottom = 50
        # tree_height = 100
        if random.random() > .5:
            x_river = list(range(300, 450))
            x_ground = list(range(25, 775))
            for x in range(len(x_river)):
                x_ground.remove(x_river[x])
            # center_x = random.randint(min(x_ground), max(x_ground))
            center_x = random.choice(x_ground)
            bottom = random.randint(0, 150)
            height = 100

            trunk_width = height / 10
            trunk_height = height / 8
            trunk_left = center_x - trunk_width / 2
            trunk_right = center_x + trunk_width / 2
            trunk_top = bottom + trunk_height

            # Draw the trunk of the pine tree.
            draw_rectangle(canvas,
                           trunk_left, trunk_top, trunk_right, bottom,
                           outline="gray20", width=1, fill="tan3")

            skirt_width = height / 2
            skirt_height = height - trunk_height
            skirt_left = center_x - skirt_width / 2
            skirt_right = center_x + skirt_width / 2
            skirt_top = bottom + height

            # Draw the crown (also called skirt) of the pine tree.
            draw_polygon(canvas, center_x, skirt_top,
                         skirt_right, trunk_top,
                         skirt_left, trunk_top,
                         outline="gray20", width=1, fill="dark green")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
                   scene_width, scene_height / 3, width=0, fill="saddleBrown")
    draw_polygon(canvas, 300, 170, 400, 170, 450,
                 0, 350, 0, fill="steelBlue1")
    draw_pine_tree(canvas)


# Call the main function so that
# this program will start executing.
main()
