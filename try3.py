#substaction and addition of images
from SimpleCV import Image
imgA = Image("C:\\Users\\TEJA\\Desktop\\MROADS\\CV\\ni8.jpg")
# Add the image to itself
added = imgA + imgA + imgA+ imgA
added.show()
import time
time.sleep(5)

#FIND THE DIFFERENCE
'''
#substaction and addition of images
from SimpleCV import Image
imgA = Image("C:\\Users\\TEJA\\Desktop\\MROADS\\CV\\DIFF1.png")
imgB = Image("C:\\Users\\TEJA\\Desktop\\MROADS\\CV\\DIFF2.png")
# Add the image to itself
diff = imgA - imgB
diff.show()
import time
time.sleep(20)
'''



#for aving camera live (webcamp here)
'''
from SimpleCV import Camera
cam = Camera(0,{ "width": 640, "height": 480 })
cam.live()
'''

#MOTION DETECTED
'''
from SimpleCV import Camera, Display
import time
# if mean color exceeds this amount, do something
threshold = 5.0
cam = Camera(0,{ "width": 640, "height": 480 })
previous = cam.getImage()
disp = Display(previous.size())
while not disp.isDone():     # Grab another frame and compare with previous
    current = cam.getImage()
    diff = current - previous
     # Convert to NumPy matrix and compute mean color
    matrix = diff.getNumpy()
    mean = matrix.mean()
     # Show on screen
    diff.save(disp)
     # Check if changed
    if mean >= threshold:
        print "Motion Detected"
     #wait for a second
        time.sleep(1)
        previous = current
'''




#dealing with the ip controlled cameras
#presently the url is not working ,have some configuration errors
'''
from SimpleCV import JpegStreamCamera
# Initialize the webcam by providing URL to the camera
cam = JpegStreamCamera("http://mycamera/video.mjpg")
cam.getImage().show()
'''

#-----------------------------------------------------------------------------

#accessing cam with required properties
'''
from SimpleCV import Camera
import time
cam = Camera(0, { "width": 640, "height": 480 })
img = cam.getImage()
img.drawText("Hello World", 160, 120)
img.show()
time.sleep(5)
'''


#for seeing image in the browser
'''
from SimpleCV import Image
import time
img = Image("C:\\Users\\TEJA\\Desktop\\23.jpg")
# This will show the logo image in a web browser img.show(type="browser")
img.show(type="browser")
time.sleep(5)
'''

#for cloasing and opening of windows
'''
from SimpleCV import Display, Image
import time
display = Display()
Image("C:\\Users\\TEJA\\Desktop\\23.jpg").save(display)
print "I launched a window"
# This while loop will keep looping until the window is closed
while not display.isDone():
    time.sleep(0.1)
print "You closed the window"
'''

#for drawing circles and all
'''
from SimpleCV import Display, Image, Color
winsize = (640,480)
display = Display(winsize)  
img = Image(winsize)
img.save(display)
while not display.isDone():
    if display.mouseLeft:
        img.dl().circle((display.mouseX, display.mouseY), 4,Color.WHITE, filled=True)
        img.save(display)
        img.save("painting.png")
'''

#TIME LAPSE PHOTOGRAPHY
'''
from SimpleCV import Camera, Image
import time
cam = Camera()
# Set the number of frames to capture
numFrames = 10
# Loop until we reach the limit set in numFrames
for x in range(0, numFrames):
    img = cam.getImage()  
    filepath = "C:\\Users\\TEJA\\Desktop\\pics\\image-" + str(x) + ".jpg"
    img.save(filepath)
    print "Saved image to: " + filepath
    time.sleep(2)
'''


##PHONE booth application
'''
from SimpleCV import Camera, Display, Color
import time
# Initialize the camera
cam = Camera()
# Initialize the display
display = Display()
# Take an initial picture
img = cam.getImage()  
# Write a message on the image
img.drawText("Left click to save a photo.",  color=Color().getRandom())  
# Show the image on the display
img.save(display)
time.sleep(5)  
counter = 0
while not display.isDone():
    # Update the display with the latest image
    img = cam.getImage()
    img.save(display)
    if display.mouseLeft:
        # Save image to the current directory
        img.save("photobooth" + str(counter) + ".jpg")  
        img.drawText("Photo saved.", color=Color().getRandom())
        img.save(display)
        time.sleep(5)
        counter = counter + 1

'''

