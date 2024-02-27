from tkinter import ttk
from tkinter import *
from Functionality import copy_to_clipboard, redirection_handler, fetch_mydocuments


def create_document_storage_app(username, password):
    page4 = Tk()
    page4.title("Document Storage System")
    page4.geometry("600x500")

    # Text Variables
    entry_var1 = StringVar()
    entry_var2 = StringVar()
    entry_var3 = StringVar()
    entry_var4 = StringVar()

    alldocs = fetch_mydocuments(username, password)
    if alldocs["Aadhar"] != None:
        entry_var1.set(alldocs["Aadhar"])

    if alldocs["Pan"] != None:
        entry_var2.set(alldocs["Pan"])

    if alldocs["Passport"] != None:
        entry_var3.set(alldocs["Passport"])

    if alldocs["Bank"] != None:
        entry_var4.set(alldocs["Bank"])

    # frame for the Header (logo and title)
    header_frame = Frame(page4)
    header_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nw")

    logo_img = PhotoImage(file="./logo.png")
    logo_img_resized = logo_img.subsample(10, 10)
    logo = Label(header_frame, image=logo_img_resized)
    logo.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    page_title = Label(
        header_frame, text="MY DOCUMENTS", font=("Arial Rounded MT Bold", 26, "bold")
    )
    page_title.grid(row=0, column=1, padx=10, pady=10)

    # Labels and Entry Fields
    label1 = Label(page4, text="AADHAR", font=("Helvetica", 16, "bold"))
    label1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    entry1 = ttk.Entry(page4, textvariable=entry_var1, width=20, font=("Arial", 14))
    entry1.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    copy_button_style = ttk.Style()
    copy_button_style.configure("TButton", font=("arial", 12, "bold"), padding=5)

    copy_button1 = ttk.Button(page4, text="Copy to Clipboard", style="TButton")
    copy_button1.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    copy_button1.config(command=lambda: copy_to_clipboard(entry1))

    label2 = Label(page4, text="PAN NO", font=("Helvetica", 16, "bold"))
    label2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    entry2 = ttk.Entry(page4, textvariable=entry_var2, width=20, font=("Arial", 14))
    entry2.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    copy_button2 = ttk.Button(page4, text="Copy to Clipboard", style="TButton")
    copy_button2.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    copy_button2.config(command=lambda: copy_to_clipboard(entry2))

    label3 = Label(page4, text="PASSPORT NO", font=("Helvetica", 16, "bold"))
    label3.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    entry3 = ttk.Entry(page4, textvariable=entry_var3, width=20, font=("Arial", 14))
    entry3.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    copy_button3 = ttk.Button(page4, text="Copy to Clipboard", style="TButton")
    copy_button3.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    copy_button3.config(command=lambda: copy_to_clipboard(entry3))

    label4 = Label(page4, text="BANK A/C NO", font=("Helvetica", 16, "bold"))
    label4.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    entry4 = ttk.Entry(page4, textvariable=entry_var4, width=20, font=("Arial", 14))
    entry4.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    copy_button4 = ttk.Button(page4, text="Copy to Clipboard", style="TButton")
    copy_button4.grid(row=4, column=2, padx=10, pady=10, sticky="w")
    copy_button4.config(command=lambda: copy_to_clipboard(entry4))

    # Back Button
    back_button = ttk.Button(
        page4,
        text="Back",
        style="TButton",
        command=lambda: redirection_handler(page4, "Main", username, password),
    )
    back_button.grid(row=5, column=1, pady=20, sticky="n")

    page4.mainloop()


if __name__ == "__main__":
    create_document_storage_app(username=None, password=None)
