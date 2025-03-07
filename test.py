import customtkinter as ctk
import requests
import os
from PIL import Image
from customtkinter import ThemeManager
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def create_logo_frame(parent):
    logo_frame = ctk.CTkFrame(parent, fg_color="transparent", height=80)
    logo_frame.pack(fill="x", padx=20, pady=(10,20))
    
    # Logo container with background
    logo_container = ctk.CTkFrame(logo_frame, fg_color="#2F6B5C", corner_radius=10)
    logo_container.pack(side="left", padx=20, pady=5)
    
    # Load and display logo image
    logo_image = Image.open("logo.png")
    # Resize image to fit nicely (adjust size as needed)
    logo_photo = ctk.CTkImage(light_image=logo_image, dark_image=logo_image, size=(40, 40))
    
    logo_label = ctk.CTkLabel(
        logo_container,
        image=logo_photo,
        text="",  # Empty text as we're using image
    )
    logo_label.pack(side="left", padx=15, pady=10)
    
    # App name with better styling
    logo_text = ctk.CTkLabel(
        logo_container,
        text="A-Level Papers",
        font=("Arial", 28, "bold"),
        text_color="white",
    )
    logo_text.pack(side="left", padx=(0,15), pady=10)
    
    return logo_frame

def on_subject_click(subject_code):
    print(f"Selected subject: {subject_code}")
    display_year_options(subject_code)

def go_back():
    clear_frame()
    display_subjects()

def display_year_options(subject_code):
    clear_frame()

    back_button = ctk.CTkButton(
        frame,
        text="← Go Back",
        command=go_back,
        fg_color="#1F4A3C",
        hover_color="#2F6B5C",
        width=100
    )
    back_button.pack(anchor="nw", padx=10, pady=10)

    # Create a container frame for years
    years_container = ctk.CTkFrame(frame, fg_color="transparent")
    years_container.pack(fill="both", expand=True, padx=20, pady=20)

    years = [
        ("2025", "s", None),
        ("2024", "s", "w"),
        ("2023", "s", "w"),
        ("2022", "s", "w"),
        ("2021", "s", "w"),
    ]

    for col, (year, summer, winter) in enumerate(years):
        year_frame = ctk.CTkFrame(years_container, fg_color="transparent")
        year_frame.grid(row=0, column=col, padx=10, pady=10)

        year_label = ctk.CTkLabel(year_frame, text=year, font=("Arial", 16, "bold"))
        year_label.pack(pady=5)

        summer_button = ctk.CTkButton(
            year_frame, 
            text="June", 
            command=lambda y=year, s=summer: display_paper_options(subject_code, y, s),
            fg_color="#2F6B5C",
            hover_color="#1F4A3C"
        )
        summer_button.pack(pady=5)

        if winter:
            winter_button = ctk.CTkButton(
                year_frame,
                text="November",
                command=lambda y=year, w=winter: display_paper_options(subject_code, y, w),
                fg_color="#2F6B5C",
                hover_color="#1F4A3C"
            )
            winter_button.pack(pady=5)

def download_all_papers(subject_code, year, season):
    paper_codes = ["11", "12", "13", "21", "22", "23", "31", "32", "33", "41", "42", "43"]
    for paper_code in paper_codes:
        download_paper(subject_code, year, season, paper_code)

