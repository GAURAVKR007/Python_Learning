from PIL import Image, ImageFilter

img = Image.open('Pokedex\pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img3 = img.filter(ImageFilter.SHARPEN)
filtered_img4 = img.convert('L')

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)


# filtered_img.save('Enhanced.png','png')
# filtered_img2.save('Enhanced2.png','png')
filtered_img3.save('Enhanced3.png','png')
filtered_img4.save('Enhanced4_grey.png','png')

# filtered_img4.show()        # To show the Image

# rotated_pickachu = filtered_img4.rotate(125)         # To Rotate the image
# rotated_pickachu.save("rotated_grey.png","png")

# resize = filtered_img3.resize((2560,1440))      # To Resize the Photo
# resize.save("2k-Pickachu.png","png")
# resize.show()

# box = (100,100,400,400)            # To Crop an Image
# region1 = filtered_img3.crop(box)
# region1.save("Cropped_Pickachu.png","png")

img2 = Image.open("Pokedex\charmander.jpg")
filtered_img5 = img2.filter(ImageFilter.SHARPEN)
filtered_img5.thumbnail((400,400))
filtered_img5.save('thumbnail_charizard.jpg')

print(filtered_img5.size)