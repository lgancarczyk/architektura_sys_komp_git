from tkinter import *

root = Tk()
root.resizable(width=0, height=0)
root.title("8086 simulator")


large_font = ('Verdana',15)
small_font = ('Verdana',10)

AX_output_desc = Label(root, text="AX", font=small_font)
AX_output_desc.grid(row=1,column=1, padx=(20,0), pady=(20, 0))
AX_output = Entry(root, font=large_font, width=6, justify='center')
AX_output.grid(row=1, column=2, padx=(0,0), pady=(20, 0))

BX_output_desc = Label(root, text="BX", font=small_font)
BX_output_desc.grid(row=3,column=1, padx=(20,0), pady=(20, 0))
BX_output = Entry(root, font=large_font, width=6, justify='center')
BX_output.grid(row=3, column=2, padx=(0,0), pady=(20, 0))

CX_output_desc = Label(root, text="CX", font=small_font)
CX_output_desc.grid(row=5,column=1, padx=(20,0), pady=(20, 0))
CX_output = Entry(root, font=large_font, width=6, justify='center')
CX_output.grid(row=5, column=2, padx=(0,0), pady=(20, 0))

DX_output_desc = Label(root, text="DX", font=small_font)
DX_output_desc.grid(row=7,column=1, padx=(20,0), pady=(20, 0))
DX_output = Entry(root, font=large_font, width=6, justify='center')
DX_output.grid(row=7, column=2, padx=(0,0), pady=(20, 0))

#############################

AH_entry_desc = Label(root, text="AH")
AH_entry_desc.grid(row=1,column=4, padx=(20,0), pady=(20, 0))
AH_entry = Entry(root, font=large_font, width=3, justify='center')
AH_entry.grid(row=1, column=5, padx=(0,0), pady=(20, 0))

BH_entry_desc = Label(root, text="BH")
BH_entry_desc.grid(row=3,column=4, padx=(20,0), pady=(20, 0))
BH_entry = Entry(root, font=large_font, width=3, justify='center')
BH_entry.grid(row=3, column=5, padx=(0,0), pady=(20, 0))

CH_entry_desc = Label(root, text="CH")
CH_entry_desc.grid(row=5,column=4, padx=(20,0), pady=(20, 0))
CH_entry = Entry(root, font=large_font, width=3, justify='center')
CH_entry.grid(row=5, column=5, padx=(0,0), pady=(20, 0))

DH_entry_desc = Label(root, text="DH")
DH_entry_desc.grid(row=7,column=4, padx=(20,0), pady=(20, 0))
DH_entry = Entry(root, font=large_font, width=3, justify='center')
DH_entry.grid(row=7, column=5, padx=(0,0), pady=(20, 0))

#############################

AL_entry_desc = Label(root, text="AL")
AL_entry_desc.grid(row=1,column=7, padx=(20,0), pady=(20, 0))
AL_entry = Entry(root, font=large_font, width=3, justify='center')
AL_entry.grid(row=1, column=8, padx=(0,20), pady=(20, 0))

BL_entry_desc = Label(root, text="BL")
BL_entry_desc.grid(row=3,column=7, padx=(20,0), pady=(20, 0))
BL_entry = Entry(root, font=large_font, width=3, justify='center')
BL_entry.grid(row=3, column=8, padx=(0,20), pady=(20, 0))

CL_entry_desc = Label(root, text="CL")
CL_entry_desc.grid(row=5,column=7, padx=(20,0), pady=(20, 0))
CL_entry = Entry(root, font=large_font, width=3, justify='center')
CL_entry.grid(row=5, column=8, padx=(0,20), pady=(20, 0))

DL_entry_desc = Label(root, text="DL")
DL_entry_desc.grid(row=7,column=7, padx=(20,0), pady=(20, 0))
DL_entry = Entry(root, font=large_font, width=3, justify='center')
DL_entry.grid(row=7, column=8, padx=(0,20), pady=(20, 0))

###################################

AX_btn_left_desc = Label(root, text="AX")
AX_btn_left_desc.grid(row=10,column=1, padx=(20,0), pady=(40, 0))
AX_btn_left = Radiobutton(root)
AX_btn_left.grid(row=10, column=2, padx=(0,0), pady=(40, 0), sticky="w")

BX_btn_desc = Label(root, text="BX")
BX_btn_desc.grid(row=12,column=1, padx=(20,0), pady=(3, 0))
BX_btn = Radiobutton(root)
BX_btn.grid(row=12, column=2, padx=(0,0), pady=(3, 0), sticky="w")




root.mainloop()
