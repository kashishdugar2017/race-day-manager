import tkinter as tk
from datetime import datetime

# ---------------- FUNCTIONS ----------------

def say_hello():

    name = name_entry.get()
    comp = comp_entry.get()

    message = f"CHAMPION: {name}\nCOMPETITION: {comp}"

    greeting_label.config(text=message)


    name_label.pack_forget()
    name_entry.pack_forget()
    comp_label.pack_forget()
    comp_entry.pack_forget()
    go_button.pack_forget()


    events_frame.pack(pady=20)

# ---------------- ADD EVENT ----------------

def add_event():

    if len(event_entries) < 20:

        event_row = tk.Frame(
            events_container,
            bg='#2C3E50'
        )

        event_row.pack(pady=8)

        done_var = tk.BooleanVar()


        event_entry = tk.Entry(
            event_row,
            font=("Arial", 18),
            width=25,
            justify='center'
        )

        event_entry.pack(side='left', padx=10)

        event_number = len(event_entries) + 1

        event_entry.insert(
            0,
            f"Enter Event {event_number}"
        )

        
        time_entry = tk.Entry(
            event_row,
            font=("Arial", 18),
            width=8,
            justify='center'
        )

        time_entry.pack(side='left', padx=5)

        time_entry.insert(0, "00:00")

   
        ampm_var = tk.StringVar()
        ampm_var.set("AM")

        ampm_menu = tk.OptionMenu(
            event_row,
            ampm_var,
            "AM",
            "PM"
        )

        ampm_menu.config(
            font=("Arial", 14),
            bg='white'
        )

        ampm_menu.pack(side='left', padx=5)

        event_entries.append(
            (
                event_entry,
                time_entry,
                done_var,
                ampm_var
            )
        )

# ---------------- DONE EVENTS ----------------

def done_events():

    add_event_button.pack_forget()
    done_button.pack_forget()

    events_title.config(
        text="Today's Schedule"
    )

    for item in event_entries:

        event_entry = item[0]
        time_entry = item[1]
        done_var = item[2]
        ampm_var = item[3]

        event_name = event_entry.get()

        event_time = (
            time_entry.get()
            + " "
            + ampm_var.get()
        )

        parent_row = event_entry.master


        event_entry.pack_forget()
        time_entry.pack_forget()

        for widget in parent_row.winfo_children():

            if isinstance(widget, tk.OptionMenu):

                widget.pack_forget()

        
        
        label = tk.Label(
            parent_row,
            text=f"{event_name}   •   {event_time}",
            font=("Arial", 20, "bold"),
            bg='#2C3E50',
            fg='white'
        )

        label.pack(side='left', padx=10)

        # ---------------- CHECK EVENT ----------------

        def event_checked(
            current_item=item,
            current_label=label
        ):

            current_label.config(
                fg="#2ECC71"
            )

            tired_label.pack(pady=10)
            tired_slider.pack(pady=10)
            submit_tired_button.pack(pady=10)

            global current_checked_item
            current_checked_item = current_item

        check = tk.Checkbutton(
            parent_row,
            variable=done_var,
            command=event_checked,
            font=("Arial", 24),
            bg='#2C3E50',
            activebackground='#2C3E50',
            selectcolor='#2C3E50'
        )

        check.pack(side='left', padx=10)

# ---------------- TIREDNESS SUBMIT ----------------

def submit_tiredness():

    tiredness = tired_slider.get()

    current_index = event_entries.index(current_checked_item)

    # ---------------- ADVICE ----------------

    if tiredness <= 3:

        advice = "Warm Up Pool\nIn & Out Swim"
        color = "#2ECC71"

    elif tiredness <= 7:

        advice = "Dryland\nSnack\nStretch"
        color = "#F1C40F"

    else:

        advice = "Recovery\nHydrate\nRest"
        color = "#E74C3C"

    # ---------------- NEXT EVENT ----------------

    if current_index + 1 < len(event_entries):

        next_item = event_entries[current_index + 1]

        next_name = next_item[0].get()

        next_time = next_item[1].get() + " " + next_item[3].get()

        info = (
            f"NEXT EVENT\n\n"
            f"{next_name}\n"
            f"AT {next_time}\n\n"
            f"TIREDNESS: {tiredness}/10\n\n"
            f"WHAT TO DO\n\n"
            f"{advice}"
        )

        next_event_label.config(
            text=info,
            fg=color
        )

    # LAST EVENT
    else:

        result_window = tk.Toplevel(root)
        result_window.title("Final Race Result")
        result_window.configure(bg='#2C3E50')
        result_window.geometry("500x350")

        tk.Label(
            result_window,
            text="DID YOU RACE WELL?",
            font=("Arial", 24, "bold"),
            bg='#2C3E50',
            fg='white'
        ).pack(pady=20)

        def yes_plan():

            next_event_label.config(
                text="🏆 AMAZING JOB 🏆\n\nPOST MEET PLAN\n\nEasy Swim\nProtein Meal\nStretch\nHydrate\nCelebrate\nGood Sleep",
                fg="#2ECC71"
            )

            result_window.destroy()

        def no_plan():

            next_event_label.config(
                text="KEEP WORKING 💪\n\nPOST MEET PLAN\n\nRecovery Swim\nHydrate\nReview Races\nStretch\nEarly Sleep\nCome Back Stronger",
                fg="#F1C40F"
            )

            result_window.destroy()

        tk.Button(result_window,
                  text="YES!",
                  font=("Arial", 18, "bold"),
                  bg="#2ECC71",
                  fg="white",
                  command=yes_plan).pack(pady=20)

        tk.Button(result_window,
                  text="NOT REALLY",
                  font=("Arial", 18, "bold"),
                  bg="#E74C3C",
                  fg="white",
                  command=no_plan).pack(pady=10)

    tired_label.pack_forget()
    tired_slider.pack_forget()
    submit_tired_button.pack_forget()

