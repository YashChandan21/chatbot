import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=None):
    if required_words is None:
        required_words = []
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty +=1

    # Calculate the percent of recognised words in user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in a string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_message(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        nonlocal highest_prob_list
        highest_prob_list[bot_response]  = message_probability(message, list_of_words, single_response, required_words)


    # Response _______________________v
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you!', ['i', 'love', 'you', 'bot'], required_words=['love'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)

    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_ADVICE, ['weather', 'image', 'price'], required_words=[])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match



def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_message(split_message)
    return response

# Testing the response system
while True:
    user_input = input('You: ')
    if user_input.lower() == 'bye':
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: " + get_response(user_input))