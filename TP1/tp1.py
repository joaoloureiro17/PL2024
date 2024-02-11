# Função para calcular o escalão etário
def calcular_escalao_etario(idade):
    return f"[{((idade - 1) // 5) * 5 + 1}-{((idade - 1) // 5) * 5 + 5}]"

# Leitura do arquivo excluindo a primeira linha (cabeçalho)
with open('emd.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()[1:]

# Lista ordenada alfabeticamente das modalidades desportivas
modalidades = sorted(set([linha.split(',')[8].strip() for linha in linhas if linha.split(',')[8].strip() != 'modalidade']))

# Contagem de atletas aptos e inaptos
total_atletas = len(linhas)
aptos = sum(1 for linha in linhas if linha.split(',')[12].strip().lower() == 'true')
inaptos = total_atletas - aptos

# Percentagens de atletas aptos e inaptos
percentagem_aptos = (aptos / total_atletas) * 100
percentagem_inaptos = (inaptos / total_atletas) * 100

# Distribuição de atletas por escalão etário
idades_atletas = [int(linha.split(',')[5].strip()) for linha in linhas]
escaloes_etarios = {intervalo: 0 for intervalo in range(0, 100, 5)}

for idade in idades_atletas:
    for intervalo in range(0, 100, 5):
        if intervalo <= idade <= intervalo + 4:
            escaloes_etarios[intervalo] += 1
            break

# Calcular total de atletas
total_atletas = len(idades_atletas)

# Filtrar os intervalos sem atletas
escaloes_etarios = {intervalo: quantidade for intervalo, quantidade in escaloes_etarios.items() if quantidade > 0}

# Exibição dos resultados
print("Lista das modalidades desportivas:")
print("[" + ",".join(modalidades) + "]")

print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
print(f"Percentagem de aptos: {percentagem_aptos:.2f}%")
print(f"Percentagem de inaptos: {percentagem_inaptos:.2f}%")

# Exibição dos resultados
print("\nDistribuição de atletas por escalão etário:")
for intervalo, quantidade in escaloes_etarios.items():
    percentagem = (quantidade / total_atletas) * 100
    print(f"[{intervalo}-{intervalo + 4}]: {quantidade} atletas ({percentagem:.2f}%)")
