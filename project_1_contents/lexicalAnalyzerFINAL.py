#table for representing transitions between states
START = "START"
IN_ID = "IN_ID"
IN_INT = "IN_INT"
DONE = "DONE"

transitionTable = {
    START: {
        'LETTER': IN_ID,
        'DIGIT': IN_INT,
        'OP': DONE,
        'SEP': DONE,
        'WHITESPACE': START,
    },
    IN_ID: {
        'LETTER': IN_ID,
        'DIGIT': IN_ID,
        'WHITESPACE': DONE,
        'OP': DONE,
        'SEP': DONE,
    },
    IN_INT: {
        'DIGIT': IN_INT,
        'WHITESPACE': DONE,
        'OP': DONE,
        'SEP': DONE,
    }
}


#checking if character falls into specific token type
def charClassification(c):
    if c.isalpha():
        return 'LETTER'
    elif c.isdigit():
        return 'DIGIT'
    elif c in {'<', '>', '=', '+', '-', '*', '/'}:
        return 'OP'
    elif c in {';', '(', ')', '{', '}'}:
        return 'SEP'
    elif c.isspace():
        return 'WHITESPACE'
    else:
        return 'UNKNOWN'

#specific for checking if lexeme is a keyword
def isKW(lexeme):
    return lexeme in ["if", "else", "for", "while", "return"]

#import the text
def textImport(filePath="p1Test.txt"):
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
    lexeme = ""
    tokens = []
    state = START
    i = 0

    #goes through each character
    #build a string one by one
    #if it hits a character is not and int or a char 
    #goes to the dead state/marks end of token
    #add to tokens array and add the token type based on met criteria 
    while(i < len(str)):
        #itterate thorugh string classifying each char
        c = str[i]
        charClass = charClassification(str[i])


        #remove comments
        if (i < len(str) - 1) and c == "/" and str[i+1] == "/":
            i = str.find("\n", i)+1
            continue

        #if state in start
        if(state == START and charClass in transitionTable[START]):
            nextState = transitionTable[START][charClass]
            if nextState == DONE:
                tokens.append([c, 'operator' if charClass == 'OP' else 'separator'])
            elif (charClass != "WHITESPACE" and charClass != "UNKNOWN"):
                state = nextState
                lexeme += c

        #if state in other states
        elif(state in transitionTable and charClass in transitionTable[state]):
            nextState = transitionTable[state][charClass]
            if nextState == state:          #if still in same state, move to next char and check
                lexeme += c
            else:                           #else it is done, process token
                if(isKW(lexeme)):           #test for keyword
                    tokenType = "keyword"
                else:
                    tokenType = 'identifier' if state == IN_ID else 'integer'
                tokens.append([lexeme, tokenType])
                lexeme = ""
                state = START
                continue

        else:       #for unknown characters, if there is a lexeme, turn it into a token
            if lexeme:
                if(isKW(lexeme)):           #test for keyword
                    tokenType = "keyword"
                else:
                    tokens.append([lexeme, 'identifier' if state == IN_ID else 'integer'])
            lexeme = ''
            state = START
        i += 1

        #for last token in case it didn't finish
    if lexeme:
        if(isKW(lexeme)):           #test for keyword
            tokenType = "keyword"
        else:
            token_type = 'identifier' if state == IN_ID else 'integer'
        tokens.append([lexeme, token_type])


    return tokens


#############################################################################

#main
tokens = lexer(textImport("p1Test.txt"))

#print it out
print("hopefully tokenized stuff (<lexeme> = <token>): ")
for t in tokens:
    print(f"    \"{t[0]}\" = {t[1]}")