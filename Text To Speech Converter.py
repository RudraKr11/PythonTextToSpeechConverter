# Creating A Text To Speech Converter
import tkinter as tk
import pyttsx3

def speak_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

engine = pyttsx3.init()

root = tk.Tk()
root.title("Text to Speech")
root.geometry("300x200")
root.configure(bg="#2E2E2E")

text_entry = tk.Text(root, height=6, width=30, font=("Arial Black", 10), wrap=tk.WORD,
                     bg="#FFFFFF", fg="#2E2E2E", bd=2, relief=tk.GROOVE)
text_entry.pack(pady=10, padx=10)

speak_button = tk.Button(root, text="Speak", command=speak_text,
                         font=("Arial Black", 12), bg="#BDA55D", fg="white",
                         padx=8, pady=5, relief=tk.RAISED)
speak_button.pack(pady=5)

label = tk.Label(root, text="Enter text and click 'Speak'", font=("Arial Black", 10),
                 bg="#2E2E2E", fg="#BDA55D")
label.pack(pady=5)

root.mainloop()
