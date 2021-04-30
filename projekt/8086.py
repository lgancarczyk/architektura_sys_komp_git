import tkinter as tk
import random
from tkinter import messagebox



large_font = ('Verdana',15)
middle_font = ('Verdana',11)
small_font = ('Verdana',10)


class Application(tk.Frame):

    def hex_to_int(self, hex_str):
        return int(hex_str, 16)

    def int_to_hex(self, intt):
        hex_str = hex(intt)[2:].upper()
        while len(hex_str)<4:
            hex_str = "0"+hex_str
        return hex_str

    def Rejest_indexowo_bazowy(self, indeks):
        if indeks==0:
            pierwszy = self.hex_to_int(self.input_list[4].get())
            drugi = self.hex_to_int(self.input_list[1].get())
            return pierwszy+drugi
        if indeks==1:
            pierwszy = self.hex_to_int(self.input_list[5].get())
            drugi = self.hex_to_int(self.input_list[1].get())
            return pierwszy+drugi
        if indeks==2:
            pierwszy = self.hex_to_int(self.input_list[4].get())
            drugi = self.hex_to_int(self.input_list[6].get())
            return pierwszy+drugi
        if indeks==3:
            pierwszy = self.hex_to_int(self.input_list[5].get())
            drugi = self.hex_to_int(self.input_list[6].get())
            return pierwszy+drugi

    def track_mode_list(self, event):
        
        print(event)
        if event=="Indeksowy":
            self.right_vertical_frame_radio_all_left_bazowy.grid_remove()
            self.right_vertical_frame_radio_all_left_indeksowo_bazowy.grid_remove()
            self.right_vertical_frame_radio_all_left_indeksowy.grid(row=0, column=0)
            pass
        if event=="Bazowy":
            self.right_vertical_frame_radio_all_left_indeksowy.grid_remove()
            self.right_vertical_frame_radio_all_left_indeksowo_bazowy.grid_remove()
            self.right_vertical_frame_radio_all_left_bazowy.grid(row=0, column=0)
            pass
        if event=="Indeksowo-Bazowy":
            self.right_vertical_frame_radio_all_left_indeksowy.grid_remove()
            self.right_vertical_frame_radio_all_left_bazowy.grid_remove()
            self.right_vertical_frame_radio_all_left_indeksowo_bazowy.grid(row=0, column=0)
            pass


    def Random(self):
        print("Random")
        for i in range(0, len(self.input_list)-1):
            hex_num =  hex(random.getrandbits(16))[2:].upper()
            while len(hex_num)<4:
                hex_num = "0"+hex_num
            print(hex_num)
            self.input_list[i].delete(0, tk.END)
            self.input_list[i].insert(0, hex_num) 

    def Reset(self):
        print("Reset")
        for i in range(0, len(self.input_list)-1):
            
            self.input_list[i].delete(0, tk.END)
            self.input_list[i].insert(0, "0000") 

    def simple_mov(self):
        print("simple MOV")
        old_register_radiobtn = self.var_right.get()
        new_register_radiobtn = self.var_left.get()

        new_reg = self.input_list[new_register_radiobtn].get()
        self.input_list[old_register_radiobtn].delete(0, tk.END)
        self.input_list[old_register_radiobtn].insert(0, new_reg)

    def simple_xchg(self):
        print("simple XCHG")
        old_register_radiobtn = self.var_right.get()
        new_register_radiobtn = self.var_left.get()

        new_reg = self.input_list[new_register_radiobtn].get()
        old_reg = self.input_list[old_register_radiobtn].get()

        self.input_list[old_register_radiobtn].delete(0, tk.END)
        self.input_list[old_register_radiobtn].insert(0, new_reg)

        self.input_list[new_register_radiobtn].delete(0, tk.END)
        self.input_list[new_register_radiobtn].insert(0, old_reg)

    def Extended_mov(self):
        mode = self.var_mode_options.get()
        print(mode)
        disp = self.input_list[7].get()

        if mode == self.mode_list[0]:
            received_hex = self.input_list[self.var_right_vertical_frame_indeksowy.get()].get()
            disp_int = self.hex_to_int(disp)
            received_hex_int = self.hex_to_int(received_hex)
            place_in_memory = disp_int+received_hex_int -1
            print(f"place in memory: {place_in_memory}")
            self.Extended_mov_stage_2(place_in_memory)

        if mode == self.mode_list[1]:
            received_hex = self.input_list[self.var_right_vertical_frame_bazowy.get()].get()
            disp_int = self.hex_to_int(disp)
            received_hex_int = self.hex_to_int(received_hex)
            place_in_memory = disp_int+received_hex_int -1
            print(f"place in memory: {place_in_memory}")
            self.Extended_mov_stage_2(place_in_memory)

        if mode == self.mode_list[2]:
            print("IB")
            rejestr_sum = self.Rejest_indexowo_bazowy(self.var_right_vertical_frame_indeksowo_bazowy.get())
            print(rejestr_sum)
            disp_int = self.hex_to_int(disp)
            place_in_memory = disp_int+rejestr_sum - 1
            print(f"place in memory: {place_in_memory}")
            self.Extended_mov_stage_2(place_in_memory)
            

    def Extended_mov_stage_2(self, place_in_mem):
        rejestr = self.var_right_vertical_frame_rejestr.get()
        memory_mode = self.var_memory_mode_options.get()

        if place_in_mem >= len(self.memory_tab)-1:
            print("Place in Memory is Out of Range")
            
            messagebox.showinfo("Error", "Out of memory range!!")   
            

        elif memory_mode == self.memory_mode_list[1]:
            print("Z rejestru do Pamięci")
            hex_str = self.input_list[rejestr].get()
            starszy_bajt = hex_str[:2]
            mlodszy_bajt = hex_str[2:]

            self.memory_tab[place_in_mem] = mlodszy_bajt
            self.memory_tab[place_in_mem + 1 ] = starszy_bajt


        elif memory_mode == self.memory_mode_list[0]:
            print("Z Pemięci do Rejestru")
            mlodszy_bajt = self.memory_tab[place_in_mem]
            starszy_bajt = self.memory_tab[place_in_mem + 1 ]

            hex_str = starszy_bajt + mlodszy_bajt
            self.input_list[rejestr].delete(0, tk.END)
            self.input_list[rejestr].insert(0, hex_str)    




    def Extended_xchg(self):
        mode = self.var_mode_options.get()
        print(mode)
        disp = self.input_list[7].get()

        if mode == self.mode_list[0]:
            received_hex = self.input_list[self.var_right_vertical_frame_indeksowy.get()].get()
            disp_int = self.hex_to_int(disp)
            received_hex_int = self.hex_to_int(received_hex)
            place_in_memory = disp_int+received_hex_int -1
            print(f"place in memory: {place_in_memory}")
            self.Extended_xchg_stage_2(place_in_memory)

        if mode == self.mode_list[1]:
            received_hex = self.input_list[self.var_right_vertical_frame_bazowy.get()].get()
            disp_int = self.hex_to_int(disp)
            received_hex_int = self.hex_to_int(received_hex)
            place_in_memory = disp_int+received_hex_int -1
            print(f"place in memory: {place_in_memory}")
            self.Extended_xchg_stage_2(place_in_memory)

        if mode == self.mode_list[2]:
            print("IB")
            rejestr_sum = self.Rejest_indexowo_bazowy(self.var_right_vertical_frame_indeksowo_bazowy.get())
            print(rejestr_sum)
            disp_int = self.hex_to_int(disp)
            place_in_memory = disp_int+rejestr_sum - 1
            print(f"place in memory: {place_in_memory}")
            self.Extended_xchg_stage_2(place_in_memory)
            

    def Extended_xchg_stage_2(self, place_in_mem):
        rejestr = self.var_right_vertical_frame_rejestr.get()

        if place_in_mem >= len(self.memory_tab)-1:
            print("Place in Memory is Out of Range")
            
            messagebox.showinfo("Error", "Out of memory range!!")   
            
        else:
            hex_str_z_input = self.input_list[rejestr].get()
            starszy_bajt_z_input = hex_str_z_input[:2]
            mlodszy_bajt_z_input = hex_str_z_input[2:]

            mlodszy_bajt_z_memory = self.memory_tab[place_in_mem]
            starszy_bajt_z_memory = self.memory_tab[place_in_mem + 1 ]
            hex_str_z_memory = starszy_bajt_z_memory + mlodszy_bajt_z_memory

            self.memory_tab[place_in_mem] = mlodszy_bajt_z_input
            self.memory_tab[place_in_mem + 1 ] = starszy_bajt_z_input
            
            self.input_list[rejestr].delete(0, tk.END)
            self.input_list[rejestr].insert(0, hex_str_z_memory) 

    def Push(self):
        wielkosc = len(self.stack_tab)
        if wielkosc>=65536:
            print("Place in Memory is Out of Range")
            
            messagebox.showinfo("Error", "Out of stack range!!")
        else:
            rejestr = self.var_right_vertical_frame_rejestr.get()
            hex_str_z_input = self.input_list[rejestr].get()
            starszy_bajt_z_input = hex_str_z_input[:2]
            mlodszy_bajt_z_input = hex_str_z_input[2:]

            self.stack_tab.append(mlodszy_bajt_z_input)
            self.stack_tab.append(starszy_bajt_z_input)

            hex_z_stosu = self.int_to_hex(len(self.stack_tab))

            self.input_list[8].delete(0, tk.END)
            self.input_list[8].insert(0, hex_z_stosu) 

    def Pop(self):
        rejestr = self.var_right_vertical_frame_rejestr.get()

        wielkosc = self.hex_to_int(self.input_list[8].get())
        if wielkosc>=65536 or len(self.stack_tab)==0:
            print("Place in Memory is Out of Range")
            
            messagebox.showinfo("Error", "Out of stack range!!")
        
        
        elif wielkosc != len(self.stack_tab):
            print("Place in Memory is Out of Range")
            
            messagebox.showinfo("Error", "Wrong Entrys!!")
 

        else:

            starszy_bajt_z_stosu = self.stack_tab[wielkosc-2]
            mlodszy_bajt_z_stosu = self.stack_tab[wielkosc-1]

            self.input_list[rejestr].delete(0, tk.END)
            self.input_list[rejestr].insert(0, mlodszy_bajt_z_stosu+starszy_bajt_z_stosu) 

            del self.stack_tab[wielkosc-1]
            del self.stack_tab[wielkosc-2]

            hex_z_stosu = self.int_to_hex(len(self.stack_tab))

            self.input_list[8].delete(0, tk.END)
            self.input_list[8].insert(0, hex_z_stosu) 

    def clear_memory(self):
        self.memory_tab = ["00"]*66536

    def clear_stack(self):
        self.stack_tab = []
        self.input_list[8].delete(0, tk.END)
        self.input_list[8].insert(0, "0000") 



    def Pop_up_msg(self, msg):
        popup = tk.Toplevel()
        popup.title("!")
        label = tk.Label(popup, text=msg) #Can add a font arg here
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()
            

    def __init__(self, master=None):
        super().__init__(master)
        
        self.input_list= ['AX_input',
                        'BX_input',
                        'CX_input',
                        'DX_input',
                        'SI_input',
                        'DI_input',
                        'BP_input',
                        'DISP_input',
                        'SP_input']
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

        self.memory_tab = ["00"]*66536
        self.stack_tab = []


        self.vertical_frame_left = tk.Frame(master)
        self.vertical_frame_left.grid(row = 0, column=0, padx=(15, 0))
        self.vertical_frame_right = tk.Frame(master)
        self.vertical_frame_right.grid(row = 0, column=1, padx=(0, 15))


        ##########################################################
        ##########################################################
        ##########################################################
        ########################################################## left vertical frame

        self.input_frame = tk.Frame(self.vertical_frame_left)
        self.input_frame.grid(row=1, column=0)


        ######################################################### reset_random frame
        self.reset_random_frame = tk.Frame(self.vertical_frame_left)
        self.reset_random_frame.grid(row=0, column=0)

        self.create_random_btn = tk.Button(self.reset_random_frame, text='Random', width=10, command=lambda : self.Random()) #self.create_random()
        self.create_random_btn.grid(row=0, column=0, pady=(15, 0), padx=(0, 20))

        self.reset_btn = tk.Button(self.reset_random_frame, text='Reset', width=10, command=lambda : self.Reset()) #self.create_random()
        self.reset_btn.grid(row=0, column=1, pady=(15, 0), padx=(20, 0))

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

        self.DISP_input_desc = tk.Label(self.upper_input, text="DISP", font=middle_font)
        self.DISP_input_desc.grid(row=3,column=2, padx=(0,0), pady=(10, 0))
        self.input_list[7] = tk.Entry(self.upper_input, font=large_font, width=6, justify='center')
        self.input_list[7].grid(row=3, column=3, padx=(0,20), pady=(10, 0))


        self.lower_input = tk.Frame(self.input_frame)
        self.lower_input.grid(row=1, column=0)

        self.SP_input_desc = tk.Label(self.lower_input, text="SP", font=middle_font)
        self.SP_input_desc.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.input_list[8] = tk.Entry(self.lower_input, font=large_font, width=6, justify='center')
        self.input_list[8].grid(row=0, column=1, padx=(0,20), pady=(10, 0))

        
        

        ######################################################### radiobuttons left vertical frame

        self.radio_buttons_left_vertical_frame = tk.Frame(self.vertical_frame_left)
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

        self.mov_xchg_left_vertical_frame = tk.Frame(self.vertical_frame_left)
        self.mov_xchg_left_vertical_frame.grid(row=3, column=0)

        self.mov_left_vertical_frame_btn = tk.Button(self.mov_xchg_left_vertical_frame, text='MOV', width=10, command=lambda : self.simple_mov()) #self.start()
        self.mov_left_vertical_frame_btn.grid(row=0, column=0, pady=(0, 15), padx=(0, 20))

        self.xchg_left_vertical_frame_btn = tk.Button(self.mov_xchg_left_vertical_frame, text='XCHG', width=10, command=lambda : self.simple_xchg()) #self.start()
        self.xchg_left_vertical_frame_btn.grid(row=0, column=1, pady=(0, 15), padx=(20, 0))



        ##########################################################
        ##########################################################
        ##########################################################
        ########################################################## right vertical frame

        self.mode_drop = tk.OptionMenu(self.vertical_frame_right, self.var_mode_options, *(self.mode_list), command = self.track_mode_list)
        self.mode_drop.grid(row=0, column=0, )

        self.mode_drop = tk.OptionMenu(self.vertical_frame_right, self.var_memory_mode_options, *self.memory_mode_list)
        self.mode_drop.grid(row=1, column=0, pady=(10, 20))

        ######################################################### radio btns
        #########################################################

        self.right_vertical_frame_radio_all = tk.Frame(self.vertical_frame_right)
        self.right_vertical_frame_radio_all.grid(row=2, column=0, pady=(10, 30))

        ######################################################### radio btns left

        ###### indeksowy

        self.right_vertical_frame_radio_all_left_indeksowy = tk.Frame(self.right_vertical_frame_radio_all)
        self.right_vertical_frame_radio_all_left_indeksowy.grid(row=0, column=0)

        self.SI_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_indeksowy, text="SI", font=middle_font)
        self.SI_btn_desc.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.SI_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_indeksowy, variable=self.var_right_vertical_frame_indeksowy, value=4)
        self.SI_btn.grid(row=0, column=1, padx=(0,30), pady=(10, 0))

        self.DI_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_indeksowy, text="DI", font=middle_font)
        self.DI_btn_desc.grid(row=1,column=0, padx=(0,0), pady=(10, 0))
        self.DI_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_indeksowy, variable=self.var_right_vertical_frame_indeksowy, value=5)
        self.DI_btn.grid(row=1, column=1, padx=(0,30), pady=(10, 0))

        ###### bazowy

        self.right_vertical_frame_radio_all_left_bazowy = tk.Frame(self.right_vertical_frame_radio_all)
        #self.right_vertical_frame_radio_all_left_bazowy.grid(row=1, column=0)

        self.BX_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_bazowy, text="BX", font=middle_font)
        self.BX_btn_desc.grid(row=0,column=0, padx=(0,0), pady=(10, 0))
        self.BX_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_bazowy, variable=self.var_right_vertical_frame_bazowy, value=1)
        self.BX_btn.grid(row=0, column=1, padx=(0,30), pady=(10, 0))

        self.BP_btn_desc = tk.Label(self.right_vertical_frame_radio_all_left_bazowy, text="BP", font=middle_font)
        self.BP_btn_desc.grid(row=1,column=0, padx=(0,0), pady=(10, 0))
        self.BP_btn = tk.Radiobutton(self.right_vertical_frame_radio_all_left_bazowy, variable=self.var_right_vertical_frame_bazowy, value=6)
        self.BP_btn.grid(row=1, column=1, padx=(0,30), pady=(10, 0))

        ###### indeksowo bazowy

        self.right_vertical_frame_radio_all_left_indeksowo_bazowy = tk.Frame(self.right_vertical_frame_radio_all)
        #self.right_vertical_frame_radio_all_left_indeksowo_bazowy.grid(row=2, column=0)

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

        ######################################################### right vertical MOV XCHG

        self.right_vertical_frame_mov_xchg = tk.Frame(self.vertical_frame_right)
        self.right_vertical_frame_mov_xchg.grid(row=3, column=0)

        self.mov_right_vertical_frame_btn = tk.Button(self.right_vertical_frame_mov_xchg, text='MOV', width=10, command=lambda : self.Extended_mov()) #self.start()
        self.mov_right_vertical_frame_btn.grid(row=0, column=0, pady=(10, 0), padx=(0, 20))

        self.xchg_right_vertical_frame_btn = tk.Button(self.right_vertical_frame_mov_xchg, text='XCHG', width=10, command=lambda : self.Extended_xchg()) #self.start()
        self.xchg_right_vertical_frame_btn.grid(row=0, column=1, pady=(10, 0), padx=(20, 0))

        #########################################################  push pop

        self.right_vertical_frame_push_pop = tk.Frame(self.vertical_frame_right)
        self.right_vertical_frame_push_pop.grid(row=4, column=0)

        self.push_right_vertical_frame_btn = tk.Button(self.right_vertical_frame_push_pop, text='PUSH', width=10, command=lambda : self.Push()) #self.start()
        self.push_right_vertical_frame_btn.grid(row=0, column=0, pady=(10, 0), padx=(0, 20))

        self.pop_right_vertical_frame_btn = tk.Button(self.right_vertical_frame_push_pop, text='POP', width=10, command=lambda : self.Pop()) #self.start()
        self.pop_right_vertical_frame_btn.grid(row=0, column=1, pady=(10, 0), padx=(20, 0))

        #########################################################  clear clear

        self.right_vertical_frame_clear = tk.Frame(self.vertical_frame_right)
        self.right_vertical_frame_clear.grid(row=5, column=0)

        self.clear_memory_right_vertical_frame_btn = tk.Button(self.right_vertical_frame_clear, text='Clear Memory', width=10, command=lambda : self.clear_memory()) #self.start()
        self.clear_memory_right_vertical_frame_btn.grid(row=0, column=0, pady=(10, 0), padx=(0, 20))

        self.clear_stack_right_vertical_frame_btn = tk.Button(self.right_vertical_frame_clear, text='Clear Stack', width=10, command=lambda : self.clear_stack()) #self.start()
        self.clear_stack_right_vertical_frame_btn.grid(row=0, column=1, pady=(10, 0), padx=(20, 0))

        self.Reset()
        self.clear_stack()



root = tk.Tk()
app = Application(master=root)
app.mainloop()