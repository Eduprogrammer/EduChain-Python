from block import Block
import time

print("\n=== 🧪 Teste de Mineração (PoW) com Logs em Tempo Real ===")

difficulty = input("Digite o prefixo de dificuldade (ex: 1234, 0000, ED000): ")

b = Block(
    index=0,
    timestamp=time.time(),
    data="Bloco de Teste PoW",
    previous_hash="0"
)

print(f"\n⛏️ Iniciando teste com dificuldade: '{difficulty}'")

start_time = time.time()
attempts = 0

# Mineração com logs a cada 1000 tentativas
while not b.hash.startswith(difficulty):
    b.nonce += 1
    attempts += 1
    b.hash = b.calculate_hash()

    # LOG a cada 1000 tentativas
    if attempts % 1000 == 0:
        elapsed = time.time() - start_time
        speed = attempts / elapsed if elapsed > 0 else 0

        print(f"Tentativas: {attempts:,} | Hash parcial: {b.hash[:12]}... | Velocidade: {speed:,.0f} H/s")

end_time = time.time()
total_time = end_time - start_time
speed = attempts / total_time

print("\n=== RESULTADO FINAL ===")
print(f"✔️ Hash encontrado após {attempts:,} tentativas")
print(f"⏱️ Tempo total: {total_time:.2f} segundos")
print(f"⚡ Velocidade média: {speed:,.0f} hashes/s")
print(f"🔗 Hash válido: {b.hash}")
print(f"Nonce encontrado: {b.nonce}")
print("=========================\n")
