# Homework: Simulated Navigation Task
# Subject: Introduction to AIML

# Step-by-step instructions for visiting Chanakya University website

steps = [
    "1. Open the homepage: https://chanakyauniversity.in/",
    "2. Scroll and click on 'Programs' or 'Acquire' (whichever is shown).",
    "3. From the menu, click on 'Undergraduate Programmes'.",
    "4. On that page, click on 'School of Engineering'.",
    "5. Then, go to 'School of Engineering and Social Sciences'.",
    "6. Finally, visit the 'About Chanakya University' page."
]

print("Simulated Navigation Task for Chanakya University")
print("--------------------------------------------------\n")

# Show each step one by one
for step in steps:
    input(step + "\nPress Enter when you finish this step...")
    print("Now, note down the main heading/title you see on this page.\n")

print("All steps are completed. End of simulation.")
