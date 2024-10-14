import tkinter as tk

with open('text.txt', 'r') as file:
    data = file.read()
    words = data.split()

root = tk.Tk()
root.title("Word Slider")

# Set the window size (width x height)
original_size = "800x400"  # Store the original window size
root.geometry(original_size)

# Variable to track the current word index and full view mode
current_word_idx = 0
full_view_enabled = False

# Function to update the label with the current word
def update_word():
    if not full_view_enabled:
        word_label.config(text=words[current_word_idx])

# Function to display all text at once with word wrapping
def show_full_data():
    text_widget.delete(1.0, tk.END)  # Clear existing text
    text_widget.insert(tk.END, data)  # Insert full data
    text_widget.config(state=tk.DISABLED)  # Make the text widget read-only

# Function to go to the next word
def next_word(event=None):
    global current_word_idx
    if current_word_idx < len(words) - 1:
        current_word_idx += 1
        update_word()

# Function to go to the previous word
def prev_word(event=None):
    global current_word_idx
    if current_word_idx > 0:
        current_word_idx -= 1
        update_word()

# Function to toggle full view on and off, with full screen mode
def toggle_full_view():
    global full_view_enabled
    full_view_enabled = not full_view_enabled
    if full_view_enabled:
        root.attributes("-fullscreen", True)  # Enable full-screen mode
        show_full_data()
        toggle_button.config(text="Disable Full View")
        prev_button.config(state=tk.DISABLED)  # Disable navigation buttons
        next_button.config(state=tk.DISABLED)
        text_widget.pack(expand=True, fill=tk.BOTH)  # Show text widget
        word_label.pack_forget()  # Hide word label
    else:
        root.attributes("-fullscreen", False)  # Exit full-screen mode
        root.geometry(original_size)  # Return to original window size
        update_word()
        toggle_button.config(text="Enable Full View")
        prev_button.config(state=tk.NORMAL)  # Enable navigation buttons
        next_button.config(state=tk.NORMAL)
        text_widget.pack_forget()  # Hide text widget
        word_label.pack(expand=True)  # Show word label again

# Create the label to display words
word_label = tk.Label(root, text=words[current_word_idx], font=('Helvetica', 36), padx=20, pady=50)
word_label.pack(expand=True)

# Create navigation buttons
prev_button = tk.Button(root, text="Previous", command=prev_word, font=('Helvetica', 18))
prev_button.pack(side=tk.LEFT, padx=50, pady=20)

next_button = tk.Button(root, text="Next", command=next_word, font=('Helvetica', 18))
next_button.pack(side=tk.RIGHT, padx=50, pady=20)

# Create toggle full view button
toggle_button = tk.Button(root, text="Enable Full View", command=toggle_full_view, font=('Helvetica', 18))
toggle_button.pack(side=tk.BOTTOM, pady=20)

# Create a Text widget for displaying full data
text_widget = tk.Text(root, wrap=tk.WORD, font=('Helvetica', 18))  # Enable word wrapping
text_widget.pack(expand=True, fill=tk.BOTH)  # Allow the text widget to fill the space
text_widget.pack_forget()  # Hide the text widget initially

# Bind left and right arrow keys to navigate words
root.bind("<Left>", prev_word)
root.bind("<Right>", next_word)

# Start tkinter event loop
root.mainloop()
