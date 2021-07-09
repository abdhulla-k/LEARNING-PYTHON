
values = [ "AbdhuOmy" , "Kallidumpil" , "Omassery" , "Kozhikode" , "Kerala" , "India"] #it is a model of a list or array
#It is mutable that means possible to add a neew array to this one and possible to change one possiton that you need

Family = [ "Ahammed Kutty" , "Ayisa" , "Fathima" , "Mariyam" , "Kadeeja" , "Sulaika"]

Family.append( "Hi" )  


print( values )
print( Family )
print( values + Family ) # possible to add list after list

print( len( values ) )   # 'len' is a function using for find the length of a list
print( len( values + Family ))

print( values[ 0 ] )     # possible to print only one possition from list or array
print( values[ -1 ] )
print( Family[ -2: ] )    #possible to print only something or remove something

values.append( input( "Enter a numbedr" )) # possible to input something to end possition of a list

print( values )