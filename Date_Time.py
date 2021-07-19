import datetime   # this is an example of date setting and date related probloms

print(datetime.datetime.now())  # this is the method for printing current date and time. 
#do you want to print custom order.then look below

x = datetime.datetime.now()
print( x.strftime( "%d/%m/%Y")) # %d = date, %m = month, %Y = year. it use as like

# do you want to print only month or date or etc... example of month is below.
print( datetime.date.today().month )

# do you want to print a spesific date.then use this method
date = datetime.datetime(2021,4,22)
print( date )

# do you want to find diferent among two dates. example is below.
date_a = datetime.datetime( 2012,3,9 )
date_b = datetime.datetime( 2021,4,24 )
dif = date_b - date_a
print( dif )

n = datetime.datetime.now()
diference = n - x  # we are finding here, the running tme of this program. x is created on top of this file
print( diference )  # diference priscenting in micro second

# eny of the probloms are possible to solve. if you want to inform about that, then you can serch in google about datetime and enything about enithing
