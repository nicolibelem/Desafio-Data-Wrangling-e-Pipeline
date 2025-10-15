#Remover ou corrigir preços negativos
if 'preco_unitario' in df.columns:
    df = df[df['preco_unitario'] >= 0]

#Criar uma nova coluna valor_total = quantidade * preco_unitario
if 'quantidade' in df.columns and 'preco_unitario' in df.columns:
    df['valor_total'] = df['quantidade'] * df['preco_unitario']
