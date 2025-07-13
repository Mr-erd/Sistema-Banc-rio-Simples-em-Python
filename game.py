import pygame
import random

# --- Constantes ---
# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
ROSA = (255,182,193)

# Dimensões da tela e do bloco
LARGURA_BLOCO = 30
ALTURA_BLOCO = 30
LARGURA_TELA = 25 * LARGURA_BLOCO
ALTURA_TELA = 28 * ALTURA_BLOCO

# --- Classes do Jogo ---

class Parede(pygame.sprite.Sprite):
    """ Classe que representa as paredes do labirinto """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([LARGURA_BLOCO, ALTURA_BLOCO])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Pilula(pygame.sprite.Sprite):
    """ Classe que representa as pílulas que o Pac-Man come """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([LARGURA_BLOCO // 4, ALTURA_BLOCO // 4])
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = x + LARGURA_BLOCO // 2
        self.rect.centery = y + ALTURA_BLOCO // 2

class Personagem(pygame.sprite.Sprite):
    """ Classe base para o Pac-Man e os Fantasmas """
    def __init__(self, cor, x, y):
        super().__init__()
        self.image = pygame.Surface([LARGURA_BLOCO, ALTURA_BLOCO])
        self.image.fill(PRETO)
        self.image.set_colorkey(PRETO) # Torna o fundo preto transparente
        pygame.draw.circle(self.image, cor, (LARGURA_BLOCO // 2, ALTURA_BLOCO // 2), LARGURA_BLOCO // 2)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel_x = 0
        self.vel_y = 0
        self.paredes = None

    def update(self):
        # Move na horizontal
        self.rect.x += self.vel_x
        # Verifica colisão com paredes
        colisoes = pygame.sprite.spritecollide(self, self.paredes, False)
        for parede in colisoes:
            if self.vel_x > 0: # Movendo para a direita
                self.rect.right = parede.rect.left
            else: # Movendo para a esquerda
                self.rect.left = parede.rect.right
        
        # Move na vertical
        self.rect.y += self.vel_y
        # Verifica colisão com paredes
        colisoes = pygame.sprite.spritecollide(self, self.paredes, False)
        for parede in colisoes:
            if self.vel_y > 0: # Movendo para baixo
                self.rect.bottom = parede.rect.top
            else: # Movendo para cima
                self.rect.top = parede.rect.bottom

class PacMan(Personagem):
    """ Classe que representa o jogador Pac-Man """
    def __init__(self, x, y):
        super().__init__(AMARELO, x, y)
        self.pontos = 0

class Fantasma(Personagem):
    """ Classe que representa os Fantasmas """
    def __init__(self, cor, x, y):
        super().__init__(cor, x, y)
        self.direcoes = [(-4, 0), (4, 0), (0, -4), (0, 4)]
        self.mudar_direcao()

    def mudar_direcao(self):
        self.vel_x, self.vel_y = random.choice(self.direcoes)

    def update(self):
        # Lógica de movimento simples: move até colidir e então muda de direção
        pos_original_x = self.rect.x
        pos_original_y = self.rect.y

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        colisoes = pygame.sprite.spritecollide(self, self.paredes, False)
        if colisoes:
            self.rect.x = pos_original_x
            self.rect.y = pos_original_y
            self.mudar_direcao()

# --- Layout do Labirinto ---
# W = Parede (Wall), . = Pílula (Pellet), P = Pac-Man, G = Fantasma
layout = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W............WW............W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
    "W.W  W.W   W.WW.W   W.W  W.W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
    "W..........................W",
    "W.WWWW.WW.WWWWWWWW.WW.WWWW.W",
    "W.WWWW.WW.WWWWWWWW.WW.WWWW.W",
    "W......WW....WW....WW......W",
    "WWWWWW.WWWWW WW WWWWW.WWWWWW",
    "     W.WWWWW WW WWWWW.W     ",
    "     W.WW    G   WW.W     ",
    "     W.WW WWWWWW WW.W     ",
    "WWWWWW.WW W G  W WW.WWWWWW",
    "      .   W    W   .      ",
    "WWWWWW.WW W G  W WW.WWWWWW",
    "     W.WW WWWWWW WW.W     ",
    "     W.WW    G   WW.W     ",
    "     W.WWWWWWWWWWWW.W     ",
    "WWWWWW.WWWWWWWWWWWW.WWWWWW",
    "W............WW............W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
    "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
    "W...WW.......P........WW...W",
    "WWW.WW.WW.WWWWWWWW.WW.WW.WWW",
    "WWW.WW.WW.WWWWWWWW.WW.WW.WWW",
    "W......WW....WW....WW......W",
    "W.WWWWWWWWWW.WW.WWWWWWWWWW.W",
    "W.WWWWWWWWWW.WW.WWWWWWWWWW.W",
    "W..........................W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# --- Função Principal do Jogo ---
def main():
    pygame.init()

    # Configurações da tela
    tela = pygame.display.set_mode([LARGURA_TELA, ALTURA_TELA])
    pygame.display.set_caption("Pac-Man Réplica")
    clock = pygame.time.Clock()

    # Cria os grupos de sprites
    todos_sprites = pygame.sprite.Group()
    paredes_grupo = pygame.sprite.Group()
    pilulas_grupo = pygame.sprite.Group()
    fantasmas_grupo = pygame.sprite.Group()

    # Cria os objetos do jogo a partir do layout
    pacman = None
    for y, linha in enumerate(layout):
        for x, caractere in enumerate(linha):
            pos_x, pos_y = x * LARGURA_BLOCO, y * ALTURA_BLOCO
            if caractere == 'W':
                parede = Parede(pos_x, pos_y)
                paredes_grupo.add(parede)
                todos_sprites.add(parede)
            elif caractere == '.':
                pilula = Pilula(pos_x, pos_y)
                pilulas_grupo.add(pilula)
                todos_sprites.add(pilula)
            elif caractere == 'P':
                pacman = PacMan(pos_x, pos_y)
            elif caractere == 'G':
                cores = [VERMELHO, ROSA, VERDE] # Cores para os fantasmas
                fantasma = Fantasma(random.choice(cores), pos_x, pos_y)
                fantasmas_grupo.add(fantasma)
                todos_sprites.add(fantasma)

    if not pacman:
        print("Erro: Pac-Man não encontrado no layout!")
        return

    pacman.paredes = paredes_grupo
    for fantasma in fantasmas_grupo:
        fantasma.paredes = paredes_grupo
    
    todos_sprites.add(pacman)

    # --- Loop Principal do Jogo ---
    rodando = True
    fim_de_jogo = False
    mensagem = ""
    fonte = pygame.font.Font(None, 48)

    while rodando:
        # Gerenciamento de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if not fim_de_jogo:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        pacman.vel_x = -4
                        pacman.vel_y = 0
                    elif evento.key == pygame.K_RIGHT:
                        pacman.vel_x = 4
                        pacman.vel_y = 0
                    elif evento.key == pygame.K_UP:
                        pacman.vel_y = -4
                        pacman.vel_x = 0
                    elif evento.key == pygame.K_DOWN:
                        pacman.vel_y = 4
                        pacman.vel_x = 0

        if not fim_de_jogo:
            # Atualiza a lógica do jogo
            todos_sprites.update()

            # Verifica colisão do Pac-Man com as pílulas
            pilulas_comidas = pygame.sprite.spritecollide(pacman, pilulas_grupo, True)
            pacman.pontos += len(pilulas_comidas)

            # Verifica colisão do Pac-Man com os fantasmas
            if pygame.sprite.spritecollide(pacman, fantasmas_grupo, False):
                fim_de_jogo = True
                mensagem = "Você Perdeu!"

            # Verifica condição de vitória
            if len(pilulas_grupo) == 0:
                fim_de_jogo = True
                mensagem = "Você Venceu!"

        # Desenha tudo na tela
        tela.fill(PRETO)
        todos_sprites.draw(tela)

        # Mostra a pontuação
        texto_pontos = fonte.render(f"Pontos: {pacman.pontos}", True, BRANCO)
        tela.blit(texto_pontos, [10, 10])

        # Mostra mensagem de fim de jogo
        if fim_de_jogo:
            texto_fim = fonte.render(mensagem, True, AMARELO)
            pos_x = (LARGURA_TELA - texto_fim.get_width()) // 2
            pos_y = (ALTURA_TELA - texto_fim.get_height()) // 2
            tela.blit(texto_fim, [pos_x, pos_y])

        # Atualiza a tela
        pygame.display.flip()
        clock.tick(30) # Limita o FPS a 30

    pygame.quit()

if __name__ == "__main__":
    main()