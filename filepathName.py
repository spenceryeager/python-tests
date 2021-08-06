import os

#testing the os.path.join function

filepath = '/test/directory'
filename = 'hello'

test1 = filepath + '/' + filename
print(test1)

test2 = os.path.join(filepath, filename)
print(test2)