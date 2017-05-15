#Definindo o Nº de Jogadores
def jogadores(n_jogadores):
    if n_jogadores < 3:
        raise ValueError("O jogo deve ter pelo menos 3 jogadores!")
    elif n_players > 5:
        raise ValueError("O número máximo de jogadores é 5!")

    # Define player class
    class Jogador(object):

        def __init__(self, jogador_id):
            self.id = jogador_id  #Identifica o Jogador
            self.dinheiro = 2000  #Dinheiro Inicial
            self.propriedades = []  #Propriedades
            self.posicao = 0  #Posição no Tabuleiro
            self.prisao_cartas = 0  #Número de cartas disponíveos p/ sair da prisão
            self.prisao_rodadas = 0  #Número de rodadas sem jogar
            self.prisao_estrategia = ''  #Estratégia Prisão

#Mover Jogadores no Tabuleiro
        def mover(self, roll, verbose=False):
            self.posicao += roll
            if self.posicao >= 40:
                self.posicao -= 40
                self.dinheiro += 200
            if verbose:
                print
                'Jogador, {} vá para a casa: {}'.format(self.id, self.posicao)
#Comprar
        def comprar(self, prop_id, valor):
            self.propriedades.append(prop_id)
            self.dinheiro -= valor

        # Pay another player
        def pagamento(self, beneficiario, pagamento):
            if self.dinheiro > pagamento:
                self.dinheiro -= pagamento
                jogadores[beneficiario].dinheiro += pagamento
            else:
                jogadores[beneficiario].dinheiro += self.dinheiro
                self.default(beneficiario, pagamento)

#Cadeia
        def ir_para_cadeia(self):
            self.posicao = 10
            self.prisao_rodadas = 2

