LETTER_TO_MORSE = { 'S': '...', 'O':'---'}

def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode('2*3')
    Traceback (most recent call last):
        ...
    KeyError: '2'

    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)

if __name__ == "__main__":
    print('Hi!')