import pygame
import random
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulasi 4 Api Unggun Berjejer")

# Warna
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)
YELLOW = (255, 223, 0)
RED = (255, 69, 0)
GRAY = (169, 169, 169)
BROWN = (139, 69, 19)

FIRE_COLORS = [RED, ORANGE, YELLOW]

# Variabel untuk partikel api dan asap
fire_particles = [[] for _ in range(4)]
smoke_particles = [[] for _ in range(4)]

# Fungsi untuk membuat partikel api
def create_fire_particle(fire_index, x_center):
    x = random.randint(x_center - 30, x_center + 30)
    y = HEIGHT - 100
    radius = random.randint(4, 10)
    color = random.choice(FIRE_COLORS)
    speed = random.uniform(1, 3)
    fire_particles[fire_index].append({"x": x, "y": y, "radius": radius, "color": color, "speed": speed})

# Fungsi untuk membuat partikel asap
def create_smoke_particle(smoke_index, x_center):
    x = random.randint(x_center - 30, x_center + 30)
    y = HEIGHT - 150
    size = random.randint(10, 20)
    alpha = random.randint(50, 150)
    smoke_particles[smoke_index].append({"x": x, "y": y, "size": size, "alpha": alpha, "speed": random.uniform(0.5, 2)})

# Loop utama
clock = pygame.time.Clock()
x_positions = [WIDTH // 5, WIDTH // 5 * 2, WIDTH // 5 * 3, WIDTH // 5 * 4]  # Posisi tengah dari setiap api

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tambahkan partikel api dan asap untuk setiap api
    for i, x_center in enumerate(x_positions):
        if random.random() < 0.5:
            create_fire_particle(i, x_center)
        if random.random() < 0.3:
            create_smoke_particle(i, x_center)

    # Perbarui layar
    screen.fill(BLACK)

    # Gambar kayu untuk setiap api
    for i, x_center in enumerate(x_positions):
        for j in range(5):
            pygame.draw.rect(screen, BROWN, (x_center - 40 + j * 15, HEIGHT - 100, 20, 10))

    # Gambar partikel api untuk setiap api
    for i in range(4):
        for particle in fire_particles[i]:
            pygame.draw.circle(screen, particle["color"], (particle["x"], int(particle["y"])), int(particle["radius"]))
            particle["y"] -= particle["speed"]
            particle["radius"] -= 0.1

        # Hapus partikel api yang terlalu kecil atau di luar layar
        fire_particles[i] = [p for p in fire_particles[i] if p["radius"] > 0 and p["y"] > 0]

    # Gambar partikel asap untuk setiap api
    for i in range(4):
        for smoke in smoke_particles[i]:
            smoke_surface = pygame.Surface((smoke["size"], smoke["size"]), pygame.SRCALPHA)
            smoke_surface.fill((GRAY[0], GRAY[1], GRAY[2], smoke["alpha"]))
            screen.blit(smoke_surface, (smoke["x"], smoke["y"]))
            smoke["y"] -= smoke["speed"]
            smoke["alpha"] -= 1

        # Hapus partikel asap yang terlalu kecil atau transparan
        smoke_particles[i] = [s for s in smoke_particles[i] if s["alpha"] > 0 and s["y"] > 0]

    # Perbarui layar
    pygame.display.flip()
    clock.tick(30)
