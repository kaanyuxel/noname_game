import pygame, sys
import Character
from math import atan2, degrees 

class Player(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)
        self.character = Character.Character()
        self.image = self.character.walk_down()[0]
        self.rect = self.image.get_rect(center = (512, 512))
        self.direction = pygame.math.Vector2()
        self.speed = 1
        self.walkCount = 0
        self.attack_frame = 0
        self.face = "down"
        self.moving = False
        self.clicked = pygame.math.Vector2(512, 512)
        self.test_keyboard = False

    def input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        click = pygame.mouse.get_pressed()
        angle = -degrees(atan2(self.rect.centery - mouse.y, self.rect.centerx - mouse.x)) + 180          
        if keys[pygame.K_f] or keys[pygame.K_r]:
            self.attack_frame += 1
            if self.attack_frame > 5:
                self.attack_frame = 0
            if keys[pygame.K_f]:    
                self.animate_fight(1, self.attack_frame)
            else:
                self.animate_fight(2, self.attack_frame)
        
        if not keys[pygame.K_f] and not keys[pygame.K_r]:    

            if click[0] == 1:
                self.clicked = pygame.math.Vector2(pygame.mouse.get_pos())

                if angle > 80 and angle < 110:
                    self.face = "up"
                elif angle > 260 and angle < 280:
                    self.face = "down"
                elif angle > 110 and angle < 260:
                    self.face = "left"
                elif angle < 80 or angle > 280:
                    self.face = "right"

            if self.walkCount >= 7:
                self.walkCount = 0

            if self.face == "up": 
                if self.clicked.y != self.rect.centery:  
                    #print(angle, self.clicked.y, self.face, self.clicked.y, self.rect.centery)  
                    self.walkCount += 1
                    self.animate_walk(self.walkCount)      
                    self.direction.x = 0
                    self.direction.y = -1
                else:  
                    self.animate_stop()
            elif self.face == "down": 
                if self.clicked.y != self.rect.centery:    
                   #print(angle, self.clicked.y, self.face, self.clicked.y, self.rect.centery)  
                   self.walkCount += 1
                   self.animate_walk(self.walkCount)      
                   self.direction.x = 0
                   self.direction.y = 1
                else:
                    self.animate_stop()   
            elif self.face == "left": 
                if self.clicked.x != self.rect.centerx:    
                    #print(self.face, self.clicked.x, self.rect.centerx)  
                    self.walkCount += 1
                    self.animate_walk(self.walkCount)      
                    self.direction.x = -1
                    self.direction.y = 0
                else:
                    self.animate_stop()    
            elif self.face == "right":
                if self.clicked.x != self.rect.centerx:   
                    #print(self.face, self.clicked.x, self.rect.centerx)   
                    self.walkCount += 1
                    self.animate_walk(self.walkCount)      
                    self.direction.x = 1
                    self.direction.y = 0
                else:
                    self.animate_stop()    

            if self.test_keyboard:            
                if keys[pygame.K_UP]:
                    y = -1
                    self.walkCount += 1
                    self.face = "up"  
                    self.animate_walk(self.walkCount)
                elif keys[pygame.K_DOWN]:
                    y = 1
                    self.walkCount += 1
                    self.face = "down"
                    self.animate_walk(self.walkCount)   
                elif keys[pygame.K_RIGHT]:     
                    x = 1
                    self.walkCount += 1
                    self.face = "right"
                    self.animate_walk(self.walkCount)
                elif keys[pygame.K_LEFT]:
                    x = -1
                    self.walkCount += 1
                    self.face = "left"
                    self.animate_walk(self.walkCount)
                else:
                    x = y = 0
                    self.animate_walk(0)

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed

    def animate_walk(self, walk_count): 
        if self.face == "right":
            self.image = self.character.walk_right()[walk_count]
        if self.face == "left":
            self.image = self.character.walk_left()[walk_count]
        if self.face == "up":
            self.image = self.character.walk_up()[walk_count]
        if self.face == "down":
            self.image = self.character.walk_down()[walk_count]
        self.rect = self.image.get_rect(center = self.rect.center)     

    def animate_fight(self, fight_type, fight_count):
        if fight_type == 1:
            if self.face == "left":
                self.image = self.character.fight_1_left()[fight_count]
            if self.face == "right":
                self.image = self.character.fight_1_right()[fight_count]    
            if self.face == "up":
                self.image = self.character.fight_1_up()[fight_count]
            if self.face == "down":
                self.image = self.character.fight_1_down()[fight_count]
        if fight_type == 2:
            if self.face == "left":
                self.image = self.character.fight_2_left()[fight_count]
            if self.face == "right":
                self.image = self.character.fight_2_right()[fight_count]    
            if self.face == "up":
                self.image = self.character.fight_2_up()[fight_count]
            if self.face == "down":
                self.image = self.character.fight_2_down()[fight_count]     
    
    def animate_stop(self):
        self.direction.x = 0
        self.direction.y = 0                  
        self.animate_walk(0)                                        