from tkinter import *


first_num = second_num = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clr():
    result_label.config(text='')
    
def get_opr(op):
    global first_num, operator
    first_num = int(result_label['text'])
    operator = op
    result_label.config(text='')
    
def get_rslt():
    global second_num
    second_num = int(result_label['text'])

    if operator == '+':
        result_label.config(text= str(first_num + second_num))
    elif operator == '-':
        result_label.config(text= str(first_num - second_num))
    elif operator == '*':
        result_label.config(text= str(first_num * second_num))
    else:
        if second_num == 0:
            result_label.config(text="Not defined")
        else:
            result_label.config(text=  round(first_num / second_num, 2))

root = Tk()

root.title("Calculator")
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')

result_label = Label(root, text = '', background='black', fg= 'white')
result_label.grid(row=0, column=0, columnspan=5, pady=(50,25), sticky= 'w')
result_label.config(font=('verdana', 30, 'bold'))

btn7 = Button(root, text='7', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_digit(7))
btn7.grid(row=1, column=0)
btn7.config(font=('verdana',14))

btn8 = Button(root, text='8', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_digit(8))
btn8.grid(row=1, column=1)
btn8.config(font=('verdana',14))

btn9 = Button(root, text='9', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_digit(9))
btn9.grid(row=1, column=2)
btn9.config(font=('verdana',14))

btn_add = Button(root, text='+', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_opr('+'))
btn_add.grid(row=1, column=3)
btn_add.config(font=('verdana',14))

btn4 = Button(root, text='4', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_digit(4))
btn4.grid(row=2, column=0)
btn4.config(font=('verdana',14))

btn5 = Button(root, text='5', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_digit(5))
btn5.grid(row=2, column=1)
btn5.config(font=('verdana',14))

btn6 = Button(root, text='6', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_digit(6))
btn6.grid(row=2, column=2)
btn6.config(font=('verdana',14))

btn_sub = Button(root, text='-', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_opr('-'))
btn_sub.grid(row=2, column=3)
btn_sub.config(font=('verdana',14))

btn1 = Button(root, text='1', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_digit(1))
btn1.grid(row=3, column=0)
btn1.config(font=('verdana',14))

btn2 = Button(root, text='2', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_digit(2))
btn2.grid(row=3, column=1)
btn2.config(font=('verdana',14))

btn3 = Button(root, text='3', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_digit(3))
btn3.grid(row=3, column=2)
btn3.config(font=('verdana',14))

btn_mul = Button(root, text='*', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_opr('*'))
btn_mul.grid(row=3, column=3)
btn_mul.config(font=('verdana',14))

btn_clr = Button(root, text='C', background='#00a65a', fg='white', width=5, height= 2, command= lambda: clr())
btn_clr.grid(row=4, column=0)
btn_clr.config(font=('verdana',14))

btn0 = Button(root, text='0', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_digit(0))
btn0.grid(row=4, column=1)
btn0.config(font=('verdana',14))

btn_eql = Button(root, text='=', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_rslt())
btn_eql.grid(row=4, column=2)
btn_eql.config(font=('verdana',14))

btn_div = Button(root, text='/', background='#00a65a', fg='white', width=5, height= 2, command= lambda: get_opr('/'))
btn_div.grid(row=4, column=3)
btn_div.config(font=('verdana',14))

root.mainloop()