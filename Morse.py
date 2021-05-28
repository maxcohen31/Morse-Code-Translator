# Morse code translator

class Morse:
    
    def __init__(self):
        self.morse = {
                    "a": ".-",     
                    "b": "-...",
                    "c": "-.-.",
                    "d": "-..",
                    "e": ".",
                    "f": "..-.",
                    "g": "--.",
                    "h": "....",
                    "i": "..",
                    "j": ".---",
                    "k": "-.-",
                    "l": ".-..",
                    "m": "--",
                    "n": "-.",
                    "o": "---",
                    "p": ".--.",
                    "q": "--.-",
                    "r": ".-.",
                    "s": "...",
                    "t": "-",
                    "u": "..-",
                    "v": "...-",
                    "w": ".--",
                    "x": "-..-",
                    "y": "-.--",
                    "z": "--..",
                    "0": "-----",
                    "1": ".----",
                    "2": "..---",
                    "3": "...--",
                    "4": "....-",
                    "5": ".....",
                    "6": "-....",
                    "7": "--...",
                    "8": "---..",
                    "9": "----.",
                    "&": ".-...",
                    "'": ".----.",
                    "@": ".--.-.",
                    ")": "-.--.-",
                    "(": "-.--.",
                    ":": "---...",
                    ",": "--..--",
                    "=": "-...-",
                    "!": "-.-.--",
                    ".": ".-.-.-",
                    "-": "-....-",
                    "+": ".-.-.",
                    '"': ".-..-.",
                    "?": "..--..",
                    "/": "-..-."}
    
    # Method to welcome the player
    def greetings(self):
        
        print('''
                ******************************
                    MORSE CODE CONVERTER    
                ******************************
                ''')
        
    # From English to Morse code       
    def english_morse_translator(self):
        self.greetings()
        words = input('Write the text to translate: ')
        if len(words) == 0:
            print('You have to provide some text')
        text = words.split() # Split the input into an array
        result = '' # This will be the translated text
        for word in text: # Loop through the words in the array
            character = []  
            for char in word: # Loop through each characters of the words
                if char.lower() in self.morse: # Check the characters to be in self.morse variable
                    character.append(self.morse[char.lower()]) # Append the characters found
            result += ''.join(character)         
            result += '  '
        return result  

    # From Morse code to English
            
    def morse_to_eng(self):
        self.greetings()
        morse = input('Insert Morse code: ') 
        if len(morse) == 0:
            print('Please, insert Morse code')
        else:    
            final_message = '' # This will be the translated code
            morse_code = morse.split() # Split rhe input into an array
            for morse_w in morse_code:
                characters = morse_w.split() # Splitting the characters variable
                for char in characters: # Loop through the characters
                    for key, value in self.morse.items(): # Looping through the self.morse dictionary
                        if char == value: # char has to be equal to value
                            final_message += key # Add keys to the final_message variable
                final_message += ''
            print(final_message)          
            
                
