from hackathon import legalese_ui  # Ensure this is imported correctly
import tkinter as tk
from tkinter import ttk
import webbrowser

def open_url(url):
    """Open the given URL in the default web browser."""
    webbrowser.open_new(url)

def create_ui():
    # Initialize the main window
    root = tk.Tk()
    root.title("Legaleze Assistance")
    root.state("zoomed")  # Open in fullscreen
    root.configure(bg="#F9F0EE")

    # Title Label
    title_label = tk.Label(root, text="Legaleze - The Legal Assistance Application", font=("Times New Roman", 35, "bold"), bg="#F9F0EE")
    title_label.pack(pady=5)

    # Subtitle Label
    subtitle_label = tk.Label(
        root,
        text="Make your life easier with Legaleze",
        font=("Arial", 14),
        bg="#F9F0EE",
    )
    subtitle_label.pack(pady=3)

    # Description Label
    description_label = tk.Label(
        root,
        text='''
        Are you finding it challenging to manage legal documents? 
        we are here to simplify the process.  
        Legaleze is an innovative platform designed to streamline the handling of legal paperwork. 
        Our platform is designed to help you understand, review, and manage legal documents. Here are some of the functionalities:
        ''',
        wraplength=1200,
        font=("Arial", 13),
        bg="#F9F0EE",
    )
    description_label.pack(pady=10)
    
    separator = ttk.Separator(root, orient="horizontal")
    separator.pack(fill="x", pady=2)  # Fills the horizontal space

    # Frame for buttons
    frame = tk.Frame(root, bg="#F9F0EE")
    frame.pack(pady=10, fill="both", expand=True)

    # Functionality Buttons
    functionalities = [
        ("OCR", "Harness the power of advanced OCR to extract text from scanned multilingual legal documents with exceptional accuracy. This tool seamlessly converts printed or handwritten text into editable English, enabling fast and efficient document digitization, even for large volumes of records."),
        ("NLP", "Let our NLP engine simplify the overwhelming complexity of legalese. This feature automatically detects and identifies essential details such as key clauses, names of involved parties, important dates, and contextual information. Save time by avoiding manual searches and ensure critical insights are always within reach."),
        ("Automated Clause Identification", "Lengthy legal documents can be daunting, but our platform makes them manageable by instantly locating and highlighting the most important clauses. Whether it's terms of agreement, indemnity clauses, or liability statements, you can pinpoint what matters most without wasting hours searching through pages."),
        ("Document Identification", "Eliminate confusion with our robust document tagging and categorization system. By intelligently segmenting legal documents, this feature ensures that different types of files are instantly recognizable, accurately organized, and readily accessible whenever needed. Stay efficient and stress-free with our streamlined approach"),
        ("Plain Language Translation", "Legal jargon can be challenging to navigate, but with our plain language translation feature, you can transform complex legal terminologies into simple, easy-to-understand text. Empower decision-making by breaking down sophisticated clauses into concise and actionable insights."),
        ("Plain Language Summaries", "For those needing a quick overview, our plain language summarization tool condenses detailed legal documents into short, clear summaries. This ensures you grasp the essence of the content without delving into the full document, saving valuable time and effort."),
    ]

    for i, (title, description) in enumerate(functionalities):
        button_frame = tk.Frame(frame, bg="#FBE4DB", highlightbackground="gray", highlightthickness=1)
        button_frame.grid(row=i//3, column=i%3, padx=20, pady=20, sticky="nsew")
        
        icon_label = tk.Label(button_frame, text="\u25A9", font=("Arial", 24), bg="#FBE4DB")  # Placeholder for icon
        icon_label.pack()

        title_label = tk.Label(button_frame, text=title, font=("Arial", 14, "bold"), bg="#FBE4DB")
        title_label.pack()

        description_label = tk.Label(button_frame, text=description, font=("Arial", 12), bg="#FBE4DB", wraplength=400)
        description_label.pack()

    # Configure rows and columns to expand
    for i in range(2):
        frame.rowconfigure(i, weight=1)
    for j in range(3):
        frame.columnconfigure(j, weight=1)

    # Get Started Button (with legalese_ui function call and destroying create_ui window)
    get_started_button = tk.Button(
        root, text="Get Started", font=("Arial", 12, "bold"), bg="#A86254", fg="white", padx=20, pady=5,
        command=lambda: (root.destroy(), legalese_ui())  # Destroy current window and call legalese_ui
    )
    get_started_button.pack(pady=20)

    # Footer
    footer_frame = tk.Frame(root, bg="#F9F0EE")
    footer_frame.pack(pady=10)

    # URLs for each label
    footer_links = {
        "My Resume": "https://drive.google.com/file/d/1yxXucZIxTqgCons7HOgQ7TgQtALdt8e7/view?usp=sharing",
        "Github": "https://github.com/nikhil8424",
        "Linkdin": "https://www.linkedin.com/in/nikhil-gupta-6b7705288/",
        "GDPR Compliance": "https://example.com/gdpr-compliance",
    }

    # Create clickable labels
    for text, url in footer_links.items():
        label = tk.Label(footer_frame, text=text, font=("Arial", 11), bg="#FBE4DB", fg="black", cursor="hand2")
        label.pack(side="left", padx=10)
        label.bind("<Button-1>", lambda e, url=url: open_url(url))

    # Copyright label
    copyright_label = tk.Label(
        root, text="Legaleze Assistance © 2023", font=("Arial", 10), bg="#FBE4DB", fg="black"
    )
    copyright_label.pack(pady=5)

    # Main loop
    root.mainloop()

if __name__ == "__main__":
    create_ui()
