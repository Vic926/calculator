import tkinter as tk
import math
#-------------------------Functions-------------------------------------

def clr_all():
    entry1.delete(0, 'end')
    return


def bck_spc():
    entry1.delete(len(entry1.get()) - 1)


def click(n):
    if n == '**':
        entry1.insert('end', '^')
    elif n == 'math.sqrt(':
        entry1.insert('end', '²√')
    elif n == 'math.cos(':
        entry1.insert('end', 'cos')
    elif n == 'math.sin(':
        entry1.insert('end', 'sin')
    elif n == 'math.tan(':
        entry1.insert('end', 'tan')
    elif n == 'math.pi':
        entry1.insert('end', 'π')
    elif n == 'math.log(':
        entry1.insert('end', 'log')
    elif n == 'math.factorial(':
        entry1.insert('end', '!')
    else:
        entry1.insert('end', n)
    return


def equals():
    e1 = entry1.get()
    if '^' in e1:
        e1 = e1.replace('^', '**')
    elif '²√' in e1:
        e1 = e1.replace('²√', 'math.sqrt(')
        e1 = str(e1 + ')')
    elif 'sin' in e1:
        e1 = e1.replace('sin', 'math.sin(')
        e1 = str(e1 + ')')
    elif 'cos' in e1:
        e1 = e1.replace('cos', 'math.cos(')
        e1 = str(e1 + ')')
    elif 'tan' in e1:
        e1 = e1.replace('tan', 'math.tan(')
        e1 = str(e1 + ')')
    elif 'log' in e1:
        e1  = e1.replace('log', 'math.log(')
        e1 = str(e1 + ')')
    elif 'π' in e1:
        e1 = e1.replace('π', 'math.pi')
    elif '!' in e1:
        e1 = e1.replace('!', 'math.factorial(')
        e1 = str(e1 + ')')
    e = eval(str(e1))


    entry1.delete(0, 'end')
    entry1.insert('end', str(round(e, 10)))




window = tk.Tk()
window.title('My Calculator')


#---------------------------Frames-----------------------------

frame1 = tk.Frame()
frame1.pack(side='top')
frame2 = tk.Frame()
frame2.pack(side='top')
frame3 = tk.Frame()
frame3.pack(side='top')
frame4 = tk.Frame()
frame4.pack(side='top')
frame5 = tk.Frame()
frame5.pack(side='top')
frame6 = tk.Frame()
frame6.pack(side='top')
frame7 = tk.Frame()
frame7.pack(side='top')
frame8 = tk.Frame()
frame8.pack(side='top')

#-------------------entry-field------------------------------------
entry1 = tk.Entry(frame1, bd=8, width=34)
entry1.pack(side='left')

#-------------------------Buttons--------------------------------
button7 = tk.Button(frame2, font=43, text=7, padx=16, pady=16,fg='white', bg='blue', bd=4, command=lambda: click('7'))
button7.pack(side='left')

button8 = tk.Button(frame2, font=43, text=8, padx=16, pady=16, fg='white', bg='blue', bd=4, command=lambda: click('8'))
button8.pack(side='left')

button9 = tk.Button(frame2, font=43, text=9, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('9'))
button9.pack(side='left')


button4 = tk.Button(frame3, font=43, text=4, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('4'))
button4.pack(side='left')

button5 = tk.Button(frame3, font=43, text=5, padx=16, pady=16, fg='white', bg='blue',bd=4,command=lambda: click('5') )
button5.pack(side='left')

button6 = tk.Button(frame3, font=43, text=6, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('6'))
button6.pack(side='left')



button1 = tk.Button(frame4, font=43, text=1, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('1') )
button1.pack(side='left')

button2 = tk.Button(frame4, font=43, text=2, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('2'))
button2.pack(side='left')

button3 = tk.Button(frame4, font=43, text=3, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('3'))
button3.pack(side='left')



btn_pls = tk.Button(frame2, font=43, text='+', padx=16, pady=16, fg='black', bg='red',bd=4, width= 8, command=lambda: click('+'))
btn_pls.pack(side='left')

btn_subtract = tk.Button(frame3, font=43, text='-', padx=16, pady=16, fg='black', bg='red',bd=4, width=8, command=lambda: click('-'))
btn_subtract.pack(side='left')

btn_times = tk.Button(frame4, font=43, text='X', padx=16, pady=16, fg='black', bg='red',bd=4, width=8, command=lambda: click('*'))
btn_times.pack(side='left')


zer0 = tk.Button(frame5, font=50, text='0', padx=16, pady=16, fg='white', bg='blue',bd=4, width=1,command=lambda: click('0'))
zer0.pack(side='left')

btn_pwr = tk.Button(frame5, font=43, text='^', padx=14, pady=16, fg='white', bg='blue',bd=4,
                    command=lambda:click('**'))
btn_pwr.pack(side='left')

sqroot = tk.Button(frame5, font=43, text='²√', padx=14, pady=16, fg='white', bg='blue', bd=4,
                   command=lambda:click('math.sqrt('))
sqroot.pack(side='left')

btn_dvd = tk.Button(frame5, font=43, text='/', padx=16, pady=16, fg='black', bg='red',bd=4, width=8, command=lambda: click('/'))
btn_dvd.pack(side='left')


brckt1 = tk.Button(frame6, font=40, text='(', padx=18, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('('))
brckt1.pack(side='left')

brckt2 = tk.Button(frame6, font=40, text=')', padx=18, pady=16, fg='white', bg='blue', bd=4, command=lambda: click(')'))
brckt2.pack(side='left')

dot = tk.Button(frame6, font=40, text='.', padx=18, pady=16, fg='white', bg='blue', bd=4,
                command=lambda: click('.'))
dot.pack(side='left')

pi = tk.Button(frame6, font=40, text='π', padx=16, pady=16, fg='white', bg='blue',bd=4,width=8, command=lambda: click('math.pi'))
pi.pack(side='left')


sine = tk.Button(frame7, font=40, text='sin', padx=10, pady=10, fg='white', bg='purple',bd=4,
                 command=lambda:click('math.sin('))
sine.pack(side='left')

cosine = tk.Button(frame7, font=40, text='cos', padx=10, pady=10, fg='white', bg='purple',bd=4,
                   command=lambda:click('math.cos('))
cosine.pack(side='left')

tan = tk.Button(frame7, font=40, text='tan', padx=10, pady=10, fg='white', bg='purple',bd=4,
                command=lambda:click('math.tan('))
tan.pack(side='left')

log = tk.Button(frame7, font=43, text='log', padx=10, pady=10, fg='white', bg='blue', bd=4,
                command=lambda: click('math.log('))
log.pack(side='left')

factorial = tk.Button(frame7, font=43, text='!', padx=19, pady=10, fg='white', bg='blue', bd=4,
                     command=lambda: click('math.factorial('))
factorial.pack(side='left')

bck_spce = tk.Button(frame8, font=43, text='C', padx=16, pady=16, fg='white', bg='blue',bd=4, command=bck_spc)
bck_spce.pack(side='left')

delete = tk.Button(frame8, font=40, text='CE', padx=11, pady=16, fg='white', bg='blue',bd=4, command=clr_all)
delete.pack(side='left')

eqls = tk.Button(frame8, font=43, text='=', padx=24, pady=16, fg='white', bg='black',bd=4, width=11,command=equals)
eqls.pack(side='left')


window.mainloop()