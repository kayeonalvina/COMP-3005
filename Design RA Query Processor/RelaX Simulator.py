import re

def main():
    text = """Employees (EID, Name, Age) = {
E1, John, 32
E2, Alice, 28
E3, Bob, 29}"""
    
    parse(text)

def parse(text):
    print(text)
    print("\n")
    spaceSplit = re.split('[, \n}{()]', text)
    print(spaceSplit)

    # removing empty strings 
    finalList = list(filter(None, spaceSplit))
    print(finalList)

    name = finalList[0]


main()