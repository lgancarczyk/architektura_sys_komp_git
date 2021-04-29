import tkinter as tk



large_font = ('Verdana',15)
middle_font = ('Verdana',11)
small_font = ('Verdana',10)


class Application(tk.Frame):

    def track_mode_list(self, event):
        
        print(event)
        pass





    def __init__(self, master=None):
        super().__init__(master)
        
        self.input_list= ['AX_input',
                        'BX_input',
                        'CX_input',
                        'DX_input',
                        'SI_input',
                        'DI_input',
                        'BP_input',
                        'SP_input',
                        'DISP_input'
                        ]
        self.var_left= tk.IntVar()
        self.var_right= tk.IntVar()

        self.var_right_vertical_frame_rejestr= tk.IntVar()

        self.var_right_vertical_frame_indeksowy= tk.IntVar()
        self.var_right_vertical_frame_bazowy= tk.IntVar()
        self.var_right_vertical_frame_indeksowo_bazowy= tk.IntVar()

        self.mode_list = [ "Indeksowy",
                    "Bazowy",
                    "Indeksowo-Bazowy"]
                    
        self.var_mode_options = tk.StringVar()
        self.var_mode_options.set(self.mode_list[0])

        self.memory_mode_list = ["Z pamieci do rejestru",
                            "Z rejestru do pamieci"]

        self.var_memory_mode_options = tk.StringVar()
        self.var_memory_mode_options.set(self.memory_mode_list[1])


        self.vertical_frame_left = tk.Frame(master)
        self.vertical_frame_left.grid(row = 0, column=0)
        self.vertical_frame_right = tk.Frame(master)
        self.vertical_frame_right.grid(row = 0, column=1)


        ##########################################################
        ##########################################################
        ##########################################################
        ########################################################## left vertical frame

        self.input_frame = tk.LabelFrame(self.vertical_frame_left)
        self.input_frame.grid(row=1, column=0)


        ######################################################### reset_random frame
        self.reset_random_frame = tk.LabelFrame(self.vertical_frame_left)
        self.reset_random_frame.grid(row=0, column=0)

        self.create_random_btn = tk.Button(self.reset_random_frame, text='Random', width=10, command=lambda : print("Random")) #self.create_random()
        self.create_random_btn.grid(row=0, column=0, pady=(0, 0), padx=(0, 20))

        self.reset_btn = tk.Button(self.reset_random_frame, text='Reset', width=10, command=lambda : print("Reset")) #self.create_random()
        self.reset_btn.grid(row=0, column=1, pady=(0, 0), padx=(20, 0))

        ######################################################### input frame

        self.upper_input = tk.Frame(self.input_frame)
        self.upper_input.grid(row=0, column=0)

        self.AX_input_desc = tk.Label(self.upper_input, text="AX", font=middle_font)
        self.AX_input_desc.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.input_list[0] = tk.Entry(self.upper_input, font=large_font, width=6, justify='center')
        self.input_list[0].grid(row=0, column=1, padx=(0,20), pady=(10, 0))

        self.BX_input_desc = tk.Label(self.upper_input, text="BX", font=middle_font)
        self.BX_input_desc.grid(row=1,column=0, padx=(0,0), pady=(10, 0))
        self.input_list[1] = tk.Entry(self.upper_input, font=large_font, width=6, justify='center')
        self.input_list[1].grid(row=1, column=1, padx=(0,20), pady=(10, 0))

        self.CX_input_desc = tk.Label(self.upper_input, text="CX", font=middle_font)
        self.CX_input_desc.grid(row=2,column=0, padx=(0,0), pady=(10, 0))
        self.input_list[2] = tk.Entry(self.upper_input, font=large_font, width=6, justify='center')
        self.input_list[2].grid(row=2, column=1, padx=(0,20), pady=(10, 0))

        self.DX_input_desc = tk.Label(self.upper_input, text="DX", font=middle_font)
        self.DX_input_desc.grid(row=3,column=0, padx=(0,0), pady=(10, 0))
        self.input_list[3] = tk.Entry(self.upper_input, font=large_font, width=6, justify='center')
        self.input_list[3].grid(row=3, column=1, padx=(0,20), pady=(10, 0))

        self.SI_input_desc = tk.Label(self.upper_input, text="SI", font=middle_font)
        self.SI_input_desc.grid(row=0,column=2, padx=(0,0), pady=(10, 0))
        self.input_list[4] = tk.Entry(self.upper_input, font=large_font, width=6, justify='center')
        self.input_list[4].grid(row=0, column=3, padx=(0,20), pady=(10, 0))

        self.DI_input_desc = tk.Label(self.upper_input, text="DI", font=middle_font)
        self.DI_input_desc.grid(row=1,column=2, padx=(0,0), pady=(10, 0))
        self.input_list[5] = tk.Entry(self.upper_input, font=large_font, width=6, justify='center')
        self.input_list[5].grid(row=1, column=3, padx=(0,20), pady=(10, 0))

        self.BP_input_desc = tk.Label(self.upper_input, text="BP", font=middle_font)
        self.BP_input_desc.grid(row=2,column=2, padx=(0,0), pady=(10, 0))
        self.input_list[6] = tk.Entry(self.upper_input, font=large_font, width=6, justify='center')
        self.input_list[6].grid(row=2, column=3, padx=(0,20), pady=(10, 0))

        self.SP_input_desc = tk.Label(self.upper_input, text="SP", font=middle_font)
        self.SP_input_desc.grid(row=3,column=2, padx=(0,0), pady=(10, 0))
        self.input_list[7] = tk.Entry(self.upper_input, font=large_font, width=6, justify='center')
        self.input_list[7].grid(row=3, column=3, padx=(0,20), pady=(10, 0))

        self.DISP_input_desc = tk.Label(self.upper_input, text="DISP", font=middle_font)
        self.DISP_input_desc.grid(row=4,column=2, padx=(0,0), pady=(10, 0))
        self.input_list[8] = tk.Entry(self.upper_input, font=large_font, width=6, justify='center')
        self.input_list[8].grid(row=4, column=3, padx=(0,20), pady=(10, 0))
        

        ######################################################### radiobuttons left vertical frame

        self.radio_buttons_left_vertical_frame = tk.LabelFrame(self.vertical_frame_left)
        self.radio_buttons_left_vertical_frame.grid(row=2, column=0)


        self.AX_btn_left_desc = tk.Label(self.radio_buttons_left_vertical_frame, text="AX", font=middle_font)
        self.AX_btn_left_desc.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.AX_btn_left = tk.Radiobutton(self.radio_buttons_left_vertical_frame, variable=self.var_left, value=0)
        self.AX_btn_left.grid(row=0, column=1, padx=(0,30), pady=(10, 0))

        self.BX_btn_left_desc = tk.Label(self.radio_buttons_left_vertical_frame, text="BX", font=middle_font)
        self.BX_btn_left_desc.grid(row=1,column=0, padx=(0,0), pady=(10, 0))
        self.BX_btn_left = tk.Radiobutton(self.radio_buttons_left_vertical_frame, variable=self.var_left, value=1)
        self.BX_btn_left.grid(row=1, column=1, padx=(0,30), pady=(10, 0))

        self.CX_btn_left_desc = tk.Label(self.radio_buttons_left_vertical_frame, text="CX", font=middle_font)
        self.CX_btn_left_desc.grid(row=2,column=0, padx=(0,0), pady=(10, 0))
        self.CX_btn_left = tk.Radiobutton(self.radio_buttons_left_vertical_frame, variable=self.var_left, value=2)
        self.CX_btn_left.grid(row=2, column=1, padx=(0,30), pady=(10, 0))

        self.DX_btn_left_desc = tk.Label(self.radio_buttons_left_vertical_frame, text="DX", font=middle_font)
        self.DX_btn_left_desc.grid(row=3,column=0, padx=(0,0), pady=(10, 0))
        self.DX_btn_left = tk.Radiobutton(self.radio_buttons_left_vertical_frame, variable=self.var_left, value=3)
        self.DX_btn_left.grid(row=3, column=1, padx=(0,30), pady=(10, 0))

        ########## right side
        self.AX_btn_right_desc = tk.Label(self.radio_buttons_left_vertical_frame, text="AX", font=middle_font)
        self.AX_btn_right_desc.grid(row=0,column=2, padx=(0,0), pady=(10, 0))
        self.AX_btn_right = tk.Radiobutton(self.radio_buttons_left_vertical_frame, variable=self.var_right, value=0)
        self.AX_btn_right.grid(row=0, column=3, padx=(0,20), pady=(10, 0))

        self.BX_btn_right_desc = tk.Label(self.radio_buttons_left_vertical_frame, text="BX", font=middle_font)
        self.BX_btn_right_desc.grid(row=1,column=2, padx=(0,0), pady=(10, 0))
        self.BX_btn_right = tk.Radiobutton(self.radio_buttons_left_vertical_frame, variable=self.var_right, value=1)
        self.BX_btn_right.grid(row=1, column=3, padx=(0,20), pady=(10, 0))

        self.CX_btn_right_desc = tk.Label(self.radio_buttons_left_vertical_frame, text="CX", font=middle_font)
        self.CX_btn_right_desc.grid(row=2,column=2, padx=(0,0), pady=(10, 0))
        self.CX_btn_right = tk.Radiobutton(self.radio_buttons_left_vertical_frame, variable=self.var_right, value=2)
        self.CX_btn_right.grid(row=2, column=3, padx=(0,20), pady=(10, 0))

        self.DX_btn_right_desc = tk.Label(self.radio_buttons_left_vertical_frame, text="DX", font=middle_font)
        self.DX_btn_right_desc.grid(row=3,column=2, padx=(0,0), pady=(10, 0))
        self.DX_btn_right = tk.Radiobutton(self.radio_buttons_left_vertical_frame, variable=self.var_right, value=3)
        self.DX_btn_right.grid(row=3, column=3, padx=(0,20), pady=(10, 0))


        ######################################################### mov_xchg left vertical frame

        self.mov_xchg_left_vertical_frame = tk.LabelFrame(self.vertical_frame_left)
        self.mov_xchg_left_vertical_frame.grid(row=3, column=0)

        self.mov_left_vertical_frame_btn = tk.Button(self.mov_xchg_left_vertical_frame, text='MOV', width=10, command=lambda : print("MOV left")) #self.start()
        self.mov_left_vertical_frame_btn.grid(row=0, column=0, pady=(0, 0), padx=(0, 20))

        self.xchg_left_vertical_frame_btn = tk.Button(self.mov_xchg_left_vertical_frame, text='XCHG', width=10, command=lambda : print("XCHG left")) #self.start()
        self.xchg_left_vertical_frame_btn.grid(row=0, column=1, pady=(0, 0), padx=(20, 0))



        ##########################################################
        ##########################################################
        ##########################################################
        ########################################################## right vertical frame

        self.mode_drop = tk.OptionMenu(self.vertical_frame_right, self.var_mode_options, *(self.mode_list), command = self.track_mode_list)
        self.mode_drop.grid(row=0, column=0)

        self.mode_drop = tk.OptionMenu(self.vertical_frame_right, self.var_memory_mode_options, *self.memory_mode_list)
        self.mode_drop.grid(row=1, column=0)

        ######################################################### radio btns
        #########################################################

        self.right_vertical_frame_radio_all = tk.Frame(self.vertical_frame_right)
        self.right_vertical_frame_radio_all.grid(row=2, column=0)

        ######################################################### radio btns left

        ###### indeksowy

        self.right_vertical_frame_radio_all_left_indeksowy = tk.Frame(self.right_vertical_frame_radio_all)
        self.right_vertical_frame_radio_all_left_indeksowy.grid(row=0, column=0)

        self.SI_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_indeksowy, text="SI", font=middle_font)
        self.SI_btn_desc.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.SI_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_indeksowy, variable=self.var_right_vertical_frame_indeksowy, value=0)
        self.SI_btn.grid(row=0, column=1, padx=(0,30), pady=(10, 0))

        self.DI_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_indeksowy, text="DI", font=middle_font)
        self.DI_btn_desc.grid(row=1,column=0, padx=(0,0), pady=(10, 0))
        self.DI_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_indeksowy, variable=self.var_right_vertical_frame_indeksowy, value=1)
        self.DI_btn.grid(row=1, column=1, padx=(0,30), pady=(10, 0))

        ###### bazowy

        self.right_vertical_frame_radio_all_left_bazowy = tk.Frame(self.right_vertical_frame_radio_all)
        self.right_vertical_frame_radio_all_left_bazowy.grid(row=1, column=0)

        self.BX_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_bazowy, text="BX", font=middle_font)
        self.BX_btn_desc.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.BX_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_bazowy, variable=self.var_right_vertical_frame_bazowy, value=0)
        self.BX_btn.grid(row=0, column=1, padx=(0,30), pady=(10, 0))

        self.BP_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_bazowy, text="BP", font=middle_font)
        self.BP_btn_desc.grid(row=1,column=0, padx=(0,0), pady=(10, 0))
        self.BP_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_bazowy, variable=self.var_right_vertical_frame_bazowy, value=1)
        self.BP_btn.grid(row=1, column=1, padx=(0,30), pady=(10, 0))

        ###### indeksowo bazowy

        self.right_vertical_frame_radio_all_left_indeksowo_bazowy = tk.Frame(self.right_vertical_frame_radio_all)
        self.right_vertical_frame_radio_all_left_indeksowo_bazowy.grid(row=2, column=0)

        self.SI_BX_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_indeksowo_bazowy, text="SI BX", font=middle_font)
        self.SI_BX_btn_desc.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.SI_BX_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_indeksowo_bazowy, variable=self.var_right_vertical_frame_indeksowo_bazowy, value=0)
        self.SI_BX_btn.grid(row=0, column=1, padx=(0,30), pady=(10, 0))

        self.DI_BX_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_indeksowo_bazowy, text="DI BX", font=middle_font)
        self.DI_BX_btn_desc.grid(row=1,column=0, padx=(0,0), pady=(10, 0))
        self.DI_BX_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_indeksowo_bazowy, variable=self.var_right_vertical_frame_indeksowo_bazowy, value=1)
        self.DI_BX_btn.grid(row=1, column=1, padx=(0,30), pady=(10, 0))

        self.SI_BP_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_indeksowo_bazowy, text="SI BP", font=middle_font)
        self.SI_BP_btn_desc.grid(row=2,column=0, padx=(0,0), pady=(10, 0))
        self.SI_BP_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_indeksowo_bazowy, variable=self.var_right_vertical_frame_indeksowo_bazowy, value=2)
        self.SI_BP_btn.grid(row=2, column=1, padx=(0,30), pady=(10, 0))

        self.DI_BP_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_indeksowo_bazowy, text="DI BP", font=middle_font)
        self.DI_BP_btn_desc.grid(row=3,column=0, padx=(0,0), pady=(10, 0))
        self.DI_BP_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_indeksowo_bazowy, variable=self.var_right_vertical_frame_indeksowo_bazowy, value=3)
        self.DI_BP_btn.grid(row=3, column=1, padx=(0,30), pady=(10, 0))



        ######################################################### radio btns right

        self.right_vertical_frame_radio_all_right = tk.Frame(self.right_vertical_frame_radio_all)
        self.right_vertical_frame_radio_all_right.grid(row=0, column=1)

        self.AX_btn_desc_right_vertical = tk.Label(self.right_vertical_frame_radio_all_right, text="AX", font=middle_font)
        self.AX_btn_desc_right_vertical.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.AX_btn_right_vertical = tk.Radiobutton(self.right_vertical_frame_radio_all_right, variable=self.var_right_vertical_frame_rejestr, value=0)
        self.AX_btn_right_vertical.grid(row=0, column=1, padx=(0,30), pady=(10, 0))

        self.BX_btn_desc_right_vertical = tk.Label(self.right_vertical_frame_radio_all_right, text="BX", font=middle_font)
        self.BX_btn_desc_right_vertical.grid(row=1,column=0, padx=(0,0), pady=(10, 0))
        self.BX_btn_right_vertical = tk.Radiobutton(self.right_vertical_frame_radio_all_right, variable=self.var_right_vertical_frame_rejestr, value=1)
        self.BX_btn_right_vertical.grid(row=1, column=1, padx=(0,30), pady=(10, 0))

        self.CX_btn_desc_right_vertical = tk.Label(self.right_vertical_frame_radio_all_right, text="CX", font=middle_font)
        self.CX_btn_desc_right_vertical.grid(row=2,column=0, padx=(0,0), pady=(10, 0))
        self.CX_btn_right_vertical = tk.Radiobutton(self.right_vertical_frame_radio_all_right, variable=self.var_right_vertical_frame_rejestr, value=2)
        self.CX_btn_right_vertical.grid(row=2, column=1, padx=(0,30), pady=(10, 0))

        self.DX_btn_desc_right_vertical = tk.Label(self.right_vertical_frame_radio_all_right, text="DX", font=middle_font)
        self.DX_btn_desc_right_vertical.grid(row=3,column=0, padx=(0,0), pady=(10, 0))
        self.DX_btn_right_vertical = tk.Radiobutton(self.right_vertical_frame_radio_all_right, variable=self.var_right_vertical_frame_rejestr, value=3)
        self.DX_btn_right_vertical.grid(row=3, column=1, padx=(0,30), pady=(10, 0))









root = tk.Tk()
app = Application(master=root)
app.mainloop()