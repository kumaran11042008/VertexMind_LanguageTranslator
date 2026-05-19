from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Main Window
root = Tk()
root.title("AI Language Translator")
root.geometry("750x550")
root.config(bg="#f0f0f0")

# Title
title = Label(
    root,
    text="AI Language Translation Tool",
    font=("Arial", 22, "bold"),
    bg="#f0f0f0",
    fg="blue"
)
title.pack(pady=15)

# Input Label
input_label = Label(
    root,
    text="Enter Text",
    font=("Arial", 13),
    bg="#f0f0f0"
)
input_label.pack()

# Input Text Box
input_text = Text(
    root,
    height=8,
    width=70,
    font=("Arial", 12)
)
input_text.pack(pady=10)

# Language List
languages = [
    "english",
    "tamil",
    "hindi",
    "french",
    "german",
    "japanese",
    "korean",
    "telugu",
    "malayalam",
    "spanish"
]

# Source Language
source_label = Label(
    root,
    text="Source Language",
    font=("Arial", 12),
    bg="#f0f0f0"
)
source_label.pack()

source_lang = ttk.Combobox(
    root,
    values=languages,
    width=30,
    font=("Arial", 11)
)
source_lang.pack()
source_lang.set("english")

# Target Language
target_label = Label(
    root,
    text="Target Language",
    font=("Arial", 12),
    bg="#f0f0f0"
)
target_label.pack()

target_lang = ttk.Combobox(
    root,
    values=languages,
    width=30,
    font=("Arial", 11)
)
target_lang.pack()
target_lang.set("tamil")

# Translate Function
def translate_text():
    try:
        text = input_text.get(1.0, END).strip()

        if text == "":
            messagebox.showwarning("Warning", "Please enter some text")
            return

        translated = GoogleTranslator(
            source=source_lang.get(),
            target=target_lang.get()
        ).translate(text)

        output_text.delete(1.0, END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Translate Button
translate_btn = Button(
    root,
    text="Translate",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    padx=15,
    pady=5,
    command=translate_text
)

translate_btn.pack(pady=20)

# Output Label
output_label = Label(
    root,
    text="Translated Text",
    font=("Arial", 13),
    bg="#f0f0f0"
)
output_label.pack()

# Output Text Box
output_text = Text(
    root,
    height=8,
    width=70,
    font=("Arial", 12)
)
output_text.pack(pady=10)

# Run Application
root.mainloop()