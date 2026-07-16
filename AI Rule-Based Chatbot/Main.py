"""
Rule-Based AI Chatbot
DecodeLabs Industrial Training Kit - Project 1

A warm, welcoming chatbot that answers predefined questions using
dictionary lookups (O(1) response time) instead of an if-elif ladder.
"""

# ---------------------------------------------------------
# PHASE 2: KNOWLEDGE BASE (the dictionary of intents)
# ---------------------------------------------------------
responses = {
    # Greetings
    "hello": "Hi there! 😊 It's so nice to hear from you. How can I help you today?",
    "hi": "Hello! Welcome, I'm glad you're here. What would you like to know?",
    "hey": "Hey! Great to see you. Ask me anything about AI!",
    "good morning": "Good morning! I hope your day is off to a wonderful start. What can I help with?",
    "good evening": "Good evening! Hope you had a great day. How can I assist you?",

    # Core AI knowledge
    "what is ai": "Artificial Intelligence (AI) is the field of computer science focused on building "
                   "machines that can perform tasks which normally require human intelligence — like "
                   "understanding language, recognizing patterns, and making decisions.",
    "define ai": "AI, or Artificial Intelligence, refers to the simulation of human intelligence "
                 "in machines that are programmed to think, learn, and solve problems.",
    "what is artificial intelligence": "Artificial Intelligence is the science of teaching computers "
                                        "to think, reason, and make decisions in ways that mimic human "
                                        "intelligence.",
    "introduce ai": "Let me introduce you to AI! Artificial Intelligence is a branch of computer "
                     "science dedicated to creating systems that can learn from data, adapt to new "
                     "inputs, and perform human-like tasks such as recognizing speech, playing games, "
                     "or even holding a conversation — just like this one!",
    "types of ai": "Great question! AI is generally grouped into three types: Narrow AI (built for a "
                   "single task, like this chatbot), General AI (human-level intelligence across tasks, "
                   "still theoretical), and Super AI (surpassing human intelligence, purely conceptual "
                   "for now).",
    "applications of ai": "AI is everywhere! It powers voice assistants, recommendation systems on "
                          "Netflix and Spotify, self-driving cars, medical diagnosis tools, fraud "
                          "detection, and chatbots just like me. 🌟",
    "difference between ai and ml": "Good one! AI is the broad goal of making machines act "
                                     "intelligently. Machine Learning (ML) is a subset of AI where "
                                     "machines learn patterns from data instead of being explicitly "
                                     "programmed with rules.",
    "who invented ai": "The term 'Artificial Intelligence' was coined by John McCarthy in 1956, at "
                       "the Dartmouth Conference — widely considered the birthplace of AI as a field.",
    "help": "I'd love to help! You can ask me things like 'what is AI', 'types of AI', 'applications "
            "of AI', or just say hello. Type 'exit' whenever you're ready to go.",

    # Exit-adjacent pleasantries
    "thank you": "You're so welcome! Happy to help anytime. 😊",
    "thanks": "Anytime! Feel free to ask me more.",
}

FALLBACK_RESPONSE = ("Hmm, I don't have an answer for that just yet, but I'm always learning! "
                     "Try asking about AI, its types, or its applications — or type 'help' for ideas.")

EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}


# ---------------------------------------------------------
# PHASE 1: INPUT & SANITIZATION
# ---------------------------------------------------------
def clean_input(raw_input: str) -> str:
    """Normalize user input: lowercase + strip whitespace."""
    return raw_input.lower().strip()


# ---------------------------------------------------------
# PHASE 3: THE HEARTBEAT (continuous loop)
# ---------------------------------------------------------
def run_chatbot():
    print("=" * 60)
    print("  🤖  Welcome! I'm your friendly AI Assistant.")
    print("      Ask me about AI, or type 'help' for ideas.")
    print("      Type 'exit' anytime to say goodbye.")
    print("=" * 60)

    while True:
        raw_input_text = input("\nYou: ")
        user_input = clean_input(raw_input_text)

        if user_input in EXIT_COMMANDS:
            print("Bot: It was truly lovely chatting with you — take care, and come back soon! 👋")
            break

        if user_input == "":
            print("Bot: I didn't quite catch that — could you type something for me?")
            continue

        # The professional approach: atomic lookup + fallback
        reply = responses.get(user_input, FALLBACK_RESPONSE)
        print(f"Bot: {reply}")


if __name__ == "__main__":
    run_chatbot()
