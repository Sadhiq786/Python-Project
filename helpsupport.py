from tkinter import*
from PIL import Image,ImageTk



class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"E:\Face_Recognition\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"E:\Face_Recognition\Images_GUI\bg4.png")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        title_lb1 =Label(self.root,text="Help Support",font=("verdana",25,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=-20,y=130,width=1400,height=45)
        

        # set image as lable
        f_lbl=Label(self.root,image=self.photobg1)
        f_lbl.place(x=0,y=176,width=1370,height=768)

        

        dev_det1=Label(f_lbl,text="Email ID", font=("verdana",20,"bold"),bg="white",fg="dark blue")
        dev_det1.place(x=470,y=95,width=400,height=30)

        dev_det2=Label(f_lbl,text="ivanmoses2000@gmail.com\n\n kandukurivikas@gmail.com\n\n sksadhiqsksadhiq@gmail.com", font=("verdana",16,"bold"),bg="white",fg="blue")
        dev_det2.place(x=470,y=125,width=400,height=220)
       






if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()