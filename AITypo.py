import openai
openai.api_key = None
print("API Key cleared")
import sys
import os
import pyperclip
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk
import webbrowser

print("Script started")

# Constants and Configurations
API_KEY_FILE = 'api_key.txt'
ENGINE_NAME = 'text-davinci-002'
MAX_TOKENS = 150

# Flag to indicate if the API key window is open
api_key_window_open = False  

# Variables to track clipboard changes
original_clipboard_content = pyperclip.paste()
edited_content = original_clipboard_content

# Function to open the OpenAI API website
def open_api_website():
    webbrowser.open('https://platform.openai.com/docs/overview')

# Function to display API key entry window
def show_api_key_entry_window():
    global api_key_window_open
    print("Trying to show API key entry window")
    if api_key_window_open:
        return  # Avoid opening a new window if one is already open

    api_key_window_open = True
    
    def save_api_key():
        global api_key_window_open
        api_key = api_key_entry.get().strip()
        if api_key:
            try:
                with open(API_KEY_FILE, 'w') as file:
                    file.write(api_key)
                messagebox.showinfo("API Key Saved", "Your API key has been saved.")
                api_key_window_open = False  # Reset the flag when the window is closed
                api_key_window.destroy()
                openai.api_key = api_key  # Re-initialize the API to ensure the key is set
            except Exception as e:
                messagebox.showerror("Error", f"Error saving API key: {e}")
        else:
            messagebox.showwarning("Warning", "No API key entered.")

    api_key_window = tk.Toplevel(window)
    api_key_window.title("Enter OpenAI API Key")

    instructions_text = (
        "To obtain your OpenAI API key, sign in or create an account on the OpenAI website, "
        "then navigate to the API section to generate your key. Enter the key below."
    )
    instructions = tk.Label(api_key_window, text=instructions_text, wraplength=400)
    instructions.pack(pady=10)

    open_website_button = tk.Button(api_key_window, text="Open OpenAI Website", command=open_api_website)
    open_website_button.pack(pady=5)

    api_key_entry = tk.Entry(api_key_window, width=50)
    api_key_entry.pack(pady=10)

    save_button = tk.Button(api_key_window, text="Save API Key", command=save_api_key)
    save_button.pack(pady=10)

# Function to read API key from a file
def get_api_key(file_path):
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return None  # Return None if the API key file is missing or empty
    with open(file_path, 'r') as file:
        return file.read().strip()

# Function to initialize OpenAI API
def initialize_openai_api():
    print("Initializing OpenAI API")
    show_api_key_entry_window()

# Initialize Tkinter window
window = ThemedTk(theme="arc")
window.title("Text Correction with OpenAI")
print("Tkinter window initialized")

# Delay the initialization of OpenAI API
window.after(100, initialize_openai_api)

# Function to process text with OpenAI
def process_text(text):
    try:
        prompt = f"Please correct only the grammatical errors in the following text in New Zealand English, and do not add or infer any additional content:\n\n{text}"
        response = openai.Completion.create(
            engine=ENGINE_NAME,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=0.1,
            frequency_penalty=0.5
        )
        corrected_text = response.choices[0].text.strip()
        return corrected_text
    except Exception as e:
        print(f"Error processing text with OpenAI: {e}")
        return None

# Function to copy text to clipboard
def copy_to_clipboard(text):
    try:
        current_clipboard_content = pyperclip.paste()
        new_clipboard_content = text if not current_clipboard_content else current_clipboard_content + "\n" + text
        pyperclip.copy(new_clipboard_content)
        print("Corrected text appended to clipboard.")
    except Exception as e:
        print(f"Error appending text to clipboard: {e}")

# Function to process text, update the GUI, and clear the input box
def process_and_update_gui(event=None):
    global edited_content
    input_text = input_text_entry.get()
    corrected_text = process_text(input_text)
    if corrected_text:
        copy_to_clipboard(corrected_text)  # Append corrected text to the clipboard
        clipboard_content = pyperclip.paste()  # Get full clipboard content
        output_text.delete("1.0", tk.END)  # Clear the output text
        output_text.insert(tk.END, clipboard_content)  # Display updated clipboard content
        edited_content = clipboard_content  # Track edited content
        input_text_entry.delete(0, tk.END)  # Clear the input text box
        save_button.config(state="normal")  # Enable the "Save Changes" button

# Function to clear the clipboard and output text
def clear_clipboard():
    global edited_content
    edited_content = ''
    pyperclip.copy('')  # Clear the clipboard
    if output_text:  # Check if output_text widget is defined
        output_text.delete("1.0", tk.END)  # Clear the output text

# Function to save changes to the clipboard
def save_changes():
    global edited_content, original_clipboard_content
    edited_content = output_text.get("1.0", tk.END).strip()
    pyperclip.copy(edited_content)  # Copy edited content to the clipboard
    original_clipboard_content = edited_content  # Update original clipboard content
    save_button.config(state="disabled")  # Disable the "Save Changes" button
    messagebox.showinfo("Saved", "Changes have been saved to the clipboard.")

# Function to handle exiting and prompt for clearing or keeping clipboard content
def exit_app():
    global edited_content
    if edited_content != original_clipboard_content:
        response = messagebox.askquestion("Exit", "Do you want to clear the clipboard before exiting?")
        if response == "yes":
            clear_clipboard()
    sys.exit(0)

# Create and configure GUI elements
input_text_label = ttk.Label(window, text="Enter text to correct:")
input_text_entry = ttk.Entry(window, width=50)
output_text = tk.Text(window, wrap=tk.WORD, height=10, width=50)
clear_button = ttk.Button(window, text="Clear Clipboard", command=clear_clipboard)
save_button = ttk.Button(window, text="Save Changes", command=save_changes, state="disabled")
exit_button = ttk.Button(window, text="Exit", command=exit_app)

# Arrange GUI elements using grid layout
input_text_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_text_entry.grid(row=0, column=1, padx=10, pady=10)
output_text.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
clear_button.grid(row=2, column=0, padx=10, pady=10)
save_button.grid(row=2, column=1, padx=10, pady=10)
exit_button.grid(row=2, column=2, padx=10, pady=10)

# Bind the Enter key to the process_and_update_gui function
input_text_entry.bind("<Return>", process_and_update_gui)

# Call clear_clipboard to clear any previous clipboard content before starting
clear_clipboard()

# Delay API initialization until after the mainloop has started
#window.after(100, initialize_openai_api)

# Start the GUI event loop
print("Starting Tkinter mainloop")
window.mainloop()
print("Tkinter mainloop ended")
