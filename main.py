import pygame as pg
import numpy as np
from pygame.locals import *


def main():
    pg.init()
    s = pg.display.set_mode((320, 240))
    # s = pg.surface((320,240))
    c = pg.time.Clock()
    i = 0
    fps = 30
    print("load wav")
#    sound1 = pg.mixer.Sound("../Lander-Resources/Music-Andrea-Baroni/OfGodsAndPhilosophers(loop).wav")
    sound1 = pg.mixer.Sound("data/andrea-baroni.ogg")
    sound2 = pg.mixer.Sound("../Lander-Resources/Sfx-Free-Retro-Musix&SE/SE-Gun-001.wav")
    sound1.set_volume(0.2)
    while True:
        s.fill(pg.Color(192, 192, 192), special_flags=BLEND_RGB_MULT)
        try:
            evt = None
            for evt in pg.event.get():
                if evt.type == QUIT or \
                        (evt.type == KEYDOWN and evt.key == K_ESCAPE):
                    pg.quit()
                    exit()
                if evt.type == KEYDOWN:
                    sound2.play()
                print(" event:", evt)
        except:
            pass
        if i == 0:
            print("play wav")
            sound1.play(-1)
        pg.draw.line(s, pg.Color("green"),
                     (np.random.rand() * 320, np.random.rand() * 320),
                     (np.random.rand() * 320, np.random.rand() * 320))
        pg.display.update()
        c.tick(fps)
        i += 1
        if i >= fps * 10000:
            break
    pg.quit()

if __name__ == '__main__':
    main()
