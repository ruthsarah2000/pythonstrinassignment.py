'''
3. Interactive Help Desk Bot
Task 1: Command Parser
Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). 
If a command is found, print a response related to the command.

Task 2: Issue Categorizer
If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. 
Print out the category of the issue for the support team.
'''

# Task 1 #

def identify_command(user_input):
   
    commands = {"help", "issue", "contact support"}
    user_input_lower = user_input.lower()

    for command in commands:
        if command in user_input_lower:
            if command == "help":
                print("Here is some help information.")
            elif command == "issue":
                print("Please describe the issue you are facing.")
            elif command == "contact support":
                print("Please contact our support team for assistance.")
            return 
    print("No predefined command found in the input.")
user_text = input("Enter your text: ")
identify_command(user_text)

# Task #

def identify_issue_category(user_input):
    keywords = {
        "login": ["login", "signin", "authentication"],
        "performance": ["slow", "lag", "performance"],
        "error": ["error", "issue", "problem"]
    }

    user_input_lower = user_input.lower()
    if "issue" in user_input_lower:
        for category, category_keywords in keywords.items():
            for keyword in category_keywords:
                if keyword in user_input_lower:
                    print(f"This is a {category} issue.")
                    return  
    
   
    print("No specific issue category found.")
user_text = input("Enter your text: ")
identify_issue_category(user_text)
