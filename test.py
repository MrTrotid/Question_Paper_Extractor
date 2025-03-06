import tkinter as tk
import requests
import os
from tkinter import ttk

def on_subject_click(subject_code):
    print(f"Selected subject: {subject_code}")
    display_year_options(subject_code)

def display_year_options(subject_code):
    for widget in frame.winfo_children():
        widget.destroy()

    years = [
        ("2025", "s", None),
        ("2024", "s", "w"),
        ("2023", "s", "w"),
        ("2022", "s", "w"),
        ("2021", "s", "w"),
    ]

    cols = len(years)  # Number of columns based on the number of years

    for col, (year, summer, winter) in enumerate(years):
        year_label = tk.Label(frame, text=year, bg="white", font=("Arial", 14, "bold"))
        year_label.grid(row=0, column=col, padx=10, pady=10)

        summer_button = tk.Button(frame, text="June", bg="white", font=("Arial", 12), command=lambda y=year, s=summer: display_paper_options(subject_code, y, s))
        summer_button.grid(row=1, column=col, padx=10, pady=10)

        if winter:
            winter_button = tk.Button(frame, text="November", bg="white", font=("Arial", 12), command=lambda y=year, w=winter: display_paper_options(subject_code, y, w))
            winter_button.grid(row=2, column=col, padx=10, pady=10)

def display_paper_options(subject_code, year, season):
    for widget in frame.winfo_children():
        widget.destroy()

    year_suffix = year[-2:]  # Get the last two digits of the year
    paper_codes = ["11", "12", "13", "21", "22", "23", "31", "32", "33", "41", "42", "43"]
    row = 0

    for paper_code in paper_codes:
        paper_label = tk.Label(frame, text=f"Paper {paper_code}", bg="white", font=("Arial", 12, "bold"))
        paper_label.grid(row=row, column=0, padx=10, pady=5)

        paper_button = tk.Button(frame, text=f"{subject_code}_{season}{year_suffix}_qp_{paper_code}.pdf", bg="white", font=("Arial", 12), command=lambda pc=paper_code: download_paper(subject_code, year, season, pc))
        paper_button.grid(row=row, column=1, padx=10, pady=5)

        row += 1

def download_paper(subject_code, year, season, paper_code):
    year_suffix = year[-2:]  # Get the last two digits of the year
    url = f"{subject_code}_{season}{year_suffix}_qp_{paper_code}.pdf"
    subject_name = next(subject[0] for subject in subjects if subject[1] == subject_code).replace(" ", "-").lower()
    full_url = f"https://bestexamhelp.com/exam/cambridge-international-a-level/{subject_name}-{subject_code}/{year}/{url}"
    response = requests.get(full_url)
    if response.status_code == 200:
        # Create the directory if it doesn't exist
        directory = os.path.join("Papers", f"{subject_name}-{subject_code}", year)
        os.makedirs(directory, exist_ok=True)
        
        # Save the file in the respective directory
        file_path = os.path.join(directory, url)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url} to {file_path}")
    else:
        print(f"Failed to download {url}")

subjects = [
    ("Accounting", "9706"),
    ("AICT", "9713"),
    ("Biology", "9700"),
    ("Business", "9609"),
    ("Business Studies", "9707"),
    ("Chemistry", "9701"),
    ("Computer Science", "9618"),
    ("Computer Science", "9608"),
    ("Computing", "9691"),
    ("Economics", "9708"),
    ("History", "9489"),
    ("Islamic Studies", "9488"),
    ("Law", "9084"),
    ("Mathematics", "9709"),
    ("Mathematics - Further", "9231"),
    ("Media Studies", "9607"),
    ("Physics", "9702"),
    ("Psychology", "9990"),
    ("Psychology", "9698"),
    ("Sociology", "9699"),
]

root = tk.Tk()
root.title("A-Level Subjects")
root.configure(bg="#2F6B5C")

frame = tk.Frame(root, bg="#2F6B5C")
frame.pack(padx=20, pady=20)

buttons = []
cols = 3  # Number of columns per row

for i, (subject, code) in enumerate(subjects):
    card = tk.Frame(frame, bg="white", padx=10, pady=10, relief=tk.RIDGE, borderwidth=2)
    card.grid(row=i//cols, column=i%cols, padx=10, pady=10, sticky="nsew")
    
    button = tk.Button(card, text=f"{subject} - {code}", bg="white", font=("Arial", 12, "bold"), relief=tk.FLAT, command=lambda c=code: on_subject_click(c))
    button.pack()
    
    buttons.append(button)

root.mainloop()