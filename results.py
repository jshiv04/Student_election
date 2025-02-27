from tkinter import *
from tkinter import messagebox

project = Tk()
project.title("CV STUDENT ELECTION-2021")

Label(project, text="CV \n STUDENT ELECTION-2021 \n RESULTS", font=('Arial Bold', 25), fg='purple').pack()

def clicked_winner():
    try:
        with open("results.txt", "r") as file:
            a_dictionary = {}
            for line in file:
                key, value = line.split()
                a_dictionary[key] = int(value)  # Convert to integer

        if not a_dictionary:
            messagebox.showinfo("No Data", "No votes recorded yet!")
            return

        winner = max(a_dictionary, key=a_dictionary.get)
        max_votes = a_dictionary[winner]

        screen1 = Toplevel(project)
        screen1.title("Winner Announcement")
        screen1.geometry("400x300")

        Label(screen1, text="WINNER", font=('Arial Bold', 30), fg='red').pack()
        Label(screen1, text=winner, font=('Arial Bold', 25), fg='black').pack()
        Label(screen1, text=f"Votes: {max_votes}", font=('Arial Bold', 25), fg='black').pack()
    
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "Results file not found. Please enter votes first.")
    except ValueError:
        messagebox.showerror("Error", "Invalid data in results file.")

Button(project, text="WINNER", fg='black', bg='light blue', font=('Italic', 18), command=clicked_winner, padx=50, pady=10).pack()

def votes():
    try:
        screen2 = Toplevel(project)
        screen2.title("Votes Table")
        screen2.geometry("500x400")

        Label(screen2, text="VOTES", font=('Arial Bold', 30), fg='red').pack()
        
        with open("results.txt", "r") as file:
            data = file.readlines()

        if not data:
            messagebox.showinfo("No Votes", "No votes recorded yet!")
            return

        formatted_data = "\n".join(data)
        Label(screen2, text=formatted_data, font=('Arial', 20), fg='black').pack()
    
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "Results file not found. Please enter votes first.")
    except ValueError:
        messagebox.showerror("Error", "Invalid data in results file.")

Button(project, text="VOTES", fg='black', bg='light blue', font=('Italic', 18), padx=50, pady=10, command=votes).pack()

project.mainloop()
