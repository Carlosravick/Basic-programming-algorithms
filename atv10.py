import pandas as pd


data = {
    'Nome': ['Ana', 'João', 'Maria', None, 'Luiza'],
    'Idade': [25, None, 22, 28, None],
    'Cidade': ['São Paulo', 'Rio de Janeiro', None, 'Curitiba', 'Rio de Janeiro']
}

df = pd.DataFrame(data)


print(df.isnull())