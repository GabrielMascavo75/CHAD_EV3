from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from time import sleep

# --- Motores ---
perna_direita  = LargeMotor(OUTPUT_B)
perna_esquerda = LargeMotor(OUTPUT_C)
bracos         = MediumMotor(OUTPUT_A)

# --- Sensor de toque na porta 1 ---
botao = TouchSensor(INPUT_1)

# --- Parametros ---
repeticoes = 15
vel = 15
vel_rapida = 35
angulo = -20
angulo_curto = -16

# --- Parametros dos bracos ---
vel_braco = 25
angulo_braco = 30
angulo_braco_curto = 30


def danca():
    """Executa a coreografia uma vez."""
    perna_direita.reset()
    perna_esquerda.reset()
    bracos.reset()

    for i in range(repeticoes):
        print("--- Repeticao {} de {} ---".format(i + 1, repeticoes))

        # ===== BRACOS: levantam =====
        bracos.on_for_degrees(speed=vel_braco, degrees=angulo_braco_curto)
        bracos.on_for_degrees(speed=vel_braco, degrees=-angulo_braco_curto)

        # Acao 5: chute rapido com a direita
        perna_direita.on_for_degrees(speed=vel_rapida, degrees=angulo_curto)
        perna_direita.on_for_degrees(speed=vel_rapida, degrees=-angulo_curto)

        # ===== BRACOS: voltam =====
        bracos.on_for_degrees(speed=vel_braco, degrees=angulo_braco)

        # Acao 6: chute rapido com a esquerda
        perna_esquerda.on_for_degrees(speed=vel_rapida, degrees=angulo_curto)
        perna_esquerda.on_for_degrees(speed=vel_rapida, degrees=-angulo_curto)

        sleep(0.1)

    print("Danca concluida!")


def soltar_motores():
    """Solta os motores sem freio."""
    perna_direita.reset()
    perna_esquerda.reset()
    bracos.reset()

    perna_direita.stop_action = 'coast'
    perna_esquerda.stop_action = 'coast'
    bracos.stop_action = 'coast'

    perna_direita.stop()
    perna_esquerda.stop()
    bracos.stop()


# ===== PROGRAMA PRINCIPAL =====
print("Aguardando toque no sensor da porta 1...")

try:
    while True:
        botao.wait_for_pressed()
        print("Toque detectado! Iniciando danca...")

        # --- Executa a danca ---
        danca()

        # --- Solta os motores ao final ---
        soltar_motores()
        print("Motores soltos. Aguardando novo toque...\n")

        sleep(0.1)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuario.")

finally:
    soltar_motores()
    print("Programa encerrado.")