def display_paper_options(subject_code, year, season):
    clear_frame()

    # Back button
    back_button = ctk.CTkButton(
        frame,
        text="← Go Back",
        command=lambda: display_year_options(subject_code),
        fg_color="#1F4A3C",
        hover_color="#2F6B5C",
        width=100
    )
    back_button.pack(anchor="nw", padx=10, pady=10)

    # Top container for buttons
    top_container = ctk.CTkFrame(frame, fg_color="transparent")
    top_container.pack(fill="x", padx=20, pady=10)

    # Paper type selector
    paper_type_var = tk.StringVar(value="all")
    paper_type_frame = ctk.CTkFrame(top_container, fg_color="#2F6B5C", corner_radius=10)
    paper_type_frame.pack(side="left", padx=10)
    
    ctk.CTkLabel(paper_type_frame, text="Filter Papers:", text_color="white").pack(side="left", padx=10)
    
    paper_types = [("All", "all"), ("Paper 1", "1"), ("Paper 2", "2"), ("Paper 3", "3"), ("Paper 4", "4")]
    for label, value in paper_types:
        ctk.CTkRadioButton(
            paper_type_frame,
            text=label,
            value=value,
            variable=paper_type_var,
            command=lambda: update_paper_list(papers_frame, subject_code, year, season, paper_type_var.get()),
            fg_color="white",
            text_color="white"
        ).pack(side="left", padx=10)

    # Download All button
    download_all_button = ctk.CTkButton(
        top_container,
        text="Download All Papers",
        command=lambda: download_filtered_papers(subject_code, year, season, paper_type_var.get()),
        fg_color="#1F4A3C",
        hover_color="#2F6B5C",
        width=200
    )
    download_all_button.pack(side="right", padx=10)

    # Create scrollable frame for papers
    papers_frame = ctk.CTkScrollableFrame(frame, width=400, height=400)
    papers_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Initial paper list
    update_paper_list(papers_frame, subject_code, year, season, "all")

def update_paper_list(papers_frame, subject_code, year, season, paper_type):
    # Clear existing papers
    for widget in papers_frame.winfo_children():
        widget.destroy()
    
    year_suffix = year[-2:]
    paper_codes = get_filtered_paper_codes(paper_type)
    
    for paper_code in paper_codes:
        paper_frame = ctk.CTkFrame(papers_frame, fg_color="transparent")
        paper_frame.pack(pady=5, fill="x")

        paper_label = ctk.CTkLabel(
            paper_frame,
            text=f"Paper {paper_code}",
            font=("Arial", 14)
        )
        paper_label.pack(side="left", padx=10)

        download_button = ctk.CTkButton(
            paper_frame,
            text=f"Download {subject_code}_{season}{year_suffix}_qp_{paper_code}.pdf",
            command=lambda pc=paper_code: download_paper(subject_code, year, season, pc),
            fg_color="#2F6B5C",
            hover_color="#1F4A3C"
        )
        download_button.pack(side="right", padx=10)

def get_filtered_paper_codes(paper_type):
    if paper_type == "all":
        return ["11", "12", "13", "21", "22", "23", "31", "32", "33", "41", "42", "43"]
    else:
        return [f"{paper_type}1", f"{paper_type}2", f"{paper_type}3"]

def download_filtered_papers(subject_code, year, season, paper_type):
    paper_codes = get_filtered_paper_codes(paper_type)
    for paper_code in paper_codes:
        download_paper(subject_code, year, season, paper_code)

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

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

def display_subjects():
    subjects_frame = ctk.CTkScrollableFrame(frame, width=800, height=500)
    subjects_frame.pack(fill="both", expand=True, padx=20, pady=20)

    grid_frame = ctk.CTkFrame(subjects_frame, fg_color="transparent")
    grid_frame.pack(fill="both", expand=True)

    cols = 3
    for i, (subject, code) in enumerate(subjects):
        subject_button = ctk.CTkButton(
            grid_frame,
            text=f"{subject}\n{code}",
            command=lambda c=code: on_subject_click(c),
            width=200,
            height=80,
            fg_color="#2F6B5C",
            hover_color="#1F4A3C",
            font=("Arial", 14)
        )
        subject_button.grid(
            row=i//cols,
            column=i%cols,
            padx=10,
            pady=10,
            sticky="nsew",
        )

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

# Initialize the GUI
root = ctk.CTk()
root.title("A-Level Papers Downloader")
root.geometry("900x600")

frame = ctk.CTkFrame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

create_logo_frame(frame)  # Add logo frame
display_subjects()  # Initial display of subjects

root.mainloop()