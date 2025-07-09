## college_life_advisor.py

# 🎓 Step 2: Welcome the User
print("🎓 Welcome to the College Life Advisor!")

name = input("What is your name? ")
gpa = float(input("What is your current GPA? "))
sleep_hours = int(input("How many hours did you sleep last night? "))
exam_tomorrow = input("Do you have an exam tomorrow? (yes or no) ").lower()

# 🧠 Step 3: Give GPA Advice
if gpa >= 3.5:
    gpa_advice = "You're doing great academically!"
elif 2.5 <= gpa < 3.5:
    gpa_advice = "You're doing okay, but there’s room to grow."
else:
    gpa_advice = "Let’s talk strategies to raise your grades."

# 😴 Step 4: Evaluate Sleep & Exam Status
if exam_tomorrow == "yes":
    if sleep_hours < 6:
        exam_advice = "You need more rest! Try a power nap and light review."
    else:
        exam_advice = "You’re on track – review your notes and get confident!"
else:
    exam_advice = "Use today to catch up or get ahead – balance is key."

# 🧮 Step 5: Combine All Advice
print("\n🎯 Final Report:")
print(f"Good luck, {name}!")
print(f"Your GPA is: {gpa}")
print(f"You got {sleep_hours} hours of sleep.")
print(f"Exam Tomorrow: {exam_tomorrow.capitalize()}")
print(f"Advice: {exam_advice}")
print(f"GPA Feedback: {gpa_advice}")
