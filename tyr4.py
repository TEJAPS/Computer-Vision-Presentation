#substaction and addition of images
from SimpleCV import Image
imgA = Image("C:\\Users\\TEJA\\Desktop\\MROADS\\CV\\DIFF1.png")
imgB = Image("C:\\Users\\TEJA\\Desktop\\MROADS\\CV\\DIFF2.png")
# Add the image to itself
diff = imgA - imgB
diff.show()
import time
time.sleep(20)