
"""
CTEC 121
<Grant Parkinson>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""




from math import *
def main():
    '''
    x = 1
    y = 2
    z = 3
    print("x: {0}, y: {1}, z: {2}".format(x, y, z))

    print("pi:", pi, "e:", e)
    print("pi: {0:0.2f}, e: {1:0.2f}".format(pi, e))
    print("pi: {0:10.4f}, e: {1:10.4f}".format(pi, e))

    # file processing
    print()
    #infile = open("sample.txt", 'r')
    # rint(infile)

    # get everything
    wholefiletext = infile.read()
    print(wholefiletext)
    wholefiletext = infile.read()
    print("*", wholefiletext, "*", sep="")

    infile.seek(5)
    wholefiletext = infile.read()
    print("*", wholefiletext, "*", sep="")

    # demo readlines()
    wholefiletextaslist = infile.readlines()
    print(wholefiletextaslist)
    for line in wholefiletextaslist:
        print(line.rstrip())

    # demo file a line at a time
    for line in infile:
        print(line, end="")


    print()
    # gets first line
    line = infile.readline()
    while line != "":  # equivilant to while not end of file(eof)
        print(line.rstrip())
        # get next line
        line = infile.readline()

    # dictionaries
    # create an empty dictionary
    dict1 = {}
    print(dict1)

    dict2 = {}
    dict2[1] = "one"
    dict2[2] = "two"
    dict2[3] = "three"
    print(dict2)

    dict1 = {1: 'one', 2: 'two', 3: 'three'}
    print(dict1)

    print(dict1[2])
    print()
    print(dict1.keys())
    print(dict1.values())
    print(dict1.items())

    num = 1234
    print("Num:", num)
    processprimitiveargument(num)
    print("Num:", num)
    '''
    num = [1234]
    print("num:", num)
    processlistargument(num)
    print("num:", num)
    print()


def processprimitiveargument(x):
    print("input value:", x)
    x = 99
    print("final value:", x)


def processlistargument(l):
    print("input list:", l)
    l[0] = 99
    print("final list:", l)


main()
