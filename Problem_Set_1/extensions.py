def main():
    file_name = input("File name: ").lower()
    print (type_detect(file_name))
           
def type_detect(file):  
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        return "image/jpeg"
    elif file.endswith(".pdf"):
        return "application/pdf"
    elif file.endswith(".txt"):
        return "application/text"
    else:
        return "application/octet-stream"

main()