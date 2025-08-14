from PIL import Image
import os
from datetime import datetime

class image_picker(object):
	def get_image_by_path(file):
		image=Image.open(file)
		return image

	def get_image_by_adb(language):
		timestamp=str(int(datetime.now().timestamp()))
		image_file=language+"."+timestamp+".png"
		command="adb shell screencap -p /sdcard/"+image_file
		os.system(command)
		command="adb pull /sdcard/"+image_file+" ./"
		os.system(command)
		command="adb shell rm /sdcard/"+image_file
		os.system(command)
		file="./"+image_file
		image=Image.open(file)
		return image,image_file

	def get_image_from_dir(dir):
		types=("png","jpg","jpeg")
		image_set=set()
		for a,b,files in os.walk(dir):
			for file in files:
				if(file.split(".")[-1] in types):
					image_set.add(file)
		return image_set