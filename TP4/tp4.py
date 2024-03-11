import re

token_patterns = {
    'SELECT': r'[Ss][Ee][Ll][Ee][Cc][Tt]',
    'FROM': r'[fF][Rr][Oo][Mm]',
    'WHERE': r'[Ww][Hh][Ee][Rr][Ee]',
    'Virgula': r',',
    'Operador': r'>=',
    'Identificador': r'[a-zA-Z_]\w*',
    'Número': r'\d+',
    'IGNORE': r'\s+',
}

def tokenize_file(file_path):
    tokens = []

    with open(file_path, 'r') as file:
        data = file.read()

    token_specification = [(t, p) for t, p in token_patterns.items()]

    while data:
        for token_type, pattern in token_specification:
            match = re.match(pattern, data)
            if match:
                if token_type != 'IGNORE':
                    tokens.append((token_type, match.group()))
                data = data[match.end():]
                break
        else:
            print(f"Illegal character '{data[0]}'")
            data = data[1:]

    return tokens

file_path = 'input.txt'
result_tokens = tokenize_file(file_path)

for token in result_tokens:
    print(token)

