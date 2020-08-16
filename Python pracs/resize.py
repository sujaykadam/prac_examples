from PIL import Image

image = Image.open('image1.jpeg')
#image.show()

# The file format of the source file
print(image.format)

# The pixel format used by the image
print(image.mode)

# Image size in pixels
print(image.size) 

# Colour palette table, if any.
print(image.palette) 

image = Image.open('image1.jpeg')
new_image = image.resize((400, 400))
new_image.save('image_1.jpeg')

print(image.size) 
print(new_image.size) 

image = Image.open('image_1.jpeg')
image.show()
