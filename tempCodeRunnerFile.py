 img_logo=Image.open('College_images/mp_logo.jpg')
        img_logo=img_logo.resize((55,55))
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo =Label(self.root,image=self.photo_logo)
        self.logo.place(x=270 , y=0 , width=50 , height=50)