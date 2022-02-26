##### FIRST PART OF THE ASSIGNMENT, MILESTONE 07 #####

from PIL import Image

background_image1=Image.open('desert.jpg')

pixels_background1=background_image1.load()

background_image2=Image.open('beach.jpg')

pixels_background2=background_image2.load()

##### SECOND PART OF THE ASSIGNMENT MILESTONE 08 #####

image_combined = Image.new("RGB", background_image1.size)

pixels_combined = image_combined.load()

second_image=Image.open('cat.jpg')

width_s_i, height_s_i= second_image.size

pixels_second=second_image.load()

for i in range(width_s_i):
    for j in range(height_s_i):
        if pixels_second[i,j][1] >= 215 and i<400:
            pixels_combined[i,j]=pixels_background1[i,j]
        elif pixels_second[i,j][1] >= 215 and i>=400:
            pixels_combined[i,j]=pixels_background2[i,j]
        else:
            pixels_combined[i,j]=pixels_second[i,j]
            
image_combined.show()

for i in range(width_s_i):
    for j in range(height_s_i):
        (r,g,b)=pixels_combined[i,j]
        pixels_combined[i,j]=(255,g,b)

image_combined.show()

image_combined.save('New Image Combined.jpg')