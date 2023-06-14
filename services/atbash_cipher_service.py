import string


class AtbashCipher:
    # Variaveis locais
    espaco = " "
    cipher = ""
    pontucao = "áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ"

    def execute(self, text):
        for letra in text:

            # Pega todos os caracteres da tabela Ascii
            asciiCharacters = string.ascii_letters

            # Condicao para ver se a letra tem acento
            if self.pontucao.__contains__(letra):
                # Acha o local da letra na tabela de pontuação
                findLetraAcentuada = self.pontucao.find(letra)

                # Acha o local da letra inversa
                localLetra = int(len(self.pontucao)/2) - findLetraAcentuada

                self.cipher += self.pontucao[localLetra]

            elif string.punctuation.__contains__(letra):
                # Acha o local da letra na tabela de pontuação
                findLetraAcentuada = string.punctuation.find(letra)

                # Acha o local da letra inversa
                localLetra = int(len(string.punctuation)/2) - findLetraAcentuada

                self.cipher += string.punctuation[localLetra]
            # Condicao pra ver se a letra é um espaço
            elif letra != self.espaco:
                # Acha o local da letra na tabel ascii
                findLetra = asciiCharacters.find(letra)

                # Acha o local da letra inversa
                localLetra = int((len(asciiCharacters)/2) - findLetra)

                # Concatena na mensagem cifrada
                letter = asciiCharacters[localLetra-1]
                self.cipher += letter
            else:
                self.cipher += self.espaco

        # Retorna a string cifrada ou decifrada
        return self.cipher
