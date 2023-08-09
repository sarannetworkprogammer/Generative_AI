import qrcode
 
# Data to be encoded
data = "https://drive.google.com/drive/folders/1JWPFeAa_OERbFWzOgp2Qcqm3KJmIEww2?usp=sharing"
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('resume.png')