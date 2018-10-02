from PIL import Image
img=Image.open('img2.png')
img=img.rotate(45,expand=True)
img.save("test.png")
