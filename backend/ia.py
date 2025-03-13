class IA:
    def __init__(self):
        self.historico = {}

    def registrar_tentativa(self, numero, resultado):
        if numero not in self.historico:
            self.historico[numero] = {'acertos': 0, 'tentativas': 0}
        self.historico[numero]['tentativas'] += 1
        if resultado:
            self.historico[numero]['acertos'] += 1

    def prever(self):
        if not self.historico:
            return 50  # chute inicial no meio
        melhores = sorted(self.historico.items(),
                          key=lambda x: x[1]['acertos']/x[1]['tentativas'],
                          reverse=True)
        return melhores[0][0]
