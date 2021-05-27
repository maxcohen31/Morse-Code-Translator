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
        
        return  '''
                ******************************
                    MORSE CODE CONVERTER    
                ******************************
                '''
        
    # From English to Morse code  
            
    def english_morse_translator(self):
        
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
            
    def morse_english_translator(self, morse):
        
        if morse == '':
            return 'Please, insert Morse code'
        else:
            text = ''
            morse = morse.split()
            
            for morse_w in morse:
                characters = morse_w.split()
                for char in characters:
                    for key, value in self.morse.items():
                        if char == value:
                            text += key
                text += ''
            return text.rstrip()          
            
                
