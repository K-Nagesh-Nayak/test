from tkinter import  *
from tkinter import messagebox
click=True
count=0

def check_winner():
    global winner
    winner=False
    for row in range(3):
        if button[row][0]["text"] == button[row][1]["text"] == button[row][2]["text"] != " ":
            return True
    for col in range(3):
        if button[0][col]["text"] == button[1][col]["text"] == button[2][col]["text"] != " ":
            return True
         
    if button[0][0]["text"] == button[1][1]["text"] == button[2][2]["text"] != " ":
        return True
    
    if button[0][2]["text"] == button[1][1]["text"] == button[2][0]["text"] != " ":
        return True
    
    empty=9
    for row in range(3):
        for col in range(3):
            if button[row][col]['text'] !=" ":
                empty-=1
    if empty==0:
        messagebox.showerror("TIE")


def clicked(row,col):
    global click,count

    if button[row][col]["text"]==" " and click==True:
        button[row][col]["text"]="X"
        click=False
        count +1
        if check_winner() ==True:
            messagebox.showerror("RSESULT","X IS WINNER")

    elif button[row][col]["text"]==" " and click==False:
        button[row][col]["text"]="O"
        click=True
        count +1
        if check_winner() ==True:
            messagebox.showerror("RSESULT","O IS WINNER")
    else:
        messagebox.showerror("ERROR","TRY OTHER BOX ")

    

if __name__=="__main__":
    root=Tk()
    root.configure(background="lightblue")
    root.geometry("470x500")
    root.title("TIC TAC TOE")

    button=[[0,0,0],
            [0,0,0],
            [0,0,0]]

    '''b1=Button(root,text=' ',bg="white",fg="red",width=20,height=10,command=lambda:clicked(b1))
    b1.grid(row=0,column=1)
    b2=Button(root,text=' ',bg="white",fg="red",width=20,height=10,command=lambda:clicked(b2))
    b2.grid(row=0,column=2)
    b3=Button(root,text=' ',bg="white",fg="red",width=20,height=10,command=lambda:clicked(b3))
    b3.grid(row=0,column=3)

    b4=Button(root,text=' ',bg="white",fg="red",width=20,height=10,command=lambda:clicked(b4))
    b4.grid(row=1,column=1)
    b5=Button(root,text=' ',bg="white",fg="red",width=20,height=10,command=lambda:clicked(b5))
    b5.grid(row=1,column=2)
    b6=Button(root,text=' ',bg="white",fg="red",width=20,height=10,command=lambda:clicked(b6))
    b6.grid(row=1,column=3)

    b7=Button(root,text=' ',bg="white",fg="red",width=20,height=10,command=lambda:clicked(b7))
    b7.grid(row=2,column=1)
    b8=Button(root,text=' ',bg="white",fg="red",width=20,height=10,command=lambda:clicked(b8))
    b8.grid(row=2,column=2)
    b9=Button(root,text=' ',bg="white",fg="red",width=20,height=10,command=lambda:clicked(b9))
    b9.grid(row=2,column=3)'''

    frame=Frame(root)
    frame.pack()
    i=0
    for row in range(3):
        for col in range(3):
            button[row][col]=Button(frame,text=' ',bg="white",fg="red",width=20,height=10,command=lambda row=row,col=col :clicked(row,col))
            button[row][col].grid(row=row,column=col)

root.mainloop()