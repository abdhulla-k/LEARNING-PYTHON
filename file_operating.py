# following is an example for file oerating .you can operate files thrue code.edit or add new file etc...

c = open("Abdhu.py","w+") # first give the file path and then permission
# for permission operators,you can serch in google as 'file permission' or serch eniting about this
c.write( "print('hello')")#this is the method for write in that file
# here we written hello throue this program
c.close() # must close the file after operation.becouse it is necessery.


# possible to read a file.the program as follow
with open( "Constructor.py" ,"r") as f:# here we are going to read 'constructor.py'.'with is tlhe keyword we used here.
    x = f.read()

print(x)