from peca import Peca 
from nos import Nos

peca1 = Peca ('123', 'Placa de Video', 'A placa de video e...', '32 categoria', '32 video', '32 imagem')
peca2 = Peca ('567', 'Placa Mae', 'A placa Mae e...', '43 categoria', '43 video', '43 imagem')
peca3 = Peca ('910', 'Fonte de Alimentacao', 'A Fonte de Alimentacao e...', '54 categoria', '54 video', '54 imagem')


informacao = Nos ('233', 'Nos', 'Explicação sobre as pessoa', 'linkedin')


print ('-------------Pagina Nos: -------------')

print(f"{informacao.__dict__} \n")

print()

print('-------------Pecas registradas: -------------')
print()
print(f"{peca1.__dict__} \n")
print(f"{peca2.__dict__} \n")
print(f"{peca3.__dict__} \n")

print()

