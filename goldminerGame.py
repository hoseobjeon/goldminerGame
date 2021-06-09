# 금캐기 게임

# 라이브러리
import os
import math
import pygame

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__() 
        self.image = image # 변경되는 이미지 정보
        self.original_image = image # 처음 전달받은 이미지
        self.rect = image.get_rect(center=position) 

        self.offset = pygame.math.Vector2(defalut_offset_x_claw, 0) # 백터를 사용해서 2차원값 x, y 값 및 각도 정의
        self.position = position

        self.direction = LEFT
        self.angle_speed = 2.5 # 집게의 각도 변경 폭
        self.angle = 10 # 집게 최초 각도

    def update(self, to_x): # 집게 반복 업데이트
        if self.direction == LEFT:
            self.angle += self.angle_speed
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed
        
        # 허용 각도를 벗어날때
        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)
        
        self.offset.x += to_x # offset을 to_x만큼 증가시킴

        self.rotate()

    def rotate(self): # 집게 회전 정의
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center=self.position + offset_rotated) # 새로운 이미지의 중간 위치 + 변경된 오프셋 값 업데이트

    def set_direction(self, direction): # 이동 방향 설정
        self.direction = direction

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5)

    def set_init_state(self): # 집게 위치, 동작 초기화
        self.offset.x = defalut_offset_x_claw
        self.angle = 10
        self.direction = LEFT

# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position, price, speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.price = price
        self.speed = speed
    
    def set_position(self, position, angle): # 보석 위치 설정
        r = self.rect.size[0] // 2
        rad_angle = math.radians(angle)
        to_x = r * math.cos(rad_angle)
        to_y = r * math.sin(rad_angle)
        self.rect.center = (position[0] + to_x, position[1] + to_y) # 집게 좌표 + 보석 크기

def setup_gemstone():
    diamone_price, diamond_speed = 500, 7
    small_gold_price, small_gold_speed = 100, 5
    big_gold_price, big_gold_speed = 300, 2
    stone_price, stone_speed = 10, 2

    # 다이아몬드 위치
    gemstone_group.add(Gemstone(gemstone_images[0], (150, 500), diamone_price, diamond_speed))
    gemstone_group.add(Gemstone(gemstone_images[0], (300, 800), diamone_price, diamond_speed))
    gemstone_group.add(Gemstone(gemstone_images[0], (480, 550), diamone_price, diamond_speed))
    gemstone_group.add(Gemstone(gemstone_images[0], (700, 420), diamone_price, diamond_speed))
    gemstone_group.add(Gemstone(gemstone_images[0], (770, 700), diamone_price, diamond_speed))

    # 작은 금 위치
    gemstone_group.add(Gemstone(gemstone_images[1], (50, 600), small_gold_price, small_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[1], (150, 800), small_gold_price, small_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[1], (200, 380), small_gold_price, small_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[1], (400, 400), small_gold_price, small_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[1], (600, 450), small_gold_price, small_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[1], (600, 700), small_gold_price, small_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[1], (800, 400), small_gold_price, small_gold_speed))

    # 큰 금 위치
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 500), big_gold_price, big_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[2], (500, 700), big_gold_price, big_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[2], (800, 500), big_gold_price, big_gold_speed))

    # 돌 위치
    gemstone_group.add(Gemstone(gemstone_images[3], (80, 440), stone_price, stone_speed))
    gemstone_group.add(Gemstone(gemstone_images[3], (250, 700), stone_price, stone_speed))
    gemstone_group.add(Gemstone(gemstone_images[3], (300, 380), stone_price, stone_speed))
    gemstone_group.add(Gemstone(gemstone_images[3], (600, 330), stone_price, stone_speed))
    gemstone_group.add(Gemstone(gemstone_images[3], (650, 600), stone_price, stone_speed))
    gemstone_group.add(Gemstone(gemstone_images[3], (800, 800), stone_price, stone_speed))

def update_score(score): # 점수 업데이트
    global curr_score
    curr_score += score

def display_score(): # 현재 점수를 보여줌
    txt_curr_score = game_font.render(f"Current Score: {curr_score:,}", True, BLACK)
    screen.blit(txt_curr_score, (400, 20))

    txt_goal_score = game_font.render(f"Goal Score: {goal_score:,}", True, BLACK)
    screen.blit(txt_goal_score, (50, 20))

