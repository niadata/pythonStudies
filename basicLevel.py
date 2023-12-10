#O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.
mensagem = input()

if len(mensagem) <= 140:
    print ('TWEET')
else:
    print ('MUTE')
