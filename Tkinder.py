from tkinter import * # import module which do you need.

window = Tk()  # here we created an object

window.geometry("500x500")  #window size creation

window.title("Welcome to LikeGeeks app") #example for title creation.
window.configure( background = "#eef334")

#below method is an example for add an exicution in to button.define the method and add that to buttun's bracket
def exicution():
    print("Hello")  



Button1 = Button(text = "Ok",width = 3, height = 2, bg="red", fg="red" ,command=exicution) # button creation,exicution add.
Label = Label(window,text="let us start")  # label creation.take a look below,called the pack.that must need for work
Button2 = Button(text = "+",width = 3, height = 2, bg="red", fg="red" ,command=exicution)

Button1.grid(row=0,column=0)
Button2.grid(row=1,column=0)


# Button1.pack()  if you use the grid,then does not need pack
# Button2.pack()
#Label.pack()




window.mainloop() # it is important for every window.for non stop working.