import tkinter as tk
import re

# Load the text from the file and split it into sentences
with open('text.txt', 'r') as file:
    data = file.read()
    sentences = re.split(r'(?<=[.!?]) +', data)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Sentence Viewer with Word Highlighting")

# Set the window to full screen
root.attributes('-fullscreen', True)

# Variables to track the current sentence and word indices
current_sentence_idx = 0
current_word_idx = 0

# Create the Text widget for displaying sentences and highlighting words
sentence_text = tk.Text(root, bg="lightgreen", font=('Helvetica', 18), wrap=tk.WORD)
sentence_text.pack(expand=True, fill=tk.BOTH)
sentence_text.config(state=tk.DISABLED)  # Make it read-only

# Function to update the display with the current sentence and highlighted word
def update_display():
    sentence_text.config(state=tk.NORMAL)  # Make it editable temporarily
    sentence_text.delete(1.0, tk.END)  # Clear the text widget
    
    # Split the current sentence into words
    sentence_words = sentences[current_sentence_idx].split()
    
    # Highlight the current word
    for i, word in enumerate(sentence_words):
        if i == current_word_idx:
            sentence_text.insert(tk.END, f" {word} ", ('highlighted',))
        else:
            sentence_text.insert(tk.END, f" {word} ")
    
    sentence_text.tag_config('highlighted', foreground='red')  # Set color for highlighted word
    sentence_text.config(state=tk.DISABLED)  # Make it read-only again

# Function to go to the next word in the sentence
def next_word(event=None):
    global current_word_idx, current_sentence_idx
    if current_word_idx < len(sentences[current_sentence_idx].split()) - 1:
        current_word_idx += 1
    else:
        if current_sentence_idx < len(sentences) - 1:
            current_sentence_idx += 1
            current_word_idx = 0  # Reset word index for the new sentence
    update_display()

# Function to go to the previous word in the sentence
def prev_word(event=None):
    global current_word_idx, current_sentence_idx
    if current_word_idx > 0:
        current_word_idx -= 1
    else:
        if current_sentence_idx > 0:
            current_sentence_idx -= 1
            current_word_idx = len(sentences[current_sentence_idx].split()) - 1  # Go to the last word of the previous sentence
    update_display()

# Function to go to the next sentence
def next_sentence(event=None):
    global current_sentence_idx, current_word_idx
    if current_sentence_idx < len(sentences) - 1:
        current_sentence_idx += 1
        current_word_idx = 0  # Reset word index for the new sentence
    update_display()

# Function to go to the previous sentence
def prev_sentence(event=None):
    global current_sentence_idx, current_word_idx
    if current_sentence_idx > 0:
        current_sentence_idx -= 1
        current_word_idx = 0  # Reset word index for the previous sentence
    update_display()

# Function to exit full-screen mode
def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)  # Add padding for better layout

# Create navigation buttons within the frame
prev_sentence_button = tk.Button(button_frame, text="Previous Sentence", command=prev_sentence, font=('Helvetica', 18))
prev_sentence_button.pack(side=tk.LEFT, padx=10)

next_sentence_button = tk.Button(button_frame, text="Next Sentence", command=next_sentence, font=('Helvetica', 18))
next_sentence_button.pack(side=tk.RIGHT, padx=10)

prev_word_button = tk.Button(button_frame, text="Previous Word", command=prev_word, font=('Helvetica', 18))
prev_word_button.pack(side=tk.LEFT, padx=10)

next_word_button = tk.Button(button_frame, text="Next Word", command=next_word, font=('Helvetica', 18))
next_word_button.pack(side=tk.RIGHT, padx=10)

# Bind left and right arrow keys to navigate words
root.bind("<Left>", prev_word)
root.bind("<Right>", next_word)

# Bind the Escape key to exit full-screen mode
root.bind("<Escape>", toggle_fullscreen)

# Initialize by displaying the first sentence
update_display()

# Start the Tkinter event loop
root.mainloop()
