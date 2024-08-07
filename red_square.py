# ****************
# EL CUADRADO ROJO
# ****************

def run(arc_A: float) -> float:
    # TU CÓDIGO AQUÍ
    PI = 3.14
    area = round(((arc_A * 2)/PI)**2,10)
    return area


if __name__ == '__main__':
    run(1)