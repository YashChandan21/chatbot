import random

R_EATING =  "I don't like eating anything becouse I'm a bot obviously!"
R_ADVICE = "I\'m offline bot, please preferred google"

def unknown():
    response = ['Could you please re-phase that?',
                "...",
                "could not understand",
                "What does that mean?"][random.randrange(4)]
    return response