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
        messagebox.showerror("MATCH RESULT","DRAW")


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

    frame=Frame(root)
    frame.pack()
    for row in range(3):
        for col in range(3):
            button[row][col]=Button(frame,text=' ',bg="white",fg="red",width=20,height=10,command=lambda row=row,col=col :clicked(row,col))
            button[row][col].grid(row=row,column=col)

root.mainloop()
