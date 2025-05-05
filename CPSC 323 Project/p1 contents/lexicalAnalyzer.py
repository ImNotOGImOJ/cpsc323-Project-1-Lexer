import re

#collection of keywords, seperators
keyword = {"if" : 0, "else" : 1, "return" : 2, "while" : 3, "int" : 4, "for" : 5}
separator = {";" : 0, "(" : 1, ")" : 2, "{" : 3, "}" : 4}
operator = {"=" : 1, ">" : 2, "<" : 3, "+" : 4, "-" : 5, "/" : 6, "*" : 7}
tokenTypes = ["keywords", "separator", "operator", "integer", "identifier"]
tokens = {}


#checking if character falls into specific token type
def isString(charS):
    return (ord(charS) >= 65 and ord(charS <= 90)) or (ord(charS) >= 97 and ord(charS) <= 122)

def isInt(intS):
    return (ord(intS) >= 48 and ord(intS) <= 57)

def isSep(c):
    return separator.get(c) != None

def isOp(c):
    return operator.get(c) != None

def isKW(c):
    return keyword.get(c) != None


def stringRE(OGText, c):
    word = c
    c += 1

    #if int or char add it to the word
    while(isInt(OGText[c]) or isString(OGText[c])):
        word = word + c
        c += 1
    
    if()

    elif ():
        


#states for if first char is an int (checks if fully int)
def intRE(OGText, c):
    word = ""
    #if next char are not an int, return 
    while(isInt(OGText[c])):
        word = word + c
        c += 1
    return word, "integer", c




def TextImport(filePath="text.txt"):
    try:
        with open(filePath, 'r') as file:
            fileContent = file.read() + " " #add extra space to stop indexing issues in string parsing

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
def lexer(str):
    wordBuilder = ""
    tokens = {}

    #goes through each character
    #build a string one by one
    #if hit a character that goes to the dead state / marks end of token
    #add to tokens dictionary and add the token type based on met criteria 
    for c in range(len(str)):
        #check for comments
        if str[c] == "/":
            print("")
            #check for opperators
            #check for integer

            #check for identifier and keywords
        elif (isString(str[c])):
            print("")
            #if end of token
        elif str[c] == " " or str[c] == "\n":
            tokens.append( "      RETURN KEY VALUE PAIR OF WORD      ")
            wordBuilder = ""
        else:
            wordBuilder += str[c]





def encode(textInput=""):
    ids = re.split(r'([,.?_!"()\']|--|\s)', textInput)
    ids = [item.strip() for item in ids if item.strip()]
    return ids


#






#main?

print(encode(TextImport("test.txt")))