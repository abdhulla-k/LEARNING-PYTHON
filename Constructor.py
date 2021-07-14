class FamilyMembersData:  # it is a class

    year = 2021         # year is a class atribute. atribute means variable.It is avilable in all objects

    def __init__(self, name, age, place) -> None:
        
        self.name = name    # this are object atribute.which means variable. it is only avilable under object
        self.age = age
        self.place = place
    
    def AdAge( self ):
        self.age = self.age + 1
    
    def Relocate( self, place ):
        self.place = place

    def DisplayAll( self ):
        print( "year is: "+str(FamilyMembersData.year )) #year is a class variable.there for, calling method of year is like this
        print( "Name is: "+self.name )
        print( "age is: "+str( self.age ))
        print( "place is: "+self.place )
        print( "______________________________________________" )

    """usage of 'classmethod' is below,  it is using to edit class variable true function. """
    @classmethod  # if you want to write a class method,Then use the keyword '@classmethod'
    def AddYear(cls):
        cls.year = cls.year + 1
        print( "======= ======= ======= ====== ========" )
        """here, 'cls' is a sample name. you can use any of name there.if you used the class name ,then it will work well.
        can use as 'FamilyMembersData.year = FamilyMembersData.year + 1'"""


x = FamilyMembersData( "Abdhu", 21, "Omassery" ) #argument passed to cunstructor.cunstructor working at the time of creation of object.
y = FamilyMembersData( "Abcd", 22, "Omassery" )#here, created two objects which x and y.then passed argument

x.DisplayAll()
y.DisplayAll()


"""This is one Editing method of class variable.onother one method is tue use the key word 'classmethod'.
Class bariable ia available globally in class"""
FamilyMembersData.year = FamilyMembersData.year + 1  
 
print( "======= ======= ======= ====== ========" )

x.AdAge()
y.AdAge()
x.Relocate( "koduvally" )
y.Relocate( "Koduvally" )
x.DisplayAll()
y.DisplayAll()


FamilyMembersData.AddYear() # here, called function 'AddYear'.This is an example for calling 'classmethod'.

x.AdAge()
y.AdAge()
x.Relocate( "Tsy" )
y.Relocate( "TSy" )
x.DisplayAll()
y.DisplayAll()

