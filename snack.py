import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 950
altura = 500
x_cobra = largura/2
y_cobra = altura/2
tamanho = 20
tamanho2 = 20
pontos = 0

x_apple = randint(0,950)
y_apple = randint(0, 500)

velocidade = 10
x_controle = velocidade
y_controle = 0

pygame.mixer.music.set_volume(0.1) #valores aceitos entre 0 e 1, assim consegue controlar o som da musica
musicadefundo = pygame.mixer.music.load('teste1.mp3')
pygame.mixer.music.play(-1) # toca a musica com o parametro -1 a musica fica tocando automaticamente

barulhodecolisao = pygame.mixer.Sound('smw_kick.wav') # todos os barulhos de fundo tem que ter a extensao .wav

# pygame.font.get_fonts() #Retorna as fontes que tenho no sistema.

fonte = pygame.font.SysFont('arial', 40, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

comprimentocobra = 1
listaCobra = []

def desenhaCobra(listaCobra):
    if len(listaCobra) > comprimentocobra:
        del listaCobra[0]
        for xey in listaCobra:
            pygame.draw.rect(tela, (255,0,255), (xey[0],xey[1], tamanho,tamanho2))

while True:
    relogio.tick(20)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}' # define a mensagem
    texto_formatado = fonte.render(mensagem, True, (255,0,255)) #defina o rederizamento da fonte e cor
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        
        #reconhece a tecla que foi clicada mais nao a se segurar
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0


    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
        

    # if pygame.key.get_pressed()[K_a]:
    #     x_cobra = x_cobra - 20
    # if pygame.key.get_pressed()[K_d]:
    #     x_cobra = x_cobra + 20

    # if pygame.key.get_pressed()[K_w]:
    #     y_cobra = y_cobra - 20
    # if pygame.key.get_pressed()[K_s]:
    #     y_cobra = y_cobra + 20

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura 

    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura


    snack = pygame.draw.rect(tela, (255,0,255), (x_cobra,y_cobra, tamanho,tamanho2))
    apple = pygame.draw.rect(tela, (255,0,0), (x_apple, y_apple, 20, 20))

    if snack.colliderect(apple):
        x_apple = randint(0,950)
        y_apple = randint(0, 500)
        pontos = pontos + 1
        barulhodecolisao.play()
        comprimentocobra = comprimentocobra + 1
        # tamanho = tamanho + 50

    listaCabeca = []
    listaCabeca.append(x_cobra)
    listaCabeca.append(y_cobra)
    listaCobra.append(listaCabeca)
    desenhaCobra(listaCobra)

    # if y == altura:
    #     y = 0
    #     x = x + 5
    # else:
    #     y = y + 1
    tela.blit(texto_formatado, (650, 40)) #mostra o texto na tela
    pygame.display.update()