def display_time(time): # 시간을 보여줌
    txt_timer = game_font.render(f"Time : {time}", True, BLACK)
    screen.blit(txt_timer, (720, 20)) # 화면 업데이트, 좌표

def display_game_over(): # 게임 종료 메시지 표시
    game_font = pygame.font.SysFont("aialrounded", 60) # 큰 폰트
    txt_game_over = game_font.render(game_result, True, BLACK)
    rect_game_over = txt_game_over.get_rect(center=(int(screen_width /2), int(screen_height /2))) # 화면 중앙에 표시
    screen.blit(txt_game_over, rect_game_over)

pygame.init()
screen_width = 900 # 가로크기
screen_height = 900 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("금캐기 게임")

clock = pygame.time.Clock()

game_font = pygame.font.SysFont("arial", 30)

# 점수 관련 변수
goal_score = 2000 # 목표 점수
curr_score = 0 # 현재 점수

# 게임 오버 관련 변수
game_result = None
total_time = 60 # 총 시간

start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴

# 게임 관련 변수
defalut_offset_x_claw = 60 # 오프셋 거리
to_x = 0
caught_gemstone = None

# 속도 변수
move_speed = 12 # 집게 이동 속도
return_speed = 20 # 집게 리턴 속도

# 방향 변수
LEFT = -1
STOP = 0
RIGHT = 1

# 색깔 변수
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "img/background.png"))

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [ # 보석들 리스트로 설정
    pygame.image.load(os.path.join(current_path, "img/diamond.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "img/small_gold.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "img/big_gold.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "img/stone.png")).convert_alpha(),]

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone()

# 트레이
tray_image = pygame.image.load(os.path.join(current_path, "img/tray.png"))
tray = Claw(tray_image, (screen_width // 2, 150))

# 집게
claw_image = pygame.image.load(os.path.join(current_path, "img/claw.png"))
claw = Claw(claw_image, (screen_width // 2, 150))

running = True # 게임 루프 설정
while running:
    clock.tick(30) # FPS 값
    
    # 이벤트 처리
    for event in pygame.event.get():
        # 종료 할때
        if event.type == pygame.QUIT:
            running = False

        # 마우스 누를때
        if event.type == pygame.MOUSEBUTTONDOWN:
            claw.set_direction(STOP)
            to_x = move_speed

    # 집게가 화면 끝일때
    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed
    
    # 오프셋값이 원래 값으로 돌아올때
    if claw.offset.x < defalut_offset_x_claw:
        to_x = 0
        claw.set_init_state()

        # 보석 잡았을때
        if caught_gemstone:
            update_score(caught_gemstone.price)
            gemstone_group.remove(caught_gemstone)
            caught_gemstone = None

    # 보석 못 잡았을때
    if not caught_gemstone:
        for gemstone in gemstone_group:

            # 집게 보석 충돌처리
            if pygame.sprite.collide_mask(claw, gemstone):
                caught_gemstone = gemstone
                to_x = -gemstone.speed 
                break

    # 보석 잡혔을때
    if caught_gemstone:
        caught_gemstone.set_position(claw.rect.center, claw.angle)

    screen.blit(background, (0, 0))

    gemstone_group.draw(screen)

    # 트레이 업데이트
    tray.draw(screen)

    # 집게 업데이트
    claw.update(to_x)
    claw.draw(screen)

    # 점수 정보
    display_score()

    # 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 현재 시간 - 시작 시간
    display_time(total_time - int(elapsed_time)) # 전체시간 - 경과시간

    # 시간 종료 및 게임 종료
    if total_time - int(elapsed_time) <= 0:
        running = False # 루프 탈출

        # 현재점수가 목표점수보다 높거나 같을때
        if curr_score >= goal_score:
            game_result = "Mission Complete"

        # 현재점수가 목표점수보다 낮을때        
        else:
            game_result = "Game Over"

        # 게임 종료 메시지 표시
        display_game_over()

    pygame.display.update() # 화면 업데이트

pygame.time.delay(1000) # 1초 대기
pygame.quit() # 게임 종료