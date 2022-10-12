import pygame
import time

#Player Class
class Character:
	def __init__(self):
		self.walk_steps = 8
		self.fight_1_steps = 6
		self.fight_2_steps = 6
		self.flash_steps = 5
		self.idle_steps = 5
		self.up    = "graphics/Warrior/Up/Png/"
		self.down  = "graphics/Warrior/Down/Png/"
		self.left  = "graphics/Warrior/Left/Png/"
		self.right = "graphics/Warrior/Right/Png/"
		self.idle()
		self.walk()
		self.fight_1()
		self.fight_2()
		self.flash()

	def get_image(self, image, frame, width, height, scale):
		image_opt = pygame.Surface((width, height), pygame.SRCALPHA)
		image_opt.blit(image, (0, 0), ((frame * width), 0, width, height))
		image_opt = pygame.transform.scale(image_opt, (width * scale, height * scale))
		return image_opt

	def animator(self, img, direction, steps):
		list = []
		for step in range(steps):
			list.append(self.get_image(img, step, 48, 48, 1.5))
		return list

	def idle(self):
		image = pygame.image.load(self.up + "WarriorUpIdle.png")
		self.idle_up = self.animator(image, 'up', self.idle_steps)
		image = pygame.image.load(self.down + "WarriorDownIdle.png")
		self.idle_down = self.animator(image, 'down', self.idle_steps)
		image = pygame.image.load(self.left + "WarriorLeftIdle.png")
		self.idle_left = self.animator(image, 'left', self.idle_steps)
		image = pygame.image.load(self.right + "WarriorRightIdle.png")
		self.idle_right = self.animator(image, 'right', self.idle_steps)

	def walk(self):
		image = pygame.image.load(self.up + "WarriorUpWalk.png")
		self.walk_up = self.animator(image, 'up', self.walk_steps)
		image = pygame.image.load(self.down + "WarriorDownWalk.png")
		self.walk_down = self.animator(image, 'down', self.walk_steps)
		image = pygame.image.load(self.left + "WarriorLeftWalk.png")
		self.walk_left = self.animator(image, 'left', self.walk_steps)
		image = pygame.image.load(self.right + "WarriorRightWalk.png")
		self.walk_right = self.animator(image, 'right', self.walk_steps)

	def fight_1(self):
		image = pygame.image.load(self.up + "WarriorUpAttack01.png")
		self.fight_1_up = self.animator(image, 'up', self.fight_1_steps)
		image = pygame.image.load(self.down + "WarriorDownAttack01.png")
		self.fight_1_down = self.animator(image, 'down', self.fight_1_steps)
		image = pygame.image.load(self.left + "WarriorLeftAttack01.png")
		self.fight_1_left = self.animator(image, 'left', self.fight_1_steps)
		image = pygame.image.load(self.right + "WarriorRightAttack01.png")
		self.fight_1_right = self.animator(image, 'right', self.fight_1_steps)

	def fight_2(self):
		image = pygame.image.load(self.up + "WarriorUpAttack02.png")
		self.fight_2_up = self.animator(image, 'up', self.fight_2_steps)
		image = pygame.image.load(self.down + "WarriorDownAttack02.png")
		self.fight_2_down = self.animator(image, 'down', self.fight_2_steps)
		image = pygame.image.load(self.left + "WarriorLeftAttack02.png")
		self.fight_2_left = self.animator(image, 'left', self.fight_2_steps)
		image = pygame.image.load(self.right + "WarriorRightAttack02.png")
		self.fight_2_right = self.animator(image, 'right', self.fight_2_steps)

	def flash(self):
		image = pygame.image.load(self.up + "WarriorUpAttack03.png")
		self.flash_up = self.animator(image, 'up', self.flash_steps)
		image = pygame.image.load(self.down + "WarriorDownAttack03.png")
		self.flash_down = self.animator(image, 'down', self.flash_steps)
		image = pygame.image.load(self.left + "WarriorLeftAttack03.png")
		self.flash_left = self.animator(image, 'left', self.flash_steps)
		image = pygame.image.load(self.right + "WarriorRightAttack03.png")
		self.flash_right = self.animator(image, 'right', self.flash_steps)