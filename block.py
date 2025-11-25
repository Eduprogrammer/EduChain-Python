import hashlib
import time

# Construtor do bloco: define o que um bloco contém

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index                    # Posição do bloco na cadeia
        self.timestamp = timestamp            # Momento exato da criação
        self.data = data                      # Informações armazenadas no bloco
        self.previous_hash = previous_hash    # Hash do bloco anterior
        
        # Nonce começa em zero e será incrementado até encontrar um hash que iremos definir.
        self.nonce = 0
        
        # Gera o hash usando SHA-256 sem mineiração
        self.hash = self.calculate_hash()

    # Função que gera o hash único do bloco
    # O hash é calculado usando:
    # - index
    # - timestamp
    # - data
    # - previous_hash
    # - nonce
    #  Cada mudança no nonce gera um hash completamente novo.
        
    def calculate_hash(self):
     
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}" #aqui entra o nonce que não tinha 
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Função de mineração (Proof-of-Work)
    def mine_block(self, difficulty_prefix):
        """
        Função de mineração (Proof-of-Work) 
        Tenta encontrar um hash que comece com a dificuldade desejada (ex: '1234').
        """

        print(f"\n⛏️ Minerando bloco... buscando hash que comece com '{difficulty_prefix}'")

        start_time = time.time()     # marca tempo inicial
        attempts = 0                # contador de tentativas

        # Loop até acertar a dificuldade
        while not self.hash.startswith(difficulty_prefix):
            self.nonce += 1
            attempts += 1
            self.hash = self.calculate_hash()

            # calcula a cada 10.000 tentativas
            if attempts % 10000 == 0:
                print(f"Tentativas: {attempts:,} | Hash atual: {self.hash[:12]}...")

        # Tempo total
        end_time = time.time()
        total_time = end_time - start_time

        # Velocidade (hashes por segundo)
        if total_time > 0:
            speed = attempts / total_time
        else:
            speed = attempts

        print(f"⏱️ Tempo total: {total_time:.2f} segundos")
        print(f"⚡ Velocidade média: {speed:,.2f} hashes/s")
        print(f"✔️ Bloco minerado! Nonce encontrado: {self.nonce}")
        print(f"🔗 Hash válido: {self.hash}")


# Classe Blockchain: controla toda a cadeia

class Blockchain:
    def __init__(self):
        # A blockchain inicia somente com o bloco gênesis
        self.chain = [self.create_genesis_block()]

    # Função que cria o bloco gênesis
    def create_genesis_block(self):
        return Block(
            index=0,
            timestamp=time.time(),
            data="Bloco Gênesis",
            previous_hash="0"
        )

    # Retorna o bloco mais recente da cadeia
    def get_last_block(self):
        return self.chain[-1]

    # Adiciona um novo bloco à blockchain
    def add_block(self, data):
        last_block = self.get_last_block()

        # Cria um novo bloco usando o hash do bloco anterior
        new_block = Block(
            index=last_block.index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=last_block.hash
        )

        # A parte mais interessante, é aqui que definimos a dificuldade da rede.
        #  Vou usar "ED000" para começar.
        difficulty = "010101"

        print(f"\n🚧 Iniciando mineração do bloco {new_block.index} com dificuldade '{difficulty}'")
        new_block.mine_block(difficulty)

        # Depois de minerado, aí sim adiciona à cadeia
        self.chain.append(new_block)
        print(f"✅ Bloco {new_block.index} adicionado à blockchain!")


    # Verifica se toda a cadeia está válida
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Verifica o hash do bloco atual
            if current.hash != current.calculate_hash():
                return False

            # Verifica se o "previous_hash" está correto
            if current.previous_hash != previous.hash:
                return False

        return True



#  PROTEÇÃO: código abaixo só roda quando chamar python block.py
#  NÃO roda quando o arquivo é importado (ex: from block import Block)


if __name__ == "__main__":

    # Criando a blockchain
    my_chain = Blockchain()

    # adicionando 3 blocos (sem PoW por enquanto)
    my_chain.add_block("Primeiro bloco após o gênesis")
    my_chain.add_block("Segundo bloco")
    my_chain.add_block("Terceiro bloco")

    # Impressão dos blocos
    for block in my_chain.chain:
        print("\n--- Bloco ---")
        print("Index:", block.index)
        print("Timestamp:", block.timestamp)
        print("Dados:", block.data)
        print("Hash:", block.hash)
        print("Hash anterior:", block.previous_hash)

    print("\nBlockchain é válida?", my_chain.is_chain_valid())
