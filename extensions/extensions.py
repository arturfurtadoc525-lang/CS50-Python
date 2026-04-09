import re

response = input("File name: ")

if re.search(".gif", response, re.IGNORECASE):
    print("image/gif")
elif re.search(".jpg", response, re.IGNORECASE):
    print("image/jpeg")
elif re.search(".jpeg", response, re.IGNORECASE):
    print("image/jpeg")
elif re.search(".pdf", response, re.IGNORECASE):
    print("application/pdf")
elif re.search(".png", response, re.IGNORECASE):
    print("image/png")
elif re.search(".txt", response, re.IGNORECASE):
    print("text/plain")
elif re.search(".zip", response, re.IGNORECASE):
    print("application/zip")
else:
    print("application/octet-stream")
