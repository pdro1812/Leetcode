from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Inicializar o conjunto com as letras da primeira palavra
        common_chars = list(words[0])
        
        # Iterar sobre as palavras restantes
        for word in words[1:]:
            # Lista temporária para as letras comuns na palavra atual
            temp_list = []
            
            for char in word:
                if char in common_chars:
                    temp_list.append(char)
                    common_chars.remove(char)
            
            # Atualizar common_chars para apenas as letras comuns até agora
            common_chars = temp_list
        
        return common_chars

# Array de palavras
words = ["bella", "label", "roller"]

# Criar uma instância da classe Solution
solucao = Solution()

# Chamar o método commonChars
resultado = solucao.commonChars(words)

# Exibir o resultado
print(resultado)
