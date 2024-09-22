alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cyphering = True

from art import logo


def ceaser(cypher_direction, input_text, shift_value):
    cypher_text = ""
    if cypher_direction == "decode":
        shift_value *= -1
    for letter in input_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            letter_shift = position + shift_value
            cyphered_letter = alphabet[letter_shift]
            cypher_text += cyphered_letter
        else:
            cypher_text += letter
    print(f"The {cypher_direction}d text is {cypher_text}")


print(logo)
while cyphering:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 45:
        shift %= 45

    ceaser(cypher_direction=direction, input_text=text, shift_value=shift)

    if input("Do you wanna go again? : ").lower() == "yes":
        cyphering = True
    else:
        cyphering = False
