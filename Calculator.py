import tkinter as tk

# Animation Functions
def type_text(widget, text, idx=0):
    """Typing animation for display"""
    if idx <= len(text):
        display_var.set(text[:idx])
        idx += 1
        widget.after(50, lambda: type_text(widget, text, idx))

def animate_buttons():
    """Slide-in animation for buttons"""
    for i, btn in enumerate(all_buttons):
        btn.place(x=-100, y=btn_positions[i][1])
        slide_in(btn, btn_positions[i][0], btn_positions[i][1])

def slide_in(widget, target_x, y, step=10):
    x = widget.winfo_x()
    if x < target_x:
        x += step
        widget.place(x=x, y=y)
        root.after(20, lambda: slide_in(widget, target_x, y))
    else:
        widget.place(x=target_x, y=y)

# Calculator Functions 
    def press(key):
    if key == "=":
        try:
            result = str(eval(display_var.get()))
            type_text(display_entry, result)
        except:
            type_text(display_entry, "Error")
    elif key == "C":
        display_var.set("")
    else:
        display_var.set(display_var.get() + key)

# Tkinter Setup 
root = tk.Tk()
root.title("Hafsa Hammadh's Calculator")
root.geometry("420x580")
root.config(bg="#1e1e2f")

# Box Border 
border_box = tk.Frame(root, bg="white", bd=3, relief="solid")
border_box.place(x=15, y=15, width=390, height=540)

display_var = tk.StringVar()

# Welcome Label
welcome_label = tk.Label(border_box, text="Welcome to Hafsa's Calculator!",
                         font=("Arial", 16, "bold"), fg="#ffffff", bg="#1e1e2f")
welcome_label.place(x=20, y=10)

# Fade-in effect
alpha = 0
def fade_in_label():
    global alpha
    alpha += 0.05
    if alpha <= 1:
        welcome_label.config(fg=f"#{int(255*alpha):02x}{int(255*alpha):02x}{int(255*alpha):02x}")
        root.after(100, fade_in_label)

fade_in_label()

# Display Entry
display_entry = tk.Entry(border_box, textvariable=display_var, font=("Arial", 24),
                         bd=0, bg="#2e2e3e", fg="white", justify="right")
display_entry.place(x=15, y=60, width=350, height=50)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

all_buttons = []
btn_positions = []

start_y = 130
btn_width = 80
btn_height = 60
spacing = 10

# Create buttons
for i, row in enumerate(buttons):
    for j, key in enumerate(row):
        x = 15 + j * (btn_width + spacing)
        y = start_y + i * (btn_height + spacing)
        b = tk.Button(border_box, text=key, font=("Arial", 20), bg="#3e3e5e", fg="white",
                      activebackground="#5e5e7e", activeforeground="white", bd=0,
                      command=lambda k=key: press(k))
        all_buttons.append(b)
        btn_positions.append((x, y))

# Start button animation
root.after(500, animate_buttons)

root.mainloop()
