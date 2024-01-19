from tkinter import *
import random
from tkinter import messagebox


root = Tk()
root.title('Number Matching Game')
root.geometry("450x550")

global finished, matches

finished = 0

matches = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]

random.shuffle(matches)

my_frame = Frame(root)
my_frame.pack(pady=10)

count = 0
answer_list = []
answer_dict = {}


def reset():
	global matches, finished
	finished = 0
	
	matches = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
	
	random.shuffle(matches)

	my_label.config(text="")

	
	button_list = [btn0,btn01,btn02,btn03,btn04,btn05,btn06,btn07,btn08,btn09,btn010,btn011,btn012,btn013,btn014,btn015]
	for button in button_list:
		button.config(text=" ", bg="SystemButtonFace", state="normal")


def win():
	messagebox.showinfo("Congratulations!" ,"You got it all correct!")
	button_list = [btn0,btn01,btn02,btn03,btn04,btn05,btn06,btn07,btn08,btn09,btn010,btn011,btn012,btn013,btn014,btn015]
	for button in button_list:
		button.config(bg="green")


def button_click(b, number):
	global count, answer_list, answer_dict, finished

	if b["text"] == ' ' and count < 2:
		b["text"] = matches[number]
		answer_list.append(number)
		answer_dict[b] = matches[number]
		count += 1
		
	if len(answer_list) == 2:
		if matches[answer_list[0]] == matches[answer_list[1]]:
			my_label.config(text="MATCH!")
			for key in answer_dict:
				key["state"] = "disabled"
			count = 0
			answer_list = []
			answer_dict = {}
			
			finished += 1
			if finished == 8:
				win()
		else:
			count = 0
			answer_list = []
			messagebox.showinfo("Incorrect!", "Try again")
			for key in answer_dict:
				key["text"] = " "
			answer_dict = {}

btn0 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn0, 0), relief="groove")
btn01 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn01, 1), relief="groove")
btn02 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn02, 2), relief="groove")
btn03 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn03, 3), relief="groove")
btn04 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn04, 4), relief="groove")
btn05 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn05, 5), relief="groove")
btn06 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn06, 6), relief="groove")
btn07 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn07, 7), relief="groove")
btn08 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn08, 8), relief="groove")
btn09 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn09, 9), relief="groove")
btn010 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn010, 10), relief="groove")
btn011 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn011, 11), relief="groove")
btn012 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn012, 12), relief="groove")
btn013 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn013, 13), relief="groove")
btn014 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn014, 14), relief="groove")
btn015 = Button(my_frame, text=' ', font=("Consolas", 20), height=3, width=6, command=lambda: button_click(btn015, 15), relief="groove")


btn0.grid(row=0, column=0)
btn01.grid(row=0, column=1)
btn02.grid(row=0, column=2)
btn03.grid(row=0, column=3)
btn04.grid(row=1, column=0)
btn05.grid(row=1, column=1)
btn06.grid(row=1, column=2)
btn07.grid(row=1, column=3)
btn08.grid(row=2, column=0)
btn09.grid(row=2, column=1)
btn010.grid(row=2, column=2)
btn011.grid(row=2, column=3)
btn012.grid(row=3, column=0)
btn013.grid(row=3, column=1)
btn014.grid(row=3, column=2)
btn015.grid(row=3, column=3)

my_label = Label(root, text="")
my_label.pack(pady=20)

my_menu = Menu(root)
root.config(menu=my_menu)


option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)
option_menu.add_separator()
option_menu.add_command(label="Exit Game", command=root.quit)

root.mainloop()