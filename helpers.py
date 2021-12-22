def juros_compostos (principal, taxa, periodo):
    """
    Fuçãp para calculo de juros compostos
    Juros compostos: P(1 + R / 100)t
    onde,
    P é quantidade principal
    R é a taxa
    T é o tempo, periodo
    :param principal:
    :param taxa:
    :param pariodo:
    :return:
    """
    calculo_juros = principal * (pow((1 + taxa / 100),periodo))
    return calculo_juros