from matplotlib import pyplot as plt
from tempo_pack.tempo import f_tempo, f_boxplot

def f_complexidade(funcao, lista_inputs, n_vezes):
    dic_stats = {}
    dic_tempos = {}
    resultados = []

    for entrada in lista_inputs:
        tempos, tempo_medio, desvio_padrao = f_tempo(funcao, entrada, n_vezes)
        resultados.append((entrada, tempo_medio, desvio_padrao))

    for entrada, tempo_medio, desvio_padrao in resultados:
        dic_stats[entrada] = (tempo_medio, desvio_padrao)
        dic_tempos[entrada] = tempos

    return dic_stats, dic_tempos


def f_complexidade_boxplot(dic_tempos):

    fig, ax = plt.subplots()
    ax.boxplot(dic_tempos.values())
    ax.set_xticklabels(dic_tempos.keys())
    ax.set_xlabel('valor do input n da função f(n)')
    ax.set_ylabel('tempo de execução da função f(n) [s]')
    ax.set_title("Estudo da variação do tempo de execução \nda função f(n), para vários valores de n")

    ax.legend(dic_tempos.keys())


    return plt.show()