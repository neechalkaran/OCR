
import os
import tempfile
from pdf2image import convert_from_path

import cv2
from PIL import Image

import pytesseract

def pdf_to_ppm_and_png():
 
	
	folder_name = input("Enter your pdf folder name : ") 
	file_name = input("Enter your pdf file name : ") 
	filename = folder_name + "/" + file_name
	counter=1
	
	if not os.path.exists('output'):
		os.makedirs('output')
		
	with tempfile.TemporaryDirectory() as path:
		 images_from_path = convert_from_path(filename, output_folder='output/', last_page=75, first_page =0)
	 
	base_filename  =  os.path.splitext(os.path.basename(filename))[0] + '.jpg'     
	 
	save_dir = 'output'
	 
	if not os.path.exists('images'):
		os.makedirs('images')
		
		
	for page in images_from_path:
		if(len(str(counter)) == 1):
			page.save(('images\\0'+str(counter)+'.png'), 'PNG')
			counter += 1
		else:
			page.save(('images\\'+str(counter)+'.png'), 'PNG')
			counter += 1
		
    

def split_images_into_half():
	
	count = 1
	img_list = []
	
	for filename in os.listdir("images"):
		img_list.append(filename)
	
	if not os.path.exists('half_images'):
		os.makedirs('half_images')
	
	
	for filename in os.listdir("images"):
		img_list.append(filename)
		img = cv2.imread(os.path.join("images", filename))                        # Read image
		wd, hg = img.shape[:2]
		s2 = img[:wd-50, :hg]
		
		cv2.imwrite(os.path.join("images", filename), s2)
		
		
	for filename in os.listdir("images"):
		
		image_obj = Image.open(os.path.join("images", filename))
		rotated_image = image_obj.rotate(-90, expand = 1)
		rotated_image.save(os.path.join("images", filename))
	
	
	for filename in sorted(img_list):
		img = cv2.imread(os.path.join("images", filename))                        # Read image
		wd, hg = img.shape[:2]
		width_cutoff = hg // 2
		s1 = img[:, :width_cutoff]
		s2 = img[:, width_cutoff:]
		if(len(str(count)) == 1):
			outfile1 = "part0"+str(count)+"_" + "1.png"
			outfile2 = "part0"+str(count)+"_" + "2.png"
		else:
			outfile1 = "part"+str(count)+"_" + "1.png"
			outfile2 = "part"+str(count)+"_" + "2.png"
		cv2.imwrite("half_images/"+outfile1, s1)
		cv2.imwrite("half_images/"+outfile2, s2)
		count = count +1
		
def img_white_space_removed():
	count = 1
	img_list = []
	
	folder_name = input("Enter your White space remove folder name : ") 
	
	for filename in os.listdir(folder_name):
		img_list.append(filename)
		img = cv2.imread(os.path.join(folder_name, filename))                        # Read image
		wd, hg = img.shape[:2]
		#s2 = img[240:wd-120, :hg] #for #half images
		s2 = img[200:wd-120, :hg]
		
		cv2.imwrite(os.path.join(folder_name, filename), s2)
		count = count +1
	#print (img_list)

	
def again_split_images_into_half():
	
	count = 1
	img_list = []
	
	folder_name = input("Enter your 2 half Images folder name : ") 
	
	for filename in os.listdir(folder_name):
		img_list.append(filename)
	
	if not os.path.exists('each2_half_images'):
		os.makedirs('each2_half_images')
	
	
	for filename in sorted(img_list):
		img = cv2.imread(os.path.join(folder_name, filename))                        # Read image
		wd, hg = img.shape[:2]
		width_cutoff = hg // 2
		s1 = img[:, :width_cutoff]
		s2 = img[:, width_cutoff:]
		if(len(str(count)) == 1):
			outfile1 = "part0"+str(count)+"_" + "1.png"
			outfile2 = "part0"+str(count)+"_" + "2.png"
		else:
			outfile1 = "part"+str(count)+"_" + "1.png"
			outfile2 = "part"+str(count)+"_" + "2.png"
		cv2.imwrite("each2_half_images/"+outfile1, s1)
		cv2.imwrite("each2_half_images/"+outfile2, s2)
		count = count +1
		

	
def rotate_image():
	
	img_list = []
	folder_name = input("Enter your 3 half Images folder name : ") 
	
	for filename in os.listdir(folder_name):
		img_list.append(filename)
	
	
	for filename in os.listdir(folder_name):
		img_list.append(filename)
		img = cv2.imread(os.path.join(folder_name, filename))                        # Read image
		wd, hg = img.shape[:2]
		s2 = img[50:wd, :hg]
		
		cv2.imwrite(os.path.join(folder_name, filename), s2)
		
		
	for filename in os.listdir(folder_name):
		
		image_obj = Image.open(os.path.join(folder_name, filename))
		rotated_image = image_obj.rotate(-90, expand = 1)
		rotated_image.save(os.path.join(folder_name, filename))
	
	count = 1
	
	
	if not os.path.exists('each3_half_images'):
		os.makedirs('each3_half_images')
	
	
	for filename in os.listdir(folder_name):
		image_obj = cv2.imread(os.path.join(folder_name, filename))                        # Read image
		
		wd, hg = image_obj.shape[:2]
		width_cutoff = hg // 3
		s1 = image_obj[:, :width_cutoff]
		s2 = image_obj[:, width_cutoff:width_cutoff+width_cutoff]
		s3 = image_obj[:, width_cutoff+width_cutoff:]
		if(len(str(count)) == 1):
			outfile1 = "part0"+str(count)+"_" + "1.png"
			outfile2 = "part0"+str(count)+"_" + "2.png"
			outfile3 = "part0"+str(count)+"_" + "3.png"
		else:
			outfile1 = "part"+str(count)+"_" + "1.png"
			outfile2 = "part"+str(count)+"_" + "2.png"
			outfile3 = "part"+str(count)+"_" + "3.png"

		cv2.imwrite("each3_half_images/"+outfile1, s1)
		cv2.imwrite("each3_half_images/"+outfile2, s2)
		cv2.imwrite("each3_half_images/"+outfile3, s3)
		count = count +1

def image_to_string():

	pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

	count =1
	content = ""
	for filename in os.listdir("each2_half_images"):
		value=Image.open(os.path.join("each2_half_images", filename))
		content = content + "\n" + pytesseract.image_to_string(value,lang='tam')
		count = count +1
		
	for filename in os.listdir("each3_half_images"):
		value=Image.open(os.path.join("each3_half_images", filename))
		content = content + "\n" + pytesseract.image_to_string(value,lang='tam')
		count = count +1

		
	completeName = os.path.join("Output.txt")
	text_file = open(completeName, "w", encoding="utf-8")
	text_file.write(str(content))
	text_file.close()
	
	
pdf_to_ppm_and_png()
#split_images_into_half()
#img_white_space_removed()
#again_split_images_into_half()
#rotate_image()
#image_to_string()