# ***
# XOR
# ***


def run(v1: bool, v2: bool) -> bool:
    # TU CÓDIGO AQUÍ
    if (v1 is False and v2 is True) or (v1 is True and v2 is False):
        xor = True
    else:
        xor = False

    return xor


if __name__ == '__main__':
    run(False, False)