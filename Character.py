import pygame
import time

#Player Class
class Character:
	def __init__(self):
		self.walk_steps = 8
		self.fight_1_steps = 6
		self.fight_2_steps = 6
		self.flash_steps = 5
		self.up    = "warrior/Up/Png/"
		self.down  = "warrior/Down/Png/"
		self.left  = "warrior/Left/Png/"
		self.right = "warrior/Right/Png/"
		self.walk()
		self.fight_1()
		self.fight_2()
		self.flash()

	def get_image(self, image, frame, width, height, scale):
		image_opt = pygame.Surface((width, height)).convert_alpha()
		image_opt.blit(image, (0, 0), ((frame * width), 0, width, height))
		image_opt = pygame.transform.scale(image_opt, (width * scale, height * scale))
		self.colour = (0,128,0)
		image_opt.set_colorkey(self.colour)
		return image_opt
	
	def animator(self, img, direction, steps):
		animation_list = []
		for step in range(steps):
			animation_list.append(self.get_image(img, step, 48, 48, 2))		
		return animation_list

	def walk(self):
		image = pygame.image.load(self.up + "WarriorUpWalk.png")
		self.animation_walk_up = self.animator(image, 'up', self.walk_steps)
		image = pygame.image.load(self.down + "WarriorDownWalk.png")
		self.animation_walk_down = self.animator(image, 'down', self.walk_steps)
		image = pygame.image.load(self.left + "WarriorLeftWalk.png")
		self.animation_walk_left = self.animator(image, 'left', self.walk_steps)
		image = pygame.image.load(self.right + "WarriorRightWalk.png")
		self.animation_walk_right = self.animator(image, 'right', self.walk_steps)

	def fight_1(self):
		image = pygame.image.load(self.up + "WarriorUpAttack01.png")
		self.animation_fight_1_up = self.animator(image, 'up', self.fight_1_steps)
		image = pygame.image.load(self.down + "WarriorDownAttack01.png")
		self.animation_fight_1_down = self.animator(image, 'down', self.fight_1_steps)
		image = pygame.image.load(self.left + "WarriorLeftAttack01.png")
		self.animation_fight_1_left = self.animator(image, 'left', self.fight_1_steps)
		image = pygame.image.load(self.right + "WarriorRightAttack01.png")
		self.animation_fight_1_right = self.animator(image, 'right', self.fight_1_steps)

	def fight_2(self):
		image = pygame.image.load(self.up + "WarriorUpAttack02.png")
		self.animation_fight_2_up = self.animator(image, 'up', self.fight_2_steps)
		image = pygame.image.load(self.down + "WarriorDownAttack02.png")
		self.animation_fight_2_down = self.animator(image, 'down', self.fight_2_steps)
		image = pygame.image.load(self.left + "WarriorLeftAttack02.png")
		self.animation_fight_2_left = self.animator(image, 'left', self.fight_2_steps)
		image = pygame.image.load(self.right + "WarriorRightAttack02.png")
		self.animation_fight_2_right = self.animator(image, 'right', self.fight_2_steps)

	def flash(self):
		image = pygame.image.load(self.up + "WarriorUpAttack03.png")
		self.animation_flash_up = self.animator(image, 'up', self.flash_steps)
		image = pygame.image.load(self.down + "WarriorDownAttack03.png")
		self.animation_flash_down = self.animator(image, 'down', self.flash_steps)
		image = pygame.image.load(self.left + "WarriorLeftAttack03.png")
		self.animation_flash_left = self.animator(image, 'left', self.flash_steps)
		image = pygame.image.load(self.right + "WarriorRightAttack03.png")
		self.animation_flash_right = self.animator(image, 'right', self.flash_steps)

	def walk_up(self):
		return self.animation_walk_up

	def walk_down(self):
		return self.animation_walk_down

	def walk_left(self):
		return self.animation_walk_left

	def walk_right(self):
		return self.animation_walk_right

	def fight_1_up(self):
		return self.animation_fight_1_up

	def fight_1_down(self):
		return self.animation_fight_1_down

	def fight_1_left(self):
		return self.animation_fight_1_left

	def fight_1_right(self):
		return self.animation_fight_1_right	

	def fight_2_up(self):
		return self.animation_fight_2_up

	def fight_2_down(self):
		return self.animation_fight_2_down

	def fight_2_left(self):
		return self.animation_fight_2_left

	def fight_2_right(self):
		return self.animation_fight_2_right	

	def flash_up(self):
		return self.animation_flash_up

	def flash_down(self):
		return self.animation_flash_down

	def flash_left(self):
		return self.animation_flash_left

	def flash_right(self):
		return self.animation_flash_right			