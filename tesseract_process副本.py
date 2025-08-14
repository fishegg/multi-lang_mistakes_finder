import pytesseract
import re
import image_process

class text_recognition(object):
	def get_text(image,lang):
		text=pytesseract.image_to_string(image,lang=lang,config="--psm 3 -c preserve_interword_spaces=1")
		result=re.split(r"\n|\s{2,}",text)
		return result