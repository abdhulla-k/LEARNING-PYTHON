class Sample:
    # below is an example for operator over loading.

    def Edit_name( self, name):

       self.name = name
    
    # it is the fmethod for add two between two objects. you have avilable methods for every operators
    def __add__(self,other):  
        name = self.name + other.name
        return name


first_name = Sample()
second_name = Sample()

first_name.Edit_name( "Abdhulla " )
second_name.Edit_name( "K" )

full_name = first_name + second_name
print( full_name )

