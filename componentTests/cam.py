import numpy as np
import cv2


import numpy as np
import cv2
import Tkinter 
from PIL import Image
from PIL import ImageTk
import time
#pip install Pillow
#pip install Image

#img = cv2.imread('img.png')
# A root window for displaying objects
root = Tkinter.Tk()  

# Convert the Image object into a TkPhoto object

canvas = Tkinter.Canvas(root, width=1200, height=1100)
canvas.pack()

canvas.create_line(0, 0, 200, 100)
canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

canvas.create_rectangle(50, 25, 150, 75, fill="blue")


cap = cv2.VideoCapture(0)
if cap.isOpened() == 0:
    cap.open(0)
while(True):
	ret, frame = cap.read()

	time.sleep(1/25)
	b,g,r = cv2.split(frame)
	img2 = cv2.merge((r,g,b))
	im = Image.fromarray(img2)
	#cv2.imwrite("fframe.png", frame)
	converted = ImageTk.PhotoImage(image=im) 

	canvas.create_image(500, 500, image=converted)
	root.update() # Start the GUI

time.sleep(30)
#cap.release()
#cv2.destroyAllWindows()