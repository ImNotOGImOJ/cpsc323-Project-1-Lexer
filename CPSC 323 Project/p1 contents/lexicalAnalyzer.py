import re

#collection of keywords, seperators
keywords = ["if", "return"]

def TextImport(filePath="text.txt"):
    try:
        with open(filePath, 'r') as file:
            fileContent = file.read()
            
            #remove comments before processing
            for c in len(fileContent):
                if fileContent[c] and 

            return fileContent
    except FileNotFoundError:
        print(f"Error: File not found at {filePath}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
#designate lines (find new line character)
#remove comments

#tokenize the input text

def encode(textInput=""):
    ids = re.split(r'([,.?_!"()\']|--|\s)', textInput)
    ids = [item.strip() for item in ids if item.strip()]
    return ids


#






#main?

print(encode(TextImport("test.txt")))