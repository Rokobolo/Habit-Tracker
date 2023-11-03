from tkinter import *
import pixela
from datetime import datetime

ENDPOINT = "https://pixe.la/v1/users"


class PixelaInterface:
    def __init__(self):

        self.window = Tk()
        self.window.title("Pixela Interface")
        self.window.config(pady=20, padx=20)

        self.frame = Frame(self.window)
        self.frame.pack()

        self.main_menu()

        self.window.mainloop()

    def main_menu(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        title_label = Label(self.frame, text="Pixela UI\nChoose an option.")
        title_label.grid(row=0, column=0)

        create_account_button = Button(self.frame, text="Create an account", width=20, command=self.create_account)
        create_account_button.grid(row=1, column=0)

        create_graph = Button(self.frame, text="Create a graph", width=20, command=self.create_graph)
        create_graph.grid(row=2, column=0, pady=5)

        add_up_del_data = Button(self.frame, text="Update Pixel", width=20, command=self.create_update_pixel)
        add_up_del_data.grid(row=3, column=0)

    def create_account(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        title_label = Label(self.frame, text="Create an account")
        title_label.grid(row=0, column=0, columnspan=2)

        user_name_label = Label(self.frame, text="User Name: ")
        user_name_label.grid(row=1, column=0)
        user_name_entry = Entry(self.frame)
        user_name_entry.grid(row=1, column=1)

        password_label = Label(self.frame, text="Password: ")
        password_label.grid(row=2, column=0)
        password_entry = Entry(self.frame)
        password_entry.grid(row=2, column=1)

        confirmation_button = Button(self.frame,
                                     text="Create",
                                     width=15,
                                     command=lambda:
                                     pixela.create_account(password=password_entry.get(),
                                                           user_name=user_name_entry.get()),
                                     )
        confirmation_button.grid(row=3, column=0)

        return_button = Button(self.frame, text="Return", width=15, command=self.main_menu)
        return_button.grid(row=3, column=1)

    def create_graph(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Top label
        title_label = Label(self.frame, text="Create a new Pixela graph")
        title_label.grid(row=0, column=0, columnspan=2)

        # Get user
        user_name_label = Label(self.frame, text="User Name: ")
        user_name_label.grid(row=1, column=0)
        user_name_entry = Entry(self.frame)
        user_name_entry.grid(row=1, column=1)

        # Get password
        password_label = Label(self.frame, text="Password: ")
        password_label.grid(row=2, column=0)
        password_entry = Entry(self.frame)
        password_entry.grid(row=2, column=1)

        # Get ID
        unique_id_label = Label(self.frame, text="Unique ID: ")
        unique_id_label.grid(row=3, column=0)
        unique_id_entry = Entry(self.frame)
        unique_id_entry.grid(row=3, column=1)

        # Get graph name
        graph_name_label = Label(self.frame, text="Graph name: ")
        graph_name_label.grid(row=4, column=0)
        graph_name_entry = Entry(self.frame)
        graph_name_entry.grid(row=4, column=1)

        # Get unit
        measure_unit_name_label = Label(self.frame, text="Unit measure: ")
        measure_unit_name_label.grid(row=5, column=0)
        measure_unit_name_entry = Entry(self.frame)
        measure_unit_name_entry.grid(row=5, column=1)

        btn1 = StringVar()

        measure_unit_name_label = Label(self.frame, text="Weight: ")
        measure_unit_name_label.grid(row=6, column=0, columnspan=2)
        measure_unit_btn1 = Radiobutton(self.frame,
                                        text="Integer",
                                        value="int",
                                        variable=btn1,
                                        )
        measure_unit_btn1.grid(row=7, column=0)

        measure_unit_btn2 = Radiobutton(self.frame,
                                        text="Decimal",
                                        value="float",
                                        variable=btn1,
                                        )
        measure_unit_btn2.grid(row=7, column=1)

        # Get color
        color_list = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Black']

        drop1 = StringVar(self.frame)
        drop1.set(color_list[0])

        drop_color_label = Label(self.frame, text="Choose a color: ")
        drop_color_label.grid(row=8, column=0)
        drop_color_entry = OptionMenu(self.frame,
                                      drop1,
                                      *color_list,
                                      )
        drop_color_entry.grid(row=8, column=1)

        confirmation_button = Button(self.frame,
                                     text="Create",
                                     width=15,
                                     command=lambda: pixela.create_graph(
                                         user_name=user_name_entry.get(),
                                         user_token=password_entry.get(),
                                         graph_id=unique_id_entry.get(),
                                         graph_name=graph_name_entry.get(),
                                         unit_name=measure_unit_name_entry.get(),
                                         unit_type=btn1.get(),
                                         color_pick=drop_color_entry.getvar(str(drop1))
                                     ))
        confirmation_button.grid(row=9, column=0)

        return_button = Button(self.frame, text="Return", width=15, command=self.main_menu)
        return_button.grid(row=9, column=1)

    def create_update_pixel(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Top label
        title_label = Label(self.frame, text="Fill or update a pixel")
        title_label.grid(row=0, column=0, columnspan=2)

        # Get user
        user_name_label = Label(self.frame, text="User Name: ")
        user_name_label.grid(row=1, column=0)
        user_name_entry = Entry(self.frame)
        user_name_entry.grid(row=1, column=1)

        # Get password
        password_label = Label(self.frame, text="Password: ")
        password_label.grid(row=2, column=0)
        password_entry = Entry(self.frame)
        password_entry.grid(row=2, column=1)

        # Confirm ID
        unique_id_label = Label(self.frame, text="Unique ID: ")
        unique_id_label.grid(row=3, column=0)
        unique_id_entry = Entry(self.frame)
        unique_id_entry.grid(row=3, column=1)

        # Get the date
        today = datetime.today()
        formatted_date = today.strftime('%Y%m%d')

        date_label = Label(self.frame, text="Date: ")
        date_label.grid(row=4, column=0)
        date_entry = Entry(self.frame)
        date_entry.insert(0, formatted_date)
        date_entry.grid(row=4, column=1)

        # Get the quantity
        measure_unit_name_label = Label(self.frame, text="Quantity: ")
        measure_unit_name_label.grid(row=5, column=0)
        measure_unit_name_entry = Entry(self.frame)
        measure_unit_name_entry.grid(row=5, column=1)

        # Buttons
        confirmation_button = Button(self.frame, text="Update pixel", width=15,
                                     command=lambda: pixela.create_value(
                                         user_name=user_name_entry.get(),
                                         user_token=password_entry.get(),
                                         graph_id=unique_id_entry.get(),
                                         d_day=date_entry.get(),
                                         q_quantity=measure_unit_name_entry.get(),
                                     ))
        confirmation_button.grid(row=6, column=0)

        return_button = Button(self.frame, text="Return", width=15, command=self.main_menu)
        return_button.grid(row=6, column=1)
