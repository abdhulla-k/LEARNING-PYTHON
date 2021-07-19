# In python, you can possible to inherit multiple classes in to one class. Example is below:


class First():

    def display(self):
        print( "From First Class" )
    
class Second():

    def display(self):
        print( "From secaond Clss" )

class Third(First, Second ):   # here we are inherited the class Firs and Second in to Thed.

    def display_third(self):
        print( "From third" )

x = Third()

x.display_third()
x.display()    # There are two methods in the same naem display. one is in first class and onother one is in second class
"""But we are only called display. when, which display will work ? at the time of inheritants, which class is inherited
firs, that class including display will work first. here, we inherited firsly the class first.then the display method is 
working from firs class"""

