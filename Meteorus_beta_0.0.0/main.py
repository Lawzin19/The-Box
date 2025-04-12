import pygame
from const import BACKGROUND_COLOR, WIDTH, HEIGHT
from ship import Ship
from projetil import Projetil
from bubble import Bubble

def main():
    pygame.init()  # Inicialização da biblioteca

    # Configuração da janela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Meteorus")  # Título

    ship = Ship(WIDTH // 2, HEIGHT - 300, 5)
    bubble = Bubble(WIDTH // 2, 80)
    projetils = []

    # Controle de cooldown
    cooldown_timer = 0

    # Loop da janela
    running = True  # "Está rodando"
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Se clicar no botão de fechar
                running = False  # Encerra o programa

        # Captura as teclas pressionadas
        keys = pygame.key.get_pressed()

        # Movimentação da ship
        ship.move(keys)

        # Cooldown
        if cooldown_timer > 0:
            cooldown_timer -= 1  # Reduz o tempo a cada frame

        # Disparo
        if keys[pygame.K_SPACE] and cooldown_timer == 0:
            projetils.append(Projetil(ship.x, ship.y))
            cooldown_timer = 15

        # Atualiza os projéteis
        for projetil in projetils:
            projetil.move()  # Faz o projétil subir

        # Removendo projéteis fora da tela
        projetils = [p for p in projetils if p.y > 0]
        
        if bubble.active:
            for projetil in projetils:
                if bubble.check_collision(projetil):
                    bubble.register_hit()
                    projetils.remove(projetil)
                    break
        bubble.update()

        # Atualizando a tela
        screen.fill(BACKGROUND_COLOR)  # Adiciona a cor de fundo

        # Desenha o círculo na parte superior
        bubble.draw(screen)

        # Desenha a nave
        ship.draw(screen)

        # Desenha os projéteis
        for projetil in projetils:
            projetil.draw(screen)

        pygame.display.flip()  # Atualiza a tela
        clock.tick(60)  # Controla a velocidade (FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
