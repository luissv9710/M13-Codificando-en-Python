# **********************
# ANIMALES SUPER RÁPIDOS
# **********************
import math


def run(speed_km_h: float) -> float:
    # TU CÓDIGO AQUÍ
    speed_cm_s = math.trunc(speed_km_h*(250/9))

    return speed_cm_s


if __name__ == '__main__':
    run(1.08)