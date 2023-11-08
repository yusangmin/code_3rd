import pygame
import random

# 게임 화면 크기 설정
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

# 색상 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 블록 크기 설정
BLOCK_SIZE = 20

# 게임 초기화
pygame.init()

# 게임 화면 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# 게임 루프
def game_loop():
    # 뱀 초기 위치 설정
    snake = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
    direction = "right"

    # 먹이 초기 위치 설정
    food = (random.randint(0, SCREEN_WIDTH / BLOCK_SIZE - 1) * BLOCK_SIZE,
            random.randint(0, SCREEN_HEIGHT / BLOCK_SIZE - 1) * BLOCK_SIZE)

    # 게임 루프
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                elif event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"

        # 뱀 이동 처리
        x, y = snake[0]
        if direction == "left":
            x -= BLOCK_SIZE
        elif direction == "right":
            x += BLOCK_SIZE
        elif direction == "up":
            y -= BLOCK_SIZE
        elif direction == "down":
            y += BLOCK_SIZE
        snake.insert(0, (x, y))

        # 뱀이 벽에 부딪히면 게임 종료
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            pygame.quit()
            quit()

        # 뱀이 자기 자신과 부딪히면 게임 종료
        if snake.count((x, y)) > 1:
            pygame.quit()
            quit()

        # 먹이 먹기 처리
        if (x, y) == food:
            food = (random.randint(0, SCREEN_WIDTH / BLOCK_SIZE - 1) * BLOCK_SIZE,
                    random.randint(0, SCREEN_HEIGHT / BLOCK_SIZE - 1) * BLOCK_SIZE)
        else:
            snake.pop()

        # 게임 화면 그리기
        screen.fill(BLACK)
        for x, y in snake:
            pygame.draw.rect(screen, GREEN, (x, y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, WHITE, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.update()

        # 게임 속도 조절
        pygame.time.Clock().tick(10)

# 게임 실행
game_loop()
