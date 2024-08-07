# ***************
# ÁREA DEL ANILLO
# ***************


def run(z: float) -> float:
    # TU CÓDIGO AQUÍ
    PI = 3.14

    white_area = (PI * (z+(z/2))**2) - (PI * (z/2)**2)

    return white_area


if __name__ == '__main__':
    run(6)