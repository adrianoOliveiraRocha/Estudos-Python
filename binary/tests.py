import pickle

a = ['test value','test value 2','test value 3']
print(a)
file_name = 'testfile'
fileObject = open(file_name, 'wb')
pickle.dump(a, fileObject)
fileObject.close()

fileObject = open(file_name, 'rb')
b = pickle.load(fileObject) 
print(b)

print(a == b)