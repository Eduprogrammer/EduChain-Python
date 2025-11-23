import hashlib
import time

# Construtor do bloco: define o que um bloco contém

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index   # Posição do bloco na cadeia
        self.timestamp = timestamp    # Momento exato da criação
        self.data = data    # Informações armazenadas no bloco
        self.previous_hash = previous_hash  # Hash do bloco anterior
        self.hash = self.calculate_hash()   # Hash calculado a partir dos dados do bloco


# Função que gera o hash único do bloco

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"

        # Gera o hash usando SHA-256 
        return hashlib.sha256(block_string.encode()).hexdigest()
# Criando o bloco gênesis (primeiro bloco da chain)
genesis_block = Block(
    index=0,    # Posição inicial
    timestamp=time.time(),   # Momento atual
    data="Bloco Gênesis",   # Dado especial do primeiro bloco
    previous_hash="0"      # Como não há bloco anterior, o hash é "0"
)

print("Hash do bloco gênesis:", genesis_block.hash)
print("Dados:", genesis_block.data)
print("Timestamp:", genesis_block.timestamp)    
print("Index:", genesis_block.index)
print("Hash anterior:", genesis_block.previous_hash)



class Blockchain:
    def __init__(self):
        # a blockchain começa com apenas o bloco gênesis
        self.chain = [self.create_genesis_block()]

     # Função que cria o bloco gênesis 
    def create_genesis_block(self):
        return Block(
            index=0,
            timestamp=time.time(),
            data="Bloco Gênesis",
            previous_hash="0"
        )
    # Retorna o último bloco da cadeia
    def get_last_block(self):
        return self.chain[-1]

    # Adiciona um novo bloco na blockchain
    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=last_block.hash
        )

        # Insere o novo bloco na cadeia
        self.chain.append(new_block)

    # Verifica se a blockchain inteira está válida
    def is_chain_valid(self):
        # Começa no bloco 1, porque o bloco 0 (gênesis) não tem anterior
        for i in range(1, len(self.chain)):
            current = self.chain[i] # bloco atual
            previous = self.chain[i - 1] # bloco anterior

            # verifica se o hash atual está correto
            if current.hash != current.calculate_hash():
                return False

            # Verifica se o "previous_hash" aponta corretamente para o bloco anterior
            if current.previous_hash != previous.hash:
                return False
        # Se passou por todas verificações, a cadeia é válida
        return True

      


# Criando a blockchain
my_chain = Blockchain()

# adicionando 3 blocos
my_chain.add_block("Primeiro bloco após o gênesis")
my_chain.add_block("Segundo bloco")
my_chain.add_block("Terceiro bloco")

# imprimindo todos os blocos
for block in my_chain.chain:
    print("\n--- Bloco ---")
    print("Index:", block.index)
    print("Timestamp:", block.timestamp)
    print("Dados:", block.data)
    print("Hash:", block.hash)
    print("Hash anterior:", block.previous_hash)
    print("\nBlockchain é válida?", my_chain.is_chain_valid())
      

    