import menu_base
import pygame

#Will be made configurable via ini at a later date
class ages_menu:
    def __init__(self,surface):
        self.timeout = 10000
        self.surface = surface
        self.base = menu_base.menu_base(self.surface,150,25)
        self.base.add_button("0-13","0-13")
        self.base.add_button("13-18","13-18")
        self.base.add_button("18-21","18-21")
        self.base.add_button("21-30","21-30")
        self.base.add_button("30-40","30-40")
        self.base.add_button("40-60","40-60")
        self.base.add_button("60+","60+")
        
    def main_loop(self):
        code = None
        pygame.draw.rect(self.surface, (0, 0, 0), self.surface.get_rect())
        while code == None:
            for event in pygame.event.get():
                code = self.base.event(event)
            pygame.display.flip()
        return code
                