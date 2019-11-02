import tkinter as tk  
from functools import partial  
   
   
def call_result(label_result, n1, n2, n3, n4):  
    num1 = (n1.get())  
    num2 = (n2.get())
    num3 = (n3.get())  
    num4 = (n4.get())
    cat1 = (int(num1)*.7)+(int(num2)*.3)
    cat2 = (int(num3)*.7)+(int(num4)*.3)  
    result = (cat1+cat2)/2
    label_result.config(text="Result = %d/50" % result)  

    return  
   
root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()
  
labelNum1 = tk.Label(root, text="CAT 1").grid(row=1, column=0)  
  
labelNum2 = tk.Label(root, text="Internal 1").grid(row=2, column=0)

labelNum3 = tk.Label(root, text="CAT 2").grid(row=3, column=0)  
  
labelNum4 = tk.Label(root, text="Internal 2").grid(row=4, column=0)

  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  

entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)  

entryNum4 = tk.Entry(root, textvariable=number4).grid(row=4, column=2)  
  
call_result = partial(call_result, labelResult, number1, number2, number3, number4)  
  
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=5, column=2)  
  
root.mainloop()
