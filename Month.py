#Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

month = input()
months_dict = {'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'Agust', '9':'Setember', '10':'october', '11':'NOvember', '12':'December'}
print (months_dict.get(month))
