from modules import datahandler
import pygame


def main():
    
    data = datahandler.DataHandler()

    pygame.init()

    surface = pygame.display.set_mode([1280, 720])

    clock = pygame.time.Clock()
    
    running = True
    
    world_map = pygame.image.load('assets/world map.jpg')
    world_map = pygame.transform.scale(world_map, [1280, 720])



    # MAIN LOOP
    while running:
        
        # DRAW
        surface.fill([0, 0, 0])

        surface.blit(world_map, [0, 0])

        for object in data.debris_list:
            lat, lon = data.get_location(object, [])
            x, y = data.convert(lat, lon)
            pygame.draw.circle(surface, [255, 0, 0], [x, y], 2)
 
        pygame.display.update()

        # UPDATE



        # INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        print(clock.tick(30))
    exit()
    # END


if __name__ == '__main__':
    main()