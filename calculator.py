import tkinter as tk
import math
#-------------------------Functions-------------------------------------

def clr_all():
    entry1.delete(0, 'end')
    return


def bck_spc():
    entry1.delete()
    return


def click(n):
    entry1.insert('end', n)
    return


def equals():
    e = eval(str(entry1.get()))
    entry1.delete(0, 'end')
    entry1.insert('end', str(e))




window = tk.Tk()
window.title('My Calculator')

entry1 = tk.Entry(bd=8)
entry1.grid(column=0, row=0)





button7 = tk.Button( font=43, text=7, padx=16, pady=16,fg='white', bg='blue', bd=4, command=lambda: click('7'))
button7.grid(column=1, row=0)

button8 = tk.Button(font=43, text=8, padx=16, pady=16, fg='white', bg='blue', bd=4, command=lambda: click('8'))
button8.grid(column=2, row=0)

button9 = tk.Button(font=43, text=9, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('9'))
button9.grid(column=3, row=0)


button4 = tk.Button(font=43, text=4, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('4'))
button4.grid(column=1, row=1)

button5 = tk.Button(font=43, text=5, padx=16, pady=16, fg='white', bg='blue',bd=4,command=lambda: click('5') )
button5.grid(column=2, row=1)

button6 = tk.Button(font=43, text=6, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('6'))
button6.grid(column=3, row=1)



button1 = tk.Button(font=43, text=1, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('1') )
button1.grid(column=1, row=2)

button2 = tk.Button(font=43, text=2, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('2'))
button2.grid(column=2, row=2)

button3 = tk.Button(font=43, text=3, padx=16, pady=16, fg='white', bg='blue',bd=4, command=lambda: click('3'))
button3.grid(column=3, row=2)






btn_pls = tk.Button(font=43, text='+', padx=16, pady=16, fg='black', bg='red',bd=4, width= 8, command=lambda: click('+'))
btn_pls.grid(column=0, row=1)

btn_subtract = tk.Button(font=43, text='-', padx=16, pady=16, fg='black', bg='red',bd=4, width=8, command=lambda: click('-'))
btn_subtract.grid(column=0, row=2)

btn_times = tk.Button(font=43, text='X', padx=16, pady=16, fg='black', bg='red',bd=4, width=8, command=lambda: click('*'))
btn_times.grid(column=0, row=3)

btn_dvd = tk.Button(font=43, text='/', padx=16, pady=16, fg='black', bg='red',bd=4, width=8, command=lambda: click('/'))
btn_dvd.grid(column=0, row=4)




zer0 = tk.Button(font=50, text='0', padx=16, pady=16, fg='white', bg='blue',bd=4, width=1,command=lambda: click('0'))
zer0.grid(column=1, row=3)

btn_pwr = tk.Button(font=43, text='^', padx=14, pady=16, fg='white', bg='blue',bd=4,
                    command=lambda:click('**') )
btn_pwr.grid(column=2, row=3)

sqroot = tk.Button(font=43, text='²√', padx=14, pady=16, fg='white', bg='blue', bd=4,
                   command=lambda:click('math.sqrt('))
sqroot.grid(column=3, row=3)



sine = tk.Button(font=40, text='sin', padx=10, pady=10, fg='white', bg='blue',bd=4,
                 command=lambda:click('math.sin('))
sine.grid(column=1, row=4)

cosine = tk.Button(font=40, text='cos', padx=10, pady=10, fg='white', bg='blue',bd=4,
                   command=lambda:click('math.cos('))
cosine.grid(column=2, row=4)

tan = tk.Button(font=40, text='tan', padx=10, pady=10, fg='white', bg='blue',bd=4,
                command=lambda:click('math.tan('))
tan.grid(column=3, row=4)


brckt1 = tk.Button(font=40, text='(', padx=16, pady=9, fg='white', bg='blue',bd=4, command=lambda: click('('))
brckt1.grid(column=1, row=5)

brckt2 = tk.Button(font=40, text=')', padx=16, pady=9, fg='white', bg='blue',bd=4, command=lambda: click(')'))
brckt2.grid(column=2, row=5)

dot = tk.Button(font=40, text='.', padx=16, pady=9, fg='white', bg='blue',bd=4,
                command=lambda: click('.'))
dot.grid(column=3, row=5)

pi = tk.Button(font=40, text='π', padx=16, pady=9, fg='white', bg='blue',bd=4,width=8, command=lambda: click('math.pi'))
pi.grid(column=0, row=5)





eqls = tk.Button(font=43, text='=', padx=16, pady=10, fg='white', bg='blue',bd=4, width=8, command=equals)
eqls.grid(column=0, row=6)

log = tk.Button(font=43, text='log', padx=10, pady=10, fg='white', bg='blue',bd=4,
                command=lambda: click('math.log('))
log.grid(column=1, row=6)

bck_spce = tk.Button(font=43, text='C', padx=16, pady=10, fg='white', bg='blue',bd=4, command=bck_spc)
bck_spce.grid(column=2, row=6)

delete = tk.Button(font=40, text='CE', padx=10, pady=10, fg='white', bg='blue',bd=4, command=clr_all)
delete.grid(column=3, row=6)




window.mainloop()