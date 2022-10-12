from pytmx.util_pygame import load_pygame
import pytmx
import pygame
import random

class AnimatedObject(pygame.sprite.Sprite):
    def __init__(self,pos,surf):
        pygame.sprite.Sprite.__init__(self)
        self.name = "animated"
        self.update_cycle = 0
        self.image_collecton = surf
        self.image = surf[0]
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.update_cycle += 1 
        self.image = self.image_collecton[self.update_cycle//20]
        self.rect = self.image.get_rect(center = self.rect.center)  
        if self.update_cycle == 60:
            self.update_cycle = 0

class Rectangle(pygame.sprite.Sprite):
    def __init__(self,obj):
        pygame.sprite.Sprite.__init__(self)
        self.name = obj.name
        self.image = pygame.Surface((obj.width, obj.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (obj.x, obj.y))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):    
        self.mask = pygame.mask.from_surface(self.image)

class Map(pygame.sprite.Group):
    def __init__(self, groups):
        super().__init__(groups)
        self.tmxdata = load_pygame("map/Arena.tmx")
        self.object_list = ["King", "People"]
        self.collision_list = ["Collision"]
        self.tile_list   = ["Environment"]
        self.group = groups
        self.Parse()

    def Parse(self):
        if len(self.collision_list) > 0:
            for col in self.collision_list:
                self.CollisionParser(col)    
        if len(self.object_list) > 0:
            for obj in self.object_list:
                self.ObjectParser(obj)        
        if len(self.tile_list) > 0:
            for tile in self.tile_list:
                self.TileParser(tile)
            

    def CollisionParser(self, name):
        for layer in self.tmxdata.visible_layers:                          
            if layer.name == name:
                for obj in layer:
                    self.collision_rect = Rectangle(obj)
                    self.group.add(self.collision_rect) 
        
    def ObjectParser(self, name):
        for layer in self.tmxdata.visible_layers:                          
            if layer.name == name:
                for obj in layer:
                    for gid, props in self.tmxdata.tile_properties.items():
                        image = self.tmxdata.get_tile_image_by_gid(gid)
                        if image == obj.image:  
                            self.pos = (obj.x, obj.y)
                            self.image_list = []
                            for i in range(len(props['frames'])):
                                image = self.tmxdata.get_tile_image_by_gid(props['frames'][i].gid)
                                image = pygame.transform.scale(image, (obj.width, obj.height))
                                self.image_list.append(image)     
                            self.anim_object = AnimatedObject(self.pos, self.image_list)    
                            self.group.add(self.anim_object)   


    def TileParser(self, name):
        for layer in self.tmxdata.visible_layers:
            if layer.name == name:
                for x, y, surf in layer:
                    for gid, props in self.tmxdata.tile_properties.items():
                            image = self.tmxdata.get_tile_image_by_gid(gid)
                            if image == self.tmxdata.get_tile_image_by_gid(surf):
                                self.pos = (x*32, (y-1)*32)
                                self.image_list = []
                                for i in range(len(props['frames'])):
                                    image = self.tmxdata.get_tile_image_by_gid(props['frames'][i].gid)
                                    self.image_list.append(image)     
                                self.anim_object = AnimatedObject(self.pos, self.image_list)    
                                self.group.add(self.anim_object)   
                                    
    def update(self):
        self.group.update()