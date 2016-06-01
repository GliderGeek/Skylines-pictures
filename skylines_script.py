from PIL import Image
from resizeimage import resizeimage
import os
from Tkinter import Label, Tk, Button, Entry, W, StringVar, Text, END, DISABLED, GROOVE
import time

root = Tk()
root.resizable(0, 0)

def check_public_link():
	user_entry = public_link_entry.get()
	while True:
		if user_entry.startswith('https://dl.dropboxusercontent.com/u'):
			url_status.configure(text='correct', foreground='green')
			url_status.update()
			break
		else:
			url_status.configure(text='incorrect, should start with https://dl.dropboxusercontent.com', foreground='red')
			url_status.update()
			
	create_thumbnails()
	create_markdown_text()
	
	
def create_thumbnails():
	images = []
	images += [each for each in os.listdir('.') if each.endswith(('.jpg', '.jpeg', '.png', '.JPG'))]
	
	thumbnail_folder_name = "thumbnails"
	if not os.path.exists(thumbnail_folder_name):
		os.makedirs(thumbnail_folder_name)
		
	for image in images:	
		fd_img = open(image, 'r')
		img = Image.open(fd_img)
		img = resizeimage.resize('thumbnail', img, [160, 160])
		img.save('%s/thumbnail_%s' %(thumbnail_folder_name, image), img.format)
		fd_img.close()

def create_markdown_text():

	markdown = ""

	### same code as in create_thumbnails, should be done neater ###
	images = []
	images += [each for each in os.listdir('.') if each.endswith(('.jpg', '.jpeg', '.png', '.JPG'))]
	thumbnail_folder_name = "thumbnails"
	###

	user = public_link_entry.get().split('/')[4]
	current_folder_name = os.path.dirname(os.path.realpath(images[0])).split('/')[-1]	
	
	index=0
	for image in images:	
		thumbnail_url = "https://dl.dropboxusercontent.com/u/%s/skylines/%s/%s/thumbnail_%s" %(user, current_folder_name, thumbnail_folder_name, image)
		image_url = "https://dl.dropboxusercontent.com/u/%s/skylines/%s/%s" %(user, current_folder_name, image)
	
		markdown += "[![alt_text](%s)](%s)   " % (thumbnail_url, image_url)
		if index%2!=0:
			markdown += "\n\n"
		
		index += 1
	
	md_text.insert(END, markdown)
	md_text.update()
	
var = StringVar()
var.set('Some text, can this be very long as well?? \n does this doo it?')

title = Label(root, text=' SkyLines photos', font=("Helvetica", 30))
public_link_text = Label(root, text='Give public link of one of the files:')
public_link_entry = Entry(root, width=60)
public_link_confirmation = Button(root, text='ok', command=check_public_link)
url_status = Label(root, text='', foreground='red')
md_title = Label(root, text='SkyLines text for pictures:')
md_text = Text(root, relief='groove', borderwidth=1)
md_text.insert(END, "")

title.grid(row=0, column=0)
public_link_text.grid(row=1, column=0, sticky=W)
public_link_entry.grid(row=2, column=0)
public_link_confirmation.grid(row=2, column=1)
url_status.grid(row=3, column=0)
md_title.grid(row=4, column=0, sticky=W)
md_text.grid(row=5, column=0, columnspan=2)

root.mainloop()
