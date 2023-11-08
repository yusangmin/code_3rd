# import pygame: pygame 라이브러리 가져온다.
import pygame
import time
import random

# pygame.init(): pygame 초기화
pygame.init()

# 게임 화면 크기 설정
# 게임 화면 크기 설정: width와 height 변수를 사용하여 게임 화면의 가로와 세로 크기 설정
width = 800
height = 600
display = pygame.display.set_mode((width, height))

# 색상 설정
# 색상 설정: white, black, red 변수를 사용하여 게임에서 사용할 색상을 설정
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 게임 속도 설정
# 게임 속도 설정: clock 변수를 사용하여 게임의 실행 속도를 설정
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 15

# 글꼴 설정
# 글꼴 설정: font_style과 score_font 변수를 사용하여 게임에서 사용할 글꼴을 설정
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# 점수 표시 함수
# 점수 표시 함수: our_snake 함수는 뱀의 위치 정보를 받아와서 화면 출력
# our_snake 함수를 정의
# 뱀의 위치 정보를 받아와서 화면에 뱀을 그리는 역할.
# 함수의 인자로는 snake_block과 snake_list가 전달
# snake_block: 뱀 한 조각의 크기를 나타내는 변수
# snake_list: 뱀의 위치 정보를 담고 있는 리스트
# snake_list에 있는 각각의 위치 정보를 반복하면서, pygame.draw.rect() 함수를 사용하여 해당 위치에 뱀을 표시.
# pygame.draw.rect() 함수는 사각형을 그리는 함수. 이 함수에는 다음과 같은 인자를 전달
# display: 뱀을 그릴 게임 화면을 나타내는 변수.
# black: 뱀의 색상을 나타내는 변수.
# [x[0], x[1], snake_block, snake_block]: 사각형의 위치와 크기를 나타내는 리스트
# x[0]과 x[1]은 뱀 한 조각의 x 좌표와 y 좌표를 나타내고, snake_block은 사각형의 가로와 세로 크기 표현
# 아래 함수의 코드는 snake_list에 있는 각 위치 정보를 가져와서 해당 위치에 뱀을 그리는 역할을 합니다. 이 함수를 호출하여 뱀을 그려줌


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [
                         x[0], x[1], snake_block, snake_block])

# 게임 실행 함수
# 게임 실행 함수: gameLoop 함수는 게임의 주요 동작을 수행하는 함수.
# 초기 위치 설정, 키 입력 처리, 충돌 검사, 먹이 처리, 점수 표시 등을 수행


def gameLoop():
    game_over = False
    game_close = False

    # 초기 위치 설정
    x1 = width / 2
    y1 = height / 2

    # 위치 변경 값 설정
    x1_change = 0
    y1_change = 0

    # 뱀의 위치 정보를 저장하는 리스트
    snake_List = []
    Length_of_snake = 1

    # 먹이 위치 설정
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    # 게임 루프
    # 게임 루프: while 루프를 사용하여 게임을 계속 실행.
    # game_over가 True가 될 때까지 게임이 실행.

    while not game_over:

        while game_close == True:
            display.fill(white)
            game_over_font = font_style.render("Game Over", True, red)
            display.blit(game_over_font, [width / 3, height / 3])
            score_text = score_font.render(
                "Your Score: " + str(Length_of_snake - 1), True, black)
            display.blit(score_text, [width / 3, height / 2])
            pygame.display.update()

            # 게임 종료 후 재시작 또는 종료 선택
            # 게임 오버 처리: game_close가 True일 때 게임 오버 화면을 표시하고 키 입력을 처리

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # 키 입력 처리
        # 키 입력 처리: pygame.KEYDOWN 이벤트를 사용하여 키 입력을 처리.
        # 방향키에 따라 뱀의 위치 변경 값을 설정

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # 벽과 충돌했을 때 게임 종료
        # 충돌 검사: 뱀의 머리와 벽 또는 자신의 몸이 충돌하는지 검사하여 게임 오버 여부를 결정

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(white)
        pygame.draw.rect(
            display, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # 자신과 충돌했을 때 게임 종료
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        # 점수 표시
        # 점수 표시: 화면에 현재 점수를 표시.
        score_text = score_font.render(
            "Score: " + str(Length_of_snake - 1), True, black)
        display.blit(score_text, [0, 0])

        pygame.display.update()

        # 먹이를 먹었을 때
        # 먹이 처리: 뱀이 먹이를 먹었을 때 먹이 위치를 변경하고 뱀의 길이를 증가
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(
                0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()  # 게임 종료: game_over가 True가 되면 pygame을 종료


gameLoop()
