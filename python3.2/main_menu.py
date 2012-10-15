import menu_base
import pygame

#Will be made configurable via ini at a later date
class main_menu:
    def __init__(self,surface):
        self.timeout = 10000
        self.surface = surface
        self.base = menu_base.menu_base(self.surface,150,25)
        self.base.add_button("Start Game",3)
        self.base.add_button("Demo",4)
        self.base.add_button("High Scores",5)
        self.base.add_button("Exit",-10)
        
    def main_loop(self):
        code = None
        pygame.draw.rect(self.surface, (0, 0, 0), self.surface.get_rect())
        while code == None:
            for event in pygame.event.get():
                code = self.base.event(event)
            pygame.display.flip()
        return code
                
if __name__ == "__main__":
    #Init the modules we need
    pygame.display.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1024, 768))
    a = main_menu(screen)
    a.main_loop()