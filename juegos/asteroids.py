import pygame
import random
import math

# Inicialización de pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuración de la nave
ship_size = 20
ship_x, ship_y = WIDTH // 2, HEIGHT // 2
ship_angle = 0
ship_speed = 5

# Configuración de los asteroides
asteroid_size = 40
asteroid_speed = 2
asteroids = []

# Configuración de los disparos
bullets = []
bullet_speed = 10

# Funciones para crear y mover asteroides
def create_asteroid():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    angle = random.uniform(0, 2 * math.pi)
    asteroids.append({"x": x, "y": y, "angle": angle})

def move_asteroids():
    for asteroid in asteroids:
        asteroid["x"] += asteroid_speed * math.cos(asteroid["angle"])
        asteroid["y"] += asteroid_speed * math.sin(asteroid["angle"])
        # Teletransportar el asteroide si sale de la pantalla
        asteroid["x"] %= WIDTH
        asteroid["y"] %= HEIGHT

# Función para disparar balas
def shoot():
    angle_rad = math.radians(ship_angle)
    bullet_x = ship_x + ship_size * math.cos(angle_rad)
    bullet_y = ship_y + ship_size * math.sin(angle_rad)
    bullets.append({"x": bullet_x, "y": bullet_y, "angle": angle_rad})

def move_bullets():
    for bullet in bullets[:]:
        bullet["x"] += bullet_speed * math.cos(bullet["angle"])
        bullet["y"] += bullet_speed * math.sin(bullet["angle"])
        if bullet["x"] < 0 or bullet["x"] > WIDTH or bullet["y"] < 0 or bullet["y"] > HEIGHT:
            bullets.remove(bullet)

# Función para dibujar objetos
def draw_objects():
    screen.fill(BLACK)
    # Dibujar la nave
    angle_rad = math.radians(ship_angle)
    tip_x = ship_x + ship_size * math.cos(angle_rad)
    tip_y = ship_y + ship_size * math.sin(angle_rad)
    pygame.draw.polygon(screen, WHITE, [(tip_x, tip_y),
                                        (ship_x + ship_size * math.cos(angle_rad + 4 * math.pi / 5), 
                                         ship_y + ship_size * math.sin(angle_rad + 4 * math.pi / 5)),
                                        (ship_x + ship_size * math.cos(angle_rad - 4 * math.pi / 5), 
                                         ship_y + ship_size * math.sin(angle_rad - 4 * math.pi / 5))])

    # Dibujar asteroides
    for asteroid in asteroids:
        pygame.draw.circle(screen, WHITE, (int(asteroid["x"]), int(asteroid["y"])), asteroid_size // 2)

    # Dibujar balas
    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, (int(bullet["x"]), int(bullet["y"])), 3)

    pygame.display.flip()

# Función de colisión entre balas y asteroides
def check_collisions():
    global asteroids, bullets
    for bullet in bullets[:]:
        for asteroid in asteroids[:]:
            distance = math.hypot(bullet["x"] - asteroid["x"], bullet["y"] - asteroid["y"])
            if distance < asteroid_size // 2:
                bullets.remove(bullet)
                asteroids.remove(asteroid)
                break

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

# Crear algunos asteroides inicialmente
for _ in range(5):
    create_asteroid()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot()

    # Controles de la nave
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_angle += 5
    if keys[pygame.K_RIGHT]:
        ship_angle -= 5
    if keys[pygame.K_UP]:
        ship_x += ship_speed * math.cos(math.radians(ship_angle))
        ship_y += ship_speed * math.sin(math.radians(ship_angle))

    # Teletransportar la nave si sale de la pantalla
    ship_x %= WIDTH
    ship_y %= HEIGHT

    # Mover y actualizar los objetos
    move_asteroids()
    move_bullets()
    check_collisions()
    draw_objects()

    # Generar nuevos asteroides si quedan pocos
    if len(asteroids) < 5:
        create_asteroid()

    # Control de velocidad del juego
    clock.tick(30)

pygame.quit()
