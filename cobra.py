import pygame, random
from pygame.locals import *


# função para posição da maça
def maçarandom():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return (x * 10, y * 10)


def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


# movimento cobra.
CIMA = 8
DIREITA = 4
BAIXO = 2
ESQUERDA = 6

pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Cobrinha')

cobra = [(200, 200), (210, 200), (220, 200)]
pele_cobra = pygame.Surface((10, 10))
pele_cobra.fill((100, 200, 170))

pos_maça = maçarandom()
maça = pygame.Surface((10, 10))
maça.fill((255, 0, 0))

direcao = ESQUERDA

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
ponto = 0

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != BAIXO:
                direcao = CIMA
            if event.key == K_DOWN and direcao != CIMA:
                direcao = BAIXO
            if event.key == K_LEFT and direcao != DIREITA:
                direcao = ESQUERDA
            if event.key == K_RIGHT and direcao != ESQUERDA:
                direcao = DIREITA

    if colisao(cobra[0], pos_maça):
        pos_maça = maçarandom()
        cobra.append((0, 0))
        ponto = ponto + 1

    # checa se bateu na parede
    if cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0:
        game_over = True
        break

    # checa se comeu o proprio rabo
    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])

    # movimento da cobra
    if direcao == CIMA:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == BAIXO:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == DIREITA:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao == ESQUERDA:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    tela.fill((0, 0, 0))
    tela.blit(maça, pos_maça)

    for x in range(0, 600, 10):  # linhas horizontais
        pygame.draw.line(tela, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):  # linhas verticais
        pygame.draw.line(tela, (40, 40, 40), (0, y), (600, y))

    fonte_ponto = font.render('Pontos: %s' % (ponto), True, (255, 255, 255))
    ponto_rect = fonte_ponto.get_rect()
    ponto_rect.topleft = (600 - 120, 10)
    tela.blit(fonte_ponto, ponto_rect)

    for pos in cobra:
        tela.blit(pele_cobra, pos)

    pygame.display.update()

while True:
    gameover_fonte = pygame.font.Font('freesansbold.ttf', 75)
    gameover_tela = gameover_fonte.render('Game Over', True, (255, 255, 255))
    gameover_rect = gameover_tela.get_rect()
    gameover_rect.midtop = (600 / 2, 10)
    tela.blit(gameover_tela, gameover_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()