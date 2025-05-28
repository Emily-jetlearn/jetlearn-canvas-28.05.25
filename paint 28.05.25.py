from tkinter import *
from tkinter.colorchooser import askcolor


class paint(object):
    default_pensize=8.0
    default_pencol="black"
    
    def __init__(self):
        self.window=Tk()
        self.window.config(bg="#7cc4af8f")
        self.font=("Comic sans ms" , 12)
        self.penbutton=Button(self.window, text="Pen",font=self.font,width=10,activebackground="pink",bg="teal",command=self.usepen)
        self.penbutton.grid(row=0,column=0)
        self.brushbutton=Button(self.window, text="Brush",font=self.font,width=10,activebackground="pink",bg="teal",command=self.usebrush)
        self.brushbutton.grid(row=0,column=1)
        self.colourbutton=Button(self.window, text="Colour",font=self.font,width=10,activebackground="pink",bg="teal",command=self.usecolour)
        self.colourbutton.grid(row=0,column=2)
        self.erasebutton=Button(self.window, text="Eraser",font=self.font,width=10,activebackground="pink",bg="teal",command=self.useeraser)
        self.erasebutton.grid(row=0,column=3)
        #sliders for tool size
        self.penslider=Scale(self.window,from_=1,to=10,orient=HORIZONTAL,label="pen size",font=self.font,width=10,bg="teal",fg="pink",activebackground="purple",troughcolor="#c47cbd")
        self.penslider.grid(row=0,column=4,pady=10)
        self.brushslider=Scale(self.window,from_=1,to=10,orient=HORIZONTAL,label="brush size",font=self.font,width=10,bg="teal",fg="pink",activebackground="purple",troughcolor="#c47cbd")
        self.eraseslider=Scale(self.window,from_=1,to=10,orient=HORIZONTAL,label="eraser size",font=self.font,width=10,bg="teal",fg="pink",activebackground="purple",troughcolor="#c47cbd")
        #canvas
        self.c=Canvas(self.window,bg="white",width=600,height=600,highlightbackground="black",highlightthickness=5)
        self.c.grid(row=1,column=0,columnspan=5,padx=20,pady=10)

        self.setup()
        

        self.window.mainloop()
    def setup(self):
        self.oldx=None
        self.oldy=None
        self.linewidth=self.penslider.get()
        self.colour=self.default_pencol.get()
        self.eraser_ON=False
        self.active_button=self.penbutton
        self.c.bind=("<B1-Motion>",self.paint)
        self.c.bind=("<ButtonRelease-1>",self.reset)
