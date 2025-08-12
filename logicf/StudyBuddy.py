import re
import random


global study_helper, fallback, general_problems

study_helper = {
    r"how to prepare for the exam|\bprepare for exam\b | \bprepare for an exam\b": [
        "Study at least a week before the exam to avoid last-minute stress.",
        "Use the Pomodoro technique: Study for 25 minutes, take a 5-minute break.",
        "Summarize key points in a notebook and review them daily."
    ],

    r"\b(how to focus|stay focused|avoid distractions)\b": [
        "Try studying in a quiet place and remove distractions like your phone.",
        "Use a timer to set short study sessions with breaks in between.",
        "Listen to instrumental music or white noise to improve concentration."
    ],

    r"\b(best way to take notes|note-taking techniques)\b": [
        "Try the Cornell Method: Divide your page into sections for key points, details, and summaries.",
        "Use mind maps to visually organize information.",
        "Rewrite or summarize your notes to reinforce learning."
    ],

    r"\b(how to manage time|time management tips|Any tips to manage)\b": [
        "Create a daily schedule and stick to it.",
        "Prioritize tasks using the Eisenhower Matrix (urgent vs. important).",
        "Break big tasks into smaller, manageable chunks."
    ],

    r"\b(feeling unmotivated|study motivation|I'm feeling unmotivated)\b": [
        "Set small, achievable goals to keep yourself on track.",
        "Reward yourself after completing study sessions.",
        "Remember why you're studying and visualize your success!"
    ],

    r"\b(how to remember better|memory tips|retain information)\b": [
        "Use spaced repetition to review material over time.",
        "Teach the material to someone else – explaining helps retention.",
        "Use mnemonic devices and visualization techniques."
    ],

    r"\b(best time to study|when should I study)\b": [
        "It depends on your energy levels! Morning is great for focus, but night works for some people too.",
        "Try studying during your peak productivity hours.",
        "Avoid studying right before bed—review instead of cramming."
    ],

    r"\b(feeling tired|exhausted|burnout)\b": [
        "Take a short break and get some fresh air.",
        "Make sure you're getting enough sleep – at least 7-8 hours per night.",
        "Stay hydrated and eat healthy snacks for energy."
    ],

    r"\b(hello|hi|hey)\b": [
        "Hey there! Ready to study? 📚",
        "Hello! What can I help you with today?",
        "Hi! Need any study tips?"
    ],

    r"\b(thank you|thanks)\b": [
        "You're welcome! Happy studying! 😊",
        "No problem! Let me know if you need more help.",
        "Glad to help! Keep up the good work!"
    ],
    
    r"\b(goodbye|bye|see you|take care)\b": [
        "Goodbye! Have a great day ahead!",
        "Take care! See you next time!"
    ]
}


fallback = [
    "Sorry, I didn't understand that. Could you rephrase your question?",
    "Hmm, that doesn't seem related to studying. Try asking about study tips or exam preparation!",
    "I didn’t quite get that. Maybe you need help with focus, motivation, or study techniques?",
    "I'm not sure about that, but I can help you with study-related questions!",
    "That doesn’t seem familiar, but if you need advice on note-taking, time management, or concentration, I’d be happy to assist.",
    "I might not have an answer for that, but feel free to ask about effective study methods!",
    "Not sure what you mean, but I can give you tips on memorization, scheduling, or exam strategies."
]



general_problems = {
    r"\b(problem|can not|unable|fails|issue|trouble|struggle|having trouble|having issues|hard time|stuck)\b.*": [
        "I'm sorry to hear that you're struggling! Here are some steps to help you tackle study-related problems:\n\n"
        "1️⃣ \tIdentify the exact problem: Are you struggling to understand a topic, focus, or manage time?\n"
        "2️⃣ \tBreak it down: If a concept is difficult, try simplifying it into smaller parts.\n"
        "3️⃣ \tUse different learning methods: Watch videos, read summaries, or teach the topic to someone else.\n"
        "4️⃣ \tTake regular breaks: Studying for long hours can be exhausting. Try the Pomodoro technique (25 minutes study, 5 minutes break).\n"
        "5️⃣ \tStay motivated: Set small goals and reward yourself when you achieve them.\n"
        "6️⃣ \tAsk for help: Discuss with friends, join study groups, or ask a teacher for guidance.\n"
        "7️⃣ \tStay healthy: Get enough sleep, eat well, and exercise to keep your brain functioning at its best.\n\n"
    ],
    
    r"\b(cannot focus|hard to focus|hard to concentrate|easily distracted)\b": [
        "It’s tough to focus sometimes! Here’s what you can do:\n\n"
        "1️⃣ \tEliminate distractions: Put your phone on silent and find a quiet study spot.\n"
        "2️⃣ \tUse the Pomodoro technique: Study in short bursts of 25 minutes with 5-minute breaks.\n"
        "3️⃣ \tTry background music: Instrumental music or white noise can help you concentrate.\n"
        "4️⃣ \tStay hydrated and take breaks: Drink water and stretch every hour to refresh your mind.\n"
        "5️⃣ \tSet clear goals: Write down what you need to accomplish before you start.\n\n"
    ],

    r"\b(forget what I study|can't remember|memory problem|how to memorize)\b": [
        "Improving memory takes practice! Here are some effective strategies:\n\n"
        "1️⃣ \tUse spaced repetition: Review the material multiple times over a few days.\n"
        "2️⃣ \tTeach what you learn: Explaining a concept to someone else helps reinforce it.\n"
        "3️⃣ \tUse mnemonics: Create acronyms or funny associations to remember key points.\n"
        "4️⃣ \tTake handwritten notes: Writing by hand helps information stick better than typing.\n"
        "5️⃣ \tGet enough sleep: Your brain processes information while you sleep, so aim for 7-8 hours of rest.\n\n"
    ]
}



def get_response(user_input):
    # mached = []
    for pattern, response in study_helper.items():
        if re.search(pattern, user_input,re.IGNORECASE):
            return random.choice(response)
        
    for key_problem, values_answer in general_problems.items():
        if re.search(key_problem, user_input,re.IGNORECASE):
            for value in values_answer:
               return value
        
    else: 
        return random.choice(fallback)



# Testing

"""
while True:
    user_input = input("You: ").lower()
    if user_input in ['exit', '-1']:
        print("Good Bye My friend")
        break               

    response = get_response(user_input)
    print(response)
"""
