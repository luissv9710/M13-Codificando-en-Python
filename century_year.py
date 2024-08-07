# **************************
# BUSCANDO EL SIGLO ADECUADO
# **************************
import math


def run(year: int) -> int:
    # TU CÓDIGO AQUÍ
    century = math.ceil(year / 100)

    return century


if __name__ == '__main__':
    run(1705)