def eh_palindromo(frase):
    frase = frase.lower()
    frase = frase.replace(" ", "")
    frase = ''.join(letra for letra in frase if letra.isalnum())
    if frase == frase[::-1]:
        return "Sim"
    else:
        return "Não"

texto = input("Digite uma palavra ou frase: ")
print(eh_palindromo(texto))

