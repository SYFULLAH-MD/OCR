from PIL import Image, ImageChops

image1=Image.open('img1.jpg')
image2=Image.open('img2.jpg')

diff=ImageChops.difference(image1, image2)

print(diff.getbbox())

if diff.getbbox():
    diff.show()