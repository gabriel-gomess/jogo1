import pygame, sys
from button import Button
from random import randint
from pygame import display
from pygame.image import load
from pygame.sprite import Sprite, Group, GroupSingle, groupcollide
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE, K_LCTRL
from pygame.time import Clock
from pygame import font

pygame.init()

# Musica inicio
pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('musica_menu.wav')
pygame.mixer.music.play(-1)
# Musica fim


TELA = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("O Menino Leitor")

BG = pygame.image.load("fundomenu.png")

icon = pygame.image.load("boneco.png")
pygame.display.set_icon(icon)


def get_font(size):
    return pygame.font.Font("8-BIT WONDER.TTF", size)


def jogar():
    while True:
        JOGAR_MOUSE_POS = pygame.mouse.get_pos()

        TELA.fill("black")

        JOGAR_TEXT = get_font(45).render("Jogo", True, "Black")
        JOGAR_RECT = JOGAR_TEXT.get_rect(center=(640, 260))
        TELA.blit(JOGAR_TEXT, JOGAR_RECT)

        JOGAR_BACK = Button(image=None, pos=(640, 460),
                            text_input="VOLTAR", font=get_font(75), base_color="#368170", hovering_color="White")

        JOGAR_BACK.changeColor(JOGAR_MOUSE_POS)
        JOGAR_BACK.update(TELA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if JOGAR_BACK.checkForInput(JOGAR_MOUSE_POS):
                    main_menu()

        pygame.display.update()

        # Acerto inicio
        acerto_pedra = pygame.mixer.Sound('musica_acerto.wav')
        acerto_pedra.set_volume(0.8)
        # Acerto fim

        tamanho = 1280, 720
        fonte = font.Font("8-BIT WONDER.TTF", 25)
        fonte_perdeu = font.Font("8-BIT WONDER.TTF", 55)
        FPS = 120
        BRANCO = (255, 255, 255)
        VERMELHO = (255, 0, 0)
        PRETO = (0, 0, 0)
        timer = 0
        tempo_segundo = 0

        superficie = display.set_mode(
            size=tamanho
        )
        fundo = load('fundojogo.png')
        display.set_caption(
            'O Menino Leitor'
        )

        # Contator de segundos
        texto = fonte.render("Tempo ", True, (BRANCO), (PRETO))
        pos_texto = texto.get_rect()
        pos_texto.center = (86, 82)

        class Boneco(Sprite):
            def __init__(self, pedra):
                super().__init__()

                self.image = load('boneco.png')
                self.rect = self.image.get_rect(
                    center=(200, randint(150, 150))
                )
                self.pedra = pedra
                self.velocidade = 5

            def jogar_pedra(self):
                if len(self.pedra) < 10:
                    self.pedra.add(
                        Pedra(*self.rect.center)
                    )
                if mortes >= 20:
                    self.pedra.add(
                        Pedra(*self.rect.center)
                    )

            def update(self):
                keys = pygame.key.get_pressed()

                pedra_fonte = fonte.render(
                    f'Pedras  {10 - len(self.pedra)}',
                    True,
                    (BRANCO), (PRETO)
                )
                superficie.blit(pedra_fonte, (10, 10))

                # Movimento nas teclas
                if keys[pygame.K_LEFT]:
                    self.rect.x -= self.velocidade
                if keys[pygame.K_RIGHT]:
                    self.rect.x += self.velocidade
                if keys[pygame.K_UP]:
                    self.rect.y -= self.velocidade
                if keys[pygame.K_DOWN]:
                    self.rect.y += self.velocidade


                # Sprite se mant??m na tela
                if self.rect.right > 1280:
                    self.rect.right = 720
                if self.rect.left < 0:
                    self.rect.left = 0
                if self.rect.bottom > 720:
                    self.rect.bottom = 720
                if self.rect.top < 80:
                    self.rect.top = 80

        class Pedra(Sprite):
            def __init__(self, x, y):
                super().__init__()

                self.image = load('pedra.png')
                self.rect = self.image.get_rect(
                    center=(x, y)
                )

            def update(self):
                self.rect.x += 4

                if self.rect.x > tamanho[0]:
                    self.kill()

        class Vilao(Sprite):
            def __init__(self):
                super().__init__()

                self.image = load('vilao.png')
                self.rect = self.image.get_rect(
                    center=(1280, randint(85, 710))
                )

            def update(self):
                self.rect.x -= 0.1

                if self.rect.x == 0:
                    self.kill()
                    global perdeu
                    perdeu = True

        class Vilao2(Sprite):
            def __init__(self):
                super().__init__()

                self.image = load('vilao2.png')
                self.rect = self.image.get_rect(
                    center=(1280, randint(85, 710))
                )

            def update(self):
                self.rect.x -= 0.1

                if self.rect.x == 0:
                    self.kill()
                    global perdeu
                    perdeu = True

        class Vilao3(Sprite):
            def __init__(self):
                super().__init__()

                self.image = load('vilao3.png')
                self.rect = self.image.get_rect(
                    center=(1280, randint(85, 710))
                )

            def update(self):
                self.rect.x -= 0.1

                if self.rect.x == 0:
                    self.kill()
                    global perdeu
                    perdeu = True

        grupo_inimigos = Group()
        grupo_pedra = Group()
        boneco = Boneco(grupo_pedra)
        grupo_boneco = GroupSingle(boneco)

        grupo_inimigos.add(Vilao())

        clock = Clock()
        mortes = 0
        round = 0
        perdeu = False

        while True:
            clock.tick(FPS)

            if round % 120 == 0:
                if mortes < 20:
                    grupo_inimigos.add(Vilao())
                if mortes > 20:
                    grupo_inimigos.add(Vilao2())
                if mortes > 30:
                    grupo_inimigos.add(Vilao3())
            print(mortes)

            # Eventos
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        boneco.jogar_pedra()

                if event.type == KEYUP:
                    if event.key == K_LCTRL:
                        boneco.image = load('bonecoup.png.png')
                        boneco.velocidade = 7


            if groupcollide(grupo_pedra, grupo_inimigos, True, True):
                mortes += 1
                acerto_pedra.play()

            if groupcollide(grupo_boneco, grupo_inimigos, True, True):
                fim = fonte_perdeu.render(
                    'GAME OVER',
                    True,
                    (VERMELHO)
                )
                superficie.blit(fim, (420, 330))
                display.update()
                pygame.time.delay(4500)

            if timer < 140:
                timer += 1
            else:
                tempo_segundo += 1
                texto = fonte.render("Tempo  " + str(tempo_segundo), True, (BRANCO), (PRETO))
                timer = 0

            # Display
            superficie.blit(fundo, (0, 0))

            fonte_mortes = fonte.render(
                f'Acertos  {mortes}',
                True,
                (BRANCO), (PRETO)
            )

            superficie.blit(fonte_mortes, (10, 40))
            grupo_boneco.draw(superficie)
            grupo_inimigos.draw(superficie)
            grupo_pedra.draw(superficie)
            superficie.blit(texto, pos_texto)

            grupo_boneco.update()
            grupo_inimigos.update()
            grupo_pedra.update()


            if perdeu:
                fim = fonte_perdeu.render(
                    'GAME OVER',
                    True,
                    (VERMELHO)
                )
                superficie.blit(fim, (210, 20))
                display.update()
                pygame.time.delay(4500)

            round += 1
            display.update()


def op??oes():
    while True:
        OP??OES_MOUSE_POS = pygame.mouse.get_pos()

        TELA.fill("#b7c1e5")

        OP??OES_TEXT = get_font(45).render("Gabriel Gomes", True, "#3c4c6c")


        OP??OES_RECT = OP??OES_TEXT.get_rect(center=(640, 220))
        TELA.blit(OP??OES_TEXT, OP??OES_RECT)



        OP??OES_BACK = Button(image=None, pos=(640, 460),
                             text_input="VOLTAR", font=get_font(75), base_color="#1a2656", hovering_color="Black")

        OP??OES_BACK.changeColor(OP??OES_MOUSE_POS)
        OP??OES_BACK.update(TELA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OP??OES_BACK.checkForInput(OP??OES_MOUSE_POS):
                    main_menu()


        pygame.display.update()


def main_menu():
    while True:
        TELA.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("MENU PRINCIPAL", True, "#7088c0")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        JOGAR_BUTTON = Button(image=pygame.image.load("Jogar Rect.png"), pos=(640, 250),
                              text_input="JOGAR", font=get_font(55), base_color="#b7c1e5", hovering_color="White")
        OP??OES_BUTTON = Button(image=pygame.image.load("Op??oes Rect.png"), pos=(640, 400),
                               text_input="CREDITOS", font=get_font(55), base_color="#b7c1e5", hovering_color="White")
        FECHAR_BUTTON = Button(image=pygame.image.load("Jogar Rect.png"), pos=(640, 550),
                               text_input="FECHAR", font=get_font(55), base_color="#b7c1e5", hovering_color="White")

        TELA.blit(MENU_TEXT, MENU_RECT)

        for button in [JOGAR_BUTTON, OP??OES_BUTTON, FECHAR_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(TELA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if JOGAR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    jogar()
                if OP??OES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    op??oes()
                if FECHAR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()


main_menu()
