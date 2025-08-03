data = {
    # Greetings intent: user says hello or greets the bot
    "greetings": [
        "hi", "hello", "hey", "hey there", "good morning", "good afternoon", "good evening",
        "what's up", "whats up", "yo", "hiya", "greetings", "howdy", "how’s it going",
        "hi there", "hiya!", "hello!", "hey!", "sup", "hey yo", "hello there", "hey friend"
    ],
    # Responses to greetings to welcome the user
    "responses": [
        "Hello there!", "Hi! How can I help you today?", "Hey! What's going on?",
        "Hi, friend!", "Howdy! Need something?", "Hi there—good to see you!",
        "Hello! How are you doing?", "What can I do for you?", "Hey! What’s up?",
        "Greetings! How may I assist?", "Hi! I'm here for you!", "Hey! Need a hand?"
    ],

    # Farewells intent: user says goodbye or leaves
    "farewells": [
        "bye", "goodbye", "see you", "see ya", "take care", "catch you later",
        "farewell", "later", "talk to you later", "I gotta go", "I am leaving",
        "bye bye", "see you soon", "see ya later", "bye for now", "cya", "peace out",
        "adios", "cheerio"
    ],
    # Responses to farewells to politely end conversation
    "farewell_responses": [
        "Goodbye! Take care.", "See you later!", "Bye for now!", "Have a great day!",
        "Catch you soon!", "Take care! It was nice chatting with you.",
        "Bye! Safe travels.", "Farewell! Until next time.", "See ya!",
        "Bye bye! Come back anytime.", "Peace out!", "Adios amigo!", "Cheerio!"
    ],

    # Questions intent: user asks about bot's identity, abilities, or status
    "questions": [
        "how are you", "how are things", "how is it going", "what are you doing",
        "what is your name", "who are you", "can you help me", "what can you do",
        "tell me about yourself", "what do you do", "what is your purpose",
        "are you a real person", "do you know me", "where do you live",
        "are you a bot", "what's your name", "your name", "can you talk to me"
    ],
    # Responses explaining bot's nature and abilities
    "question_responses": [
        "I'm just a bot, but I'm doing great!", "I'm here to assist you!",
        "I'm your friendly chatbot!", "Ask me anything!",
        "I’m a Python-based chatbot using NLP!", "I can chat, answer simple questions, and learn.",
        "My name? I'm your helpful chatbot.", "I live in the cloud!",
        "I don't eat or sleep—I just talk!",
        "I exist to chat and help you out!", "Yes, I’m a bot—but a friendly one!",
        "I’m here any time you need a chat."
    ],

    # Small talk intent: casual or general chit-chat statements/questions
    "small_talk": [
        "what's up", "whats up", "how's life", "hows life", "how are things",
        "tell me something", "what's new", "anything interesting", "what’s new",
        "got any news", "coffee?", "what do you think", "thoughts?", "random talk",
        "just chatting", "small talk", "how’s everything", "how you doing"
    ],
    # Responses for casual conversation and engagement
    "small_talk_responses": [
        "Not much, just hanging out in cyberspace!", "Life’s good in the code world!",
        "Always here, always ready.", "Thinking about deep learning!",
        "Just chatting with wonderful people like you.", "I enjoy talking to you!",
        "I'm here—what’s on your mind?", "All is quiet on my end.",
        "Living the chatbot life!", "Just bits and bytes over here.",
        "Talking is my favorite pastime!", "I'm here, and I'm listening."
    ],

    # Time intent: user asks for the current time
    "time": [
        "what time is it", "tell me the time", "current time", "can you give me the time",
        "time?", "do you know the time", "time now", "what's the time"
    ],
    # Responses to time-related questions (bot doesn't have real-time access)
    "time_responses": [
        "Sorry, I can't tell time yet!", "I’m not sure of the time, but it’s always a good time to chat!",
        "Time is just a concept here!", "I don’t have a clock—but I have you!",
        "I can't check the time, but let's keep chatting!"
    ],

    # Date intent: user asks about the current date
    "date": [
        "what is the date", "tell me today's date", "todays date", "current date",
        "date?", "do you know the date", "what's the date today", "today's date"
    ],
    # Responses about date with chatbot limitations
    "date_responses": [
        "I can't check the date right now.", "I live outside of time!",
        "Every day is today for me.", "Not sure of the date—but I'm always present!",
        "I can't see calendars—but I see you!"
    ],

    # Thanks intent: user expresses gratitude
    "thanks": [
        "thanks", "thank you", "thx", "much appreciated", "thanks a lot", "cheers",
        "thank u", "thanks so much", "thanks!", "thank you very much", "ty"
    ],
    # Responses to thank the user or acknowledge thanks
    "thanks_responses": [
        "You're welcome!", "Glad to help!", "Anytime!", "No problem!",
        "My pleasure!", "Happy to assist!", "Sure thing!", "Don't mention it!",
        "I'm always here for you!"
    ],

    # Emotions intent: user expresses feelings or emotional states
    "emotions": [
        "i'm sad", "i am sad", "i'm happy", "i am happy", "i feel great", "i feel good",
        "i'm angry", "i am angry", "i'm upset", "i feel upset", "i'm excited", "i feel excited",
        "i'm feeling down", "i feel down", "i'm worried", "i feel worried", "i need support"
    ],
    # Responses to acknowledge feelings and offer support
    "emotions_responses": [
        "I'm here for you!", "That's great to hear!", "Stay positive!",
        "It's okay to feel that way.", "Want to talk more about it?",
        "I’m listening if you want to share.", "Hope it gets better soon.",
        "I believe in you!", "Big hugs!", "How can I help you feel better?"
    ],

    # Help intent: user asks for help or assistance
    "help": [
        "i need help", "can you help me", "help me", "i need assistance",
        "can you assist me", "help please", "i'm stuck", "need advice",
        "need support", "please help", "help!"
    ],
    # Responses offering assistance and encouraging sharing of issues
    "help_responses": [
        "Sure! What do you need help with?",
        "Of course, I’m here to help.", "Tell me what's wrong—I'll do my best.",
        "I’ll try my best—what’s troubling you?", "Let me know, happy to assist!"
    ],

    # Food intent: user talks about hunger or food suggestions
    "food": [
        "i'm hungry", "i am hungry", "what's for dinner", "what should i eat",
        "suggest food", "food ideas", "i want food", "hungry!"
    ],
    # Responses suggesting food ideas or meals
    "food_responses": [
        "How about pizza or pasta?", "Tacos sound good today!", "Maybe order some sushi?",
        "A nice sandwich could hit the spot!", "Fresh salad or fruit salad might be nice!",
        "Have you tried local cuisine?", "How about a bowl of soup?", "Craving something sweet?"
    ],

    # Compliments intent: user praises the bot
    "compliments": [
        "you are smart", "you are helpful", "what's for dinner", "good bot",
        "nice bot", "well done", "great job", "you’re amazing",
        "you are awesome", "you rock", "i like you", "i love you chatbot"
    ],
    # Responses to show gratitude for compliments
    "compliments_responses": [
        "Thank you so much!", "You're very kind!", "I appreciate that!",
        "You made my day!", "Glad to hear that!", "That means a lot!",
        "Thank you—I'm here for you!"
    ],
"weather": [
    "what's the weather", "how's the weather", "is it raining", "will it rain today",
    "is it sunny", "weather forecast", "do I need an umbrella", "current weather",
    "tell me the weather", "weather today", "is it hot outside", "cold today?"
],
"weather_responses": [
    "I can't fetch live weather yet, but I hope it's nice out!",
    "Check your local forecast to be sure!",
    "No idea, but I’d guess a 50% chance of awesome!",
    "I don't have weather data right now—try a weather app.",
    "I hope it's sunny where you are!",
    "Stay dry out there if it’s raining!"
],

"shopping": [
    "what should I buy", "recommend something", "any shopping tips", "help me shop",
    "i want to buy something", "gift ideas", "what to get for birthday", "shopping list",
    "i need gift ideas", "recommend a product"
],
"shopping_responses": [
    "Looking for something specific?",
    "How about a thoughtful gift card or book?",
    "You can’t go wrong with tech gadgets!",
    "Make a list and prioritize needs vs wants!",
    "Check online reviews before buying anything.",
    "I’d go with something useful and meaningful."
],

"health": [
    "i want to get fit", "how to stay healthy", "fitness tips", "healthy food ideas",
    "how to lose weight", "how to gain weight", "is walking good exercise",
    "how much water should I drink", "tips for sleeping better"
],
"health_responses": [
    "Drink plenty of water and move a little every day!",
    "Sleep, nutrition, and activity are key!",
    "Small habits make big changes over time.",
    "Walking is a great low-impact exercise!",
    "Balance is the secret—no extremes!",
    "I’m not a doctor, but I can encourage you to stay healthy!"
],

"productivity": [
    "i can't focus", "how to be productive", "study tips", "how to stop procrastinating",
    "help me study", "how to manage time", "productivity hacks", "i'm distracted"
],
"productivity_responses": [
    "Try the Pomodoro technique: 25 mins focus, 5 mins break.",
    "Set small goals and reward yourself!",
    "Start with one small task—it builds momentum.",
    "Eliminate distractions and create a plan!",
    "Stay consistent, not perfect.",
    "You’ve got this! One step at a time."
],

"fun": [
    "tell me a joke", "make me laugh", "bored", "i'm bored", "fun stuff",
    "something funny", "cheer me up", "i need a laugh"
],
"fun_responses": [
    "Why don’t skeletons fight? They don’t have the guts.",
    "I would tell you a construction joke, but I’m still working on it.",
    "Knock knock! Who’s there? Chatbot. Chatbot who? Chatbot you a coffee!",
    "Wanna hear a pun? I'm pun-stoppable!",
    "Did you smile? Mission accomplished!",
    "Laughter is the best code-free therapy!"
],

"sleep": [
    "i'm tired", "i need sleep", "i can't sleep", "how to sleep better",
    "insomnia help", "why can't i sleep", "sleep tips", "i'm sleepy"
],
"sleep_responses": [
    "Try winding down with a book or some calm music.",
    "Screens off at least 30 minutes before bed!",
    "Deep breaths and a dark room can help.",
    "Hope you catch some great Zzz’s!",
    "You deserve rest—take care of yourself.",
    "Sleep is essential—don’t skip it!"
],

"travel": [
    "i want to travel", "suggest places to visit", "vacation ideas", "where should i go",
    "best travel destinations", "i'm planning a trip", "help me plan vacation",
    "fun places to visit"
],
"travel_responses": [
    "How about the mountains or a quiet beach?",
    "City trip or nature escape?",
    "A road trip can be a great adventure!",
    "Travel light, live fully!",
    "Make sure to pack snacks and a playlist!",
    "Where have you always wanted to go?"
],
    "jokes": [
    "tell me a joke", "i want to hear a joke", "make me laugh", "say something funny",
    "give me a joke", "funny please", "joke time"
],
"jokes_responses": [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Parallel lines have so much in common… it’s a shame they’ll never meet.",
    "I told my computer I needed a break, and it said 'no problem, I’ll go to sleep.'"
],
}
