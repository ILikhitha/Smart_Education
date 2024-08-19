import random

# Dictionary of Indian states and their capitals
states_and_capitals = {
    'Andhra Pradesh': 'Amaravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata'
}

def conduct_quiz(num_questions):
    score = 0
    questions = random.sample(list(states_and_capitals.items()), num_questions)
    
    for state, capital in questions:
        print(f"What is the capital of {state}?")
        answer = input("Your answer: ").strip()
        
        if answer.lower() == capital.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {capital}.\n")
    
    print(f"Quiz completed! Your score: {score}/{num_questions}")

def main():
    print("Welcome to the States and Capitals Quiz!")
    num_questions = int(input("How many questions would you like to answer? "))
    
    if num_questions > len(states_and_capitals):
        print(f"Sorry, only {len(states_and_capitals)} questions are available.")
        num_questions = len(states_and_capitals)
    
    conduct_quiz(num_questions)

if __name__ == "__main__":
    main()
