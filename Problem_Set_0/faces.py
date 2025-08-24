def convert(text):
    str_final = text.replace(':)', '🙂').replace(':(', '🙁')
    return (str_final)

def main():
    string = input()
    print (convert(string))
           
main()