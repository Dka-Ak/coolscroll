import tkinter as tk
from tkinter import messagebox

# Questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Rome", "Berlin"],
        "correct": 0
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answers": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct": 1
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "answers": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Jane Austen"],
        "correct": 0
    }
]

# Game variables
current_question_index = 0
score = 0
coins = 0

# Functions
def start_game():
    global current_question_index, score, coins
    current_question_index = 0
    score = 0
    coins = 0
    score_label.config(text=f"Score: {score}")
    coins_label.config(text=f"Coins: {coins}")
    next_button.config(text="Next Question")
    show_question()

def show_question():
    global current_question_index
    reset_state()
    current_question = questions[current_question_index]
    question_label.config(text=current_question["question"])
    for i, answer in enumerate(current_question["answers"]):
        answer_buttons[i].config(text=answer, command=lambda i=i: select_answer(i))

def reset_state():
    for button in answer_buttons:
        button.config(bg="SystemButtonFace")

def select_answer(index):
    global current_question_index, score, coins
    current_question = questions[current_question_index]
    if index == current_question["correct"]:
        score += 1
        coins += 1
        score_label.config(text=f"Score: {score}")
        coins_label.config(text=f"Coins: {coins}")
        answer_buttons[index].config(bg="green")
    else:
        answer_buttons[index].config(bg="red")
    if current_question_index < len(questions) - 1:
        next_button.config(state=tk.NORMAL)
    else:
        next_button.config(text="Restart", state=tk.NORMAL)

def next_question():
    global current_question_index
    current_question_index += 1
    if current_question_index < len(questions):
        show_question()
    else:
        start_game()

def purchase_item(item, cost):
    global coins
    if coins >= cost:
        coins -= cost
        coins_label.config(text=f"Coins: {coins}")
        messagebox.showinfo("Purchase", f"Purchased {item}!")
    else:
        messagebox.showwarning("Error", "Not enough coins!")

# GUI setup
window = tk.Tk()
window.title("Quiz Game with Rewards")

# Widgets
question_label = tk.Label(window, text="Question text", font=("Arial", 16))
question_label.pack(pady=20)

answer_buttons = []
for i in range(4):
    button = tk.Button(window, text=f"Answer {i + 1}", font=("Arial", 14), width=20)
    button.pack(pady=5)
    answer_buttons.append(button)

next_button = tk.Button(window, text="Next Question", font=("Arial", 14), state=tk.DISABLED, command=next_question)
next_button.pack(pady=20)

score_label = tk.Label(window, text="Score: 0", font=("Arial", 14))
score_label.pack(pady=5)

coins_label = tk.Label(window, text="Coins: 0", font=("Arial", 14))
coins_label.pack(pady=5)

store_label = tk.Label(window, text="Store", font=("Arial", 16))
store_label.pack(pady=10)

store_items = [("Extra Time", 10), ("Hint", 5), ("Skip Question", 15)]
for item, cost in store_items:
    button = tk.Button(window, text=f"{item} ({cost} coins)", font=("Arial", 14), command=lambda item=item, cost=cost: purchase_item(item, cost))
    button.pack(pady=5)

# Start the game
start_game()

window.mainloop()

