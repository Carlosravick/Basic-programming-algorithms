import pandas as pd


data = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro', 'Luiza'],
    'Idade': [25, 30, 22, 28, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Curitiba', 'Rio de Janeiro']
}

df = pd.DataFrame(data)


coluna_nome = df['Nome']


filtro_idade = df[df['Idade'] > 25]


print("Coluna 'Nome':")
print(coluna_nome)
print("\nLinhas onde a 'Idade' é maior que 25:")
print(filtro_idade)