# ---------------- COLORED SLIDER (ONLY CHANGE) ----------------

def update_slider_color(value):

    value = int(value)

    if value <= 3:
        color = "#2ECC71"   #
        
        
        
    elif value <= 7:
        color = "#F1C40F"
        
    else:
        color = "#E74C3C"
        

    tired_slider.config(
        troughcolor=color,
        activebackground=color,
        highlightbackground=color
    )

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Race Day Manager")
root.state('zoomed')
root.configure(bg='#2C3E50')

# ---------------- NAME ----------------

name_label = tk.Label(root, text="Enter your name:",
                      font=("Arial", 20),
                      bg='#2C3E50', fg='white')
name_label.pack(pady=10)

name_entry = tk.Entry(root, font=("Arial", 20))
name_entry.pack()

# ---------------- COMP ----------------

comp_label = tk.Label(root, text="Enter Competition:",
                      font=("Arial", 20),
                      bg='#2C3E50', fg='white')
comp_label.pack(pady=10)

comp_entry = tk.Entry(root, font=("Arial", 20))
comp_entry.pack()

# ---------------- START BUTTON ----------------

go_button = tk.Button(root,
                      text="Start My Day",
                      font=("Arial", 16, "bold"),
                      bg="#27AE60",
                      fg="white",
                      command=say_hello)

go_button.pack(pady=10)

# ---------------- GREETING ----------------

greeting_label = tk.Label(root,
                          text="",
                          font=("Arial", 40, "bold"),
                          bg='#2C3E50',
                          fg="#F1C40F")
greeting_label.pack(pady=40)

# ---------------- EVENTS FRAME ----------------

events_frame = tk.Frame(root, bg='#2C3E50')

top_buttons_frame = tk.Frame(events_frame, bg='#2C3E50')
top_buttons_frame.pack(pady=10)

add_event_button = tk.Button(top_buttons_frame,
                             text="+ Add Event",
                             font=("Arial", 16, "bold"),
                             bg="#3498DB",
                             fg="white",
                             command=add_event)

add_event_button.pack(side='left', padx=10)

done_button = tk.Button(top_buttons_frame,
                        text="DONE",
                        font=("Arial", 16, "bold"),
                        bg="#E74C3C",
                        fg="white",
                        command=done_events)

done_button.pack(side='left', padx=10)

events_title = tk.Label(events_frame,
                        text="Today's Events",
                        font=("Arial", 28, "bold"),
                        bg='#2C3E50',
                        fg='white')

events_title.pack(pady=10)

events_container = tk.Frame(events_frame, bg='#2C3E50')
events_container.pack()

next_event_label = tk.Label(events_frame,
                            text="",
                            font=("Arial", 24, "bold"),
                            bg='#2C3E50',
                            fg='white',
                            justify='center')

next_event_label.pack(pady=30)

# ---------------- TIREDNESS ----------------

tired_label = tk.Label(events_frame,
                       text="How Tired Are You?",
                       font=("Arial", 22, "bold"),
                       bg='#2C3E50',
                       fg='white')

tired_slider = tk.Scale(
    events_frame,
    from_=1,
    to=10,
    orient='horizontal',
    length=500,
    font=("Arial", 16, "bold"),
    bg='#2C3E50',
    fg='white',
    troughcolor='#2ECC71',
    activebackground='#2ECC71',
    highlightthickness=0,
    sliderlength=40,
    command=update_slider_color  
)

submit_tired_button = tk.Button(events_frame,
                                text="Submit Tiredness",
                                font=("Arial", 16, "bold"),
                                bg="#9B59B6",
                                fg="white",
                                command=submit_tiredness)

# ---------------- STORAGE ----------------

event_entries = []
current_checked_item = None

# ---------------- FIRST EVENT ----------------
add_event()

root.mainloop()