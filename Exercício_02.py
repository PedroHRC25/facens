import os
import re
os.system("cls")
pergunta=("Pergunta aki")

print(pergunta)
resposta= ("resposta da pergunta aki")

if re.search ("\\bpergunta\\b|\\babc\\b", pergunta, re.IGNORECASE):
    print(resposta)
else:
    print("sem resposta")