#various ways of loading images
'''
from SimpleCV import Image
#name of the image
builtInImg = Image("logo")
#from internet
webImg = Image("http://simplecv.s3.amazonaws.com/simplecv_lg.png")
from local hard disk
localImg = Image("image.jpg")
'''

#dealing with images sets ,here storing images from webcams into folder
'''
from SimpleCV import Camera, ImageSet
import time
cam = Camera()
camImages = ImageSet("C:\\Users\\TEJA\\Desktop\\pics")  
# Set to a maximum of 10 images saved # Feel free to increase, but bewared running out of space
maxImages = 10
for counter in range(maxImages):
    # Capture a new image and add to set
    img = cam.getImage()
    camImages.append(img)  
     # Show the image and wait before capturing another
    img.show()
    time.sleep(1)
camImages.save(verbose=True)
camImages.show(3)#shows images as slideshow with time pause as 3 sec b/w each image
'''



#another ip controlled camera
#again url is not working
'''
from SimpleCV import JpegStreamCamera, Display
import time
#initialize the IP camera
cam = JpegStreamCamera("http://35.13.176.227/video.mjpg")  
display = Display()  
img = cam.getImage()
img.save(display)
while not display.isDone():
    img = cam.getImage()
    img.drawText(time.ctime())
    img.save(display)
     # This might be a good spot to also save to disk     # But watch out for filling up the hard drive
    time.sleep(1)
'''


#virtual camera
'''
from SimpleCV import VirtualCamera
import time
# Load an existing video into the virtual camera
vir = VirtualCamera("C:\\Users\\TEJA\\Desktop\\current\\n12.mp4", "video")
vir.getImage().show()
time.sleep(2)
'''

#virtual camera
'''
from SimpleCV import VirtualCamera,Image
from cv2 import cv
import cv2
import numpy as np
from PIL import Image
import time
# Load an existing video into the virtual camera
vir = VirtualCamera("C:\\Users\\TEJA\\Desktop\\current\\n12.mp4", "video")
Image.fromarray(vir.live()).show()
time.sleep(1)
'''



#multple ip cameras in single windows
#not working cos of url
'''
from SimpleCV import JpegStreamCamera, Display
from SimpleCV import Camera, Display import time
#initialize the IP cameras
cam1 = JpegStreamCamera("http://admin:1234@192.168.1.10/video.mjpg")
cam2 = JpegStreamCamera("http://admin:1234@192.168.1.11/video.mjpg")
cam3 = JpegStreamCamera("http://admin:1234@192.168.1.12/video.mjpg")
cam4 = JpegStreamCamera("http://admin:1234@192.168.1.13/video.mjpg")
display = Display((640,480))  
while not display.isDone():
    img1 = cam1.getImage().resize(320, 240)
    img2 = cam2.getImage().resize(320, 240)
    img3 = cam3.getImage().resize(320, 240)
    img4 = cam4.getImage().resize(320, 240)
    top = img1.sideBySide(img2)
    bottom = img3.sideBySide(img4)
    combined = top.sideBySide(bottom, side="bottom")  
    combined.save(display)
    time.sleep(5) 

'''




#notify when percent chaneg is greater thant 50% in pixels. not done but explain
'''
from SimpleCV import Image
# Take the candy difference computed in the previous example
diff = Image("candydiff.png")
# Extract the individual pixels into a flat matrix
matrix = diff.getNumpy()
flat = matrix.flatten()  
# Find how much changed
num_change = np.count_nonzero(flat)
percent_change = float(num_change) / float(len(flat))  
if percent_change > 0.1:
    print "Stop eating candy!
'''



#histogram
'''
from SimpleCV import Image
img = Image('C:\\Users\\TEJA\\Desktop\\ni8.jpg')
# Generate the histogram
histogram = img.histogram()
# Output the raw histogram data
print histogram
'''

