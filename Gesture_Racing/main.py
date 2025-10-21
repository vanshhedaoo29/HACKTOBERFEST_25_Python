import sys
import json
import random
import time
from collections import deque
import cv2
import numpy as np
import mediapipe as mp
import pygame


SCREEN_W, SCREEN_H = 800, 600
CAR_W, CAR_H = 60, 100
LANE_MARGIN = 60
OBSTACLE_W_MIN, OBSTACLE_W_MAX = 40, 120
OBSTACLE_H = 30
OBSTACLE_SPAWN_INTERVAL = 1.0  
BASE_SPEED = 4.0
SPEED_INCREMENT_PER_SEC = 0.02   
BOOST_MULTIPLIER = 1.8
BOOST_Y_THRESHOLD = 0.4 
LEADERBOARD_FILE = "leaderboard.json"
MAX_LEADERBOARD = 5


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (35, 35, 35)
GREEN = (50, 200, 50)
RED = (220, 60, 60)
YELLOW = (240, 220, 70)
BLUE = (60, 140, 220)


def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_leaderboard(board):
    try:
        with open(LEADERBOARD_FILE, "w") as f:
            json.dump(board[:MAX_LEADERBOARD], f, indent=2)
    except Exception as e:
        print("Could not save leaderboard:", e)

def add_score_to_leaderboard(name, score):
    board = load_leaderboard()
    board.append({"name": name, "score": round(score, 1), "time": time.strftime("%Y-%m-%d %H:%M:%S")})
    board.sort(key=lambda x: x["score"], reverse=True)
    save_leaderboard(board)


class Obstacle:
    def __init__(self, x, y, w, h, color=RED):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=6)

    def update(self, dy):
        self.rect.y += dy

