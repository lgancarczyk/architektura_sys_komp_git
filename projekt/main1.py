from tkinter import *
import random


root=Tk()
root.title("8086 simulator")
width=600
height=500
root.geometry(f"{width}x{height}")

large_font = ('Verdana',15)
middle_font = ('Verdana',11)
small_font = ('Verdana',10)

options_list = [ "MOV",
                 "XCHG"]

var_drop_options = IntVar()
var_drop_options.set(options_list[0])

heksadecymalne= {'0000':'0',
                 '0001':'1',
                 '0010':'2',
                 '0011':'3',
                 '0100':'4',
                 '0101':'5',
                 '0110':'6',
                 '0111':'7',
                 '1000':'8',
                 '1001':'9',
                 '1010':'A',
                 '1011':'B',
                 '1100':'C',
                 '1101':'D',
                 '1110':'E',
                 '1111':'F',
                 }   

class Simulator:

    # var_left= IntVar()
    # var_right= IntVar()

    # var_drop_options = IntVar()
    # var_drop_options.set(options_list[0])

    

    def __init__(self, master):

        self.input_list= {'AH_entry':"",
                        'BH_entry':"", 
                        'CH_entry':"", 
                        'DH_entry':"",
                        'AL_entry':"",
                        'BL_entry':"",
                        'CL_entry':"",
                        'DL_entry':"",
                        }
        
        self.var_left= IntVar()
        self.var_right= IntVar()

        ######################################################### output frame

        self.output_frame = LabelFrame(master, text="output_frame", pady=10)
        self.output_frame.pack(side=LEFT, anchor=N, padx=(10,0))

        self.AX_output_desc = Label(self.output_frame, text="AX", font=middle_font)
        self.AX_output_desc.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.AX_output = Entry(self.output_frame, font=large_font, width=6, justify='center', state="disabled")
        self.AX_output.grid(row=0, column=1, padx=(0,20), pady=(10, 0))

        self.BX_output_desc = Label(self.output_frame, text="BX", font=middle_font)
        self.BX_output_desc.grid(row=1,column=0, padx=(0,0), pady=(10, 0))
        self.BX_output = Entry(self.output_frame, font=large_font, width=6, justify='center', state="disabled")
        self.BX_output.grid(row=1, column=1, padx=(0,20), pady=(10, 0))

        self.CX_output_desc = Label(self.output_frame, text="CX", font=middle_font)
        self.CX_output_desc.grid(row=2,column=0, padx=(0,0), pady=(10, 0))
        self.CX_output = Entry(self.output_frame, font=large_font, width=6, justify='center', state="disabled")
        self.CX_output.grid(row=2, column=1, padx=(0,20), pady=(10, 0))

        self.CX_output_desc = Label(self.output_frame, text="DX", font=middle_font)
        self.CX_output_desc.grid(row=3,column=0, padx=(0,0), pady=(10, 0))
        self.CX_output = Entry(self.output_frame, font=large_font, width=6, justify='center', state="disabled")
        self.CX_output.grid(row=3, column=1, padx=(0,20), pady=(10, 0))

        ######################################################### input frame

        self.entry_frame = LabelFrame(master, text="entry_frame", pady=10)
        self.entry_frame.pack(side=RIGHT,anchor=N, padx=(0, 10))

        ########## left side
        self.AH_entry_desc = Label(self.entry_frame, text="AH")
        self.AH_entry_desc.grid(row=0, column=0, padx=(0,0), pady=(10, 0))
        self.input_list['AH_entry'] = Entry(self.entry_frame, font=large_font, width=3, justify='center')
        self.input_list['AH_entry'].grid(row=0, column=1, padx=(0,40), pady=(10, 0))

        self.BH_entry_desc = Label(self.entry_frame, text="BH")
        self.BH_entry_desc.grid(row=1, column=0, padx=(0,0), pady=(10, 0))
        self.input_list['BH_entry'] = Entry(self.entry_frame, font=large_font, width=3, justify='center')
        self.input_list['BH_entry'].grid(row=1, column=1, padx=(0,40), pady=(10, 0))

        self.CH_entry_desc = Label(self.entry_frame, text="CH")
        self.CH_entry_desc.grid(row=2, column=0, padx=(0,0), pady=(10, 0))
        self.input_list['CH_entry'] = Entry(self.entry_frame, font=large_font, width=3, justify='center')
        self.input_list['CH_entry'].grid(row=2, column=1, padx=(0,40), pady=(10, 0))

        self.DH_entry_desc = Label(self.entry_frame, text="DH")
        self.DH_entry_desc.grid(row=3, column=0, padx=(0,0), pady=(10, 0))
        self.input_list['DH_entry'] = Entry(self.entry_frame, font=large_font, width=3, justify='center')
        self.input_list['DH_entry'].grid(row=3, column=1, padx=(0,40), pady=(10, 0))

        ########## right side
        self.AL_entry_desc = Label(self.entry_frame, text="AL")
        self.AL_entry_desc.grid(row=0, column=2, padx=(0,0), pady=(10, 0))
        self.input_list['AL_entry'] = Entry(self.entry_frame, font=large_font, width=3, justify='center')
        self.input_list['AL_entry'].grid(row=0, column=3, padx=(0,20), pady=(10, 0))

        self.BL_entry_desc = Label(self.entry_frame, text="BL")
        self.BL_entry_desc.grid(row=1, column=2, padx=(0,0), pady=(10, 0))
        self.input_list['BL_entry'] = Entry(self.entry_frame, font=large_font, width=3, justify='center')
        self.input_list['BL_entry'].grid(row=1, column=3, padx=(0,20), pady=(10, 0))

        self.CL_entry_desc = Label(self.entry_frame, text="CL")
        self.CL_entry_desc.grid(row=2, column=2, padx=(0,0), pady=(10, 0))
        self.input_list['CL_entry'] = Entry(self.entry_frame, font=large_font, width=3, justify='center')
        self.input_list['CL_entry'].grid(row=2, column=3, padx=(0,20), pady=(10, 0))

        self.DL_entry_desc = Label(self.entry_frame, text="DL")
        self.DL_entry_desc.grid(row=3, column=2, padx=(0,0), pady=(10, 0))
        self.input_list['DL_entry'] = Entry(self.entry_frame, font=large_font, width=3, justify='center')
        self.input_list['DL_entry'].grid(row=3, column=3, padx=(0,20), pady=(10, 0))

        ######################################################### radio buttons frame

        self.radio_buttons_frame = LabelFrame(master, text="radio_buttons", pady=10)
        self.radio_buttons_frame.pack(side=LEFT,anchor=S, padx=(0, 10))

        ########## left side
        self.AX_btn_left_desc = Label(self.radio_buttons_frame, text="AX", font=middle_font)
        self.AX_btn_left_desc.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.AX_btn_left = Radiobutton(self.radio_buttons_frame, variable=self.var_left, value=0)
        self.AX_btn_left.grid(row=0, column=1, padx=(0,30), pady=(10, 0))

        self.BX_btn_left_desc = Label(self.radio_buttons_frame, text="BX", font=middle_font)
        self.BX_btn_left_desc.grid(row=1,column=0, padx=(0,0), pady=(10, 0))
        self.BX_btn_left = Radiobutton(self.radio_buttons_frame, variable=self.var_left, value=1)
        self.BX_btn_left.grid(row=1, column=1, padx=(0,30), pady=(10, 0))

        self.CX_btn_left_desc = Label(self.radio_buttons_frame, text="CX", font=middle_font)
        self.CX_btn_left_desc.grid(row=2,column=0, padx=(0,0), pady=(10, 0))
        self.CX_btn_left = Radiobutton(self.radio_buttons_frame, variable=self.var_left, value=2)
        self.CX_btn_left.grid(row=2, column=1, padx=(0,30), pady=(10, 0))

        self.DX_btn_left_desc = Label(self.radio_buttons_frame, text="DX", font=middle_font)
        self.DX_btn_left_desc.grid(row=3,column=0, padx=(0,0), pady=(10, 0))
        self.DX_btn_left = Radiobutton(self.radio_buttons_frame, variable=self.var_left, value=3)
        self.DX_btn_left.grid(row=3, column=1, padx=(0,30), pady=(10, 0))

        ########## right side
        self.AX_btn_right_desc = Label(self.radio_buttons_frame, text="AX", font=middle_font)
        self.AX_btn_right_desc.grid(row=0,column=2, padx=(0,0), pady=(10, 0))
        self.AX_btn_right = Radiobutton(self.radio_buttons_frame, variable=self.var_right, value=0)
        self.AX_btn_right.grid(row=0, column=3, padx=(0,20), pady=(10, 0))

        self.BX_btn_right_desc = Label(self.radio_buttons_frame, text="BX", font=middle_font)
        self.BX_btn_right_desc.grid(row=1,column=2, padx=(0,0), pady=(10, 0))
        self.BX_btn_right = Radiobutton(self.radio_buttons_frame, variable=self.var_right, value=1)
        self.BX_btn_right.grid(row=1, column=3, padx=(0,20), pady=(10, 0))

        self.CX_btn_right_desc = Label(self.radio_buttons_frame, text="CX", font=middle_font)
        self.CX_btn_right_desc.grid(row=2,column=2, padx=(0,0), pady=(10, 0))
        self.CX_btn_right = Radiobutton(self.radio_buttons_frame, variable=self.var_right, value=2)
        self.CX_btn_right.grid(row=2, column=3, padx=(0,20), pady=(10, 0))

        self.DX_btn_right_desc = Label(self.radio_buttons_frame, text="DX", font=middle_font)
        self.DX_btn_right_desc.grid(row=3,column=2, padx=(0,0), pady=(10, 0))
        self.DX_btn_right = Radiobutton(self.radio_buttons_frame, variable=self.var_right, value=3)
        self.DX_btn_right.grid(row=3, column=3, padx=(0,20), pady=(10, 0))
        
        ######################################################### buttons frame

        self.buttons_frame = LabelFrame(master, text="buttons", pady=10)
        self.buttons_frame.pack(side=RIGHT,anchor=S, padx=(0, 10))

        self.drop_options = OptionMenu(self.buttons_frame, var_drop_options , *options_list)  # gwiazdka jest potrzebna, inaczej cała lista bedzie wyświetlana jako jedna opcja (1 linijka) 
        self.drop_options.grid(row=0, column=0,columnspan=1, sticky="w", pady=(0, 0))

        self.create_random_btn = Button(self.buttons_frame, text='Random', width=10)
        self.create_random_btn.grid(row=0, column=1, pady=(0, 0))

        self.start_btn = Button(self.buttons_frame, text='Start', width=10)
        self.start_btn.grid(row=1, column=0, pady=(0, 0))



s = Simulator(root)

root.mainloop()