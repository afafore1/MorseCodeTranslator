import streamlit as st

# Define the morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def translate_to_morse_code(text):
    """
    Function to convert text to Morse code.
    """
    morse_code = ""
    for letter in text:
        if letter != " ":
            morse_code += MORSE_CODE_DICT[letter.upper()] + " "
        else:
            morse_code += " "
    return morse_code

# Streamlit app
def app():
    st.title("Morse Code Translator")
    input_text = st.text_input("Enter text to translate:")
    if st.button("Translate"):
        morse_code = translate_to_morse_code(input_text)
        st.write(f"**Morse Code:** {morse_code}")

app()
