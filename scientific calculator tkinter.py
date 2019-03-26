from tkinter import *
import math
root= Tk()
root.title('Scientific Calculator')
root.geometry('728x272')

h = font.Font(root, size=11, weight=font.BOLD)
#virtual

def inputvalue(agr):
    global a
    a = a + str(agr)
    equation.set(a)

    

def clrall():
    global a
    a = ""
    equation.set("")
    

def clr():
    global a
    a=str(a[0:-1])
    equation.set(a)


#~~~~~real~~~~~~~~~~~~~~~~~~

#replica is replica of inputvalue
def replica(ar):
    global c
    c=c+str(ar)
    

#clear is replica of clr
def clear():
    global c
    c=str(c[0:-1])


def clearall():
    global c
    c = ""

    
def equal():
    global c
    global a
    try:
        total = str(eval(c))
        equation.set(total)
       
        w=open("calcy.txt","a+")
        w.writelines(a)
        w.writelines(" = ")
        w.writelines(total)
        w.write("\n")
        w.close()
        
        a = total
        c = total
    except SyntaxError:
        equation.set('Error')
        a = ""
        c = ""


#~~~~~~~~~~~~~~~~~~~~~history~~~~~~~~~~~~~~~~~~~~~
def history():
    r=open("calcy.txt","r+")
    x=r.readlines()
    y=len(x)-2
    equation.set(x[y][0:-2])
    r.close()
    


c = ""
a = ""
equation = StringVar()
calculation = Entry(root,textvariable = equation,width=50)
equation.set("Input")
calculation.grid(row=0, column=1,rowspan=1,columnspan=40)

Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="History",command=lambda:history()).grid(row=0, column=0)

Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="sin",command=lambda:[inputvalue('sin('),replica('math.sin(')]).grid(row=2, column=0)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="cos",command=lambda:[inputvalue('cos('),replica('math.cos(')]).grid(row=2, column=1)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="tan",command=lambda:[inputvalue('tan('),replica('math.tan(')]).grid(row=2, column=2)
Button(root,font= h, height='2', width='7',bg="red", fg="white", text="²√",command=lambda:[inputvalue('√('),replica('math.sqrt(')]).grid(row=2, column=3)
Button(root,font= h, height='2', width='7',bg="red", fg="white", text="³√",command=lambda:[inputvalue('^(1/3)'),replica('**(1/3)')]).grid(row=2, column=4)
Button(root,font= h, height='2', width='7',bg="red", fg="white", text="x²",command=lambda:[inputvalue('^2'),replica('**2')]).grid(row=2, column=5)
Button(root,font= h, height='2', width='7',bg="red", fg="white", text="Clr",command=lambda:[clr(),clear()]).grid(row=2, column=6)
Button(root,font= h, height='2', width='7',bg="red", fg="white", text="AC",command=lambda:[clrall(),clearall()]).grid(row=2, column=7)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="sin¯¹",command=lambda:[inputvalue('sin¯¹('),replica('math.asin(')]).grid(row=3, column=0)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="cos¯¹",command=lambda:[inputvalue('cos¯¹('),replica('math.acos(')]).grid(row=3, column=1)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="tan¯¹",command=lambda:[inputvalue('tan¯¹('),replica('math.atan(')]).grid(row=3, column=2)
Button(root,font= h, height='2', width='7',bg="black", fg="white", text="7",command=lambda:[inputvalue(7),replica(7)]).grid(row=3, column=3)
Button(root,font= h, height='2', width='7',bg="black", fg="white", text="8",command=lambda:[inputvalue(8),replica(8)]).grid(row=3, column=4)
Button(root,font= h, height='2', width='7',bg="black", fg="white", text="9",command=lambda:[inputvalue(9),replica(9)]).grid(row=3, column=5)
Button(root,font= h, height='2', width='7',bg="blue", fg="white", text="π",command=lambda:[inputvalue('3.14'),replica('3.14')]).grid(row=3, column=6)
Button(root,font= h, height='2', width='7',bg="blue", fg="white", text="mod",command=lambda:[inputvalue('%'),replica('%')]).grid(row=3, column=7)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="n!",command=lambda:[inputvalue('fact('),replica('math.factorial(')]).grid(row=4, column=0)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="e",command=lambda:[inputvalue('2.71828'),replica('2.71828')]).grid(row=4, column=1)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="x³",command=lambda:[inputvalue('^3'),replica('**3')]).grid(row=4, column=2)
Button(root,font= h, height='2', width='7',bg="black", fg="white", text="4",command=lambda:[inputvalue(4),replica(4)]).grid(row=4, column=3)
Button(root,font= h, height='2', width='7',bg="black", fg="white", text="5",command=lambda:[inputvalue(5),replica(5)]).grid(row=4, column=4)
Button(root,font= h, height='2', width='7',bg="black", fg="white", text="6",command=lambda:[inputvalue(6),replica(6)]).grid(row=4, column=5)
Button(root,font= h, height='2', width='7',bg="blue", fg="white", text="x",command=lambda:[inputvalue('x'),replica('*')]).grid(row=4, column=6)
Button(root,font= h, height='2', width='7',bg="blue", fg="white", text="÷",command=lambda:[inputvalue('÷'),replica('/')]).grid(row=4, column=7)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="xⁿ",command=lambda:[inputvalue('^'),replica('**')]).grid(row=5, column=0)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="10ⁿ",command=lambda:[inputvalue('10^'),replica('10**')]).grid(row=5, column=1)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="2ⁿ",command=lambda:[inputvalue('2^'),replica('2**')]).grid(row=5, column=2)
Button(root,font= h, height='2', width='7',bg="black", fg="white", text="1",command=lambda:[inputvalue(1),replica(1)]).grid(row=5, column=3)
Button(root,font= h, height='2', width='7',bg="black", fg="white", text="2",command=lambda:[inputvalue(2),replica(2)]).grid(row=5, column=4)
Button(root,font= h, height='2', width='7',bg="black", fg="white", text="3",command=lambda:[inputvalue(3),replica(3)]).grid(row=5, column=5)
Button(root,font= h, height='2', width='7',bg="blue", fg="white", text="+",command=lambda:[inputvalue('+'),replica('+')]).grid(row=5, column=6)
Button(root,font= h, height='2', width='7',bg="blue", fg="white", text="-",command=lambda:[inputvalue('-'),replica('-')]).grid(row=5, column=7)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="eⁿ",command=lambda:[inputvalue('e^('),replica('math.exp(')]).grid(row=6, column=0)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="x¯¹",command=lambda:[inputvalue('(1÷('),replica('(1/(')]).grid(row=6, column=1)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="log",command=lambda:[inputvalue('log('),replica('math.log(')]).grid(row=6, column=2)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text=".",command=lambda:[inputvalue('.'),replica('.')]).grid(row=6, column=3)
Button(root,font= h, height='2', width='7',bg="black", fg="white", text="0",command=lambda:[inputvalue(0),replica(0)]).grid(row=6, column=4)
Button(root,font= h, height='2', width='7',bg="gray24", fg="white", text="=",command=equal).grid(row=6, column=5)
Button(root,font= h, height='2', width='7',bg="blue", fg="white", text="(",command=lambda:[inputvalue('('),replica('(')]).grid(row=6, column=6)
Button(root,font= h, height='2', width='7',bg="blue", fg="white", text=")",command=lambda:[inputvalue(')'),replica(')')]).grid(row=6, column=7)



root.mainloop()
