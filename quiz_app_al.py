# Multiple choice Quiz Application
import random
import sys

# question ans data
Python = [
    {
        "question": "1.	What is an operating system?",
        "options": ["a) interface between the hardware and application programs", "b) collection of programs that manages hardware resources",
                     "c) system service provider to the application programs", "d) all of the mentioned"],
        "correct_answer": "d"
    },
    {
        "question": "2.	To access the services of the operating system, the interface is provided by the ___________",
        "options": ["a) Library", "b) System calls", "c) Assembly instructions", "d) API"],
        "correct_answer": "b"
    },
    {
        "question": "3.	If a process fails, most operating system write the error information to a ______",
        "options": ["a) new file", "b) another running process", "c) log file", "d) none of the mentioned"],
        "correct_answer": "c"
    },
    {
        "question": "4.	Which of the following is not an operating system?",
        "options": ["a)	Windows", "b) Linux", "c) Oracle", "d) DOS"],
        "correct_answer": "c"
    },
    {
        "question": "5.	What is the full name of FAT?",
        "options": ["a)	File attribute table", "b) File allocation table", "c) Font attribute table", "d) Format allocation table"],
        "correct_answer": "b"
    }
]


Operating_System  = [
    {
        "question": "1.	What is an operating system?",
        "options": ["a) interface between the hardware and application programs", "b) collection of programs that manages hardware resources", 
                    "c) system service provider to the application programs", "d) all of the mentioned"],
        "correct_answer": "d"
    },
    {
        "question": "2.	To access the services of the operating system, the interface is provided by the ___________ ?",
        "options": ["a) Library", "b) System calls", "c) Assembly instructions", "d) API"],
        "correct_answer": "b"
    },
    {
        "question": "3.	If a process fails, most operating system write the error information to a ______",
        "options": ["a) new file", "b) another running process", "c) log file", "d) none of the mentioned"],
        "correct_answer": "c"
    },
    {
        "question": "4.	Which of the following is not an operating system?",
        "options": ["a) Windows", "b) Linux", "c) Oracle", "d) DOS"],
        "correct_answer": "c"
    },
    {
        "question": "5.	What is the full name of FAT?",
        "options": ["a)	File attribute table", "b)	File allocation table", "c)	Font attribute table", "d)	Format allocation table"],
        "correct_answer": "b"
    }
]

# program start
all_subject_names  = {"1": "Python", "2" : "Operating_System"}


print("#"*110)
print("Enter topic number?    ")
for key, value in all_subject_names.items():
    print("\t",key+")", value)

selected_subject = input("\nChoice : ")


quit = True
while selected_subject.lower() != 'q':
    if selected_subject in all_subject_names:
        print("You have chosen:", all_subject_names[selected_subject])
        quit = False
        break
    else:
        print("Invalid choice. Please select a correct topic number.")

    selected_subject = input("Enter topic number, or 'q' for quit : ")
if quit:
    print("Exsiting the program.")
    sys.exit()


subject_data = globals()[all_subject_names[selected_subject]] 
print("#"*110)
list_question_number = list(range(len(subject_data)))

random.shuffle(list_question_number)

score = 0

# Iterate all question 
for i in list_question_number:
    present_question_all_data = subject_data[i]
    
    print(f"Question : {present_question_all_data['question']}")
    for option in present_question_all_data['options']:
        print(option)
    
    user_submited_answer = input("Your answer (a/b/c/d) : ").strip().lower()
    
    # Check if the user's answer is correct 
    if user_submited_answer == present_question_all_data['correct_answer']:
        print("Correct Answer \n")
        score += 1
    else:
        print(f"Wrong Answer, The correct answer is: {present_question_all_data['correct_answer'].upper()}\n")

# Display the final score of user
print("-"*110)
print(f"You scored {score} out of {len(subject_data)} questions.")

if score == len(subject_data):
    print("Congratulations! You are the quiz champion!")
print("-"*110)
