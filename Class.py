class FamilyMembersData:  # class creation format is this.
    
    def Hello( self,name ):
        self.name = name
    def PrintName( self ):
        print( self.name )


x = FamilyMembersData()  #create object like this and call as below.
y = FamilyMembersData()

name = "Abdhu"   # you can pass argument also like this

x.Hello( name )
y.Hello( "Abcd" )

x.PrintName()
y.PrintName()

