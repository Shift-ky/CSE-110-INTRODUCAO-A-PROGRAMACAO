from random import sample

palavra_secreta = "moises"
tentativa = "Marcos"  # exemplo

palavra = ""


tentativa = ''.join(sample(tentativa, len(tentativa)))
for i, letra in enumerate(palavra_secreta):
    if letra in tentativa:
        if i < len(tentativa) and tentativa[i] == letra:
            palavra += letra.upper()  # posição correta
        else:
            palavra += letra.lower()  # letra existe mas está em outra posição
    else:
        palavra += "_"

print(f"Sua dica é: {palavra}")