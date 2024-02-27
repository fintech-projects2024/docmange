from tkinter import messagebox
from dotenv import load_dotenv
import mysql.connector as sql
import bcrypt
import pyperclip
import os


def redirection_handler(page, destination, username=None, password=None):
    page.destroy()

    if destination == "Login":
        from Login_Page import create_login_page

        create_login_page()

    elif destination == "Register":
        from Register_Page import create_register_page

        create_register_page()

    elif destination == "Main":
        from Main_Page import main_page_app

        main_page_app(username, password)

    elif destination == "Show_Documents":
        from ShowDocument_Page import create_document_storage_app

        create_document_storage_app(username, password)

    elif destination == "Add-Update_Documents":
        from AddDocument_Page import create_document_insertion_app

        create_document_insertion_app(username, password)


def toggle_password(show_password_var, password_entry):
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# Register page :


def register(username, password, page, destination):
    user_status = insert_new_user(username, password)
    if user_status:
        redirection_handler(page, destination, username, password)


#  Show Documents


# Function to copy text to clipboard
def copy_to_clipboard(entry_widget):
    text_to_copy = entry_widget.get()
    pyperclip.copy(text_to_copy)


# Mysql Connectivity  Methods


def establish_db_connection():
    load_dotenv()

    database_info = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_DATABASE"),
    }
    conn = sql.connect(
        host=database_info["host"],
        user=database_info["user"],
        password=database_info["password"],
        database=database_info["database"],
    )

    return conn


def insert_new_user(username, password):
    try:
        # Create a MySQL database connection
        conn = establish_db_connection()
        mycursor = conn.cursor()

        # Check if the user already exists
        query = "SELECT * FROM documents WHERE username = %s"
        mycursor.execute(query, (username,))
        user_exist = mycursor.fetchone()

        if user_exist:
            messagebox.showinfo(
                title=f" {username} already exists",
                message="This Username is not available , Please choose a different username.",
            )
            return False

        else:
            if len(password) < 8:
                messagebox.showinfo(
                    title="Password is Too Short",
                    message=f"Your Password Length is too short , it Should be at least 8 .",
                )
                return False

            # Hash the password using bcrypt
            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

            # Insert the new user into the database
            query = "INSERT INTO documents (username, password) VALUES (%s, %s)"
            mycursor.execute(query, (username, hashed_password))
            conn.commit()

            messagebox.showinfo(
                title="New User",
                message=f"Welcome {username}, you have been Registered. Please sign in through the Login Page.",
            )
            return True

    except Exception as e:
        messagebox.showerror("DATABASE ERROR:", str(e))

    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()


def login(username, password, page, destination):
    try:
        conn = establish_db_connection()

        mycursor = conn.cursor()

        # Retrieve the hashed password from the database for the provided username
        select_query = "SELECT password FROM documents WHERE username = %s"
        mycursor.execute(select_query, (username,))
        user = mycursor.fetchone()

        if user:
            hashed_password = user[0].encode("utf-8")
            password_status = bcrypt.checkpw(password.encode("utf-8"), hashed_password)

            if password_status:
                redirection_handler(page, destination, username, password)
            else:
                messagebox.showerror(
                    title="Login Failed",
                    message="    Incorrect password , Please Check the Password and Try again .",
                )

        else:
            messagebox.showerror(
                title="Login Failed",
                message=" Invalid Username , User Not Found",
            )

    except sql.Error as e:
        messagebox.showerror("DATABASE ERROR : ", e)

    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()


def fetch_mydocuments(username, password):
    try:
        conn = establish_db_connection()

        mycursor = conn.cursor()

        if username == None and password == None:
            raise ValueError

        query = (
            "select AADHAR,PANCARD,PASSPORT,BANK_AC from documents where username = %s "
        )
        mycursor.execute(query, (username,))

        row = mycursor.fetchone()

        all_documents = {
            "Aadhar": row[0],
            "Pan": row[1],
            "Passport": row[2],
            "Bank": row[3],
        }
        return all_documents

    except sql.Error as e:
        messagebox.showerror("DATABASE ERROR : ", e)

    except ValueError as e:
        messagebox.showerror(message="Username and Password are Invalid")

    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()


def insert_document(username, document_type, document_input):
    try:
        conn = establish_db_connection()

        mycursor = conn.cursor()
        validation_result = Document_Validation(document_type, document_input)

        if validation_result:
            query = f"update documents set {document_type}='{document_input}' where username='{username}'"
            mycursor.execute(query)
            conn.commit()
            messagebox.showinfo(
                title="Document Inserted Successfully",
                message=f"{document_type} Added",
            )

    except sql.Error as e:
        messagebox.showerror("DATABASE ERROR : ", e)

    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()


def Document_Validation(document_type, document_input):
    if document_type == "AADHAR":
        if len(document_input) != 12:
            messagebox.showerror(
                title="INVALID INPUT",
                message="INVALID AADHAR NUMBER - IT SHOULD BE OF 12 NUMBERS",
            )
            return False

    elif document_type == "PANCARD":
        if len(document_input) != 10:
            messagebox.showerror(
                title="INVALID INPUT",
                message="INVALID PANCARD NUMBER - IT SHOULD BE OF 10 ALPHA-NUMERIC CHARACTERS",
            )
            return False

    elif document_type == "PASSPORT":
        if len(document_input) > 12 or len(document_input) < 8:
            messagebox.showerror(
                title="INVALID INPUT",
                message="INVALID PASSPORT NUMBER - IT SHOULD BE BETWEEN 8 - 12 ALPHA-NUMERIC CHARACTERS",
            )
            return False

    elif document_type == "BANK_AC":
        if len(document_input) > 12 or len(document_input) < 8:
            messagebox.showerror(
                title="INVALID INPUT",
                message="INVALID BANK ACCOUNT NUMBER - IT SHOULD BE BETWEEN 8 - 12 NUMBERS",
            )
            return False

    return True
