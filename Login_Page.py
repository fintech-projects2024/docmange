import tkinter as tk
from tkinter import ttk
from Functionality import login, redirection_handler, toggle_password


def create_login_page():
    page1 = tk.Tk()
    page1.title("Document Storage System")
    page1.geometry("500x500")

    # Text Variables
    username_var = tk.StringVar()
    password_var = tk.StringVar()
    show_password_var = tk.BooleanVar()

    # Frame for the header (logo and title)
    header_frame = tk.Frame(page1)
    header_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nw")

    logo_img = tk.PhotoImage(file="./logo.png")
    logo_img_resized = logo_img.subsample(10, 10)
    logo = tk.Label(header_frame, image=logo_img_resized)
    logo.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    page_title = tk.Label(
        header_frame, text="Login Page", font=("Arial Rounded MT Bold", 26, "bold")
    )
    page_title.grid(row=0, column=1, padx=10, pady=10)

    # frame for the login-related elements
    login_frame = tk.Frame(page1)
    login_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nw")

    username_label = tk.Label(
        login_frame, text="Username", font=("Helvetica", 16, "bold")
    )
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    username_entry = ttk.Entry(
        login_frame, textvariable=username_var, width=25, font=("Arial", 14)
    )
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = tk.Label(
        login_frame, text="Password", font=("Helvetica", 16, "bold")
    )
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    password_entry = ttk.Entry(
        login_frame, textvariable=password_var, show="*", width=25, font=("Arial", 14)
    )
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    show_password_checkbox = tk.Checkbutton(
        login_frame,
        text="Show Password",
        variable=show_password_var,
        font=("Helvetica", 12),
        command=lambda: toggle_password(show_password_var, password_entry),
    )
    show_password_checkbox.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    login_style = ttk.Style()
    login_style.configure("TButton", font=("arial", 16, "bold"), padding=10)
    login_button = ttk.Button(
        page1,
        text="Submit",
        command=lambda: login(username_var.get(), password_var.get(), page1, "Main"),
        style="TButton",
    )
    login_button.grid(row=2, column=0, columnspan=2, pady=(20, 10))

    # frame for the "Don't have an Account?" label and "Click me" button
    register_frame = tk.Frame(page1)
    register_frame.grid(
        row=3, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nw"
    )

    register_label = tk.Label(
        register_frame, text="Don't have an Account?", font=("arial", 12)
    )
    register_label.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="e")

    # "Click me" button
    register_button_style = ttk.Style()
    register_button_style.configure(
        "TButton",
        font=("arial", 12, "bold"),
        padding=5,
    )
    register_button = ttk.Button(
        register_frame,
        text="Click me",
        command=lambda: redirection_handler(page1, "Register"),
        style="TButton",
    )
    register_button.grid(row=0, column=1, padx=5, pady=10, sticky="w")

    page1.mainloop()


if __name__ == "__main__":
    create_login_page()
