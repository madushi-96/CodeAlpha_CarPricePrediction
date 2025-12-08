import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import joblib
import numpy as np

# Load model
model = joblib.load("car_price_model.pkl")

# ---------------- LOGIN WINDOW ---------------- #

def login_window():

    login = tk.Toplevel()
    login.title("Login")
    login.geometry("350x250")
    login.resizable(False, False)

    tk.Label(login, text="Username:").pack(pady=10)
    user_entry = tk.Entry(login)
    user_entry.pack()

    tk.Label(login, text="Password:").pack(pady=10)
    pass_entry = tk.Entry(login, show="*")
    pass_entry.pack()

    def check_login():
        username = user_entry.get()
        password = pass_entry.get()

        # Simple fixed login
        if username == "admin" and password == "1234":
            messagebox.showinfo("Success", "Login Successful!")
            login.destroy()
            main_interface()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    tk.Button(login, text="Login", command=check_login).pack(pady=20)

# ---------------- MAIN PREDICTION WINDOW ---------------- #

def main_interface():

    window = tk.Toplevel()
    window.title("Car Price Prediction")
    window.geometry("700x500")
    window.resizable(False, False)

    # Background image
    bg = Image.open("bg.jpg")
    bg = bg.resize((700, 500), Image.Resampling.LANCZOS)
    bg_img = ImageTk.PhotoImage(bg)

    bg_label = tk.Label(window, image=bg_img)
    bg_label.image = bg_img
    bg_label.place(x=0, y=0)

    # ---------------------- TITLE ---------------------- #
    tk.Label(window, 
             text="CAR PRICE PREDICTION",
             font=("Arial", 24, "bold"),
             fg="white",
             bg="#1a1a1a").place(x=180, y=10)

    # ---------------------- FORM LABELS ---------------------- #
    label_font = ("Arial", 12, "bold")

    tk.Label(window, text="Year:", font=label_font, bg="lightgray").place(x=120, y=80)
    year_entry = tk.Entry(window)
    year_entry.place(x=480, y=80)

    tk.Label(window, text="Present Price:", font=label_font, bg="lightgray").place(x=120, y=130)
    present_entry = tk.Entry(window)
    present_entry.place(x=480, y=130)

    tk.Label(window, text="Driven Kms:", font=label_font, bg="lightgray").place(x=120, y=180)
    kms_entry = tk.Entry(window)
    kms_entry.place(x=480, y=180)

    tk.Label(window, text="Fuel Type (0=Petrol,1=Diesel,2=CNG):", font=label_font, bg="lightgray").place(x=120, y=230)
    fuel_entry = tk.Entry(window)
    fuel_entry.place(x=480, y=230)

    tk.Label(window, text="Selling Type (0=Dealer,1=Individual):", font=label_font, bg="lightgray").place(x=120, y=280)
    selling_entry = tk.Entry(window)
    selling_entry.place(x=480, y=280)

    tk.Label(window, text="Transmission (0=Manual,1=Automatic):", font=label_font, bg="lightgray").place(x=120, y=330)
    trans_entry = tk.Entry(window)
    trans_entry.place(x=480, y=330)

    tk.Label(window, text="Owner Count:", font=label_font, bg="lightgray").place(x=120, y=380)
    owner_entry = tk.Entry(window)
    owner_entry.place(x=480, y=380)

    # ---------------------- PREDICTION FUNCTION ---------------------- #
    def predict_price():
        try:
            year = int(year_entry.get())
            present = float(present_entry.get())
            kms = int(kms_entry.get())
            fuel = int(fuel_entry.get())
            sell = int(selling_entry.get())
            trans = int(trans_entry.get())
            owner = int(owner_entry.get())

            input_data = np.array([[year, present, kms, fuel, sell, trans, owner]])
            result = model.predict(input_data)[0]

            messagebox.showinfo("Predicted Price", f"Predicted Price: {result:.2f} lakhs")

        except:
            messagebox.showerror("Error", "Invalid inputs!")

    # ---------------------- BUTTONS ---------------------- #
    tk.Button(window, text="Predict Price", command=predict_price, font=("Arial", 12, "bold"), bg="#00cc66").place(x=220, y=430)

    # Logout Button (Moved to bottom)
    def logout():
        window.destroy()
        messagebox.showinfo("Logout", "Logged out successfully!")

    tk.Button(window, text="Logout", command=logout, font=("Arial", 12, "bold"), bg="#ff5050").place(x=430, y=430)


# ---------------- ROOT WINDOW ---------------- #

root = tk.Tk()
root.title("Car Price App")
root.geometry("300x200")

tk.Label(root, text="Welcome to Car Price App").pack(pady=20)
tk.Button(root, text="Login", command=login_window).pack()

root.mainloop()
