from tkinter import *
from tkinter import ttk
import data

def set_textvariable():
	LINUX_TERMS=['FILE COMMANDS','PROCESS MGMNT','FILE PERMISSIONS','SSH','SEARCHING','SYS INFO','COMPRESSION','NETWORK']
	PYTHON_TERMS=['FUNCTIONS','LIST','TUPLE','DICTIONARY','SET','STRING','EXCEPTIONS','KEYWORDS']
	BUTTONS_TEXT=[text1,text2,text3,text4,text5,text6,text7,text8]
	if filename.get() == 'linux':
		for v in range(8):
			mark=LINUX_TERMS[v]
			BUTTONS_TEXT[v].set(mark)
	elif filename.get() == 'python':
		for v in range(8):
			mark=PYTHON_TERMS[v]
			BUTTONS_TEXT[v].set(mark)
	else:
		for v in range(8):
			BUTTONS_TEXT[v].set('NONE')

def get_info(key):
	text['state']='normal'
	text.delete('1.0','end')
	response=data.get_data(filename.get(),key)
	i=1
	for k,v in response.items():
		idx=f'{i}.0'
		idx2=f'{i+1}.0'
		text.insert(idx,f'{k}      ->{v}')
		text.insert(idx2,'\n')
		i+=1

	text['state']='disabled'	

def get_info_python(*args):
	filename.set('python')
	set_textvariable()

def get_info_linux(*args):
	filename.set('linux')
	set_textvariable()


root=Tk()
root.title('mySearch.local')

mainframe=ttk.Frame(root,padding='10 10 10 10')
mainframe.grid(column=0,row=0)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

frame1=ttk.Frame(mainframe)
frame1.grid(column=0,row=1,sticky='n')

filename=StringVar()
text1,text2,text3,text4,text5,text6,text7,text8=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()

btn1=ttk.Button(frame1,text='PYTHON',width=18,command=get_info_python)
btn1.grid(row=1,column=0)
btn2=ttk.Button(frame1,text='LINUX',width=18,command=get_info_linux)
btn2.grid(row=2,column=0)

frame2=ttk.Frame(mainframe,width=60,height=30)
frame2.grid(row=1,column=1,sticky='n')

ttk.Button(frame2,textvariable=text1,width=18,command=lambda *args: get_info(1)).grid(column=0,row=1)
ttk.Button(frame2,textvariable=text2,width=18,command=lambda *args: get_info(2)).grid(column=0,row=2)
ttk.Button(frame2,textvariable=text3,width=18,command=lambda *args: get_info(3)).grid(column=0,row=3)
ttk.Button(frame2,textvariable=text4,width=18,command=lambda *args: get_info(4)).grid(column=0,row=4)
ttk.Button(frame2,textvariable=text5,width=18,command=lambda *args: get_info(5)).grid(column=0,row=5)
ttk.Button(frame2,textvariable=text6,width=18,command=lambda *args: get_info(6)).grid(column=0,row=6)
ttk.Button(frame2,textvariable=text7,width=18,command=lambda *args: get_info(7)).grid(column=0,row=7)
ttk.Button(frame2,textvariable=text8,width=18,command=lambda *args: get_info(8)).grid(column=0,row=8)


frame3=ttk.Frame(mainframe,width=60,height=30)
frame3.grid(row=1,column=2)

text=Text(frame3,height=25,width=55,wrap='word',background='black',foreground='yellow')
text.grid(row=1,column=0)
ys=ttk.Scrollbar(frame3,orient='vertical',command=text.yview)
text['yscrollcommand']=ys.set
ys.grid(row=1,column=1,sticky='ns')
text['state']='disabled'

root.mainloop()



