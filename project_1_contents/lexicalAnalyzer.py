#checking if character falls into specific token type
def isString(charS):
    return charS.isalpha()

def isInt(intS):
    return intS.isdigit()

def isSeparator(c):
    return c in {";", "(", ")", "{", "}"}

def isOperator(c):
    return (c) in {"=",">","<","+","-","/","*"}

def isKW(c):
    keyword = {"if" : 0, "else" : 1, "return" : 2, "while" : 3, "int" : 4, "for" : 5}
    return keyword.get(c) != None



#import the text
def TextImport(filePath="p1Test.txt"):
    try:
        with open(filePath, 'r') as file:
            fileContent = file.read() + "\n" #add \n to stop indexing issues in string parsing and mark end of line/file

            return fileContent
    except FileNotFoundError:
        print(f"Error: File not found at {filePath}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



#tokenize the input text
def lexer(str):
    lexemes = []
    c = 0

    #goes through each character
    #build a string one by one
    #if it hits a character is not and int or a char 
    #goes to the dead state/marks end of token
    #add to tokens array and add the token type based on met criteria 
    while(c < len(str)):
        if(str[c] != " " and str[c] != "\n" and str[c] != "\t"):
            word = ""

            #check for comments
            #if there are, move to next line
            if(str[c] == "/" and str[c + 1] == "/"):
                c = str.find("\n", c)

        
            #check if integer
            elif(isInt(str[c])):
                while(isInt(str[c])):
                    word = word + str[c]

                    #dont skip to next if next is not int
                    if (isInt(str[c+1])):
                        c += 1
                    else:
                        break
                    
                lexemes.append([word, "integer"])

            #if the lexme does not start with an integer, 
            #then it must start with letters(identifier, and keywords), an operator, or a seperator
            else:
                while(isString(str[c])):
                    word = word + str[c]

                    #dont skip to next if next is not string or int
                    if (isString(str[c+1])):
                        c += 1
                    else:
                        break

                if(word == ""):
                    word = str[c]

                #if word is a keyword
                if(isKW(word)):
                    lexemes.append([word, "keyword"])

                #if word is a operator
                elif(isOperator(word)):
                    lexemes.append([word, "operator"])

                #if word is a seperator
                elif(isSeparator(word)):
                    lexemes.append([word, "separator"])

                else:
                    #otherwise return identifier
                    lexemes.append([word, "identifier"])
        c += 1  #skip spaces

    return lexemes



#############################################################################

#main
tokens = lexer(TextImport("p1Test.txt"))

#print it out
print("hopefully tokenized stuff (<lexeme> = <token>): ")
for t in tokens:
    print(f"    {t[0]} = {t[1]}")