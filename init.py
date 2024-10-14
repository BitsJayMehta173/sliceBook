import tkinter as tk
import re

with open('text.txt', 'r') as file:
    data = file.read()
    sentences = re.split(r'(?<=[.!?]) +', data)


root = tk.Tk()
root.title("SliceBook")

# Set the window size (width x height)
original_size = "800x400"
root.geometry(original_size)

# Variables to track the current sentence and word indices
current_sentence_idx = 0
current_word_idx = 0

# Function to update the display with the current sentence and highlighted word
def update_display():
    # Split the current sentence into words
    sentence_words = sentences[current_sentence_idx].split()
    # Highlight the current word by adding a green background
    highlighted_sentence = ""
    for i, word in enumerate(sentence_words):
        if i == current_word_idx:
            highlighted_sentence += f" [ {word} ] "  # Adding special formatting for the highlighted word
        else:
            highlighted_sentence += f" {word} "
    
    # Update the label with the formatted sentence
    sentence_label.config(text=highlighted_sentence.strip(), bg="white", font=('Helvetica', 18))

# Function to go to the next word in the sentence
def next_word(event=None):
    global current_word_idx, current_sentence_idx
    # Check if the current word is the last one in the sentence
    if current_word_idx < len(sentences[current_sentence_idx].split()) - 1:
        current_word_idx += 1
    else:
        # Move to the next sentence if available
        if current_sentence_idx < len(sentences) - 1:
            current_sentence_idx += 1
            current_word_idx = 0  # Reset word index for the new sentence
    update_display()

# Function to go to the previous word in the sentence
def prev_word(event=None):
    global current_word_idx, current_sentence_idx
    # Check if the current word is the first one in the sentence
    if current_word_idx > 0:
        current_word_idx -= 1
    else:
        # Move to the previous sentence if available
        if current_sentence_idx > 0:
            current_sentence_idx -= 1
            current_word_idx = len(sentences[current_sentence_idx].split()) - 1  # Go to the last word of the previous sentence
    update_display()

# Create the label to display sentences and highlighted words
sentence_label = tk.Label(root, text="", bg="white", font=('Helvetica', 18), padx=20, pady=50)
sentence_label.pack(expand=True, fill=tk.BOTH)

# Create navigation buttons
prev_button = tk.Button(root, text="Previous Word", command=prev_word, font=('Helvetica', 18))
prev_button.pack(side=tk.LEFT, padx=50, pady=20)

next_button = tk.Button(root, text="Next Word", command=next_word, font=('Helvetica', 18))
next_button.pack(side=tk.RIGHT, padx=50, pady=20)

# Bind left and right arrow keys to navigate words
root.bind("<Left>", prev_word)
root.bind("<Right>", next_word)

# Initialize by displaying the first sentence
update_display()

# Start tkinter event loop
root.mainloop()
