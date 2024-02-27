import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from Functionality import insert_document, redirection_handler


def create_document_insertion_app(username, password):
    page5 = tk.Tk()
    page5.title("Document Storage System")
    page5.geometry("500x500")

    # Frame for the header (logo and title)
    header_frame = tk.Frame(page5)
    header_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nw")

    logo_img = tk.PhotoImage(file="./logo.png")
    logo_img_resized = logo_img.subsample(10, 10)
    logo = tk.Label(header_frame, image=logo_img_resized)
    logo.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    page_title = tk.Label(
        header_frame,
        text="Add / Update \n my Documents",
        font=("Arial Rounded MT Bold", 26, "bold"),
    )
    page_title.grid(row=0, column=1, padx=10, pady=10)

    # Dropdown menu for document types
    document_type_var = tk.StringVar()
    document_type_var.set("Select Document Type")  # Default selection

    # themed style
    style = ThemedStyle(page5)
    style.set_theme("breeze")

    document_type_label = tk.Label(
        page5, text="Document Type", font=("Helvetica", 16, "bold")
    )
    document_type_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    document_list = ["AADHAR", "PANCARD", "PASSPORT", "BANK_AC"]

    document_type_menu = ttk.Combobox(
        page5, textvariable=document_type_var, values=document_list, font=("Arial", 14)
    )
    document_type_menu.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Text field for document text
    document_text_var = tk.StringVar()
    document_text_label = tk.Label(
        page5, text="Document No.", font=("Helvetica", 16, "bold")
    )
    document_text_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    document_text_entry = ttk.Entry(
        page5, textvariable=document_text_var, width=25, font=("Arial", 14)
    )
    document_text_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Insert Document button
    insert_document_button_style = ttk.Style()
    insert_document_button_style.configure(
        "TButton", font=("Arial", 16, "bold"), padding=10
    )

    insert_document_button = ttk.Button(
        page5,
        text="Insert Document",
        command=lambda: insert_document(
            username, document_type_var.get(), document_text_var.get()
        ),
        style="TButton",
    )
    insert_document_button.grid(row=3, column=0, columnspan=2, pady=(20, 10))

    # Back Button
    back_button = ttk.Button(
        page5,
        text="Back",
        command=lambda: redirection_handler(page5, "Main", username, password),
        style="TButton",
    )
    back_button.grid(row=4, column=0, columnspan=2, pady=(10, 20))

    page5.mainloop()


if __name__ == "__main__":
    create_document_insertion_app(username=None, password=None)
