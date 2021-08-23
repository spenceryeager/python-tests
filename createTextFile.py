import os

workingdir = '/home/spenceryeager/Documents/python_bits/text_test'
filename = 'readme.txt'

path = os.path.join(workingdir, filename)
testText = open(path, 'w')

testVar = "This is also a test"
testText.write("hello test"+ testVar + '\n' + testVar)
testText.close()