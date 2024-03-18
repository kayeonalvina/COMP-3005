import re

def main():
    text = """Employees (EID, Name, Age) = {
E1, John, 32
E2, Alice, 28
E3, Bob, 29}"""
    
    parse(text)

def parse(text):
    print(text)
    print()
    lineSplit = re.split('\n', text)
    print(lineSplit)


    # spltting first line and filtering out empty strings
    firstLine = re.split("[(,)={ ]", lineSplit[0])
    finalfirst = list(filter(None, firstLine))

    dataStruct = {}

    for x in range (1, len(lineSplit)):
        pass


    # removing empty strings 
    # finalList = list(filter(None, lineSplit))
    # print(finalList)

    # name = finalList[0]


main()