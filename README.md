# 🟩 EduChain — Blockchain Educacional em Python

Este é um projeto educacional onde construí uma blockchain do zero utilizando apenas Python, com o objetivo de entender passo a passo como funcionam as bases de blockchains reais como Bitcoin, Ethereum, Cosmos e Xion.

Sem frameworks, sem SDKs — apenas terminal, lógica, criptografia e agora Proof-of-Work real.

🚀 Funcionalidades Implementadas
✔️ Estrutura completa de um bloco

index

timestamp

data

previous_hash

nonce

hash (SHA-256)

✔️ Encadeamento real entre blocos

Cada bloco sempre aponta para o hash do anterior.

✔️ Hashing usando SHA-256

Mesma base criptográfica das blockchains tradicionais.

✔️ Validação completa da blockchain

Se qualquer bloco for alterado → a cadeia inteira se torna inválida.

✔️ Geração automática de novos blocos

O script cria blocos sequenciais automaticamente.

✔️ Proof-of-Work (PoW) real

Agora a EduChain exige que cada bloco atenda uma dificuldade personalizada definida por um prefixo, como:

010101

E exibe em tempo real:

Tentativas
Hash atual
Tempo total
Velocidade média (hashes/s)
Nonce encontrado
Hash válido final
Exemplo real do terminal:

⛏️ Minerando bloco...
Tentativas: 27,690,000 | Hash atual: c0f44fa23d8c...
⏱️ Tempo total: 45.18 segundos
⚡ Velocidade média: 613,235 hashes/s
✔️ Bloco minerado! Nonce encontrado: 27,704,036
🔗 Hash válido: 0101017662f3da39dad713dd6...



## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório:

```bash
git clone https://github.com/Eduprogrammer/EduChain-Python.git
cd EduChain-Python

2️⃣ Execute o script principal:

python3 block.py

ou

python block.py

E troque a dificuldade dentro do arquivo, por exemplo:
difficulty = "010101"
ou:
difficulty = "0000"


3️⃣ Você verá algo como:

--- Bloco ---
Index: 0
Dados: Bloco Gênesis
Hash: ...
Hash anterior: 0

Blockchain é válida? True


🎯 Objetivo do Projeto

A EduChain foi criada para ensinar, de forma prática e transparente:

Como blocos são estruturados
Como funciona o encadeamento via hash
Como uma blockchain mantém imutabilidade
O papel da criptografia SHA-256
Como Proof-of-Work realmente funciona
Como a rede valida cada bloco

Tudo explicado de maneira simples e evolutiva.

🔄 Próximas Evoluções da EduChain

A blockchain continuará evoluindo com:

⛏️ Dificuldade dinâmica (igual ao Bitcoin)
🌐 Rede P2P simples
🔐 Transações assinadas com chaves privadas
🧪 API para rodar como um Node
📦 Persistência dos blocos em arquivo ou banco
🦀 Versão completa em Rust (alta performance)
📡 Simulação de ataque 51%

📬 Contato

Quer conversar sobre blockchain, Python, Rust, Web3, Xion, CosmWasm ou desenvolvimento em geral?

Me chama no LinkedIn 👇
https://www.linkedin.com/in/educarlos29/

Aprendizado constante. Construção constante. 🟩
