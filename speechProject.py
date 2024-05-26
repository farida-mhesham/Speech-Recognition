import speech_recognition as sr
from googletrans import Translator

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Say something:")
        try:
            audio = recognizer.listen(mic, timeout=5)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

        return None

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    while True:
        user_input = recognize_speech()

        if user_input:
            print(f"You said: {user_input}")

            translate_option = input("Do you want to translate? (yes/no): ").lower()

            if translate_option == 'yes':
                target_language = input("Enter target language ( 'fr' for French, 'de' for German, 'ar' for Arabic): ").lower()

                translated_text = translate_text(user_input, target_language)
                print(f"Translation: {translated_text}\n")
            elif translate_option == 'no':
                print("Translation skipped.\n")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.\n")

        end_option = input("Do you want to end the program? (yes/no): ").lower()
        if end_option == 'yes':
            print("Ending the program.")
            break
        elif end_option != 'no':
            print("Invalid input. Please enter 'yes' or 'no'.\n")

if __name__ == "__main__":
    main()

