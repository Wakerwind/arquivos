#Usamos o open para abrir um arquivo, passando o nome e extensão do arquivo mais a operação a ser realizada: r, w


# sem with
arquivo = open("meu_arquivo.txt", 'w')

# se der um bug na linha do write, ou em qualquer linha antes do close, vai dar erro
# arquivo.write para escrever no arquivo
arquivo.write("Eita Lirinha, manda video novo pra gente ai")

#fechando o arquivo
arquivo.close()

# Se der erro de escrita o arquivo fica aberto e dá problema na próxima abertura

# com with

# aqui, o with já lida com o abrir e fechar do arquivo, então ele não dá erro

with open("meu_arquivo.txt",'w') as arquivo:
    arquivo.write('Olá mundo! tijolo joia!')

# pode usar para ler tb, sem problemas

with open("meu_arquivo.txt","r") as arquivo:
    arq = arquivo.read()
    print(f'Arquivo lido: {arq}')

# O readline permite ler e separar o conteúdo do documento por linhas.
# É usado para docs com várias linhas
# Isso ajudar a analisar melhor o documento e retornar algo de interesse mais facilemente
# Ele retorna uma lista onde cada posição da lista é uma linha do txt

with open("linhas.txt",'r', encoding="utf-8") as arquivo:
    texto = arquivo.readlines()
    print(f'Retorno do readlines: {texto}')

# Retorna a linha que contem a palavra batman
for frase in texto:
    if "batman" in frase:
        print(f'Pesquisa: {frase}')


# Usamos arquivo.write() para escrever em um arquivo.
# Se o arquivo já existir sobrescreve suas informações se não cria o arquivo

with open('email.txt','w', encoding='utf-8') as arq:

    arq.write('joaovitorraposodeoliveira5@gmail.com')

with open('email.txt','r',encoding='utf-8') as arq:
    email = arq.read()
    print(f'Email escrito: {email}')

# Se quisermos adicionar informações no arquivo sem apagar as anteriores usamos...
# arquivo.append()

with open('email.txt','a', encoding='utf-8') as arq:
    # Uso o \n para pular a linha no documento
    arq.write('\njoavitorraposodeoliveira2@gmail.com')

with open('email.txt','r',encoding='utf-8') as arq:
    email = arq.read()
    print(f'Emails adicionados: {email}')

# Tentando pegar o último email adicionado

with open('email.txt','r',encoding='utf-8') as arq:
    email = arq.readlines()
    print(f'Último email adicionado: {email[-1]}')




