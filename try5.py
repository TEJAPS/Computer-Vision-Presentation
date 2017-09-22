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