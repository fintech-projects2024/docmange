from tkinter import ttk
from tkinter import *
from Functionality import redirection_handler


def main_page_app(username, password):
    page3 = Tk()
    page3.title("Document Storage System")
    page3.geometry("500x500")

    header_frame = Frame(page3)
    header_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nw")

    logo_img = PhotoImage(file="./logo.png")
    logo_img_resized = logo_img.subsample(10, 10)
    logo = Label(header_frame, image=logo_img_resized)
    logo.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    page_title = Label(
        header_frame,
        text="DOCUMENT \n MANAGER ",
        font=("Arial Rounded MT Bold", 26, "bold"),
    )
    page_title.grid(row=0, column=1, padx=10, pady=10)

    # frame for the buttons
    button_frame = Frame(page3)
    button_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="n")

    show_documents_button_style = ttk.Style()
    show_documents_button_style.configure(
        "TButton", font=("arial", 16, "bold"), padding=10
    )
    show_documents_button = ttk.Button(
        button_frame,
        text="Show Documents",
        command=lambda: redirection_handler(
            page3, "Show_Documents", username, password
        ),
        style="TButton",
    )
    show_documents_button.grid(row=0, column=0, padx=10, pady=10)

    # "Add / Update Documents" button
    add_update_documents_button_style = ttk.Style()
    add_update_documents_button_style.configure(
        "TButton", font=("arial", 16, "bold"), padding=10
    )
    add_update_documents_button = ttk.Button(
        button_frame,
        text="Add / Update Documents",
        command=lambda: redirection_handler(
            page3, "Add-Update_Documents", username, password
        ),
        style="TButton",
    )
    add_update_documents_button.grid(row=1, column=0, padx=10, pady=10)

    #  "LOGOUT" button
    logout_style = ttk.Style()
    logout_style.configure("TButton", font=("arial", 16, "bold"), padding=10)
    logout_button = ttk.Button(
        button_frame,
        text="LOGOUT",
        command=lambda: redirection_handler(page3, "Login", username="", password=""),
        style="TButton",
    )
    logout_button.grid(row=2, column=0, padx=10, pady=10)

    # Align the buttons both horizontally and vertically
    button_frame.columnconfigure(0, weight=1)
    button_frame.rowconfigure(0, weight=1)
    button_frame.rowconfigure(1, weight=1)

    page3.mainloop()


if __name__ == "__main__":
    main_page_app(username=None, password=None)
