import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore

# Initialize the speech engine
engine = pyttsx3.init()

# Sample catalog of items
food_store = {
    'apple': 1.50,
    'banana': 0.75,
    'bread': 2.00,
    'milk': 1.25,
    'eggs': 2.50
}

cart = {}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you say that again?")
        return None
    return query.lower()

def add_to_cart(item):
    if item in food_store:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
        speak(f"Added {item} to your cart.")
    else:
        speak(f"Sorry, we don't have {item}.")

def open_catalog():
    speak("Here is the catalog of available items:")
    for item, price in food_store.items():
        speak(f"{item} is priced at ${price:.2f}")

def get_total():
    total = sum(food_store[item] * quantity for item, quantity in cart.items())
    speak(f"Your total is ${total:.2f}")

if __name__ == "__main__":
    speak("Hello, welcome to the Voice Food Store. How can I help you today?")
    while True:
        query = take_command()

        if query:
            if 'add' in query:
                item = query.replace('add', '').strip()
                add_to_cart(item)
            elif 'open catalog' in query:
                open_catalog()
            elif 'total' in query:
                get_total()
            elif 'stop' in query or 'bye' in query:
                speak("Thank you for visiting the Voice Food Store. Goodbye!")
                break
            else:
                speak("Sorry, I can’t perform that task yet.")



