import tkinter as tk

#Gets data from the entrybox, inserts it into the main textbox and deletes the contents of the entrybox. It is also where commands are stored
def getext(event = None):
	etext = entry.get()
	text.insert(tk.END, etext + "\n")
	if etext == "stats":
		 text.insert(tk.END, "HP: " + str(HP) + "\n" + "ATK: " + str(ATK) + "\n" + "DEF: " + str(DEF) + "\n")
	elif etext == "clear":
		text.delete(1.0, tk.END)
	entry.delete(0, tk.END)
	
#Sets the Health, Attack and Defence stats
HP = 100
ATK = 10
DEF = 10

#Makes the window, sets it to 700x500 and sets the title to "GAME"
root = tk.Tk()
root.geometry("728x500")
root.title("GAME")
root.resizable(False, False)

#Binds the Enter key to to the "getext" function
root.bind("<Return>", getext)

#Sets bgimg to "paperbg.png", makes a label for the image and places the image in the center of the window
bgimg = tk.PhotoImage(file = "paperbg.png")
bg = tk.Label(root, image = bgimg)
bg.place(x = 0, y = 0)

#Sets the logo to "text.png", sets the border to be raised with a width of 5 and places it at the top of the window
IMAGE = tk.PhotoImage( file = "text.png")
image = tk.Label(borderwidth = 5, relief=tk.RAISED, image = IMAGE)
image.pack(side = tk.TOP, padx = 5, pady = 5)

#Makes the entry bar and places it at the bottom of the window
entry = tk.Entry()
entry.pack(side = tk.BOTTOM, fill = tk.BOTH, padx = 5, pady = 5)

#Makes the main textbox and places it at the top and makes it fill all remaining space in the window
text = tk.Text()
text.pack(side = tk.RIGHT, expand = True, fill = tk.BOTH, padx = 5, pady = 5)

#Initializes the main window
entry.focus()
root.mainloop()
