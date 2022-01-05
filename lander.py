#              ___        _             _
#             | _ \___ __| |__ _ _ __ _| |__
#             |   / -_) _` / _| '_/ _` | '_ \
#             |_|_\___\__,_\__|_| \__,_|_.__/
#                  | |   __ _ _ _  __| |___ _ _
#                  | |__/ _` | ' \/ _` / -_) '_|
#                  |____\__,_|_||_\__,_\___|_|

# Portage of Redcrab Lander 1.4.1, initially design with FreeBasic

import pygame as pg
from pygame.locals import *
import numpy as np
import math
import os
from enum import Enum
from datetime import datetime
import zipfile
import io


class RedcrabLander:
    class TV_Polar2D:
        def __init__(self):
            self.radius = 0.0
            self.angle = 0.0

    class TV_vertex2D:
        def __init__(self):
            self.x = 0.0
            self.y = 0.0

    class TV_Glyph:
        def __init__(self):
            self.glyph = ""

    class TinyVectrex:
        def __init__(self):
            self.plot = tuple(RedcrabLander.TV_Polar2D() for _ in range(18))
            self.plotxy = tuple(RedcrabLander.TV_vertex2D() for _ in range(18))
            self.size = 0.0
            self.angle = 0.0
            self.cx = 0
            self.alphabet = tuple(RedcrabLander.TV_Glyph() for _ in range(356))
            self.boom = 1.0
            self.set_center_text(0.5)
            j = 1
            for i in np.linspace(0, 1.75 * np.pi, 8):
                self.plot[j].radius = 1.0
                self.plot[j + 8].radius = (2 ** .5) / 2.0
                self.plot[j].angle = self.plot[j + 8].angle = i
                j += 1
            self.scale_rotation(4.0, 0.0)
            # sign
            self.alphabet[ord("+")].glyph = "PL NJ"
            self.alphabet[ord("-")].glyph = "NJ"
            self.alphabet[ord("*")].glyph = "OK MQ NJ"
            self.alphabet[ord("/")].glyph = "IE"
            self.alphabet[ord(":")].glyph = "PP LL"
            self.alphabet[ord("!")].glyph = "PA LL"
            self.alphabet[ord(".")].glyph = "LL"
            self.alphabet[ord(",")].glyph = "LD"
            self.alphabet[ord("'")].glyph = "HP"
            self.alphabet[ord("?")].glyph = "OGHIAL DD"
            self.alphabet[ord("(")].glyph = "HGED"
            self.alphabet[ord(")")].glyph = "HICD"
            self.alphabet[ord("_")].glyph = "EC"
            self.alphabet[ord("~")].glyph = "2E0D2C 2HCBDFEH"  # small ship with thrust
            self.alphabet[ord("^")].glyph = "2HCBDFEH"  # small ship without thrust
            self.alphabet[ord("$")].glyph = "HCBDFEH"  # normal-&sized ship
            self.alphabet[ord("&")].glyph = "2HCBDFEH 0BCDEFGHIB"  # rounded lander
            self.alphabet[ord("#")].glyph = "JKLMNOPQJ BJ CK DL EM FN GO HP IQ"  # sun
            self.alphabet[ord("~")].glyph = "GICEG BDFHB"  # star
            self.alphabet[ord("§")].glyph = "0H3I0B3C0D3E0F3G0H 3I0I 3C0C 3E0E 3G0G"  # Energy sucker
            self.alphabet[ord("%")].glyph = "BHFNECJB"  # Arrow
            #  Digit
            self.alphabet[ord("0")].glyph = "EIHGEDCI"
            self.alphabet[ord("1")].glyph = "GHL"
            self.alphabet[ord("2")].glyph = "GHIEC"
            self.alphabet[ord("3")].glyph = "GHIACDE"
            self.alphabet[ord("4")].glyph = "LHNJ"
            self.alphabet[ord("5")].glyph = "IGNJCDE"
            self.alphabet[ord("6")].glyph = "IHGEDCJN"
            self.alphabet[ord("7")].glyph = "GIL"
            self.alphabet[ord("8")].glyph = "NGHICDENJ"
            self.alphabet[ord("9")].glyph = "JNGHICDE"
            #  Alphabet Uppercase
            self.alphabet[ord("A")].glyph = "ENOPQJC NJ"
            self.alphabet[ord("B")].glyph = "EGPQAKLE NA"
            self.alphabet[ord("C")].glyph = "KLMNOPQ"
            self.alphabet[ord("D")].glyph = "EGPQJKLE"
            self.alphabet[ord("E")].glyph = "IGEC NA"
            self.alphabet[ord("F")].glyph = "IGE NA"
            self.alphabet[ord("G")].glyph = "AJKLMNOPQ"
            self.alphabet[ord("H")].glyph = "GE IC NJ"
            self.alphabet[ord("I")].glyph = "PL"
            self.alphabet[ord("J")].glyph = "QKLM"
            self.alphabet[ord("K")].glyph = "GE NP NC"
            self.alphabet[ord("L")].glyph = "GEC"
            self.alphabet[ord("M")].glyph = "EGAIC"
            self.alphabet[ord("N")].glyph = "EGCI"
            self.alphabet[ord("O")].glyph = "JKLMNOPQJ"
            self.alphabet[ord("P")].glyph = "EGPQAN"
            self.alphabet[ord("Q")].glyph = "AKLMNOPQJK"
            self.alphabet[ord("R")].glyph = "EGPQAN AC"
            self.alphabet[ord("S")].glyph = "QPOKLM"
            self.alphabet[ord("T")].glyph = "PL GI"
            self.alphabet[ord("U")].glyph = "GNMLKJI"
            self.alphabet[ord("V")].glyph = "GLI"
            self.alphabet[ord("W")].glyph = "GEACI"
            self.alphabet[ord("X")].glyph = "GC EI"
            self.alphabet[ord("Y")].glyph = "GAI AL"
            self.alphabet[ord("Z")].glyph = "GIEC"
            # Alphabet lower case
            self.alphabet[ord("a")].glyph = "1ENOPQJC NJ"
            self.alphabet[ord("b")].glyph = "1EGPQAKLE NA"
            self.alphabet[ord("c")].glyph = "1KLMNOPQ"
            self.alphabet[ord("d")].glyph = "1EGPQJKLE"
            self.alphabet[ord("e")].glyph = "1IGEC NA"
            self.alphabet[ord("f")].glyph = "1IGE NA"
            self.alphabet[ord("g")].glyph = "1AJKLMNOPQ"
            self.alphabet[ord("h")].glyph = "1GE IC NJ"
            self.alphabet[ord("i")].glyph = "1PL"
            self.alphabet[ord("j")].glyph = "1QKLM"
            self.alphabet[ord("k")].glyph = "1GE NP NC"
            self.alphabet[ord("l")].glyph = "1GEC"
            self.alphabet[ord("m")].glyph = "1EGAIC"
            self.alphabet[ord("n")].glyph = "1EGCI"
            self.alphabet[ord("o")].glyph = "1JKLMNOPQJ"
            self.alphabet[ord("p")].glyph = "1EGPQAN"
            self.alphabet[ord("q")].glyph = "1AKLMNOPQJK"
            self.alphabet[ord("r")].glyph = "1EGPQAN AC"
            self.alphabet[ord("s")].glyph = "1QPOKLM"
            self.alphabet[ord("t")].glyph = "1PL GI"
            self.alphabet[ord("u")].glyph = "1GNMLKJI"
            self.alphabet[ord("v")].glyph = "1GLI"
            self.alphabet[ord("w")].glyph = "1GEACI"
            self.alphabet[ord("x")].glyph = "1GC EI"
            self.alphabet[ord("y")].glyph = "1GAI AL"
            self.alphabet[ord("z")].glyph = "1GIEC"

        def set_center_text(self, cenx):
            self.cx = cenx

        def scale_rotation(self, psize, pangle):
            for i in range(18):
                self.plotxy[i].x = psize * math.cos(pangle + self.plot[i].angle) * self.plot[i].radius
                self.plotxy[i].y = psize * math.sin(pangle + self.plot[i].angle) * self.plot[i].radius
            self.size = psize
            self.angle = pangle

        def draw_script(self, ctx, glyph_design, xc, yc, colour, explode=None):
            explode = self.boom if explode is None else explode
            default_colour = colour
            xo = 0.0
            yo = 0.0
            k = 1
            pen_is_up = True
            if glyph_design is None:
                return
            glyph_primitives = iter(glyph_design)
            for glyph_primitive in glyph_primitives:
                if glyph_primitive == "$":
                    glyph_primitive = next(glyph_primitives)
                    colour = ord(glyph_primitive)
                    if 48 <= colour <= 57:
                        colour -= 48
                    elif 65 <= colour <= 70:
                        colour -= 55
                    else:
                        colour = default_colour
                elif glyph_primitive == " ":
                    pen_is_up = True
                else:
                    a = ord(glyph_primitive)
                    if 65 <= a < (65 + 17):
                        a -= 65
                        if k == 1.0:
                            x = self.plotxy[a].x + xc
                            y = self.plotxy[a].y + yc
                        else:
                            x = self.plotxy[a].x * k + xc
                            y = self.plotxy[a].y * k + yc
                        if not pen_is_up:
                            if explode == 1.0:
                                ctx.draw_line(xo, yo, x, y, colour)
                            else:
                                xx = (xo + x) / 2.0 - xc
                                yy = (yo + y) / 2.0 - yc
                                xx = xx * explode - xx
                                yy = yy * explode - yy
                                x1 = xo + xx
                                y1 = yo + yy
                                x2 = x + xx
                                y2 = y + yy
                                ctx.draw_line(x1, y1, x2, y2, colour)
                        xo = x
                        yo = y
                        pen_is_up = False
                    else:  # Factor for sub grid
                        if 48 <= a <= 57:  # from 0 to 9
                            if a == 48:  # 0 is 1 : square_root_of_2 power 0
                                k = 1.0
                            elif a == 49:  # 1 is square_root_of_2 power 1
                                k = 0.70710678118654752440084436210485
                            else:  # square_root_of_2 power n (2 to 9)
                                k = 0.70710678118654752440084436210485 ** (a - 48)

        def draw_text(self, ctx, s, xc, yc, colour, text_angle=None):
            text_angle = self.angle if (text_angle is None) else text_angle
            c = s.__len__() * self.cx
            dx = self.size * math.cos(text_angle) * 1.80
            dy = self.size * math.sin(text_angle) * 1.80
            j = 0
            for letter in s:
                self.draw_script(ctx, self.alphabet[ord(letter)].glyph,
                                 (xc + dx * (j - c)), (yc + dy * (j - c)), colour)
                j += 1

        def draw_text_rich(self, ctx, s, xc, yc, colour, text_angle=None):
            text_angle = self.angle if (text_angle is None) else text_angle
            c, _ = self.draw_text_length(s)
            c = float(c * self.cx)
            default_colour = colour
            dx = self.size * math.cos(text_angle) * 1.80
            dy = self.size * math.sin(text_angle) * 1.80
            j = 0
            read_colour = False
            for letter in s:
                if letter == "@":
                    read_colour = True
                elif read_colour:
                    a = ord(letter)
                    if 48 <= a <= 57:
                        colour = a - 48
                    elif 65 <= a <= 70:
                        colour = a - 55
                    else:
                        colour = default_colour
                    read_colour = False
                else:
                    a = ord(letter)
                    self.draw_script(ctx, self.alphabet[a].glyph, (xc + dx * (j - c)), (yc + dy * (j - c)), colour)
                    j += 1

        def draw_text_length(self, s):
            number_character = 0
            if s is None:
                return 0, 0
            it = iter(s)
            for c in it:
                if c == "@":
                    next(it)
                    number_character += 1
                else:
                    number_character += 1
            return number_character, self.size * 1.8 * number_character

    class GameStatus(Enum):
        GS_START = 0
        GS_INTRO = 1
        GS_RUN = 2
        GS_PAUSE = 3
        GS_CRASHED = 4
        GS_LANDED = 5
        GS_GAME_OVER = 6
        GS_FINISH = 7
        GS_EDIT = 8
        GS_EDIT_TEXT = 9

    class PlayerAction(Enum):
        PA_NOTHING = 0
        PA_LEFT = 1
        PA_RIGHT = 2
        PA_THRUST = 3
        PA_QUIT = 4
        PA_PAUSE = 5

    class LanderStatus(Enum):
        LS_NORMAL = 0
        LS_THRUST = 1
        LS_LANDED = 2
        LS_LANDED_NO_SKY = 3
        LS_CRASH = 4

    class EnergySuckerStatus(Enum):
        SS_NORMAL = 0
        SS_EXPLODED = 1

    class Vertex2D:
        def __init__(self):
            self.x = 0.0
            self.y = 0.0

    class Lander:
        def __init__(self, x=0, y=0):
            self.LANDER_NORMAL = "$F2HCBDFEH"
            self.LANDER_LANDED = "$F2HCBDFEH"
            self.LANDER_THRUST = "$E2E0D2C$$ $F2HCBDFEH"
            self.model = RedcrabLander.TinyVectrex()
            self.location = RedcrabLander.Vertex2D()
            self.speed = RedcrabLander.Vertex2D()
            self.fuel = 0.0
            self.angle = 0.0
            self.size = 0.0
            self.status = RedcrabLander.LanderStatus.LS_NORMAL
            self.crash_tic = 0
            self.noise_tic = 0
            self.tic = 0
            self.init()
            self.location.x = x
            self.location.y = y

        def init(self):
            self.location.x = 160
            self.location.y = 230
            self.fuel = 100
            self.angle = 0
            self.size = 7
            self.status = RedcrabLander.LanderStatus.LS_NORMAL
            self.crash_tic = 0
            self.tic = 0
            self.noise_tic = 0
            self.model.boom = 1

        def draw(self, ctx):
            self.model.scale_rotation(self.size * 2 * ctx.KW, self.angle)
            self.tic += 1
            if self.status == RedcrabLander.LanderStatus.LS_NORMAL:
                self.crash_tic = 0
                self.model.boom = 1
                self.model.draw_script(ctx, self.LANDER_NORMAL, (self.location.x * ctx.KW),
                                       ((240 - self.location.y) * ctx.KH), 10)
                if self.fuel <= 0:
                    ctx.vectrex_text_small.draw_text(ctx, "I'M CRASHING!", (self.location.x * ctx.KW),
                                                     ((240 - self.location.y - self.size - 7) * ctx.KH), 15)
            elif self.status == RedcrabLander.LanderStatus.LS_LANDED or \
                    self.status == RedcrabLander.LanderStatus.LS_LANDED_NO_SKY:
                self.crash_tic = 0
                self.model.boom = 1
                self.model.draw_script(ctx, self.LANDER_NORMAL, (self.location.x * ctx.KW),
                                       ((240 - self.location.y) * ctx.KH), 10)
                ctx.draw_circle(self.location.x * ctx.KW, (240 - self.location.y) * ctx.KH,
                                (self.size + 5 + 3 * math.sin(self.tic / 10.0)) * ctx.KW, 8)
                if 70 <= self.fuel <= 99:
                    if self.status == RedcrabLander.LanderStatus.LS_LANDED:
                        ctx.vectrex_text_small.draw_text(ctx, "Launch To " +
                                                         str(int(3 - ((self.fuel - 70.0) / 30 * 4))),
                                                         (self.location.x * ctx.KW),
                                                         ((240 - self.location.y - self.size - 7) * ctx.KH), 15)
                    else:
                        ctx.vectrex_text_small.draw_text(ctx, "I'm Ready !", (self.location.x * ctx.KW),
                                                         ((240 - self.location.y - self.size - 7) * ctx.KH), 15)
                if self.fuel >= 100 and self.location.y < 300 and self.status == RedcrabLander.LanderStatus.LS_LANDED:
                    self.angle = 0
                    self.location.y *= 1.01

            if self.status == RedcrabLander.LanderStatus.LS_CRASH:
                self.crash_tic += 1

                if self.crash_tic < 60:
                    self.model.boom = 1 - self.crash_tic / 15.0
                    self.model.draw_script(ctx, self.LANDER_NORMAL, (self.location.x * ctx.KW),
                                           ((240 - self.location.y) * ctx.KH), 10)
            if self.status == RedcrabLander.LanderStatus.LS_THRUST:
                self.noise_tic = 0

                if self.tic % 20 < self.fuel / 5 and self.fuel > 0:
                    self.model.draw_script(ctx, self.LANDER_THRUST, (self.location.x * ctx.KW),
                                           ((240 - self.location.y) * ctx.KH), 10)
                    if self.tic % 3 == 0:
                        ctx.sound_play_thrust()  # SoundManager.instance.NoiseStart();
                else:
                    self.model.draw_script(ctx, self.LANDER_NORMAL, (self.location.x * ctx.KW),
                                           ((240 - self.location.y) * ctx.KH), 10)
            if self.status != RedcrabLander.LanderStatus.LS_THRUST:
                self.noise_tic += 1
                #  if (self.noise_tic>5) SoundManager.instance.NoiseStop();

    class EnergySucker:
        def __init__(self):
            self.EnergySucker_NORMAL = "$C0H3I0B3C0D3E0F3G0H $E3I0I 3C0C 3E0E 3G0G"
            self.model = RedcrabLander.TinyVectrex()
            self.location = RedcrabLander.Vertex2D()
            self.speed = RedcrabLander.Vertex2D()
            self.angle = 0.0
            self.size = 0.0
            self.tic = 0
            self.status = RedcrabLander.EnergySuckerStatus.SS_NORMAL
            self.init()

        def draw(self, ctx):
            self.tic += 1
            if self.status == RedcrabLander.EnergySuckerStatus.SS_NORMAL:
                self.model.scale_rotation(self.size * ctx.KW, self.tic * np.pi / 90.0)
                self.model.draw_script(ctx, self.EnergySucker_NORMAL, (self.location.x * ctx.KW),
                                       ((240 - self.location.y) * ctx.KH), 10)
            elif self.status == RedcrabLander.EnergySuckerStatus.SS_EXPLODED:
                pass  # future evolution : when energy sucker are destroyable

        def init(self, x=0, y=0):
            self.tic = 0
            self.status = RedcrabLander.EnergySuckerStatus.SS_NORMAL
            self.location.x = 0
            self.location.y = 0
            self.speed.x = 0
            self.speed.y = 0
            self.angle = 0
            self.size = 7
            self.model.boom = 1
            self.location.x = x
            self.location.y = y

    class Scene:
        class Landscape:
            def __init__(self):
                self.ground = 0
                self.sky = 0

        def __init__(self):
            self.landscape = tuple(RedcrabLander.Scene.Landscape() for _ in range(320))
            self.pad_location = RedcrabLander.Vertex2D()
            self.fuel_location = RedcrabLander.Vertex2D()
            self.gravity = 0.0
            self.start_location = RedcrabLander.Vertex2D()
            self.inverse = 0
            self.tic = 0
            self.go_up = 0
            self.go_down = 0
            self.go_left = 0
            self.go_right = 0
            self.allow_take_off = 0
            self.landed_message = ""
            self.init()

        def draw(self, ctx):
            self.tic += 1
            for i in range(self.landscape.__len__() - 1):
                if self.landscape[i].ground != self.landscape[i].sky or \
                        self.landscape[i + 1].ground != self.landscape[i + 1].sky:
                    if self.landscape[i].ground >= 20 and self.landscape[i + 1].ground >= 20:
                        ctx.draw_line(i * ctx.KW, (240 - int(self.landscape[i].ground)) * ctx.KH, (i + 1) * ctx.KW,
                                      (240 - int(self.landscape[i + 1].ground)) * ctx.KH, 13)
                    ctx.draw_line(i * ctx.KW, (240 - int(self.landscape[i].sky)) * ctx.KH, (i + 1) * ctx.KW,
                                  (240 - int(self.landscape[i + 1].sky)) * ctx.KH, 13)
            ctx.draw_box_full(int(self.pad_location.x - 10) * ctx.KW, (240 - int(self.pad_location.y)) * ctx.KH,
                              int(self.pad_location.x + 10) * ctx.KW, (245 - int(self.pad_location.y)) * ctx.KH, 11)
            ctx.vectrex_text_small.draw_text(ctx, "Target", ((self.pad_location.x + 1) * ctx.KW),
                                             ((240 - self.pad_location.y + 8) * ctx.KH), 11)
            ctx.draw_box_full(int(self.fuel_location.x - 10) * ctx.KW, (240 - int(self.fuel_location.y)) * ctx.KH,
                              int(self.fuel_location.x + 10) * ctx.KW, (245 - int(self.fuel_location.y)) * ctx.KH, 11)
            if self.tic % 240 < 120:
                energy = "Energy"
            else:
                energy = "Reload"
            ctx.vectrex_text_small.draw_text(ctx, energy, ((self.fuel_location.x + 1) * ctx.KW),
                                             ((240 - self.fuel_location.y + 8) * ctx.KH), 11)

        def init(self, global_level=0):
            self.tic = 0
            self.gravity = 0.0025 * (int(global_level / 10.0) / 3.0 + 1.0)
            self.inverse = 0
            self.allow_take_off = 1
            self.go_up = 0
            self.go_down = 0
            self.go_left = 0
            self.go_right = 0
            self.landed_message = "LANDED"
            if global_level <= 0:
                global_level = 1
            level = global_level % 10
            ub = self.landscape.__len__() - 1
            self.start_location.x = 160
            self.start_location.y = 230
            prev = np.random.rand() * 200 + 20
            for land_slice in self.landscape:
                land_slice.sky = 250
                land_slice.ground = prev
            for j in range(1, 7):
                slope = np.random.rand() * (level + 1) * 250 / j - ((level + 1) * 250 / 2 / j)
                cnt = 0
                for i in range(ub + 1):
                    cur = self.landscape[i].ground + slope * cnt
                    self.landscape[i].ground = cur
                    cnt += 1
                    if cnt > 320 / 2 ** j:
                        slope = np.random.rand() * (level + 1) * 250 / j - ((level + 1) * 250 / 2 / j)
                        cnt = 0
                        if i < ub:
                            delta = cur - self.landscape[i + 1].ground
                        else:
                            delta = 0
                        for k in range(i + 1, ub + 1):
                            self.landscape[k].ground += delta
            delta = 0
            mini = 1000
            maxi = 0
            for land_slice in self.landscape:
                mini = land_slice.ground if (land_slice.ground < mini) else mini
                maxi = land_slice.ground if (land_slice.ground > maxi) else maxi
                delta += land_slice.ground
            ground = (maxi - mini) / 5 * (1 if level == 0 else level)
            mini = maxi - ground
            for land_slice in self.landscape:
                land_slice.ground = mini if (land_slice.ground < mini) else land_slice.ground
                land_slice.ground = (land_slice.ground - mini) / (maxi - mini) * (level / 8.0) * 200 + 20
                land_slice.ground = float(np.clip(land_slice.ground, 20.0, 220.0))

            self.fuel_location.x = -100.0
            self.fuel_location.y = -100
            self.pad_location.x = (int(np.random.rand() * 2) * 300 - 150) * (level / 10.0) + 160
            self.pad_location.y = (self.landscape[int(self.pad_location.x) - 10].ground +
                                   self.landscape[int(self.pad_location.x) + 10].ground) / 2
            self.pad_location.y = 20 if (self.pad_location.y < 20) else self.pad_location.y
            lb = int(self.pad_location.x) - 10
            ub = int(self.pad_location.x) + 10
            for i in range(lb, ub + 1):
                self.landscape[i].ground = self.pad_location.y

    class Game:
        def __init__(self):
            self.tic = 0
            self.tic2 = 0
            self.life = 0
            self.safe_land = 0
            self.sub_level_x = 0
            self.sub_level_y = 0
            self.score = 0
            self.showing_message_screen = True
            self.showing_message_editor_help = False
            self.message = tuple()
            self.ship = RedcrabLander.Lander()
            self.sucker = tuple(RedcrabLander.EnergySucker() for _ in range(101))
            self.number_of_sucker = 0
            self.scene = RedcrabLander.Scene()
            self.player_action = RedcrabLander.PlayerAction.PA_NOTHING
            self.status = RedcrabLander.GameStatus.GS_INTRO
            self.level_title = [""] * 201
            self.xm = 0.0
            self.ym = 0.0
            self.bm = 0
            self.xrm = 0
            self.yrm = 0
            self.init()
            self.best_safe_land = 0
            self.best_score = 0
            try:
                btf = open(RedcrabLander.data_path + "LANDER.SCO")
                self.best_score = int(btf.readline())
                self.best_safe_land = int(btf.readline())
                btf.close()
            except Exception as n:
                print(n)

            for i in range(self.level_title.__len__()):
                self.level_title[i] = "Press Any Key to Start"
            # default level titles if the level can't be loaded
            self.level_title[1] = "Another easy one,"
            self.level_title[2] = "Looks to be the same"
            self.level_title[3] = "Detecting FOE not far away"
            self.level_title[4] = "ALERT ! § Energy sucker ! Avoid it !"
            self.level_title[5] = "It was easy... ! But it still here !"
            self.level_title[6] = "1 more § !"
            self.level_title[7] = "Energy Sucker Engine Enhanced !"
            self.level_title[8] = "BEWARE ! They fly a bit faster!"
            self.level_title[9] = "§ speed limit ! But they are 3 !"
            self.level_title[10] = "New planet with higher gravity"
            self.level_title[11] = "Hope you're not tired"
            self.level_title[12] = "He he ! 4 suckers now !"
            self.level_title[13] = "Again !"
            self.level_title[14] = "Again !"
            self.level_title[15] = "Again !"
            self.level_title[16] = "Ooh ! 5 Energy Suckers Now"
            self.level_title[17] = "Again !"
            self.level_title[18] = "Again !"
            self.level_title[19] = "One more sucker ! "
            self.level_title[20] = "New planet with higher gravity and 6 § !"
            self.level_title[21] = "Keep going almost finished !"
            self.level_title[22] = "Grr ! Here come another one"
            self.level_title[23] = "----------"

        def init(self):
            self.safe_land = 0
            self.score = 0
            self.life = 3
            self.status = RedcrabLander.GameStatus.GS_INTRO
            self.tic = 0
            self.tic2 = 0
            self.number_of_sucker = 0
            self.init_level(0)

        def draw(self, ctx):
            aLife = RedcrabLander.Lander()
            ctx.clear_all_drawing()
            #  Landscape
            self.scene.draw(ctx)
            #  Lander
            self.ship.draw(ctx)
            #  Sucker
            for i in range(self.number_of_sucker):
                self.sucker[i].draw(ctx)
            #  Score
            if self.status != RedcrabLander.GameStatus.GS_EDIT and \
                    self.status != RedcrabLander.GameStatus.GS_EDIT_TEXT:
                ctx.vectrex_board_text.draw_text(ctx, " & " + str(self.safe_land) + "  # " + str(self.score),
                                                 0, (234 * ctx.KH), 10)
            else:
                if self.scene.allow_take_off == 0:
                    m = "L"
                else:
                    m = "T"
                ctx.vectrex_board_text.draw_text(ctx, " & " + str(self.safe_land) +
                                                 " (" + str(self.sub_level_x) + "," + str(
                    self.sub_level_y) + ")" + m, 0, (234 * ctx.KH), 10)

            # Life
            if self.status != RedcrabLander.GameStatus.GS_EDIT and \
                    self.status != RedcrabLander.GameStatus.GS_EDIT_TEXT:
                aLife.size = 5
                aLife.status = RedcrabLander.LanderStatus.LS_NORMAL
                aLife.location.y = 6
                for i in range(1, self.life + 1):
                    aLife.location.x = 88 + 25 + (i - 1) * 12
                    aLife.angle = self.tic * np.pi / 180
                    aLife.draw(ctx)

            # Arrow to show possible direction
            if self.scene.go_up != 0:
                ctx.vectrex_board_text.scale_rotation(ctx.vectrex_board_text.size, 0)
                ctx.vectrex_board_text.draw_text(ctx, "%", (88 * ctx.KW), (229 * ctx.KH), 10)
            if self.scene.go_down != 0:
                ctx.vectrex_board_text.scale_rotation(ctx.vectrex_board_text.size, np.pi)
                ctx.vectrex_board_text.draw_text(ctx, "%", (88 * ctx.KW), (235 * ctx.KH), 10)
            if self.scene.go_left != 0:
                ctx.vectrex_board_text.scale_rotation(ctx.vectrex_board_text.size, -np.pi / 2)
                ctx.vectrex_board_text.draw_text(ctx, "%", (85 * ctx.KW), (232 * ctx.KH), 10)
            if self.scene.go_right != 0:
                ctx.vectrex_board_text.scale_rotation(ctx.vectrex_board_text.size, np.pi / 2)
                ctx.vectrex_board_text.draw_text(ctx, "%", (91 * ctx.KW), (232 * ctx.KH), 10)

            # Fuel	
            ctx.vectrex_board_text.scale_rotation(ctx.vectrex_board_text.size, self.tic * np.pi / 180)
            ctx.vectrex_board_text.draw_text(ctx, " ~", (150 * ctx.KW), (235 * ctx.KH), 14, 0)
            ctx.vectrex_board_text.scale_rotation(ctx.vectrex_board_text.size, 0)
            colour = 10
            colour = 14 if (self.ship.fuel < 50) else colour
            colour = 12 if (self.ship.fuel < 25) else colour
            ctx.draw_box_full(161 * ctx.KW, 231 * ctx.KH, (161 + self.ship.fuel) * ctx.KW, 239 * ctx.KH, colour)
            ctx.draw_box(161 * ctx.KW, 231 * ctx.KH, 261 * ctx.KW, 239 * ctx.KH, 15)

            # Speed
            if self.ship.speed.y < 0:
                speed = int((self.ship.speed.x ** 2 + self.ship.speed.y ** 2) * 1000)
                speed = 100 if (int(abs(self.ship.angle / (np.pi / 180))) >= 10) else speed
                speed = 100 if (speed > 100) else speed
                colour = 10
                colour = 14 if (speed > 30) else colour
                colour = 12 if (speed > 60) else colour
                ctx.draw_box_full(265 * ctx.KW, 231 * ctx.KH, (265 + speed / 2) * ctx.KW, 239 * ctx.KH, colour)
            ctx.draw_box(265 * ctx.KW, 231 * ctx.KH, (265 + 60 / 2) * ctx.KW, 239 * ctx.KH, 15)
            ctx.draw_box(265 * ctx.KW, 231 * ctx.KH, (265 + 50) * ctx.KW, 239 * ctx.KH, 15)

            if self.status == RedcrabLander.GameStatus.GS_START:
                #  START
                if self.tic2 < 200:
                    ctx.vectrex_text_1.draw_text(ctx, self.level_title[self.safe_land], ctx.G_WIDTH / 2.0,
                                                 (120 * ctx.KH * (self.tic2 - 10) / 190.0), 10)
                else:
                    if self.tic2 > 500:
                        ctx.vectrex_text_1.scale_rotation(4 * ctx.KW,
                                                          math.sin((self.tic2 - 500) * np.pi / 180 / 2) * np.pi / 4.0)
                    ctx.vectrex_text_1.draw_text(ctx, self.level_title[self.safe_land],
                                                 ctx.G_WIDTH / 2.0, (120.0 * ctx.KH), 10)
                    ctx.vectrex_text_1.scale_rotation(4.0 * ctx.KW, 0)
            elif self.status == RedcrabLander.GameStatus.GS_INTRO:
                #  INTRO
                if self.tic2 == 1:
                    ctx.sound_play_title()
                if self.tic2 <= 200:
                    ctx.vectrex_text_big.scale_rotation(1.0 * self.tic2 / 200.0 * 5.0 * ctx.KW,
                                                        1.0 * self.tic2 / 100.0 * np.pi)
                ctx.vectrex_text_big.draw_text(ctx, "$ Captain Lander $",
                                               ctx.G_WIDTH / 2.0, (95 * ctx.KH), 10)
                if self.tic2 >= 200:
                    ctx.vectrex_text_1.draw_text(ctx, "Left   : Turn left ",
                                                 ctx.G_WIDTH / 2.0, ((105 + 9) * ctx.KH), 10)
                if self.tic2 >= 230:
                    ctx.vectrex_text_1.draw_text(ctx, "Right  : Turn right",
                                                 ctx.G_WIDTH / 2.0, ((105 + 18) * ctx.KH), 10)
                if self.tic2 >= 260:
                    ctx.vectrex_text_1.draw_text(ctx, "Up     : Thrust    ",
                                                 ctx.G_WIDTH / 2.0, ((105 + 27) * ctx.KH), 10)
                if self.tic2 >= 290:
                    ctx.vectrex_text_1.draw_text(ctx, "Space  : Pause     ",
                                                 ctx.G_WIDTH / 2.0, ((105 + 36) * ctx.KH), 10)
                if self.tic2 >= 320:
                    ctx.vectrex_text_1.draw_text(ctx, "Escape : Quit      ",
                                                 ctx.G_WIDTH / 2.0, ((105 + 45) * ctx.KH), 10)
                if self.tic2 >= 320 and self.best_score != 0:
                    ctx.vectrex_text_1.draw_text(ctx, "Best score " + str(self.best_score) + " with " + str(
                        self.best_safe_land) + " landings", ctx.G_WIDTH / 2.0, ((105 + 62) * ctx.KH), 10)
                if self.tic2 >= 320 and self.best_score == 0:
                    ctx.vectrex_text_1.draw_text(ctx, "No Best Score Yet !",
                                                 ctx.G_WIDTH / 2.0, ((105 + 62) * ctx.KH), 10)
                if 200 <= self.tic2 <= 350:
                    ctx.vectrex_text_1.draw_text(ctx, self.level_title[self.safe_land], ctx.G_WIDTH / 2.0,
                                                 ((110.0 + 72) * ctx.KH * (self.tic2 - 300.0) / (350 - 300.0)), 10)
                else:
                    if self.tic2 >= 350:
                        ctx.vectrex_text_1.draw_text(ctx, self.level_title[self.safe_land],
                                                     ctx.G_WIDTH / 2.0, ((110 + 72) * ctx.KH), 10)
            elif self.status == RedcrabLander.GameStatus.GS_PAUSE:
                #  PAUSE
                if self.tic % 60 < 30:
                    ctx.vectrex_text_big.scale_rotation(5 * ctx.KW, 0)
                    ctx.vectrex_text_big.draw_text(ctx, "Pause", ctx.G_WIDTH / 2.0, (120 * ctx.KH), 12)
            elif self.status == RedcrabLander.GameStatus.GS_RUN:
                #  RUNNING
                if self.ship.fuel <= 0:
                    if self.tic % 30 < 15:
                        ctx.vectrex_text_big.scale_rotation(5 * ctx.KW, 0)
                        ctx.vectrex_text_big.draw_text(ctx, "NO ENERGY !", ctx.G_WIDTH / 2.0, (120 * ctx.KH), 12)
            elif self.status == RedcrabLander.GameStatus.GS_CRASHED:
                #  CRASHED
                #  "Life request" animation
                if self.tic2 <= 60:
                    aLife.location.x = 88 + 25 + self.life * 12
                    aLife.angle = self.tic * np.pi / 180
                    aLife.draw(ctx)
                if self.tic2 == 60:
                    self.load_level(self.safe_land, 0, 0)
                if self.tic2 > 60:
                    destination_x = self.scene.start_location.x
                    destination_y = self.scene.start_location.y
                    if self.tic2 < 60 + 200:
                        aLife.location.x = (destination_x - (88 + 25 + self.life * 12)) / 200.0 * (
                                self.tic2 - 60) + 88 + 25 + self.life * 12
                        aLife.location.y = (destination_y - 6.0) / 200.0 * (self.tic2 - 60) + 6
                        aLife.size = (7.0 - 5.0) / 200.0 * (self.tic2 - 60) + 5
                        aLife.angle = self.tic * np.pi / 180
                    else:
                        ctx.vectrex_text_small.draw_text(ctx, "I'm Ready", (destination_x * ctx.KW),
                                                         (((240.0 - destination_y) + 7 + 4) * ctx.KW), 15)
                        aLife.location.x = destination_x
                        aLife.location.y = destination_y
                        aLife.size = 7
                        aLife.angle = self.tic * np.pi / 180
                    aLife.draw(ctx)
                if self.tic2 < 200:
                    if self.tic2 % 4 == 0:
                        ctx.vectrex_text_2.scale_rotation((15.0 + np.random.rand() * 2.0) * ctx.KW,
                                                          (np.random.rand() * 0.2) - 0.1)
                else:
                    ctx.vectrex_text_2.boom = 1
                ctx.vectrex_text_2.draw_text(ctx, "CRASH!", ctx.G_WIDTH / 2.0, (120.0 * ctx.KH), 14)
                ctx.vectrex_text_2.boom = 1
            elif self.status == RedcrabLander.GameStatus.GS_GAME_OVER:
                #  GAME OVER
                if self.tic2 < 200:
                    ctx.vectrex_text_2.boom = 10 - (9 / 200.0 * self.tic2)
                    ctx.vectrex_text_2.scale_rotation(5 * ctx.KW * self.tic2 / 60, 0)
                ctx.vectrex_text_2.draw_text(ctx, "GAME OVER", ctx.G_WIDTH / 2.0, (120 * ctx.KH), 15)
                ctx.vectrex_text_2.boom = 1
            elif self.status == RedcrabLander.GameStatus.GS_FINISH:
                #  FINISH THE GAME
                if self.tic2 < 200:
                    ctx.vectrex_text_2.boom = 10 - (9 / 200.0 * self.tic2)
                    ctx.vectrex_text_2.scale_rotation(5 * ctx.KW * self.tic2 / 60.0, 0)
                ctx.vectrex_text_2.draw_text(ctx, "YOU WIN", ctx.G_WIDTH / 2.0, (120.0 * ctx.KH), 15)
                ctx.vectrex_text_2.boom = 1
            elif self.status == RedcrabLander.GameStatus.GS_LANDED:
                #  LANDED
                if self.tic2 <= 180:
                    ctx.vectrex_text_2.scale_rotation(5 * ctx.KW * self.tic2 / 60.0, self.tic2 * 1.0 / 90 * np.pi)
                ctx.vectrex_text_2.draw_text(ctx, self.scene.landed_message, ctx.G_WIDTH / 2.0, (120 * ctx.KH), 15)
            elif self.status == RedcrabLander.GameStatus.GS_EDIT or \
                    self.status == RedcrabLander.GameStatus.GS_EDIT_TEXT:
                # LEVEL editor
                if ctx.action_key_f1:
                    self.showing_message_editor_help = True
                    self.showing_message_screen = True
                    self.tic = 0
                if self.scene.go_up != 0:
                    ctx.draw_box(0, 0, 319.0 * ctx.KW, 5.0 * ctx.KH, 9)
                if self.scene.go_down != 0:
                    ctx.draw_box(0, (239.0 - 20.0) * ctx.KH, 319.0 * ctx.KW, (240.0 - 20.0 - 5.0) * ctx.KH, 9)
                if self.scene.go_left != 0:
                    ctx.draw_box(0, 0, 5.0 * ctx.KW, (240.0 - 20.0) * ctx.KH, 9)
                if self.scene.go_right != 0:
                    ctx.draw_box((320.0 - 5.0) * ctx.KW, 0, 319.0 * ctx.KW, (240.0 - 20.0) * ctx.KH, 9)
                ctx.vectrex_board_text.draw_text(ctx, "G", 80.0 * ctx.KW, 234.0 * ctx.KH, 10)
                ctx.draw_box(88.0 * ctx.KW, 230.0 * ctx.KH, (88.0 + 50.0) * ctx.KW, 239.0 * ctx.KH, 10)
                ctx.draw_box_full(88.0 * ctx.KW, 230.0 * ctx.KH, (88.0 + (self.scene.gravity * 2000.0)) * ctx.KW,
                                  239.0 * ctx.KH, 10)
                ctx.vectrex_board_text.draw_text(ctx, "LEVEL EDITOR", 246.0 * ctx.KW, 226.0 * ctx.KH, 9)
                if self.status == RedcrabLander.GameStatus.GS_EDIT_TEXT:
                    if self.tic % 30 < 15:
                        pst = " "
                    else:
                        pst = "_"
                    pst = self.level_title[self.safe_land] + pst
                    ctx.vectrex_text_1.scale_rotation(4.0 * ctx.KW, 0)
                    ctx.vectrex_text_1.draw_text(ctx, pst, ctx.G_WIDTH / 2.0, 120.0 * ctx.KH, 10)
                ctx.vectrex_board_text.draw_text(ctx, "X", self.xm * ctx.KW, self.ym * ctx.KH, 10)

        def init_level(self, level):
            self.player_action = RedcrabLander.PlayerAction.PA_NOTHING
            self.ship.init()
            self.number_of_sucker = 0
            self.sub_level_x = 0
            self.sub_level_y = 0
            i = self.load_level(level)
            if i == 0:
                self.scene.init(level)
                if self.safe_land > 3:
                    self.number_of_sucker = int(self.safe_land / 3.0)
                    self.number_of_sucker = self.sucker.__len__() \
                        if (self.number_of_sucker > self.sucker.__len__()) else self.number_of_sucker
                    for i in range(self.number_of_sucker):
                        self.sucker[i].location.x = 160 + 160 - self.scene.pad_location.x + np.random.rand() * 30 - 15
                        if abs(self.sucker[i].location.x - self.scene.pad_location.x) < 100:
                            self.sucker[i].location.x *= 2.0
                            self.sucker[i].location.x = 319 if (self.sucker[i].location.x > 319) else self.sucker[
                                i].location.x
                        self.sucker[i].location.y = self.scene.landscape[int(self.sucker[i].location.x)].ground + 20 + (
                                220 - self.scene.landscape[int(self.sucker[i].location.x)].ground) * np.random.rand()
            self.ship.location.x = self.scene.start_location.x
            self.ship.location.y = self.scene.start_location.y

        def energy_sucker_action(self, ctx):
            perTicSpeed = 14.0 / ctx.fps
            xs = self.ship.location.x
            ys = self.ship.location.y
            if self.status == RedcrabLander.GameStatus.GS_RUN:
                for i in range(self.number_of_sucker):
                    if self.sucker[i].status == RedcrabLander.EnergySuckerStatus.SS_NORMAL:
                        xm = self.sucker[i].location.x
                        ym = self.sucker[i].location.y
                        d = ((xs - xm) ** 2 + (ys - ym) ** 2) ** 0.5
                        dx = xs - xm
                        dy = ys - ym
                        k = perTicSpeed / d
                        # detect collision to ship, if so then still ship energy
                        if d < self.ship.size + self.sucker[i].size:
                            if (self.tic + i) % 10 == 0:
                                if self.ship.fuel > 0:
                                    self.ship.fuel -= 1
                        self.sucker[i].speed.x = k * dx
                        self.sucker[i].speed.y = k * dy
                        xm += self.sucker[i].speed.x
                        ym += self.sucker[i].speed.y
                        xm = 319 if (xm > 319) else xm
                        xm = 0 if (xm < 0) else xm
                        new_alt = ym - self.scene.landscape[int(xm)].ground
                        new_sky_dist = self.scene.landscape[int(xm)].sky - ym
                        # ground detection
                        if (0 <= new_alt <= 10) or (0 <= new_sky_dist <= 10):
                            self.sucker[i].speed.y = 0
                            self.sucker[i].speed.x = math.copysign(perTicSpeed, self.sucker[i].speed.x)

                        if new_alt <= 0 and new_sky_dist <= 0:
                            self.sucker[i].speed.y = 0
                            self.sucker[i].speed.x = 0
                        else:
                            if new_alt < 0:  # in  ground
                                self.sucker[i].speed.y = perTicSpeed
                                self.sucker[i].speed.x = 0

                            if new_sky_dist < 0:  # in  sky
                                self.sucker[i].speed.y = -perTicSpeed
                                self.sucker[i].speed.x = 0

                        self.sucker[i].location.x += self.sucker[i].speed.x
                        self.sucker[i].location.y += self.sucker[i].speed.y

        def tick(self, ctx):
            self.tic += 1
            self.tic2 += 1
            st = ctx.key_text  # (ctx.anyKey()) ? "+" : "";
            #  Player action
            self.player_action = RedcrabLander.PlayerAction.PA_NOTHING
            if ctx.action_rotate_left:
                self.player_action = RedcrabLander.PlayerAction.PA_LEFT
            if ctx.action_rotate_right:
                self.player_action = RedcrabLander.PlayerAction.PA_RIGHT
            if ctx.action_thrust:
                self.player_action = RedcrabLander.PlayerAction.PA_THRUST
            if ctx.action_pause_resume:
                self.player_action = RedcrabLander.PlayerAction.PA_PAUSE
            if ctx.action_quit:
                self.player_action = RedcrabLander.PlayerAction.PA_QUIT
            # if (UNITY_EDITOR)
            # 'Input.GetKey(KeyCode.F10)'
            if ctx.action_edit and self.status != RedcrabLander.GameStatus.GS_EDIT and self.tic > 60:
                ctx.sound_pause()  # SoundManager.instance.Pause();
                self.status = RedcrabLander.GameStatus.GS_EDIT
                self.ship.speed.x = 0
                self.ship.speed.y = 0
                self.ship.status = RedcrabLander.LanderStatus.LS_NORMAL
                self.tic = 0
                self.tic2 = 0
                self.load_level(self.safe_land, self.sub_level_x, self.sub_level_y)

            #  Cheat keys (Debugging purpose)
            # If st="-" Then self.ship.status = LS_CRASH
            # If st="+" Then self.ship.status = LS_NORMAL
            if st == "*":
                self.ship.fuel = 100
            if st == "/":
                self.tic = 0
                self.life = 0
                self.tic2 = 0
                self.status = RedcrabLander.GameStatus.GS_GAME_OVER
            # endif
            # Enemy action
            self.energy_sucker_action(ctx)

            if self.status == RedcrabLander.GameStatus.GS_GAME_OVER or \
                    self.status == RedcrabLander.GameStatus.GS_FINISH:
                if self.best_score < self.score:
                    self.best_score = self.score
                    self.best_safe_land = self.safe_land
                    try:
                        fi = open(RedcrabLander.data_path + "LANDER.SCO", "wt")
                        print(self.best_score, file=fi)
                        print(self.best_safe_land, file=fi)
                        fi.close()
                    except Exception as n:
                        print(n)  # don"t care :) if the best score failed to be saved

            #  Process player action
            if self.status == RedcrabLander.GameStatus.GS_START:
                self.ship.location.x = self.scene.start_location.x
                self.ship.location.y = self.scene.start_location.y
                if ctx.is_any_key_pressed() and self.tic > 30:
                    self.status = RedcrabLander.GameStatus.GS_RUN
                    self.tic = 0

            if self.status == RedcrabLander.GameStatus.GS_INTRO:
                self.ship.location.x = self.scene.start_location.x
                self.ship.location.y = self.scene.start_location.y
                if ctx.is_any_key_pressed() and self.tic > 30:
                    self.status = RedcrabLander.GameStatus.GS_RUN
                    self.tic = 0

            if self.status == RedcrabLander.GameStatus.GS_LANDED and self.tic > 120:
                if self.ship.fuel < 100 and self.tic % 3 == 0:
                    self.ship.fuel += 1
                if ctx.is_any_key_pressed() or self.ship.location.y > 280 or self.tic > 60 * 10:
                    self.tic = 0
                    self.showing_message_screen = True
                    self.status = RedcrabLander.GameStatus.GS_START
                    self.init_level(self.safe_land)
                    self.tic = 0
                    self.tic2 = 0

            if self.status == RedcrabLander.GameStatus.GS_CRASHED and self.tic > 120:
                if ctx.is_any_key_pressed() and self.tic2 > 260 + 180:
                    self.status = RedcrabLander.GameStatus.GS_START
                    self.ship.init()
                    self.init_level(self.safe_land)
                    self.tic = 0
                    self.tic2 = 0

            if self.status == RedcrabLander.GameStatus.GS_GAME_OVER and self.tic > 120:
                if ctx.is_any_key_pressed() or self.tic > 800:
                    self.init()
                    self.tic = 0
                    self.tic2 = 0

            if self.status == RedcrabLander.GameStatus.GS_FINISH and self.tic > 120:
                if ctx.is_any_key_pressed() or self.tic > 800:
                    self.init()
                    self.tic = 0
                    self.tic2 = 0

            if self.status == RedcrabLander.GameStatus.GS_PAUSE and self.tic > 60:
                if self.player_action == RedcrabLander.PlayerAction.PA_PAUSE:
                    self.status = RedcrabLander.GameStatus.GS_RUN
                    self.player_action = RedcrabLander.PlayerAction.PA_NOTHING
                    self.tic = 0
                    ctx.sound_unpause()
            # if (UNITY_EDITOR)
            if self.status == RedcrabLander.GameStatus.GS_EDIT or \
                    self.status == RedcrabLander.GameStatus.GS_EDIT_TEXT:
                self.bm = 1 if ctx.action_mouse_button1 else 0
                self.bm += 2 if ctx.action_mouse_button3 else 0
                self.bm += 4 if ctx.action_mouse_button2 else 0
                self.xm = ctx.action_mouse_position_x / ctx.KW * 1.0
                self.ym = ctx.action_mouse_position_y / ctx.KH * 1.0
                self.xrm = ctx.action_mouse_rel_x / ctx.KW * 1.0
                self.yrm = ctx.action_mouse_rel_y / ctx.KH * 1.0
                self.scene.start_location.x = self.ship.location.x
                self.scene.start_location.y = self.ship.location.y

                if not ctx.action_key_ctrl:
                    if not ctx.action_key_shift:
                        if ctx.action_key_up_arrow:
                            self.ship.location.y += 1.0
                        if ctx.action_key_down_arrow:
                            self.ship.location.y -= 1.0
                        if ctx.action_key_left_arrow:
                            self.ship.location.x -= 1.0
                        if ctx.action_key_rightarrow:
                            self.ship.location.x += 1.0
                    else:
                        if ctx.action_key_left_arrow:
                            self.ship.angle -= np.pi / 100.0
                            if self.ship.angle < -np.pi:
                                self.ship.angle += 2.0 * np.pi
                        if ctx.action_key_rightarrow:
                            self.ship.angle += np.pi / 100.0
                            if self.ship.angle > np.pi:
                                self.ship.angle -= 2.0 * np.pi
                else:
                    if ctx.action_key_up_arrow:
                        for land_slice in self.scene.landscape:
                            land_slice.ground += 1
                            land_slice.sky += 1
                        for sucker in self.sucker:
                            sucker.location.y += 1
                        self.scene.pad_location.y += 1
                        self.scene.fuel_location.y += 1
                        self.ship.location.y += 1
                    if ctx.action_key_down_arrow:
                        for land_slice in self.scene.landscape:
                            land_slice.ground -= 1
                            land_slice.sky -= 1
                        for i in range(self.sucker.__len__()):
                            self.sucker[i].location.y -= 1
                        self.scene.pad_location.y -= 1
                        self.scene.fuel_location.y -= 1
                        self.ship.location.y -= 1
                    if ctx.action_key_left_arrow:
                        tg = self.scene.landscape[-1].ground
                        ts = self.scene.landscape[-1].sky
                        for i in range(self.scene.landscape.__len__() - 1, 0, -1):
                            self.scene.landscape[i].ground = self.scene.landscape[i - 1].ground
                            self.scene.landscape[i].sky = self.scene.landscape[i - 1].sky
                        self.scene.landscape[0].ground = tg
                        self.scene.landscape[0].sky = ts
                        for sucker in self.sucker:
                            sucker.location.x += 1
                            if sucker.location.x >= 320:
                                sucker.location.x -= 320
                        if self.scene.pad_location.x > -100:
                            self.scene.pad_location.x += 1
                            if self.scene.pad_location.x >= 320:
                                self.scene.pad_location.x -= 320
                        if self.scene.fuel_location.x > -100:
                            self.scene.fuel_location.x += 1
                            if self.scene.fuel_location.x >= 320:
                                self.scene.fuel_location.x -= 320
                        self.ship.location.x += 1
                        if self.ship.location.x >= 320:
                            self.ship.location.x -= 320
                    if ctx.action_key_rightarrow:
                        tg = self.scene.landscape[0].ground
                        ts = self.scene.landscape[0].sky
                        for i in range(self.scene.landscape.__len__() - 1):
                            self.scene.landscape[i].ground = self.scene.landscape[i + 1].ground
                            self.scene.landscape[i].sky = self.scene.landscape[i + 1].sky
                        self.scene.landscape[-1].ground = tg
                        self.scene.landscape[-1].sky = ts
                        for sucker in self.sucker:
                            sucker.location.x -= 1
                            if sucker.location.x < 0:
                                sucker.location.x += 320
                        if self.scene.pad_location.x > -100:
                            self.scene.pad_location.x -= 1
                            if self.scene.pad_location.x < 0:
                                self.scene.pad_location.x += 320
                        if self.scene.fuel_location.x > -100:
                            self.scene.fuel_location.x -= 1
                            if self.scene.fuel_location.x < 0:
                                self.scene.fuel_location.x += 320
                        self.ship.location.x -= 1
                        if self.ship.location.x < 0:
                            self.ship.location.x += 320
                if ctx.action_edit and self.tic > 60:
                    ctx.sound_unpause()
                    self.status = RedcrabLander.GameStatus.GS_START
                    self.tic = self.tic2 = 0
                    self.save_level(self.safe_land, self.sub_level_x, self.sub_level_y)
                    self.showing_message_screen = True
                #  DRAW GROUND (bm== 1) or SKY (bm == 2)
                if self.bm == 1 or self.bm == 2:
                    if 0 <= int(self.xm) < 320:
                        if ctx.action_mouse_drag:
                            if self.xrm > 0:
                                x_start = int(self.xm - self.xrm)
                                x_end = int(self.xm)
                                y_start = self.ym - self.yrm
                                y_delta = self.yrm / self.xrm
                            elif self.xrm < 0:
                                x_end = int(self.xm - self.xrm)
                                x_start = int(self.xm)
                                y_start = self.ym
                                y_delta = self.yrm / self.xrm
                            else:
                                x_start = int(self.xm)
                                x_end = int(self.xm)
                                y_start = self.ym
                                y_delta = 0
                        else:
                            x_start = int(self.xm)
                            x_end = int(self.xm)
                            y_start = self.ym
                            y_delta = 0

                        for x_slice in range(x_start, x_end + 1):
                            if 0 <= x_slice < 320:

                                if self.bm == 1:
                                    self.scene.landscape[x_slice].ground = int(240 - y_start)
                                    if self.scene.landscape[x_slice].ground < 20:
                                        self.scene.landscape[x_slice].ground = -20
                                    if self.scene.landscape[x_slice].ground > 220:
                                        self.scene.landscape[x_slice].ground = 220
                                    if self.scene.landscape[x_slice].ground > self.scene.landscape[x_slice].sky:
                                        self.scene.landscape[x_slice].sky = self.scene.landscape[x_slice].ground
                                else:  # bm == 2
                                    self.scene.landscape[x_slice].sky = int(240 - y_start)
                                    if self.scene.landscape[x_slice].sky < 20:
                                        self.scene.landscape[x_slice].sky = 20
                                    if self.scene.landscape[x_slice].sky > 220:
                                        self.scene.landscape[x_slice].sky = 250
                                    if self.scene.landscape[x_slice].ground > self.scene.landscape[x_slice].sky:
                                        self.scene.landscape[x_slice].ground = self.scene.landscape[x_slice].sky
                            y_start += y_delta
                if self.status == RedcrabLander.GameStatus.GS_EDIT_TEXT:  # change text
                    if st != "":
                        isBackSpace = ctx.action_key_backspace
                        isEnter = (st == '\n' or st == '\r')
                        isCharacter = not isBackSpace and not isEnter
                        if isCharacter:
                            self.level_title[self.safe_land] += st
                        if isBackSpace:
                            self.level_title[self.safe_land] = self.level_title[self.safe_land][:-1]
                        if isEnter:
                            self.status = RedcrabLander.GameStatus.GS_EDIT
                else:
                    #  SWITCH TO EDIT LEVEL MESSAGE MODE
                    if ctx.action_key_backspace:  # == '\b':
                        self.status = RedcrabLander.GameStatus.GS_EDIT_TEXT
                    #  INSERT LAND PAD
                    if st == " " and not ctx.action_key_lshift:
                        self.xm = np.clip(self.xm, 10, 309)
                        self.scene.pad_location.x = self.xm
                        self.scene.pad_location.y = 240 - self.ym
                        for i in range(int(self.xm - 10), int(self.xm + 11)):
                            self.scene.landscape[i].ground = self.scene.pad_location.y
                    #  INSERT FUEL PAD
                    if st == " " and ctx.action_key_lshift:
                        self.xm = np.clip(self.xm, 10, 309)
                        self.scene.fuel_location.x = self.xm
                        self.scene.fuel_location.y = 240 - self.ym
                        for i in range(int(self.xm - 10), int(self.xm + 11)):
                            self.scene.landscape[i].ground = self.scene.fuel_location.y
                    #  ENABLE/DISABLE UP/DOWN/LEFT/RIGHT PASS
                    if st == "t":
                        self.scene.go_up = 1 if self.scene.go_up == 0 else 0
                    if st == "b":
                        self.scene.go_down = 1 if self.scene.go_down == 0 else 0
                    if st == "l":
                        self.scene.go_left = 1 if self.scene.go_left == 0 else 0
                    if st == "r":
                        self.scene.go_right = 1 if self.scene.go_right == 0 else 0
                    #  CHANGE SUB-LEVEL
                    if st == "T":
                        self.sub_level_y += 1
                    if st == "B":
                        self.sub_level_y -= 1
                    if st == "L":
                        self.sub_level_x -= 1
                    if st == "R":
                        self.sub_level_x += 1
                    #  SWITCH TO ONE LEVEL MORE
                    if st == "+" and self.safe_land < 22:
                        self.safe_land += 1
                    #  SWITCH TO ONE LEVEL LESS
                    if st == "-" and self.safe_land >= 0:
                        self.safe_land -= 1
                    #  SAVE LEVEL
                    if self.tic > 60 and ctx.action_key_f2:
                        self.tic = 0
                        self.save_level(self.safe_land, self.sub_level_x, self.sub_level_y)
                    #  LOAD LEVEL
                    if self.tic > 60 and ctx.action_key_f3:
                        self.tic = 0
                        self.save_level(999)
                        self.ship.init()
                        if self.sub_level_x == 0 and self.sub_level_y == 0:
                            if self.load_level(self.safe_land) == 0:
                                self.load_level(999)
                        else:
                            if self.load_level(self.safe_land, self.sub_level_x, self.sub_level_y) == 0:
                                self.load_level(999)
                    #  ALLOW / DISALLOW TAKE OFF after landing
                    if self.tic > 60 and ctx.action_key_f5:
                        self.scene.allow_take_off = 1 if self.scene.allow_take_off == 0 else 0
                        self.tic = 0
                    #  REMOVE LAND PAD
                    if ctx.action_key_f6:
                        self.scene.pad_location.x = -100
                    #  REMOVE FUEL PAD
                    if ctx.action_key_f7:
                        self.scene.fuel_location.x = -100
                    #  GENERATE LEVEL
                    if self.tic > 3 and ctx.action_key_f4:
                        self.tic = 0
                        self.scene.init(self.safe_land)
                    #  ADD ONE MORE ENERGY SUCKET AT MOUSE POSITION
                    if self.tic > 15 and ctx.action_key_insert:
                        self.tic = 0
                        self.number_of_sucker += 1
                        self.sucker[self.number_of_sucker - 1].location.x = self.xm
                        self.sucker[self.number_of_sucker - 1].location.y = 240.0 - self.ym
                    #  REMOVE LAST ADDED ENERGY SUCKER
                    if self.tic > 15 and ctx.action_key_delete:
                        self.tic = 0
                        if self.number_of_sucker > 0:
                            self.number_of_sucker -= 1
                    #  ADD MORE FUEL
                    if self.tic > 3 and ctx.action_key_pageup:
                        self.tic = 0
                        if self.ship.fuel < 100:
                            self.ship.fuel += 1
                    #  REMOVE FUEL
                    if self.tic > 3 and ctx.action_key_page_down:
                        self.tic = 0
                        if self.ship.fuel > 0:
                            self.ship.fuel -= 1
                    #  ADD MORE GRAVITY
                    if self.tic > 3 and ctx.action_key_home:
                        self.tic = 0
                        self.scene.gravity = int(self.scene.gravity / 0.0025 + 0.5) * 0.0025
                        if self.scene.gravity < 0.025:
                            self.scene.gravity += 0.0025
                    #  REMOVE GRAVITY
                    if self.tic > 3 and ctx.action_key_end:
                        self.tic = 0
                        self.scene.gravity = int(self.scene.gravity / 0.0025 + 0.5) * 0.0025
                        if self.scene.gravity > 0:
                            self.scene.gravity -= 0.0025
            # endif
            if self.status == RedcrabLander.GameStatus.GS_RUN:
                if self.ship.fuel <= 0:
                    if self.scene.gravity < 0.0025:
                        self.scene.gravity = 0.0025
                if self.player_action == RedcrabLander.PlayerAction.PA_PAUSE and self.tic > 30:
                    self.status = RedcrabLander.GameStatus.GS_PAUSE
                    self.player_action = RedcrabLander.PlayerAction.PA_NOTHING
                    ctx.sound_pause()
                    self.tic = 0
                if self.player_action == RedcrabLander.PlayerAction.PA_THRUST:
                    self.ship.status = RedcrabLander.LanderStatus.LS_THRUST
                else:
                    if self.ship.status != RedcrabLander.LanderStatus.LS_CRASH:
                        self.ship.status = RedcrabLander.LanderStatus.LS_NORMAL
                if self.player_action == RedcrabLander.PlayerAction.PA_LEFT and self.ship.fuel > 0:
                    self.ship.angle -= np.pi / 180
                if self.player_action == RedcrabLander.PlayerAction.PA_RIGHT and self.ship.fuel > 0:
                    self.ship.angle += np.pi / 180
                if self.ship.angle > np.pi:
                    self.ship.angle -= 2 * np.pi
                if self.ship.angle < -np.pi:
                    self.ship.angle += 2 * np.pi
                if self.player_action == RedcrabLander.PlayerAction.PA_THRUST and self.ship.fuel > 0:
                    self.ship.speed.x += math.sin(self.ship.angle) * 0.03
                    self.ship.speed.y += math.cos(self.ship.angle) * 0.03
                    if self.tic % 4 == 0:
                        self.ship.fuel -= 1
                self.ship.speed.y -= self.scene.gravity
                self.ship.location.x += self.ship.speed.x
                self.ship.location.y += self.ship.speed.y

                if self.ship.location.x < 0:
                    if self.scene.go_left != 0:
                        if self.load_level(self.safe_land, self.sub_level_x - 1, self.sub_level_y) != 0:
                            self.sub_level_x -= 1
                            self.ship.location.x = 320 - 5
                        else:
                            self.ship.location.x = 0
                            self.ship.speed.x = -self.ship.speed.x / 2.0
                    else:
                        self.ship.location.x = 0
                        self.ship.speed.x = -self.ship.speed.x / 2.0
                if self.ship.location.x >= 319:
                    if self.scene.go_right != 0:
                        if self.load_level(self.safe_land, self.sub_level_x + 1, self.sub_level_y) != 0:
                            self.sub_level_x += 1
                            self.ship.location.x = 5
                        else:
                            self.ship.location.x = 319
                            self.ship.speed.x = -self.ship.speed.x / 2.0
                    else:
                        self.ship.location.x = 319
                        self.ship.speed.x = -self.ship.speed.x / 2.0
                if self.ship.location.y < 20:
                    if self.scene.go_down != 0:
                        if self.load_level(self.safe_land, self.sub_level_x, self.sub_level_y - 1) != 0:
                            self.sub_level_y -= 1
                            self.ship.location.y = 240 - 5
                        else:
                            self.ship.location.y = 20
                            self.ship.speed.y = -self.ship.speed.y / 2.0
                    else:
                        self.ship.location.y = 20
                        self.ship.speed.y = -self.ship.speed.y / 2.0
                if self.ship.location.y > 240:
                    if self.scene.go_up != 0:
                        if self.load_level(self.safe_land, self.sub_level_x, self.sub_level_y + 1) != 0:
                            self.sub_level_y += 1
                            self.ship.location.y = 25
                        else:
                            self.ship.location.y = 239
                            self.ship.speed.y = -self.ship.speed.y / 2.0
                    else:
                        self.ship.location.y = 239
                        self.ship.speed.y = -self.ship.speed.y / 2.0
                if self.ship.location.y <= self.scene.landscape[int(self.ship.location.x)].ground + \
                        self.ship.size * 0.80 or \
                        self.ship.location.y >= self.scene.landscape[int(self.ship.location.x)].sky - \
                        self.ship.size * 0.80:
                    speed = int((self.ship.speed.x ** 2 + self.ship.speed.y ** 2) * 1000)
                    angle = int(abs(self.ship.angle / (np.pi / 180)))
                    if (speed <= 60 and angle < 10 and
                        self.ship.location.y <= self.scene.landscape[int(self.ship.location.x)].ground +
                        self.ship.size * 0.80) and \
                            ((self.scene.pad_location.x - 10 < self.ship.location.x < self.scene.pad_location.x + 10) or
                             (self.scene.fuel_location.x - 10 <
                              self.ship.location.x < self.scene.fuel_location.x + 10)):
                        if self.scene.pad_location.x - 10 < self.ship.location.x < self.scene.pad_location.x + 10:
                            self.safe_land += 1
                            self.score += int(self.ship.fuel)
                            self.ship.status = RedcrabLander.LanderStatus.LS_LANDED
                            if self.scene.landscape[int(self.ship.location.x)].sky <= 240 or \
                                    self.scene.allow_take_off == 0:
                                self.ship.status = RedcrabLander.LanderStatus.LS_LANDED_NO_SKY
                            if self.safe_land >= 23:
                                self.status = RedcrabLander.GameStatus.GS_FINISH
                            else:
                                ctx.sound_play_landed()
                                self.status = RedcrabLander.GameStatus.GS_LANDED
                            self.tic = 0
                        else:
                            if self.tic % 3 == 0 and self.ship.fuel < 100:
                                self.ship.fuel += 1
                            self.ship.location.y = self.scene.landscape[int(self.ship.location.x)].ground \
                                                   + self.ship.size * 0.80
                    else:
                        self.status = RedcrabLander.GameStatus.GS_CRASHED
                        self.ship.status = RedcrabLander.LanderStatus.LS_CRASH
                        ctx.sound_play_explosion()
                        if self.life == 0:
                            self.status = RedcrabLander.GameStatus.GS_GAME_OVER
                            ctx.sound_play_game_over()
                        else:
                            self.life -= 1
                        self.tic = 0
                    self.tic2 = 0
                    self.ship.speed.x = 0
                    self.ship.speed.y = 0
            self.draw(ctx)

            if ctx.action_quit:
                if self.best_score < self.score:
                    self.best_score = self.score
                    self.best_safe_land = self.safe_land
                    try:
                        fi = open(RedcrabLander.data_path + "LANDER.SCO", "wt")
                        print(self.best_score, file=fi)
                        print(self.best_safe_land, file=fi)
                        fi.close()
                    except Exception as n:
                        print(n)
                self.safe_land = 99
                self.tic = 0
                self.tic2 = 0
                self.showing_message_screen = True
                return False
            return True

        def load_level(self, lvl, sub_level_x=-100, sub_level_y=-100):
            vv = "." + str(sub_level_x) + "." + str(sub_level_y)
            if sub_level_x <= -100 and sub_level_y <= -100:
                vv = ".0.0"
            level_name = "l" + str(lvl) + vv + ".lvl"
            levelFilename = RedcrabLander.data_path + level_name
            if os.path.exists(levelFilename):
                fi = open(levelFilename)
            else:
                try:
                    fi = io.TextIOWrapper(zipfile.ZipFile(RedcrabLander.data_archive).open(level_name, "r"),
                                          newline=None)
                except Exception as ex:
                    print("Can't open level " + level_name)
                    print("  ", ex)
                    return 0
            # Check file structure version
            vv = fi.readline().rstrip('\n')
            if vv != "version=1":
                fi.close()
                return 0
            for land_slice in self.scene.landscape:
                land_slice.sky = float(fi.readline())
                land_slice.ground = float(fi.readline())
            self.scene.go_up = int(fi.readline())
            self.scene.go_down = int(fi.readline())
            self.scene.go_left = int(fi.readline())
            self.scene.go_right = int(fi.readline())
            self.scene.inverse = int(fi.readline())
            self.scene.allow_take_off = int(fi.readline())
            self.scene.landed_message = fi.readline().rstrip('\n')
            #  get pad location
            self.scene.pad_location.x = float(fi.readline())
            self.scene.pad_location.y = float(fi.readline())
            #  get fuel location
            self.scene.fuel_location.x = float(fi.readline())
            self.scene.fuel_location.y = float(fi.readline())
            #  get gravity
            self.scene.gravity = float(fi.readline())
            if (sub_level_x <= -100 and sub_level_y <= -100) or self.status == RedcrabLander.GameStatus.GS_EDIT or \
                    self.status == RedcrabLander.GameStatus.GS_EDIT_TEXT:
                #  get lander location
                self.ship.location.x = float(fi.readline())
                self.ship.location.y = float(fi.readline())
                self.scene.start_location.x = self.ship.location.x
                self.scene.start_location.y = self.ship.location.y
                #  get lander speed
                self.ship.speed.x = float(fi.readline())
                self.ship.speed.y = float(fi.readline())
                #  get lander angle
                self.ship.angle = float(fi.readline())
                #  get fuel
                self.ship.fuel = int(fi.readline())
            else:
                #  read ship info to ignore
                for _ in range(6):
                    fi.readline()
            #  get enemies quantity of "Energy sucker"
            self.number_of_sucker = int(fi.readline())
            for i in range(self.number_of_sucker):
                #  get enemy location
                self.sucker[i].location.x = float(fi.readline())
                self.sucker[i].location.y = float(fi.readline())
            # get message of level
            if 0 <= lvl < self.level_title.__len__():
                self.level_title[lvl] = fi.readline().rstrip('\n')
            fi.close()
            return 1

        def save_level(self, lvl, sub_level_x=-100, sub_level_y=-100):
            if sub_level_x <= -100 and sub_level_y <= -100:
                vv = ".0.0"
            else:
                vv = "." + str(sub_level_x) + "." + str(sub_level_y)
            level_file_name = RedcrabLander.data_path + "l" + str(lvl) + vv + ".lvl"
            if os.path.exists(level_file_name):
                old_file_name = level_file_name + ".backup-" + datetime.now().strftime("%Y%m%d%H%M%S")
                if os.path.exists(old_file_name):
                    os.remove(old_file_name)
                os.rename(level_file_name, old_file_name)
            fi = open(level_file_name, "wt")
            print("version=1", file=fi)
            for land_slice in self.scene.landscape:
                print(land_slice.sky, file=fi)
                print(land_slice.ground, file=fi)
            print(self.scene.go_up, file=fi)
            print(self.scene.go_down, file=fi)
            print(self.scene.go_left, file=fi)
            print(self.scene.go_right, file=fi)
            print(self.scene.inverse, file=fi)
            print(self.scene.allow_take_off, file=fi)
            print(self.scene.landed_message, file=fi)
            #  put pad location
            print(self.scene.pad_location.x, file=fi)
            print(self.scene.pad_location.y, file=fi)
            #  put fuel location
            print(self.scene.fuel_location.x, file=fi)
            print(self.scene.fuel_location.y, file=fi)
            # put gravity
            print(self.scene.gravity, file=fi)
            #  put lander location
            print(int(self.ship.location.x * 1000.0) / 1000.0, file=fi)
            print(int(self.ship.location.y * 1000.0) / 1000.0, file=fi)
            #  put lander speed
            print(int(self.ship.speed.x * 100000.0) / 100000.0, file=fi)
            print(int(self.ship.speed.y * 100000.0) / 100000.0, file=fi)
            #  put lander angle
            print(self.ship.angle, file=fi)
            #  put fuel
            print(self.ship.fuel, file=fi)
            #  put enemies quantity of "Energy sucker"
            print(self.number_of_sucker, file=fi)
            for i in range(self.number_of_sucker):
                print(self.sucker[i].location.x, file=fi)
                print(self.sucker[i].location.y, file=fi)
            # put message of level
            if 0 <= lvl < self.level_title.__len__():
                print(self.level_title[lvl], file=fi)
            else:
                print("Msg" + str(lvl), file=fi)
            fi.close()
            print("Level file", level_file_name, "saved.")
            return 1

        def _get_message(self):
            m = ()
            if self.showing_message_editor_help:
                m = ("@CEDITOR COMMAND",
                     "@C--------------",
                     "",
                     "@8General",
                     " F1 @8......................@E This help",
                     " F10 @8.....................@E Enter / Leave Level Editor",
                     " F2 @8......................@E Save current Level",
                     " F3 @8......................@E Load current Level",
                     "",
                     "@8Title, Gravity, Take-off",
                     " BACK-SPC @8................@E Enter Title Edit Mode",
                     " ENTER @8...................@E Valid Title(Edit Mode)",
                     " HOME/END @8................@E + / - Gravity",
                     " PGUP/DOWN @8...............@E + / - Energy",
                     " F5 @8......................@E Allow/disallow launch after landing (end level anim)",
                     "",
                     "@8Level and Sub-level",
                     " + / - @8...................@E Change Level Up/Down",
                     " T,B,L,R @8.................@E move to sub level top/bottom/left/right",
                     " t,b,l,r @8.................@E allow/disallow sub level top/bottom/left/right",
                     "",
                     "@8Landscape",
                     " F4 @8......................@E random a ground landscape (current level and no sky)",
                     " CTRL+UP/DOWN/LEFT/RIGHT@8 .@E Shift landscape ",
                     " LEFT MOUSE BUTTON @8.......@E Draw Ground",
                     " RIGHT MOUSE BUTTON @8......@E Draw Sky",
                     "",
                     "@8Land and Energy pads",
                     " SPACE @8...................@E Place Land Pad at mouse position",
                     " F6 @8......................@E Remove land pad",
                     " SHIFT + SPACE @8...........@E Place Energy Reload Pad at mouse position",
                     " F7 @8......................@E Remove fuel pad",
                     "",
                     "@8Lander and Sucker",
                     " INSERT @8..................@E Add an Energy Sucker at mouse position",
                     " DELETE @8..................@E Remove Last Added Energy Sucker",
                     " LEFT/RIGHT/UP/DOWN @8......@E Move Lander",
                     " LEFT Sft+LEFT/RIGHT @8.....@E Rotate Lander",
                     " ",
                     "",
                     " @FAuto-save level when leaving Editor @$F10",
                     " @FAuto-load level when entering Editor @$F10",
                     " ",
                     "@8Press Any Key to continue")
            else:
                file_name = "m" + str(self.safe_land) + ".lvl"
                messageFilename = RedcrabLander.data_path + file_name
                if os.path.exists(messageFilename):
                    fi = open(messageFilename)
                    m = fi.readlines()
                    fi.close()
                else:
                    if os.path.exists(RedcrabLander.data_archive):
                        zf = zipfile.ZipFile(RedcrabLander.data_archive)
                        try:
                            fi = io.TextIOWrapper(zf.open(file_name, "r"),
                                                  newline=None)
                            m = fi.readlines()
                            fi.close()
                        except KeyError:
                            pass
            return m

        def show_message(self, ctx):
            if self.tic == 0:
                self.message = self._get_message()
                ctx.vectrex_text_big.scale_rotation(7 * ctx.KW, 0)

            if self.message.__len__() == 0:
                self.tic = 0
                self.tic2 = 0
                self.showing_message_screen = self.showing_message_editor_help = False
                return

            if self.tic2 < ctx.fps * 3:
                if self.tic2 == 0:
                    ctx.sound_play_incoming_transmission()

                if self.tic2 == ctx.fps:
                    ctx.sound_play_modem()

                ctx.clear_all_drawing()
                if int(self.tic2 / 15) % 2 == 0:
                    ctx.vectrex_text_big.draw_text(ctx, "incoming transmission",
                                                   ctx.G_WIDTH / 2.0, ctx.G_HEIGHT / 2, 12)
                self.tic2 += 1
                return

            m = self.message
            lmax = 0
            for aline in m:
                number_character, _ = ctx.vectrex_text_1.draw_text_length(aline)
                lmax = number_character if number_character > lmax else lmax
            lmax += 2
            ctx.clear_all_drawing()
            ctx.vectrex_text_1.scale_rotation(4.0 * ctx.KW, 0)
            i = 0
            colour = 10
            limit = 0
            for aline in m:
                if not self.showing_message_editor_help:
                    tt = int(self.tic / 2)
                    limit = int(tt / lmax)
                    previous_tt = int((self.tic - 1) / 2)
                    previous_limit = int(previous_tt / lmax)
                    if previous_limit != limit and limit <= m.__len__():
                        ctx.sound_play_zing()
                    colour = 10
                    if limit == (i + 1):
                        if aline[:tt % lmax].__len__() != \
                                aline[:(previous_tt if previous_tt >= 0 else 0) % lmax].__len__():
                            ctx.sound_play_zing()
                        aline = aline[:tt % lmax] + ("@F" if int(self.tic / 10) % 2 == 0 else "@0") + "#"
                        colour = 10
                    elif limit < (i + 1):
                        aline = ""
                number_character, _ = ctx.vectrex_text_1.draw_text_length(aline)
                aline = " " + aline + (" " * (lmax - number_character))
                if self.showing_message_editor_help:
                    ctx.vectrex_text_small.draw_text_rich(ctx, aline, ctx.G_WIDTH / 2.0, (i * 4.5 + 6.0) * ctx.KH, 10)
                else:
                    ctx.vectrex_text_1.draw_text_rich(ctx,
                                                      aline.rstrip('\n'),
                                                      ctx.G_WIDTH / 2.0,
                                                      ((24 - (limit if limit < m.__len__() else m.__len__()) + i)
                                                       * 9.0 + 6.0) * ctx.KH,
                                                      colour)
                i += 1
            self.tic += 1
            if self.tic > ctx.fps * 40 or (ctx.is_any_key_pressed() and self.tic > ctx.fps * 3):
                self.tic = self.tic2 = 0
                self.showing_message_screen = self.showing_message_editor_help = False
            return

    class GameContext:
        class VectrexMemory:
            def __init__(self):
                self.p1 = pg.math.Vector2(0, 0)
                self.p2 = pg.math.Vector2(0, 0)
                self.colour = pg.Color(0, 0, 0)

        def __init__(self):
            self.frames = 0
            self.slow_host = False
            self.action_mouse_button1 = False
            self.action_mouse_button2 = False
            self.action_mouse_button3 = False
            self.action_mouse_drag = True
            self.action_mouse_position_y = 0
            self.action_mouse_position_x = 0
            self.action_mouse_rel_y = 0
            self.action_mouse_rel_x = 0
            self.action_key_f1 = False
            self.action_key_f2 = False
            self.action_key_f3 = False
            self.action_key_f4 = False
            self.action_key_f5 = False
            self.action_key_f6 = False
            self.action_key_f7 = False
            self.action_key_f8 = False
            self.action_key_f9 = False
            self.action_key_f10 = False
            self.action_key_backspace = False
            self.action_key_delete = False
            self.action_key_insert = False
            self.action_key_page_down = False
            self.action_key_pageup = False
            self.action_key_end = False
            self.action_key_home = False
            self.action_key_down_arrow = False
            self.action_key_up_arrow = False
            self.action_key_rightarrow = False
            self.action_key_left_arrow = False
            self.action_key_shift = False
            self.action_key_right_shit = False
            self.action_key_lshift = False
            self.action_key_ctrl = False
            self.action_key_right_ctrl = False
            self.action_key_left_ctrl = False
            self.action_edit = False
            self.action_key_any = False
            self.last_event = None
            self.action_pause_resume = False
            self.action_thrust = False
            self.action_rotate_right = False
            self.action_rotate_left = False
            self.action_quit = False
            self.fps = 50.0
            self.G_WIDTH = 1024
            self.G_HEIGHT = 768
            pg.init()
            self.clock = pg.time.Clock()
            self.screen = pg.display.set_mode((self.G_WIDTH, self.G_HEIGHT))
            pg.display.set_caption('Captain Lander')
            pg.display.set_icon(pg.image.load(RedcrabLander.data_asset_path + "icon.png"))
            self.number_segment_circle = 16
            self.key_text = ""
            self.vectrex_memory = tuple(RedcrabLander.GameContext.VectrexMemory() for _ in range(10000))
            self.vectrex_memory_size = 0
            self.vectrex_text_1 = RedcrabLander.TinyVectrex()
            self.vectrex_board_text = RedcrabLander.TinyVectrex()
            self.vectrex_text_2 = RedcrabLander.TinyVectrex()
            self.vectrex_text_small = RedcrabLander.TinyVectrex()
            self.vectrex_text_big = RedcrabLander.TinyVectrex()
            self.palette = (
                pg.Color("black"), pg.Color("blue"), pg.Color("green"), pg.Color("cyan"), pg.Color("red"),
                pg.Color("magenta"), pg.Color("yellow"), pg.Color("white"),
                pg.Color("grey"), pg.Color("blue"), pg.Color("green"), pg.Color("cyan"), pg.Color("red"),
                pg.Color("magenta"), pg.Color("yellow"), pg.Color("white"))
            self.sound = (
                pg.mixer.Sound(RedcrabLander.data_asset_path + "andrea-baroni.ogg"),
                pg.mixer.Sound(RedcrabLander.data_asset_path + "game_over.ogg"),
                pg.mixer.Sound(RedcrabLander.data_asset_path + "thrust.ogg"),
                pg.mixer.Sound(RedcrabLander.data_asset_path + "explosion.ogg"),
                pg.mixer.Sound(RedcrabLander.data_asset_path + "landed.ogg"),
                pg.mixer.Sound(RedcrabLander.data_asset_path + "SE-Gun-001.ogg"),
                pg.mixer.Sound(RedcrabLander.data_asset_path + "tzing01.ogg"),
                pg.mixer.Sound(RedcrabLander.data_asset_path + "incoming-transmission.ogg"),
                pg.mixer.Sound(RedcrabLander.data_asset_path + "modem.ogg")
            )
            self.music_channel = None
            self.KW = self.G_WIDTH / 320.0
            self.KH = self.G_HEIGHT / 240.0
            self.vectrex_text_small.scale_rotation(2 * self.KW, 0)
            self.vectrex_text_big.scale_rotation(5 * self.KW, 0)
            self.vectrex_text_1.scale_rotation(4 * self.KW, 0)
            self.vectrex_text_2.scale_rotation(4 * self.KW, 0)
            self.vectrex_board_text.scale_rotation(3.5 * self.KW, 0)
            self.vectrex_board_text.set_center_text(0)

        def sound_pause(self):
            if self.music_channel is not None:
                pg.mixer.pause()

        def sound_unpause(self):
            if self.music_channel is not None:
                pg.mixer.unpause()

        def sound_play_score(self):
            if self.music_channel is None:
                self.sound[0].set_volume(0.15)
                self.music_channel = self.sound[0].play(-1)

        def sound_stop_score(self):
            if self.music_channel is not None:
                self.music_channel.stop()
                self.music_channel = None

        def sound_play_game_over(self):
            self.sound[1].play()

        def sound_play_thrust(self):
            self.sound[2].play(fade_ms=100)

        def sound_play_explosion(self):
            self.sound[3].play()

        def sound_play_landed(self):
            self.sound[4].play()

        def sound_play_title(self):
            self.sound[5].play(maxtime=4250, fade_ms=2000)

        def sound_play_zing(self):
            self.sound[6].set_volume(0.1)
            self.sound[6].play(maxtime=30)

        def sound_play_incoming_transmission(self):
            self.sound[7].set_volume(0.5)
            self.sound[7].play()

        def sound_play_modem(self):
            self.sound[8].set_volume(0.2)
            self.sound[8].play()

        def draw_line(self, x1, y1, x2, y2, colour):
            if self.vectrex_memory_size >= self.vectrex_memory.__len__():
                print("Out of Vertex memory (max " + str(self.vectrex_memory_size) + ")")
                return
            self.vectrex_memory[self.vectrex_memory_size].p1.x = float(x1)
            self.vectrex_memory[self.vectrex_memory_size].p1.y = float(y1)
            if x1 == x2 and y1 == y2:
                self.vectrex_memory[self.vectrex_memory_size].p2.x = float(x2) + 1
                self.vectrex_memory[self.vectrex_memory_size].p2.y = float(y2)
            else:
                self.vectrex_memory[self.vectrex_memory_size].p2.x = float(x2)
                self.vectrex_memory[self.vectrex_memory_size].p2.y = float(y2)
            self.vectrex_memory[self.vectrex_memory_size].colour = self.palette[colour]
            self.vectrex_memory_size += 1

        def draw_box_full(self, x1, y1, x2, y2, colour):
            self.draw_box(x1, y1, x2, y2, colour)
            xx1 = x1 if (x1 < x2) else x2
            xx2 = x2 if (x1 < x2) else x1
            yy1 = y1 if (y1 < y2) else y2
            yy2 = y2 if (y1 < y2) else y1
            yy = yy1
            while yy <= yy2:
                self.draw_line(xx1, yy, xx2, yy, colour)
                yy += 1

        def draw_box(self, x1, y1, x2, y2, colour):
            self.draw_line(x1, y1, x2, y1, colour)
            self.draw_line(x1, y2, x2, y2, colour)
            self.draw_line(x1, y1, x1, y2, colour)
            self.draw_line(x2, y1, x2, y2, colour)

        def draw_circle(self, x, y, radius, colour):
            deltaAngle = np.pi * 2 / self.number_segment_circle
            for i in range(self.number_segment_circle):
                angle1 = deltaAngle * i
                angle2 = angle1 + deltaAngle
                x1 = x + math.cos(angle1) * radius
                y1 = y + math.sin(angle1) * radius
                x2 = x + math.cos(angle2) * radius
                y2 = y + math.sin(angle2) * radius
                self.draw_line(x1, y1, x2, y2, colour)

        def clear_all_drawing(self):
            self.vectrex_memory_size = 0

        def is_any_key_pressed(self):  # return True or False
            return self.action_key_any

        def capture_input(self):
            self.key_text = ""
            self.action_quit = False
            self.last_event = None
            for self.last_event in pg.event.get():
                if self.last_event.type == QUIT or \
                        (self.last_event.type == KEYDOWN and self.last_event.key == K_ESCAPE):
                    self.action_quit = True
                if self.last_event.type == KEYDOWN or self.last_event.type == KEYUP:
                    self.action_key_any = self.last_event.type == KEYDOWN
                    self.action_key_left_ctrl = (self.last_event.mod & KMOD_LCTRL) != 0
                    self.action_key_right_ctrl = (self.last_event.mod & KMOD_RCTRL) != 0
                    self.action_key_ctrl = (self.last_event.mod & KMOD_CTRL) != 0
                    self.action_key_lshift = (self.last_event.mod & KMOD_LSHIFT) != 0
                    self.action_key_right_shit = (self.last_event.mod & KMOD_RSHIFT) != 0
                    self.action_key_shift = (self.last_event.mod & KMOD_SHIFT) != 0
                    if self.last_event.key == K_LEFT:
                        self.action_rotate_left = self.last_event.type == KEYDOWN
                        self.action_key_left_arrow = self.action_rotate_left
                    elif self.last_event.key == K_RIGHT:
                        self.action_rotate_right = self.last_event.type == KEYDOWN
                        self.action_key_rightarrow = self.action_rotate_right
                    elif self.last_event.key == K_UP:
                        self.action_thrust = self.last_event.type == KEYDOWN
                        self.action_key_up_arrow = self.action_thrust
                    elif self.last_event.key == K_DOWN:
                        self.action_key_down_arrow = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_HOME:
                        self.action_key_home = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_END:
                        self.action_key_end = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_PAGEUP:
                        self.action_key_pageup = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_PAGEDOWN:
                        self.action_key_page_down = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_INSERT:
                        self.action_key_insert = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_DELETE:
                        self.action_key_delete = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_BACKSPACE:
                        self.action_key_backspace = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_F1:
                        self.action_key_f1 = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_F2:
                        self.action_key_f2 = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_F3:
                        self.action_key_f3 = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_F4:
                        self.action_key_f4 = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_F5:
                        self.action_key_f5 = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_F6:
                        self.action_key_f6 = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_F7:
                        self.action_key_f7 = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_F8:
                        self.action_key_f8 = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_F9:
                        self.action_key_f9 = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_F10:
                        self.action_edit = self.last_event.type == KEYDOWN
                        self.action_key_f10 = self.action_edit
                    elif self.last_event.key == K_SPACE:
                        self.action_pause_resume = self.last_event.type == KEYDOWN

                    if self.last_event.type == KEYDOWN:
                        self.key_text = self.last_event.unicode
                elif self.last_event.type == MOUSEMOTION or \
                        self.last_event.type == MOUSEBUTTONUP or \
                        self.last_event.type == MOUSEBUTTONDOWN:
                    self.action_mouse_position_x = self.last_event.pos[0]
                    self.action_mouse_position_y = self.last_event.pos[1]
                    if self.last_event.type == MOUSEMOTION:
                        self.action_mouse_rel_x = self.last_event.rel[0]
                        self.action_mouse_rel_y = self.last_event.rel[1]
                        self.action_mouse_button1 = self.last_event.buttons[0] != 0
                        self.action_mouse_button2 = self.last_event.buttons[1] != 0
                        self.action_mouse_button3 = self.last_event.buttons[2] != 0
                        self.action_mouse_drag = \
                            self.action_mouse_button1 or \
                            self.action_mouse_button2 or \
                            self.action_mouse_button3
                    elif self.last_event.type == MOUSEBUTTONDOWN:
                        self.action_mouse_drag = False
                        if self.last_event.button == 1:
                            self.action_mouse_button1 = True
                        elif self.last_event.button == 2:
                            self.action_mouse_button2 = True
                        elif self.last_event.button == 3:
                            self.action_mouse_button3 = True
                    elif self.last_event.type == MOUSEBUTTONUP:
                        self.action_mouse_drag = False
                        if self.last_event.button == 1:
                            self.action_mouse_button1 = False
                        elif self.last_event.button == 2:
                            self.action_mouse_button2 = False
                        elif self.last_event.button == 3:
                            self.action_mouse_button3 = False

        def render_all_drawing(self):
            if self.slow_host:
                self.screen.fill(pg.Color(0, 0, 0))
                maxVM = self.vectrex_memory_size
                iVM = 0
                for vm in self.vectrex_memory:
                    if iVM >= maxVM:
                        break
                    pg.draw.line(self.screen, vm.colour, vm.p1, vm.p2)
                    iVM += 1
            else:
                if 40 < self.frames < 800 and self.clock.get_fps() <= int(0.8 * self.fps):
                    self.slow_host = True
                    print("Slow host detected, do not execute intensive display primitive")
                self.screen.fill(pg.Color(192, 192, 192), special_flags=BLEND_RGB_MULT)
                maxVM = self.vectrex_memory_size
                iVM = 0
                for vm in self.vectrex_memory:
                    if iVM >= maxVM:
                        break
                    pg.draw.aaline(self.screen, vm.colour, vm.p1, vm.p2)
                    iVM += 1
            pg.display.update()
            self.frames += 1
            self.clock.tick(int(self.fps))

    data_path = "data/"
    data_asset_path = "asset/"
    data_archive = data_asset_path + "lander.lvl"

    def __init__(self):
        self.run = True
        self.game = RedcrabLander.Game()
        self.game_context = RedcrabLander.GameContext()
        self.timer = 0.0
        self.game_context.fps = 50
        print("Captain Lander running")
        self.game_context.sound_play_score()

    def play(self):
        self.run = True
        while self.run or self.game.showing_message_screen:
            self.game_context.capture_input()
            if self.game.showing_message_screen:
                self.game.show_message(self.game_context)
            else:
                self.run = self.game.tick(self.game_context)
            self.game_context.render_all_drawing()
        pg.quit()


if __name__ == '__main__':
    print("Get ready")
    RedcrabLander().play()
    print("Bye bye")
