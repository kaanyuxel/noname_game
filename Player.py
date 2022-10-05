import pygame, sys
import Character
from math import atan2, degrees 

class Player(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)
        self.character = Character.Character()
        self.image = self.character.walk_down()[0]
        self.rect = self.image.get_rect(center = (512, 512))
        
        self.walkCount = 0
        self.attack_frame = 0
        self.face = "down"
        self.test_keyboard = True

        self.fight_1 = False
        self.fight_2 = False
        self.attacking = False


        self.left_click = False
        self.pos = pygame.Vector2(self.rect.centerx, self.rect.centery)
        self.target = pygame.Vector2(self.rect.centerx, self.rect.centery)
        self.speed = 2
        self.cam_group = group
        

    def input(self):
        
        #click = pygame.mouse.get_pressed()     
        if self.left_click:
            self.target = pygame.math.Vector2(pygame.mouse.get_pos()) + self.cam_group.offset
            self.face_update()    
            self.left_click = False
        
        keys = pygame.key.get_pressed()     
        if not keys[pygame.K_f] and not keys[pygame.K_r]:    
            if self.test_keyboard:            
                if keys[pygame.K_UP]:
                    self.face = "up"  
                    self.target = pygame.Vector2(self.rect.centerx , self.rect.centery - 1*self.speed)
                elif keys[pygame.K_DOWN]:
                    self.face = "down"
                    self.target = pygame.Vector2(self.rect.centerx, self.rect.centery + 1*self.speed)
                elif keys[pygame.K_RIGHT]:     
                    self.face = "right"
                    self.target = pygame.Vector2(self.rect.centerx + 1*self.speed, self.rect.centery)
                elif keys[pygame.K_LEFT]:
                    self.face = "left"
                    self.target = pygame.Vector2(self.rect.centerx - 1*self.speed, self.rect.centery)
        
    def update(self):
        self.input()
        self.attack()
        self.movement()


    def face_update(self):
        angle = -degrees(atan2(self.rect.centery - self.target.y, self.rect.centerx - self.target.x)) + 180 
        if angle > 80 and angle < 100:
            self.face = "up"
        if angle > 260 and angle < 280:
            self.face = "down"
        
        if angle > 100 and angle < 260:
            self.face = "left"
        if angle < 80 or angle > 280:
            self.face = "right"   

    def movement(self):
        if self.walkCount >= 35:
            self.walkCount = 0 

        move = self.target - self.pos
        move_length = move.length()
        
        if move_length < self.speed:
            self.pos = self.target
            self.pos = self.rect.center 
            #self.animate_walk(0)
        elif move_length != 0:
            self.walkCount += 1
            move.normalize_ip()
            move = move * self.speed
            self.pos += move   
            self.animate_walk(self.walkCount//7)
            if self.attacking == True:
                self.attack() 

        self.rect.center = list(int(v) for v in self.pos)

    def set_attack(self, key):
        if key == pygame.K_f:
            self.fight_1 = True
        if key == pygame.K_r:
            self.fight_2 = True
        self.attacking = True             

    def attack(self):
        if self.fight_1 or self.fight_2:
            self.attack_frame += 1
            if self.fight_1:                 
                if self.attack_frame > 30:
                    self.attack_frame = 0
                    self.fight_1 = False
                    self.attacking = False
                self.animate_fight(1, self.attack_frame//6)
                
            if self.fight_2:
                if self.attack_frame > 30:
                    self.attack_frame = 0
                    self.fight_2 = False
                    self.attacking = False
                self.animate_fight(2, self.attack_frame//6)
        else:
            self.animate_walk(0)                          
        
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