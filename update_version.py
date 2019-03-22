import os
import requests

image_url = "https://raw.githubusercontent.com/Butterfly9/upgrade/master/make_pdf.py"
  
r = requests.get(image_url) # create HTTP response object 
  
with open("make_pdf.py",'wb') as f: 
    f.write(r.content)

print("file downloaded")
os.remove("../website/make_pdf.py")
print("File deleted")
os.rename("make_pdf.py", "../website/make_pdf.py")
print("File copied")

