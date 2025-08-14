import image_process
import tesseract_process
import book_process
import os

option=int(input("1=file,2=adb,3=directory:"))
strings=[]
book_file="your_book_file.xlsx"
book=book_process.book(book_file)
book.read()
if(option==1):
	image_file="your_image_file.png"
	language=image_file.split("\\")[-1].split(".")[0]
	image=image_process.image_picker.get_image_by_path(image_file)
	strings=tesseract_process.text_recognition.get_text(image,language)
	book.record(strings,image_file)
elif(option==2):
	language=input("language:")
	while(True):
		image,image_file=image_process.image_picker.get_image_by_adb(language)
		strings=tesseract_process.text_recognition.get_text(image,language)
		book.record(strings,image_file)
		flag=input("input n to stop or enter to continue")
		if(flag=="n"):
			break
elif(option==3):
	dir=
	image_set=image_process.image_picker.get_image_from_dir(dir)
	for image_file in image_set:
		language=image_file.split(".")[0]
		image_file=os.path.join(dir,image_file)
		print(image_file)
		image=image_process.image_picker.get_image_by_path(image_file)
		strings=tesseract_process.text_recognition.get_text(image,language)
		book.record(strings,image_file)
book.save()