class Car:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CAR_W, CAR_H)
        self.color = BLUE

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=8)
        
        wheel_w, wheel_h = 12, 20
        pygame.draw.rect(surf, BLACK, (self.rect.left+8, self.rect.bottom-wheel_h/1.5, wheel_w, wheel_h), border_radius=4)
        pygame.draw.rect(surf, BLACK, (self.rect.right-8-wheel_w, self.rect.bottom-wheel_h/1.5, wheel_w, wheel_h), border_radius=4)


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Gesture Racer")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    bigfont = pygame.font.SysFont(None, 48)

    
    car = Car((SCREEN_W - CAR_W)//2, SCREEN_H - CAR_H - 30)

    
    obstacles = []

    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: Could not open webcam. Use keyboard controls instead.")
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    hands = mp_hands.Hands(static_image_mode=False,
                           max_num_hands=1,
                           min_detection_confidence=0.5,
                           min_tracking_confidence=0.5)

    running = True
    game_over = False
    last_obstacle_time = time.time()
    start_time = time.time()
    score = 0.0
    speed = BASE_SPEED
    boost = False
    fps_deque = deque(maxlen=30)
    use_hand = True if cap.isOpened() else False

    
    def map_hand_x_to_screen(nx):
        
        return int(nx * (SCREEN_W - CAR_W))

    while running:
        dt = clock.tick(60) / 1000.0  
        fps_deque.append(clock.get_fps())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False
                if game_over and event.key == pygame.K_r:
                    
                    obstacles.clear()
                    car.rect.x = (SCREEN_W - CAR_W)//2
                    car.rect.y = SCREEN_H - CAR_H - 30
                    game_over = False
                    last_obstacle_time = time.time()
                    start_time = time.time()
                    score = 0.0
                    speed = BASE_SPEED

        
        hand_x_norm = None
        hand_y_norm = None
        if use_hand and not game_over:
            ret, frame = cap.read()
            if not ret:
                use_hand = False
            else:
                frame = cv2.flip(frame, 1)  
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(rgb)
                if results.multi_hand_landmarks:
                    lm = results.multi_hand_landmarks[0].landmark
                    
                    ix = lm[8].x  
                    iy = lm[8].y
                    hand_x_norm = ix
                    hand_y_norm = iy
                    
                else:
                    
                    hand_x_norm = None

        
        keys = pygame.key.get_pressed()
        if not game_over:
            if hand_x_norm is not None:
                
                target_x = map_hand_x_to_screen(hand_x_norm)
               
                car.rect.x += int((target_x - car.rect.x) * min(8 * dt, 1))
            else:
                
                if keys[pygame.K_LEFT]:
                    car.rect.x -= int(300 * dt)
                if keys[pygame.K_RIGHT]:
                    car.rect.x += int(300 * dt)

            
            if hand_y_norm is not None:
                boost = (hand_y_norm < BOOST_Y_THRESHOLD)  
            else:
                boost = keys[pygame.K_UP]

            
            car.rect.x = max(0, min(car.rect.x, SCREEN_W - CAR_W))

        
        if not game_over:
            
            elapsed = time.time() - start_time
            speed = BASE_SPEED + (SPEED_INCREMENT_PER_SEC * elapsed * 60) 
            if boost:
                current_speed = speed * BOOST_MULTIPLIER
            else:
                current_speed = speed

            
            spawn_interval = max(0.35, OBSTACLE_SPAWN_INTERVAL - (elapsed * 0.015))
            if time.time() - last_obstacle_time > spawn_interval:
                ow = random.randint(OBSTACLE_W_MIN, OBSTACLE_W_MAX)
                ox = random.randint(0, SCREEN_W - ow)
                obstacles.append(Obstacle(ox, -OBSTACLE_H - 10, ow, OBSTACLE_H))
                last_obstacle_time = time.time()

            
            for ob in obstacles:
                ob.update(current_speed)
            
            obstacles = [o for o in obstacles if o.rect.top <= SCREEN_H + 50]

            
            score += current_speed * dt * 1.2

        
        if not game_over:
            for ob in obstacles:
                if car.rect.colliderect(ob.rect):
                    game_over = True
                    
                    add_score_to_leaderboard("You", score)
                    break

        
        screen.fill(GRAY)

        
        road_rect = pygame.Rect(LANE_MARGIN, 0, SCREEN_W - LANE_MARGIN*2, SCREEN_H)
        pygame.draw.rect(screen, (50, 50, 50), road_rect)
        
        lane_x = SCREEN_W // 2
        dash_h = 20
        dash_gap = 16
        y_pos = -((time.time() - start_time) * (speed*2)) % (dash_h + dash_gap)
        while y_pos < SCREEN_H:
            pygame.draw.rect(screen, YELLOW, (lane_x - 6, int(y_pos), 12, dash_h))
            y_pos += dash_h + dash_gap

        
        for ob in obstacles:
            ob.draw(screen)

        
        car.draw(screen)

        
        fps = sum(fps_deque)/len(fps_deque) if fps_deque else 0
        hud_lines = [
            f"Score: {int(score)}",
            f"Speed: {current_speed:.1f}" if not game_over else "Speed: 0.0",
            f"Boost: {'ON' if boost and not game_over else 'OFF'}",
            f"FPS: {fps:.0f}"
        ]
        for i, line in enumerate(hud_lines):
            txt = font.render(line, True, WHITE)
            screen.blit(txt, (10, 8 + i*22))

        
        if use_hand:
            try:
                
                small_h = 120
                small_w = int(small_h * (frame.shape[1] / frame.shape[0]))
                preview = cv2.resize(frame, (small_w, small_h))
                preview = cv2.cvtColor(preview, cv2.COLOR_BGR2RGB)
                surf = pygame.surfarray.make_surface(np.rot90(preview))
                screen.blit(surf, (SCREEN_W - small_w - 10, 10))
            except Exception:
                pass

        
        if game_over:
            overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
            overlay.fill((0,0,0,160))
            screen.blit(overlay, (0,0))
            go_text = bigfont.render("GAME OVER", True, RED)
            score_text = font.render(f"Score: {int(score)}", True, WHITE)
            retry_text = font.render("Press R to Restart or Q/ESC to Quit", True, WHITE)
            screen.blit(go_text, ((SCREEN_W - go_text.get_width())//2, SCREEN_H//2 - 80))
            screen.blit(score_text, ((SCREEN_W - score_text.get_width())//2, SCREEN_H//2 - 20))
            screen.blit(retry_text, ((SCREEN_W - retry_text.get_width())//2, SCREEN_H//2 + 20))

            
            board = load_leaderboard()
            lb_title = font.render("Leaderboard:", True, WHITE)
            screen.blit(lb_title, (SCREEN_W//2 - 150, SCREEN_H//2 + 70))
            for i, entry in enumerate(board[:MAX_LEADERBOARD]):
                txt = font.render(f"{i+1}. {entry['name']} - {entry['score']}", True, WHITE)
                screen.blit(txt, (SCREEN_W//2 - 150, SCREEN_H//2 + 100 + i*26))

        pygame.display.flip()

    
    cap.release()
    hands.close()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    try:
        run_game()
    except Exception as e:
        print("An error occurred:", e)
        print("Make sure your webcam is available and required python packages are installed.")
