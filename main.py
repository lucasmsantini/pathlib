from pathlib import Path
path = Path('arq1.txt')
print (path)
print (path.home())
print (path.exists())
print (path.is_file())
print (path.is_dir())
print (path.suffix)
print (path.stem)
print (path.parent)
print (path.absolute())



'''
nova_pasta = Path('.')
novo_arquivo = nova_pasta / 'teste1'
#print(novo_arquivo)

print(novo_arquivo.resolve())
print(novo_arquivo.exists())
print(type(novo_arquivo))


print(novo_arquivo.exists())
print(novo_arquivo.absolute())
print(novo_arquivo.absolute() == novo_arquivo)
print(novo_arquivo.absolute().samefile(novo_arquivo))

print(novo_arquivo.absolute().parent.joinpath('arq.txt').samefile(novo_arquivo))

novo_arquivo /= 'arq1.txt'
for file_name in novo_arquivo.parent.iterdir():
    print(file_name)
novo_arquivo /= 'arq1.txt'
for file_name in novo_arquivo.parent.parent.iterdir():
    if file_name.match('*.py'):
        print(file_name)
print(novo_arquivo.exists())
print (str(novo_arquivo))
with novo_arquivo.open() as f:
    f.readline()'''