import string
from translate import Translator

#constants
tRanslator: Translator = Translator(to_lang="fr")
ALPHABET: set = set(string.ascii_letters)
isAlphabet: bool = lambda letter : letter in ALPHABET
STORAGE: dict[str,str] = {}

class StringText:
    content: str
    isSymbol: bool
    translatedText: str
    """
    Takes in a word or a symbol and wether is it a symbol or not
    StringText( content: str, isSymbol: bool)
    e.g 
    StringText("Names", false)
    """
    def __init__(self, content, isSymbol) -> None:
        self.content = content
        self.isSymbol = isSymbol
        self.translatedText =  None

class Container:
    originLine: str
    modifiedLine: str
    allContent: list[StringText]

    def __init__(self) -> None:
        self.allContent = list([])

    def setLines(self,originLine: str,modifiedLine: str) -> None:
        self.originLine = originLine
        self.modifiedLine = modifiedLine
    
    def add(self,word: StringText, symbol: StringText) -> None:
        self.allContent.append(word)
        self.allContent.append(symbol)
    
    def getsyntaxList(self) -> list[str]:
        return [text.content for text in self.allContent]

    def getTranslatedSyntax(self) -> list[str]:
        return [
            text.translatedText if not text.isSymbol else text.content for text in self.allContent
            ]
    
    def getAllContent(self) -> list[StringText]:
        return self.allContent


def equals(one: str, two:str):
    return one == two

def translate(text: StringText) -> tuple[str, str]:
    global STORAGE
    if not (text.content in STORAGE):
        # if record does not exists then store data
        translation: str = tRanslator.translate(text.content)
        firstLang, secondLang = text.content, translation
        STORAGE[firstLang] = secondLang
    else:
        # if record already exists then get data
        firstLang, secondLang = text.content, STORAGE[text.content]
    
    return secondLang

def processTranslate(line: str, lineNumber: int) -> Container :
    container: Container = Container()
    output: str = ""
    word: str = ""
    for index, letter in enumerate(line):
        if isAlphabet(letter):
            word += letter
        elif not isAlphabet(letter) or equals(index, len(line)-1):
            word_: StringText = StringText(word, False)
            symbol_: StringText = StringText(letter, True)
            container.add(word_, symbol_)
            output += word + " "
            word = ""
    container.setLines(line,output)
    return container


def breakTextFile(fileName: str) -> list[str]: 
    with open(fileName, "r") as f:
        Lines: list[str] = f.readlines()

    for index, line in enumerate(Lines):
        lineNumber: int = index
        processedLine: Container = processTranslate(line, lineNumber)
        for word in processedLine.getAllContent():
            if not word.isSymbol:
                word.translatedText = translate(word)
        line = "".join(processedLine.getTranslatedSyntax())
        print(line)

        
        

if __name__ == "__main__":
    breakTextFile("main.py")






    
