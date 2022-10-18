import pygame

class SkillBar(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('graphics/PlayerUI/skillbar.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.name = "skill_bar"

class HealthBar(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.empty_bar = pygame.image.load('graphics/PlayerUI/bar.png').convert_alpha()
        self.image = self.combine()
        self.rect = self.image.get_rect(center = pos)
        self.pos = pos
        self.name = "health_bar"
    
    def set_position(self, pos):
        self.image = self.combine()
        self.rect = self.image.get_rect(center = pos)
        self.pos = pos

    def combine(self):
        image_bar = self.get_image(self.empty_bar, 1, 120, 20, 1)
        image_health = self.health()
        image_mana = self.mana()
        surf = pygame.Surface((120, 20), pygame.SRCALPHA)
        surf.blit(image_bar, (0, 0))
        surf.blit(image_health , (0, -5))
        surf.blit(image_mana, (0, 5))
        image = pygame.transform.scale(surf, (120, 20))
        return image
      
    def health(self):
        image_opt = self.get_image(self.empty_bar, 0, 120, 10, 1)
        return image_opt

    def mana(self):
        image_opt = self.get_image(self.empty_bar, 1, 120, 10, 1)
        return image_opt

    def get_image(self, image, frame, width, height, scale):
        image_opt = pygame.Surface((width, height), pygame.SRCALPHA)
        image_opt.blit(image, (0, 0), (0, (frame * height), width, height))
        image_opt = pygame.transform.scale(image_opt, (width * scale, height * scale))
        return image_opt

class PlayerUI(pygame.sprite.Group):
    def __init__(self, groups):
        super().__init__(groups)


    def update(self):
        print("updated!")