from tkinter import *
import random

# Define fun messages and relationship tips based on score ranges
MESSAGES_AND_TIPS = {
    "high": {
        "message": [
            "You're a perfect match! \U0001F495",
            "This could be your soulmate! \U0001F60D",
            "True love is in the air! \U0001F339",
            "You are destined for each other! \U0001F48F",
            "Keep shining together! \U0001F308"
        ],
        "tips": [
            "Plan a surprise date to make your bond stronger.",
            "Always appreciate each other’s efforts, big or small.",
            "Be kind, be patient, and keep communicating openly.",
            "Cherish the little moments together; they matter the most.",
            "Trust and honesty are the foundation of lasting love."
        ]
    },
    "medium": {
        "message": [
            "You're doing great! \U0001F60A",
            "Pretty good compatibility! Keep it up! \U0001F4AA",
            "There’s a strong bond here! \U0001F49E",
            "A wonderful connection is building! \U0001F618",
            "Keep nurturing your relationship! \U0001F49C"
        ],
        "tips": [
            "Spend quality time together to strengthen your bond.",
            "Learn each other's love languages for better understanding.",
            "Celebrate your differences; they make you unique as a couple.",
            "Find shared hobbies or activities you can enjoy together.",
            "A small act of kindness every day goes a long way."
        ]
    },
    "low": {
        "message": [
            "It’s a bit rocky, but don’t lose hope! \U0001F914",
            "Love takes effort, keep trying! \U0001F64F",
            "Start with friendship first; it’s the best foundation. \U0001F91D",
            "There’s potential; focus on understanding each other. \U0001F642",
            "Patience is key; give it time. \U0001F550"
        ],
        "tips": [
            "Be open to understanding each other’s perspectives.",
            "Start by building a strong friendship; love may follow.",
            "Talk openly about what matters most to each of you.",
            "Respect each other’s space and individuality.",
            "Love grows with time, kindness, and shared experiences."
        ]
    }
}

# Function to calculate love percentage
def calculate_love():
    name1_text = name1.get().strip()
    name2_text = name2.get().strip()

    if not name1_text or not name2_text:
        result.config(text="Please enter both names!", fg="red")
        return

    # Calculate love percentage based on names
    combined_names = name1_text.lower() + name2_text.lower()
    love_score = sum(ord(char) for char in combined_names) % 100

    # Select appropriate message and tip
    if love_score > 80:
        category = "high"
    elif love_score > 50:
        category = "medium"
    else:
        category = "low"

    message = random.choice(MESSAGES_AND_TIPS[category]["message"])
    tip = random.choice(MESSAGES_AND_TIPS[category]["tips"])

    # Display the result with the fun message and tip
    result.config(
        text=f"Love Percentage: {love_score}%\n\n{message}\n\nTip: {tip}",
        fg="black"
    )

# Function to reset the input fields and result
def reset_fields():
    name1.delete(0, END)
    name2.delete(0, END)
    result.config(text="Love Percentage between both of You:", fg="black")

# Creating GUI window
root = Tk()
root.geometry('530x440')
root.title('Love Calculator ❤️')

# Heading on Top
heading = Label(
    root, 
    text='🧮The Love Algorithm:Find Your Compatibility Score!💘', 
    font=("Helvetica", 14, "bold"),  # Change the font style and size
    fg="white",  # Set text color to white
    bg="black"   # Set background color to black
)
heading.pack(pady=15)


# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:", font=("Arial", 12, "bold"))
slot1.pack()
name1 = Entry(root, border=5, font=("Arial", 12))
name1.pack(pady=5)

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Partner's Name:", font=("Arial", 12, "bold"))
slot2.pack()
name2 = Entry(root, border=5, font=("Arial", 12))
name2.pack(pady=5)

# Buttons for calculation and reset
bt = Button(root, text="Calculate", height=1, width=10, command=calculate_love, bg="lightgreen", font=("Arial", 12))
bt.pack(pady=15)

reset_btn = Button(root, text="Reset", height=1, width=10, command=reset_fields, bg="lightcoral", font=("Arial", 12))
reset_btn.pack(pady=5)

# Text on result slot
result = Label(
    root, 
    text='Love Percentage between both of You:', 
    font=("Arial", 12, "italic"), 
    wraplength=450, 
    justify="center"
)
result.pack(pady=20)

# Starting the GUI
root.mainloop()



