import qrcode
 
# Data to be encoded
data = "https://www.linkedin.com/in/saran-m-6384a299/"
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('linkedin.png')