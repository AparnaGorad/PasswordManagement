from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(0, nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(0, nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(0, nr_numbers)]

    password_list = password_number + password_symbol + password_letter

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# to write in data

def save():
    global entry_web, entry_user, entry_pass

    password = entry_pass.get()
    website = entry_web.get()
    user_email = entry_user.get()

    if len(password) == 0 or len(website) == 0 or len(user_email) == 0:
        oops = messagebox.showinfo(title="oops", message="Please do not leave any fields empty")
    else:
        is_details_ok = messagebox.askokcancel(title="Details Verification", message=f"These are the details:\n"
                                                                                     f"Email:{user_email}\n "
                                                                                     f"website:{website}\n "
                                                                                     f"password:{password}")
        if is_details_ok:
            with open("data.txt", "a") as f:
                f.write(f"{user_email} | {website} | {password}\n")
            entry_user.delete(0, END)
            entry_web.delete(0, END)
            entry_pass.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

# label_web
label_web = Label(text="website:", font=("Aerial", 14))
label_web.grid(row=1, column=0)

# label_email
label_email = Label(text="Email/User_name:", font=("Aerial", 14))
label_email.grid(row=2, column=0)

# label_Password
label_Password = Label(text="Password:", font=("Aerial", 14))
label_Password.grid(row=3, column=0)

# Entries
entry_web = Entry(width=42)
entry_web.grid(row=1, column=1, columnspan=2, sticky="w")
entry_web.focus()

entry_user = Entry(width=42)
entry_user.insert(0, "goradaparna@gmail.com")
entry_user.grid(row=2, column=1, columnspan=2, sticky="w")

entry_pass = Entry(width=24)
entry_pass.grid(row=3, column=1, columnspan=1, sticky="w")

generate_button = Button(text="Generate Password", command=generate_password, width=14, highlightthickness=0,
                         borderwidth=1)
generate_button.grid(row=3, column=1, sticky="e", columnspan=2)

add_button = Button(text="Add", command=save, width=36, bg="white", highlightthickness=0,
                    borderwidth=1)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
