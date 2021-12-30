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


class RedcrabLander:
    class TV_Polar2D:
        def __init__(self):
            self.radius = 0.0
            self.angle = 0.0

    class TV_vertex2D:
        def __init__(self):
            self.x = 0.0
            self.y = 0.0

    class TinyVectrex:
        def __init__(self):
            self.plot = tuple(RedcrabLander.TV_Polar2D() for _ in range(18))
            self.plotxy = tuple(RedcrabLander.TV_vertex2D() for _ in range(18))
            self.size = 0.0
            self.angle = 0.0
            self.cx = 0
            self.alphabet = [""] * 356
            self.boom = 1.0
            self.setCenterText(0.5)
            j = 1
            for i in np.linspace(0, 1.75 * np.pi, 8):
                self.plot[j].radius = 1.0
                self.plot[j + 8].radius = (2 ** .5) / 2.0
                self.plot[j].angle = self.plot[j + 8].angle = i
                j += 1
            self.scaleRot(4.0, 0.0)
            # sign
            self.alphabet[ord("+")] = "PL NJ"
            self.alphabet[ord("-")] = "NJ"
            self.alphabet[ord("*")] = "OK MQ NJ"
            self.alphabet[ord("/")] = "IE"
            self.alphabet[ord(":")] = "PP LL"
            self.alphabet[ord("!")] = "PA LL"
            self.alphabet[ord(".")] = "LL"
            self.alphabet[ord(",")] = "LD"
            self.alphabet[ord("'")] = "HP"
            self.alphabet[ord("(")] = "HGED"
            self.alphabet[ord(")")] = "HICD"
            self.alphabet[ord("_")] = "EC"
            self.alphabet[ord("~")] = "2E0D2C 2HCBDFEH"  # small ship with thrust
            self.alphabet[ord("^")] = "2HCBDFEH"  # small ship without thrust
            self.alphabet[ord("$")] = "HCBDFEH"  # normal-&sized ship
            self.alphabet[ord("&")] = "2HCBDFEH 0BCDEFGHIB"  # rounded lander
            self.alphabet[ord("#")] = "JKLMNOPQJ BJ CK DL EM FN GO HP IQ"  # sun
            self.alphabet[ord("~")] = "GICEG BDFHB"  # star
            self.alphabet[ord("§")] = "0H3I0B3C0D3E0F3G0H 3I0I 3C0C 3E0E 3G0G"  # Energy sucker
            self.alphabet[ord("%")] = "BHFNECJB"  # Arrow
            #  Digit
            self.alphabet[ord("0")] = "EIHGEDCI"
            self.alphabet[ord("1")] = "GHL"
            self.alphabet[ord("2")] = "GHIEC"
            self.alphabet[ord("3")] = "GHIACDE"
            self.alphabet[ord("4")] = "LHNJ"
            self.alphabet[ord("5")] = "IGNJCDE"
            self.alphabet[ord("6")] = "IHGEDCJN"
            self.alphabet[ord("7")] = "GIL"
            self.alphabet[ord("8")] = "NGHICDENJ"
            self.alphabet[ord("9")] = "JNGHICDE"
            #  Alphabet Uppercase
            self.alphabet[ord("A")] = "ENOPQJC NJ"
            self.alphabet[ord("B")] = "EGPQAKLE NA"
            self.alphabet[ord("C")] = "KLMNOPQ"
            self.alphabet[ord("D")] = "EGPQJKLE"
            self.alphabet[ord("E")] = "IGEC NA"
            self.alphabet[ord("F")] = "IGE NA"
            self.alphabet[ord("G")] = "AJKLMNOPQ"
            self.alphabet[ord("H")] = "GE IC NJ"
            self.alphabet[ord("I")] = "PL"
            self.alphabet[ord("J")] = "QKLM"
            self.alphabet[ord("K")] = "GE NP NC"
            self.alphabet[ord("L")] = "GEC"
            self.alphabet[ord("M")] = "EGAIC"
            self.alphabet[ord("N")] = "EGCI"
            self.alphabet[ord("O")] = "JKLMNOPQJ"
            self.alphabet[ord("P")] = "EGPQAN"
            self.alphabet[ord("Q")] = "AKLMNOPQJK"
            self.alphabet[ord("R")] = "EGPQAN AC"
            self.alphabet[ord("S")] = "QPOKLM"
            self.alphabet[ord("T")] = "PL GI"
            self.alphabet[ord("U")] = "GNMLKJI"
            self.alphabet[ord("V")] = "GLI"
            self.alphabet[ord("W")] = "GEACI"
            self.alphabet[ord("X")] = "GC EI"
            self.alphabet[ord("Y")] = "GAI AL"
            self.alphabet[ord("Z")] = "GIEC"
            # Alphabet lower case
            self.alphabet[ord("a")] = "1ENOPQJC NJ"
            self.alphabet[ord("b")] = "1EGPQAKLE NA"
            self.alphabet[ord("c")] = "1KLMNOPQ"
            self.alphabet[ord("d")] = "1EGPQJKLE"
            self.alphabet[ord("e")] = "1IGEC NA"
            self.alphabet[ord("f")] = "1IGE NA"
            self.alphabet[ord("g")] = "1AJKLMNOPQ"
            self.alphabet[ord("h")] = "1GE IC NJ"
            self.alphabet[ord("i")] = "1PL"
            self.alphabet[ord("j")] = "1QKLM"
            self.alphabet[ord("k")] = "1GE NP NC"
            self.alphabet[ord("l")] = "1GEC"
            self.alphabet[ord("m")] = "1EGAIC"
            self.alphabet[ord("n")] = "1EGCI"
            self.alphabet[ord("o")] = "1JKLMNOPQJ"
            self.alphabet[ord("p")] = "1EGPQAN"
            self.alphabet[ord("q")] = "1AKLMNOPQJK"
            self.alphabet[ord("r")] = "1EGPQAN AC"
            self.alphabet[ord("s")] = "1QPOKLM"
            self.alphabet[ord("t")] = "1PL GI"
            self.alphabet[ord("u")] = "1GNMLKJI"
            self.alphabet[ord("v")] = "1GLI"
            self.alphabet[ord("w")] = "1GEACI"
            self.alphabet[ord("x")] = "1GC EI"
            self.alphabet[ord("y")] = "1GAI AL"
            self.alphabet[ord("z")] = "1GIEC"

        def setCenterText(self, cenx):
            self.cx = cenx

        def scaleRot(self, psize, pangle):
            for i in range(18):
                self.plotxy[i].x = psize * math.cos(pangle + self.plot[i].angle) * self.plot[i].radius
                self.plotxy[i].y = psize * math.sin(pangle + self.plot[i].angle) * self.plot[i].radius
            self.size = psize
            self.angle = pangle

        def drawScript(self, ctx, s, xc, yc, colour, exp=None):
            if exp is None:
                explode = self.boom
            else:
                explode = exp
            defaultColour = colour
            xo = 0.0
            yo = 0.0
            k = 1
            b = 0
            if s is None:
                return
            ss = " " + s.upper()
            instructIdx = iter(range(ss.__len__()))
            for i in instructIdx:
                c = ss[i]
                if c == "$":
                    i = next(instructIdx)
                    c = ss[i]
                    a = ord(c)
                    if 48 <= a <= 57:
                        a -= 48
                    elif 65 <= a <= 70:
                        a -= 55
                    else:
                        a = defaultColour
                    colour = a
                elif c == " ":
                    b = 1
                else:
                    a = ord(c)
                    if 65 <= a < (65 + 17):
                        a -= 65
                        if k == 1.0:
                            x = self.plotxy[a].x + xc
                            y = self.plotxy[a].y + yc
                        else:
                            x = self.plotxy[a].x * k + xc
                            y = self.plotxy[a].y * k + yc
                        if b == 0:
                            if explode == 1.0:
                                ctx.Line(xo, yo, x, y, colour)
                            else:
                                xx = (xo + x) / 2.0 - xc
                                yy = (yo + y) / 2.0 - yc
                                xx = xx * explode - xx
                                yy = yy * explode - yy
                                x1 = xo + xx
                                y1 = yo + yy
                                x2 = x + xx
                                y2 = y + yy
                                ctx.Line(x1, y1, x2, y2, colour)
                        xo = x
                        yo = y
                        b = 0
                    else:
                        if 48 <= a <= 57:
                            if a == 48:
                                k = 1.0
                            elif a == 49:
                                k = 0.70710678118654752440084436210485
                            else:
                                k = 0.70710678118654752440084436210485 ** (a - 48)

        def drawText(self, ctx, s, xc, yc, colour, txtA=None):
            txtAngle = self.angle if (txtA is None) else txtA
            c = float(s.__len__() * self.cx)
            dx = self.size * math.cos(txtAngle) * 1.80
            dy = self.size * math.sin(txtAngle) * 1.80
            for i in range(s.__len__()):
                a = ord(s[i])
                self.drawScript(ctx, self.alphabet[a], (xc + dx * (i - c)), (yc + dy * (i - c)), colour)

    class game_status(Enum):
        GS_START = 0
        GS_INTRO = 1
        GS_RUN = 2
        GS_PAUSE = 3
        GS_CRASHED = 4
        GS_LANDED = 5
        GS_GAMEOVER = 6
        GS_FINISH = 7
        GS_EDIT = 8
        GS_EDIT_TEXT = 9

    class player_action(Enum):
        PA_NOTHING = 0
        PA_LEFT = 1
        PA_RIGHT = 2
        PA_THRUST = 3
        PA_QUIT = 4
        PA_PAUSE = 5

    class lander_status(Enum):
        LS_NORMAL = 0
        LS_THRUST = 1
        LS_LANDED = 2
        LS_LANDED_NOSKY = 3
        LS_CRASH = 4

    class EnergySucker_Status(Enum):
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
            self.Speed = RedcrabLander.Vertex2D()
            self.fuel = 0.0
            self.angle = 0.0
            self.size = 0.0
            self.status = RedcrabLander.lander_status.LS_NORMAL
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
            self.status = RedcrabLander.lander_status.LS_NORMAL
            self.crash_tic = 0
            self.tic = 0
            self.noise_tic = 0
            self.model.boom = 1

        def Draw(self, ctx):
            # 	Static tic As Integer
            # int v1; //, v2; // Dim As Integer v1, v2
            self.model.scaleRot(self.size * 2 * ctx.KW, self.angle)
            self.tic += 1
            if self.status == RedcrabLander.lander_status.LS_NORMAL:
                self.crash_tic = 0
                self.model.boom = 1
                self.model.drawScript(ctx, self.LANDER_NORMAL, (self.location.x * ctx.KW),
                                      ((240 - self.location.y) * ctx.KH), 10)
                if self.fuel <= 0:
                    ctx.smalltxt.drawText(ctx, "I'M CRASHING!", (self.location.x * ctx.KW),
                                          ((240 - self.location.y - self.size - 7) * ctx.KH), 15)
            elif self.status == RedcrabLander.lander_status.LS_LANDED or \
                    self.status == RedcrabLander.lander_status.LS_LANDED_NOSKY:
                self.crash_tic = 0
                self.model.boom = 1
                self.model.drawScript(ctx, self.LANDER_NORMAL, (self.location.x * ctx.KW),
                                      ((240 - self.location.y) * ctx.KH), 10)
                ctx.Circle(self.location.x * ctx.KW, (240 - self.location.y) * ctx.KH,
                           (self.size + 5 + 3 * math.sin(self.tic / 10.0)) * ctx.KW, 8)
                if 70 <= self.fuel <= 99:
                    if self.status == RedcrabLander.lander_status.LS_LANDED:
                        ctx.smalltxt.drawText(ctx, "Launch To " + str(int(3 - ((self.fuel - 70.0) / 30 * 4))),
                                              (self.location.x * ctx.KW),
                                              ((240 - self.location.y - self.size - 7) * ctx.KH), 15)
                    else:
                        ctx.smalltxt.drawText(ctx, "I'm Ready !", (self.location.x * ctx.KW),
                                              ((240 - self.location.y - self.size - 7) * ctx.KH), 15)
                if self.fuel >= 100 and self.location.y < 300 and self.status == RedcrabLander.lander_status.LS_LANDED:
                    self.angle = 0
                    self.location.y *= 1.01

            if self.status == RedcrabLander.lander_status.LS_CRASH:
                self.crash_tic += 1

                if self.crash_tic < 60:
                    self.model.boom = 1 - self.crash_tic / 15.0
                    self.model.drawScript(ctx, self.LANDER_NORMAL, (self.location.x * ctx.KW),
                                          ((240 - self.location.y) * ctx.KH), 10)
            if self.status == RedcrabLander.lander_status.LS_THRUST:
                self.noise_tic = 0

                if self.tic % 20 < self.fuel / 5 and self.fuel > 0:
                    self.model.drawScript(ctx, self.LANDER_THRUST, (self.location.x * ctx.KW),
                                          ((240 - self.location.y) * ctx.KH), 10)
                    if self.tic%3 == 0:
                        ctx.sound_play_thrust()  # SoundManager.instance.NoiseStart();
                else:
                    self.model.drawScript(ctx, self.LANDER_NORMAL, (self.location.x * ctx.KW),
                                          ((240 - self.location.y) * ctx.KH), 10)
            if self.status != RedcrabLander.lander_status.LS_THRUST:
                self.noise_tic += 1
                #  if (self.noise_tic>5) SoundManager.instance.NoiseStop();

    class EnergySucker:
        def __init__(self):
            self.EnergySucker_NORMAL = "$C0H3I0B3C0D3E0F3G0H $E3I0I 3C0C 3E0E 3G0G"
            self.model = RedcrabLander.TinyVectrex()
            self.location = RedcrabLander.Vertex2D()
            self.Speed = RedcrabLander.Vertex2D()
            self.angle = 0.0
            self.size = 0.0
            self.tic = 0
            self.status = RedcrabLander.EnergySucker_Status.SS_NORMAL
            self.init()

        def Draw(self, ctx):
            self.tic += 1
            if self.status == RedcrabLander.EnergySucker_Status.SS_NORMAL:
                self.model.scaleRot(self.size * ctx.KW, self.tic * np.pi / 90.0)
                self.model.drawScript(ctx, self.EnergySucker_NORMAL, (self.location.x * ctx.KW),
                                      ((240 - self.location.y) * ctx.KH), 10)
            elif self.status == RedcrabLander.EnergySucker_Status.SS_EXPLODED:
                pass  # future evolution : when energy sucker are destroyable

        def init(self, x=0, y=0):
            self.tic = 0
            self.status = RedcrabLander.EnergySucker_Status.SS_NORMAL
            self.location.x = 0
            self.location.y = 0
            self.Speed.x = 0
            self.Speed.y = 0
            self.angle = 0
            self.size = 7
            self.model.boom = 1
            self.location.x = x
            self.location.y = y

    class Landscape:
        def __init__(self):
            self.ground = [0.0] * 320
            self.sky = [0.0] * 320
            self.padLocation = RedcrabLander.Vertex2D()
            self.fuelLocation = RedcrabLander.Vertex2D()
            self.gravity = 0.0
            self.startLocation = RedcrabLander.Vertex2D()
            self.inverse = 0
            self.tic = 0
            self.go_up = 0
            self.go_down = 0
            self.go_left = 0
            self.go_right = 0
            self.allowtakeoff = 0
            self.landedmsg = ""
            self.init()

        def Draw(self, ctx):
            self.tic += 1
            ub = self.ground.__len__() - 1
            for i in range(ub):
                if self.ground[i] != self.sky[i] or self.ground[i + 1] != self.sky[i + 1]:
                    if self.ground[i] >= 20 and self.ground[i + 1] >= 20:
                        ctx.Line(i * ctx.KW, (240 - int(self.ground[i])) * ctx.KH, (i + 1) * ctx.KW,
                                 (240 - int(self.ground[i + 1])) * ctx.KH, 13)
                    ctx.Line(i * ctx.KW, (240 - int(self.sky[i])) * ctx.KH, (i + 1) * ctx.KW,
                             (240 - int(self.sky[i + 1])) * ctx.KH, 13)
            ctx.LineBF(int(self.padLocation.x - 10) * ctx.KW, (240 - int(self.padLocation.y)) * ctx.KH,
                       int(self.padLocation.x + 10) * ctx.KW, (245 - int(self.padLocation.y)) * ctx.KH, 11)
            ctx.smalltxt.drawText(ctx, "Target", ((self.padLocation.x + 1) * ctx.KW),
                                  ((240 - self.padLocation.y + 8) * ctx.KH), 11)
            ctx.LineBF(int(self.fuelLocation.x - 10) * ctx.KW, (240 - int(self.fuelLocation.y)) * ctx.KH,
                       int(self.fuelLocation.x + 10) * ctx.KW, (245 - int(self.fuelLocation.y)) * ctx.KH, 11)
            if self.tic % 240 < 120:
                energy = "Energy"
            else:
                energy = "Reload"
            ctx.smalltxt.drawText(ctx, energy, ((self.fuelLocation.x + 1) * ctx.KW),
                                  ((240 - self.fuelLocation.y + 8) * ctx.KH), 11)

        def init(self, Glevel=0):
            self.tic = 0
            self.gravity = 0.0025 * (int(Glevel / 10.0) / 3.0 + 1.0)
            self.inverse = 0
            self.allowtakeoff = 1
            self.go_up = 0
            self.go_down = 0
            self.go_left = 0
            self.go_right = 0
            self.landedmsg = "LANDED"
            if Glevel <= 0:
                Glevel = 1
            level = Glevel % 10
            # lb = 0
            ub = self.ground.__len__() - 1
            self.startLocation.x = 160
            self.startLocation.y = 230
            prev = np.random.rand() * 200 + 20
            for i in range(ub + 1):
                self.sky[i] = 250
                self.ground[i] = prev
            for j in range(1, 7):
                slope = np.random.rand() * (level + 1) * 250 / j - ((level + 1) * 250 / 2 / j)
                cnt = 0
                for i in range(ub + 1):
                    cur = self.ground[i] + slope * cnt
                    self.ground[i] = cur
                    cnt += 1
                    if cnt > 320 / 2 ** j:
                        slope = np.random.rand() * (level + 1) * 250 / j - ((level + 1) * 250 / 2 / j)
                        cnt = 0
                        if i < ub:
                            delta = cur - self.ground[i + 1]
                        else:
                            delta = 0
                        for k in range(i + 1, ub + 1):
                            self.ground[k] += delta
            delta = 0
            mini = 1000
            maxi = 0
            for i in range(ub + 1):
                mini = self.ground[i] if (self.ground[i] < mini) else mini
                maxi = self.ground[i] if (self.ground[i] > maxi) else maxi
                delta += self.ground[i]
            ground = (maxi - mini) / 5 * (1 if level == 0 else level)
            mini = maxi - ground
            for i in range(ub + 1):
                self.ground[i] = mini if (self.ground[i] < mini) else self.ground[i]
                self.ground[i] = (self.ground[i] - mini) / (maxi - mini) * (level / 8.0) * 200 + 20
            for i in range(ub + 1):
                self.ground[i] = float(np.clip(self.ground[i], 20.0, 220.0))

            self.fuelLocation.x = -100.0
            self.fuelLocation.y = -100
            self.padLocation.x = (int(np.random.rand() * 2) * 300 - 150) * (level / 10.0) + 160
            self.padLocation.y = (self.ground[int(self.padLocation.x) - 10] + self.ground[
                int(self.padLocation.x) + 10]) / 2
            self.padLocation.y = 20 if (self.padLocation.y < 20) else self.padLocation.y
            lb = int(self.padLocation.x) - 10
            ub = int(self.padLocation.x) + 10
            for i in range(lb, ub + 1):
                self.ground[i] = self.padLocation.y

    class game:
        def __init__(self):
            self.tic = 0
            self.tic2 = 0
            self.life = 0
            self.bestsafeland = 0
            self.safeland = 0
            self.sublevelx = 0
            self.sublevely = 0
            self.bestscore = 0
            self.score = 0
            self.showMessage = True
            self.showMessageHelp = False
            self.ship = RedcrabLander.Lander()
            self.Sucker = tuple(RedcrabLander.EnergySucker() for _ in range(101))
            self.nbSucker = 0
            self.scene = RedcrabLander.Landscape()
            self.playerAct = RedcrabLander.player_action.PA_NOTHING
            self.status = RedcrabLander.game_status.GS_INTRO
            self.msg = [""] * 201
            self.xm = 0.0
            self.ym = 0.0
            self.bm = 0

            self.init()
            self.bestsafeland = 0
            self.bestscore = 0

            try:
                btf = open(RedcrabLander.data_path + "LANDER.SCO")
                self.bestscore = int(btf.readline())
                self.bestsafeland = int(btf.readline())
                btf.close()
            except Exception as n:
                print(n)

            for i in range(self.msg.__len__()):
                self.msg[i] = "Press Any Key to Start"
            self.msg[1] = "Another easy one,"
            self.msg[2] = "Looks to be the same"
            self.msg[3] = "Detecting FOE not far away"
            self.msg[4] = "ALERT ! § Energy sucker ! Avoid it !"
            self.msg[5] = "It was easy... ! But it still here !"
            self.msg[6] = "1 more § !"
            self.msg[7] = "Energy Sucker Engine Enhanced !"
            self.msg[8] = "BEWARE ! They fly a bit faster!"
            self.msg[9] = "§ speed linit ! But they are 3 !"
            self.msg[10] = "New planet with higher gravity"
            self.msg[11] = "Hope you're not tired"
            self.msg[12] = "He he ! 4 suckers now !"
            self.msg[13] = "Again !"
            self.msg[14] = "Again !"
            self.msg[15] = "Again !"
            self.msg[16] = "Oooh ! 5 Energy Suckers Now"
            self.msg[17] = "Again !"
            self.msg[18] = "Again !"
            self.msg[19] = "One more sucker ! "
            self.msg[20] = "New planet with higher gravity and 6 § !"
            self.msg[21] = "Keep going almost finished !"
            self.msg[22] = "Grr ! Here come another one"
            self.msg[23] = "----------"

        def init(self):
            self.safeland = 0
            self.score = 0
            self.life = 3
            self.status = RedcrabLander.game_status.GS_INTRO
            self.tic = 0
            self.tic2 = 0
            self.nbSucker = 0
            self.initLevel(0)

        def Draw(self, ctx):
            aLife = RedcrabLander.Lander()
            ctx.Cls()
            #  Lanscape
            self.scene.Draw(ctx)
            #  Lander
            self.ship.Draw(ctx)
            #  Sucker
            for i in range(self.nbSucker):
                self.Sucker[i].Draw(ctx)
            # Score
            if self.status != RedcrabLander.game_status.GS_EDIT and \
                    self.status != RedcrabLander.game_status.GS_EDIT_TEXT:
                ctx.boardtxt.drawText(ctx, " & " + str(self.safeland) + "  # " + str(self.score), 0, (234 * ctx.KH), 10)
            else:
                if self.scene.allowtakeoff == 0:
                    m = "L"
                else:
                    m = "T"
                ctx.boardtxt.drawText(ctx, " & " + str(self.safeland) + " (" + str(self.sublevelx) + "," + str(
                    self.sublevely) + ")" + m, 0, (234 * ctx.KH), 10)

            # Life
            if self.status != RedcrabLander.game_status.GS_EDIT and \
                    self.status != RedcrabLander.game_status.GS_EDIT_TEXT:
                aLife.size = 5
                aLife.status = RedcrabLander.lander_status.LS_NORMAL
                aLife.location.y = 6
                for i in range(1, self.life + 1):
                    aLife.location.x = 88 + 25 + (i - 1) * 12
                    aLife.angle = self.tic * np.pi / 180
                    aLife.Draw(ctx)

            # Arrow to show possible direction
            if self.scene.go_up != 0:
                ctx.boardtxt.scaleRot(ctx.boardtxt.size, 0)
                ctx.boardtxt.drawText(ctx, "%", (88 * ctx.KW), (229 * ctx.KH), 10)
            if self.scene.go_down != 0:
                ctx.boardtxt.scaleRot(ctx.boardtxt.size, np.pi)
                ctx.boardtxt.drawText(ctx, "%", (88 * ctx.KW), (235 * ctx.KH), 10)
            if self.scene.go_left != 0:
                ctx.boardtxt.scaleRot(ctx.boardtxt.size, -np.pi / 2)
                ctx.boardtxt.drawText(ctx, "%", (85 * ctx.KW), (232 * ctx.KH), 10)
            if self.scene.go_right != 0:
                ctx.boardtxt.scaleRot(ctx.boardtxt.size, np.pi / 2)
                ctx.boardtxt.drawText(ctx, "%", (91 * ctx.KW), (232 * ctx.KH), 10)

            # Fuel	
            ctx.boardtxt.scaleRot(ctx.boardtxt.size, self.tic * np.pi / 180)
            ctx.boardtxt.drawText(ctx, " ~", (150 * ctx.KW), (235 * ctx.KH), 14, 0)
            ctx.boardtxt.scaleRot(ctx.boardtxt.size, 0)
            ctx.LineBF(161 * ctx.KW, 231 * ctx.KH, (161 + self.ship.fuel) * ctx.KW, 239 * ctx.KH, 14)
            ctx.LineB(161 * ctx.KW, 231 * ctx.KH, 261 * ctx.KW, 239 * ctx.KH, 15)

            # Speed
            if self.ship.Speed.y < 0:
                speed = int((self.ship.Speed.x ** 2 + self.ship.Speed.y ** 2) * 1000)
                speed = 100 if (int(abs(self.ship.angle / (np.pi / 180))) >= 10) else speed
                speed = 100 if (speed > 100) else speed
                ctx.LineBF(265 * ctx.KW, 231 * ctx.KH, (265 + speed / 2) * ctx.KW, 239 * ctx.KH, 14)
            ctx.LineB(265 * ctx.KW, 231 * ctx.KH, (265 + 60 / 2) * ctx.KW, 239 * ctx.KH, 15)
            ctx.LineB(265 * ctx.KW, 231 * ctx.KH, (265 + 50) * ctx.KW, 239 * ctx.KH, 15)

            if self.status == RedcrabLander.game_status.GS_START:
                #  START
                if self.tic2 < 200:
                    ctx.text.drawText(ctx, self.msg[self.safeland], ctx.G_WIDTH / 2.0,
                                      (120 * ctx.KH * (self.tic2 - 10) / 190.0), 10)
                else:
                    if self.tic2 > 500:
                        ctx.text.scaleRot(4 * ctx.KW, math.sin((self.tic2 - 500) * np.pi / 180 / 2) * np.pi / 4.0)
                    ctx.text.drawText(ctx, self.msg[self.safeland], ctx.G_WIDTH / 2.0, (120.0 * ctx.KH), 10)
                    ctx.text.scaleRot(4.0 * ctx.KW, 0)
            elif self.status == RedcrabLander.game_status.GS_INTRO:
                #  INTRO
                if self.tic2 == 1:
                    pass
                    ctx.sound_play_title()  # SoundManager.instance.PlaySingle(ctx.dl.titleSound,0.10f,1.25f);
                if self.tic2 <= 200:
                    ctx.bigtxt.scaleRot(1.0 * self.tic2 / 200.0 * 5.0 * ctx.KW, 1.0 * self.tic2 / 100.0 * np.pi)
                ctx.bigtxt.drawText(ctx, "$ Captain Lander $", ctx.G_WIDTH / 2.0, (95 * ctx.KH), 10)
                if self.tic2 >= 200:
                    ctx.text.drawText(ctx, "Left   : Turn left ", ctx.G_WIDTH / 2.0, ((105 + 9) * ctx.KH), 10)
                if self.tic2 >= 230:
                    ctx.text.drawText(ctx, "Right  : Turn right", ctx.G_WIDTH / 2.0, ((105 + 18) * ctx.KH), 10)
                if self.tic2 >= 260:
                    ctx.text.drawText(ctx, "Up     : Thrust    ", ctx.G_WIDTH / 2.0, ((105 + 27) * ctx.KH), 10)
                if self.tic2 >= 290:
                    ctx.text.drawText(ctx, "Space  : Pause     ", ctx.G_WIDTH / 2.0, ((105 + 36) * ctx.KH), 10)
                if self.tic2 >= 320:
                    ctx.text.drawText(ctx, "Escape : Quit      ", ctx.G_WIDTH / 2.0, ((105 + 45) * ctx.KH), 10)
                if self.tic2 >= 320 and self.bestscore != 0:
                    ctx.text.drawText(ctx, "Best score " + str(self.bestscore) + " with " + str(
                        self.bestsafeland) + " completed project", ctx.G_WIDTH / 2.0, ((105 + 62) * ctx.KH), 10)
                if self.tic2 >= 320 and self.bestscore == 0:
                    ctx.text.drawText(ctx, "No Best Score Yet !", ctx.G_WIDTH / 2.0, ((105 + 62) * ctx.KH), 10)
                if 200 <= self.tic2 <= 350:
                    ctx.text.drawText(ctx, self.msg[self.safeland], ctx.G_WIDTH / 2.0,
                                      ((110.0 + 72) * ctx.KH * (self.tic2 - 300.0) / (350 - 300.0)), 10)
                else:
                    if self.tic2 >= 350:
                        ctx.text.drawText(ctx, self.msg[self.safeland], ctx.G_WIDTH / 2.0, ((110 + 72) * ctx.KH), 10)
            elif self.status == RedcrabLander.game_status.GS_PAUSE:
                #  PAUSE
                if self.tic % 60 < 30:
                    ctx.bigtxt.scaleRot(5 * ctx.KW, 0)
                    ctx.bigtxt.drawText(ctx, "Pause", ctx.G_WIDTH / 2.0, (120 * ctx.KH), 12)
            elif self.status == RedcrabLander.game_status.GS_RUN:
                #  RUNNING
                if self.ship.fuel <= 0:
                    if self.tic % 30 < 15:
                        ctx.bigtxt.scaleRot(5 * ctx.KW, 0)
                        ctx.bigtxt.drawText(ctx, "NO ENERGY !", ctx.G_WIDTH / 2.0, (120 * ctx.KH), 12)
            elif self.status == RedcrabLander.game_status.GS_CRASHED:
                #  CRASHED
                #  "Life request" animation
                if self.tic2 <= 60:
                    aLife.location.x = 88 + 25 + self.life * 12
                    aLife.angle = self.tic * np.pi / 180
                    aLife.Draw(ctx)
                if self.tic2 == 60:
                    self.LoadLevel(self.safeland, 0, 0)
                if self.tic2 > 60:
                    destx = self.scene.startLocation.x
                    desty = self.scene.startLocation.y
                    if self.tic2 < 60 + 200:
                        aLife.location.x = (destx - (88 + 25 + self.life * 12)) / 200.0 * (
                                self.tic2 - 60) + 88 + 25 + self.life * 12
                        aLife.location.y = (desty - 6.0) / 200.0 * (self.tic2 - 60) + 6
                        aLife.size = (7.0 - 5.0) / 200.0 * (self.tic2 - 60) + 5
                        aLife.angle = self.tic * np.pi / 180
                    else:
                        ctx.smalltxt.drawText(ctx, "I'm Ready", (destx * ctx.KW),
                                              (((240.0 - desty) + 7 + 4) * ctx.KW), 15)
                        aLife.location.x = destx
                        aLife.location.y = desty
                        aLife.size = 7
                        aLife.angle = self.tic * np.pi / 180
                    aLife.Draw(ctx)
                if self.tic2 < 200:
                    # text2.boom = (10/200.0*self.tic2)-9
                    if self.tic2 % 4 == 0:
                        ctx.text2.scaleRot((15.0 + np.random.rand() * 2.0) * ctx.KW, (np.random.rand() * 0.2) - 0.1)
                else:
                    ctx.text2.boom = 1
                ctx.text2.drawText(ctx, "CRASH!", ctx.G_WIDTH / 2.0, (120.0 * ctx.KH), 14)
                ctx.text2.boom = 1
            elif self.status == RedcrabLander.game_status.GS_GAMEOVER:
                #  GAME OVER
                if self.tic2 < 200:
                    ctx.text2.boom = 10 - (9 / 200.0 * self.tic2)
                    ctx.text2.scaleRot(5 * ctx.KW * self.tic2 / 60, 0)
                ctx.text2.drawText(ctx, "GAME OVER", ctx.G_WIDTH / 2.0, (120 * ctx.KH), 15)
                ctx.text2.boom = 1
            elif self.status == RedcrabLander.game_status.GS_FINISH:
                #  FINISH THE GAME
                if self.tic2 < 200:
                    ctx.text2.boom = 10 - (9 / 200.0 * self.tic2)
                    ctx.text2.scaleRot(5 * ctx.KW * self.tic2 / 60.0, 0)
                ctx.text2.drawText(ctx, "YOU WIN", ctx.G_WIDTH / 2.0, (120.0 * ctx.KH), 15)
                ctx.text2.boom = 1
            elif self.status == RedcrabLander.game_status.GS_LANDED:
                #  LANDED
                if self.tic2 <= 180:
                    ctx.text2.scaleRot(5 * ctx.KW * self.tic2 / 60.0, self.tic2 * 1.0 / 90 * np.pi)
                ctx.text2.drawText(ctx, self.scene.landedmsg, ctx.G_WIDTH / 2.0, (120 * ctx.KH), 15)
            elif self.status == RedcrabLander.game_status.GS_EDIT or \
                    self.status == RedcrabLander.game_status.GS_EDIT_TEXT:
                # //LEVEL editor
                if ctx.action_key_f1:
                    self.showMessageHelp = True
                    self.showMessage = True
                    self.tic = 0
                if self.scene.go_up != 0:
                    ctx.LineB(0, 0, 319.0 * ctx.KW, 5.0 * ctx.KH, 9)
                if self.scene.go_down != 0:
                    ctx.LineB(0, (239.0 - 20.0) * ctx.KH, 319.0 * ctx.KW, (240.0 - 20.0 - 5.0) * ctx.KH, 9)
                if self.scene.go_left != 0:
                    ctx.LineB(0, 0, 5.0 * ctx.KW, (240.0 - 20.0) * ctx.KH, 9)
                if self.scene.go_right != 0:
                    ctx.LineB((320.0 - 5.0) * ctx.KW, 0, 319.0 * ctx.KW, (240.0 - 20.0) * ctx.KH, 9)
                ctx.boardtxt.drawText(ctx, "G", 80.0 * ctx.KW, 234.0 * ctx.KH, 10)
                ctx.LineB(88.0 * ctx.KW, 230.0 * ctx.KH, (88.0 + 50.0) * ctx.KW, 239.0 * ctx.KH, 10)
                ctx.LineBF(88.0 * ctx.KW, 230.0 * ctx.KH, (88.0 + (self.scene.gravity * 2000.0)) * ctx.KW,
                           239.0 * ctx.KH, 10)
                ctx.boardtxt.drawText(ctx, "LEVEL EDITOR", 246.0 * ctx.KW, 226.0 * ctx.KH, 9)
                if self.status == RedcrabLander.game_status.GS_EDIT_TEXT:
                    # pst = ""
                    if self.tic % 30 < 15:
                        pst = " "
                    else:
                        pst = "_"
                    pst = self.msg[self.safeland] + pst
                    ctx.text.scaleRot(4.0 * ctx.KW, 0)
                    ctx.text.drawText(ctx, pst, ctx.G_WIDTH / 2.0, 120.0 * ctx.KH, 10)
                ctx.boardtxt.drawText(ctx, "X", self.xm * ctx.KW, self.ym * ctx.KH, 10)

        def initLevel(self, level):
            self.playerAct = RedcrabLander.player_action.PA_NOTHING
            self.ship.init()
            self.nbSucker = 0
            self.sublevelx = 0
            self.sublevely = 0
            i = self.LoadLevel(level)
            if i == 0:
                self.scene.init(level)
                if self.safeland > 3:
                    self.nbSucker = int(self.safeland / 3.0)
                    self.nbSucker = self.Sucker.__len__() if (self.nbSucker > self.Sucker.__len__()) else self.nbSucker
                    for i in range(self.nbSucker):
                        self.Sucker[i].location.x = 160 + 160 - self.scene.padLocation.x + np.random.rand() * 30 - 15
                        if abs(self.Sucker[i].location.x - self.scene.padLocation.x) < 100:
                            self.Sucker[i].location.x *= 2.0
                            self.Sucker[i].location.x = 319 if (self.Sucker[i].location.x > 319) else self.Sucker[
                                i].location.x
                        self.Sucker[i].location.y = self.scene.ground[int(self.Sucker[i].location.x)] + 20 + (
                                220 - self.scene.ground[int(self.Sucker[i].location.x)]) * np.random.rand()
            self.ship.location.x = self.scene.startLocation.x
            self.ship.location.y = self.scene.startLocation.y

        def EnergySuckerAction(self, ctx):
            perTicSpeed = 14.0 / ctx.fps
            xs = self.ship.location.x
            ys = self.ship.location.y
            if self.status == RedcrabLander.game_status.GS_RUN:
                for i in range(self.nbSucker):
                    if self.Sucker[i].status == RedcrabLander.EnergySucker_Status.SS_NORMAL:
                        xm = self.Sucker[i].location.x
                        ym = self.Sucker[i].location.y
                        d = ((xs - xm) ** 2 + (ys - ym) ** 2) ** 0.5
                        dx = xs - xm
                        dy = ys - ym
                        k = perTicSpeed / d
                        # detect collision to ship, if so then still ship energy
                        if d < self.ship.size + self.Sucker[i].size:
                            if (self.tic + i) % 10 == 0:
                                if self.ship.fuel > 0:
                                    self.ship.fuel -= 1
                        self.Sucker[i].Speed.x = k * dx
                        self.Sucker[i].Speed.y = k * dy
                        xm += self.Sucker[i].Speed.x
                        ym += self.Sucker[i].Speed.y
                        xm = 319 if (xm > 319) else xm
                        xm = 0 if (xm < 0) else xm
                        new_alt = ym - self.scene.ground[int(xm)]
                        new_skydist = self.scene.sky[int(xm)] - ym
                        # ground detection
                        if (0 <= new_alt <= 10) or (0 <= new_skydist <= 10):
                            self.Sucker[i].Speed.y = 0
                            self.Sucker[i].Speed.x = math.copysign(perTicSpeed, self.Sucker[i].Speed.x)

                        if new_alt <= 0 and new_skydist <= 0:
                            self.Sucker[i].Speed.y = 0
                            self.Sucker[i].Speed.x = 0
                        else:
                            if new_alt < 0:  # in  ground
                                self.Sucker[i].Speed.y = perTicSpeed
                                self.Sucker[i].Speed.x = 0

                            if new_skydist < 0:  # in  sky
                                self.Sucker[i].Speed.y = -perTicSpeed
                                self.Sucker[i].Speed.x = 0

                        self.Sucker[i].location.x += self.Sucker[i].Speed.x
                        self.Sucker[i].location.y += self.Sucker[i].Speed.y

        def tick(self, ctx):
            self.tic += 1
            self.tic2 += 1
            st = ctx.inkey  # (ctx.anyKey()) ? "+" : "";
            #  Player action
            self.playerAct = RedcrabLander.player_action.PA_NOTHING
            if ctx.action_rotate_left:
                self.playerAct = RedcrabLander.player_action.PA_LEFT
            if ctx.action_rotate_right:
                self.playerAct = RedcrabLander.player_action.PA_RIGHT
            if ctx.action_thrust:
                self.playerAct = RedcrabLander.player_action.PA_THRUST
            if ctx.action_pause_resume:
                self.playerAct = RedcrabLander.player_action.PA_PAUSE
            if ctx.action_quit:
                self.playerAct = RedcrabLander.player_action.PA_QUIT
            # if (UNITY_EDITOR)
            # 'Input.GetKey(KeyCode.F10)'
            if ctx.action_edit and self.status != RedcrabLander.game_status.GS_EDIT and self.tic > 60:
                ctx.sound_pause()  # SoundManager.instance.Pause();
                self.status = RedcrabLander.game_status.GS_EDIT
                self.ship.Speed.x = 0
                self.ship.Speed.y = 0
                self.ship.status = RedcrabLander.lander_status.LS_NORMAL
                self.tic = 0
                self.tic2 = 0
                self.LoadLevel(self.safeland, self.sublevelx, self.sublevely)

            # //        # Ifdef CHEAT
            #  Cheat keys (Debugging purpose)
            # If st="-" Then self.ship.status = LS_CRASH
            # If st="+" Then self.ship.status = LS_NORMAL
            if st == "*":
                self.ship.fuel = 100
            if st == "/":
                self.tic = 0
                self.life = 0
                self.tic2 = 0
                self.status = RedcrabLander.game_status.GS_GAMEOVER
            # endif
            # Enemy action
            self.EnergySuckerAction(ctx)

            if self.status == RedcrabLander.game_status.GS_GAMEOVER or \
                    self.status == RedcrabLander.game_status.GS_FINISH:
                if self.bestscore < self.score:
                    self.bestscore = self.score
                    self.bestsafeland = self.safeland
                    try:
                        fi = open(RedcrabLander.data_path + "LANDER.SCO", "wt")
                        print(self.bestscore, file=fi)
                        print(self.bestsafeland, file=fi)
                        fi.close()
                    except Exception as n:
                        print(n)  # don"t care :) if the best score failed to be saved

            #  Process player action
            if self.status == RedcrabLander.game_status.GS_START:
                self.ship.location.x = self.scene.startLocation.x
                self.ship.location.y = self.scene.startLocation.y
                if ctx.anyKey() and self.tic > 30:
                    self.status = RedcrabLander.game_status.GS_RUN
                    self.tic = 0

            if self.status == RedcrabLander.game_status.GS_INTRO:
                self.ship.location.x = self.scene.startLocation.x
                self.ship.location.y = self.scene.startLocation.y
                if ctx.anyKey() and self.tic > 30:
                    self.status = RedcrabLander.game_status.GS_RUN
                    # TODO SoundManager.instance.Stop()
                    self.tic = 0

            if self.status == RedcrabLander.game_status.GS_LANDED and self.tic > 120:
                if self.ship.fuel < 100 and self.tic % 3 == 0:
                    self.ship.fuel += 1
                if ctx.anyKey() or self.ship.location.y > 280 or self.tic > 60 * 10:
                    self.tic = 0
                    self.showMessage = True
                    self.status = RedcrabLander.game_status.GS_START
                    self.initLevel(self.safeland)
                    self.tic = 0
                    self.tic2 = 0

            if self.status == RedcrabLander.game_status.GS_CRASHED and self.tic > 120:
                if ctx.anyKey() and self.tic2 > 260 + 180:
                    self.status = RedcrabLander.game_status.GS_START
                    self.ship.init()
                    self.initLevel(self.safeland)
                    self.tic = 0
                    self.tic2 = 0

            if self.status == RedcrabLander.game_status.GS_GAMEOVER and self.tic > 120:
                if ctx.anyKey() or self.tic > 800:
                    self.init()
                    self.tic = 0
                    self.tic2 = 0

            if self.status == RedcrabLander.game_status.GS_FINISH and self.tic > 120:
                if ctx.anyKey() or self.tic > 800:
                    self.init()
                    self.tic = 0
                    self.tic2 = 0

            if self.status == RedcrabLander.game_status.GS_PAUSE and self.tic > 60:
                if self.playerAct == RedcrabLander.player_action.PA_PAUSE:
                    self.status = RedcrabLander.game_status.GS_RUN
                    self.playerAct = RedcrabLander.player_action.PA_NOTHING
                    self.tic = 0
                    ctx.sound_unpause()  # SoundManager.instance.UnPause()
            # if (UNITY_EDITOR)
            if self.status == RedcrabLander.game_status.GS_EDIT or \
                    self.status == RedcrabLander.game_status.GS_EDIT_TEXT:
                # If self.safeland = 0 Then self.safeland = 1
                xxm = ctx.action_mouse_position_x  # Input.mousePosition.x/Screen.width
                yym = ctx.action_mouse_position_y  # nput.mousePosition.y/Screen.height
                mbutton = 1 if ctx.action_mouse_button1 else 0  # Input.GetKey(KeyCode.Mouse0)?1:0
                mbutton += 2 if ctx.action_mouse_button2 else 0  # Input.GetKey(KeyCode.Mouse1) ? 2 : 0
                mbutton += 4 if ctx.action_mouse_button3 else 0  # Input.GetKey(KeyCode.Mouse2) ? 4 : 0
                self.bm = mbutton
                self.xm = xxm / ctx.KW * 1.0
                self.ym = yym / ctx.KH * 1.0
                self.scene.startLocation.x = self.ship.location.x
                self.scene.startLocation.y = self.ship.location.y

                # If MultiKey(FB.SC_CONTROL)= 0 then
                if not ctx.action_key_ctrl:
                    if not ctx.action_key_shift:
                        # If MultiKey(FB.SC_UP) And MultiKey(FB.SC_LSHIFT)= 0 Then self.ship.location.y += 1 / KH
                        if ctx.action_key_uparrow:
                            self.ship.location.y += 1.0
                        # If MultiKey(FB.SC_DOWN) And MultiKey(FB.SC_LSHIFT)= 0 Then   self.ship.location.y -= 1 / KH
                        if ctx.action_key_downarrow:
                            self.ship.location.y -= 1.0
                        # If MultiKey(FB.SC_LEFT) And MultiKey(FB.SC_LSHIFT)= 0 Then self.ship.location.x -= 1 / KW
                        if ctx.action_key_leftarrow:
                            self.ship.location.x -= 1.0
                        # If MultiKey(FB.SC_RIGHT) And MultiKey(FB.SC_LSHIFT)= 0 Then self.ship.location.x += 1 / KW
                        if ctx.action_key_rightarrow:
                            self.ship.location.x += 1.0
                    else:
                        # If MultiKey(FB.SC_LEFT) And MultiKey(FB.SC_LSHIFT) Then
                        if ctx.action_key_leftarrow:
                            self.ship.angle -= np.pi / 100.0
                            if self.ship.angle < -np.pi:
                                self.ship.angle += 2.0 * np.pi
                        if ctx.action_key_rightarrow:
                            self.ship.angle += np.pi / 100.0
                            if self.ship.angle > np.pi:
                                self.ship.angle -= 2.0 * np.pi
                else:
                    # If MultiKey(FB.SC_UP) Then
                    if ctx.action_key_uparrow:
                        for i in range(self.scene.ground.__len__()):
                            self.scene.ground[i] += 1
                            self.scene.sky[i] += 1
                        for i in range(self.Sucker.__len__()):
                            self.Sucker[i].location.y += 1
                        self.scene.padLocation.y += 1
                        self.scene.fuelLocation.y += 1
                        self.ship.location.y += 1
                    # If MultiKey(FB.SC_DOWN) Then
                    if ctx.action_key_downarrow:
                        for i in range(self.scene.ground.__len__()):
                            self.scene.ground[i] -= 1
                            self.scene.sky[i] -= 1
                        for i in range(self.Sucker.__len__()):
                            self.Sucker[i].location.y -= 1
                        self.scene.padLocation.y -= 1
                        self.scene.fuelLocation.y -= 1
                        self.ship.location.y -= 1
                    # If MultiKey(FB.SC_LEFT) Then
                    if ctx.action_key_leftarrow:
                        tg = self.scene.ground[self.scene.ground.__len__() - 1]
                        ts = self.scene.sky[self.scene.sky.__len__() - 1]
                        for i in range(self.scene.ground.__len__(), 0, -1):
                            self.scene.ground[i] = self.scene.ground[i - 1]
                            self.scene.sky[i] = self.scene.sky[i - 1]
                        self.scene.ground[0] = tg
                        self.scene.sky[0] = ts
                        for i in range(self.Sucker.__len__()):
                            self.Sucker[i].location.x += 1
                            if self.Sucker[i].location.x >= 320:
                                self.Sucker[i].location.x -= 320
                        if self.scene.padLocation.x > -100:
                            self.scene.padLocation.x += 1
                            if self.scene.padLocation.x >= 320:
                                self.scene.padLocation.x -= 320
                        if self.scene.fuelLocation.x > -100:
                            self.scene.fuelLocation.x += 1
                            if self.scene.fuelLocation.x >= 320:
                                self.scene.fuelLocation.x -= 320
                        self.ship.location.x += 1
                        if self.ship.location.x >= 320:
                            self.ship.location.x -= 320
                    # If MultiKey(FB.SC_RIGHT) Then
                    if ctx.action_key_rightarrow:
                        tg = self.scene.ground[0]
                        ts = self.scene.sky[0]
                        for i in range(self.scene.ground.__len__()):
                            self.scene.ground[i] = self.scene.ground[i + 1]
                            self.scene.sky[i] = self.scene.sky[i + 1]
                        self.scene.ground[self.scene.ground.__len__() - 1] = tg
                        self.scene.sky[self.scene.sky.__len__() - 1] = ts
                        for i in range(self.Sucker.__len__()):
                            self.Sucker[i].location.x -= 1
                            if self.Sucker[i].location.x < 0:
                                self.Sucker[i].location.x += 320
                        if self.scene.padLocation.x > -100:
                            self.scene.padLocation.x -= 1
                            if self.scene.padLocation.x < 0:
                                self.scene.padLocation.x += 320
                        if self.scene.fuelLocation.x > -100:
                            self.scene.fuelLocation.x -= 1
                            if self.scene.fuelLocation.x < 0:
                                self.scene.fuelLocation.x += 320
                        self.ship.location.x -= 1
                        if self.ship.location.x < 0:
                            self.ship.location.x += 320
                # If MultiKey(FB.SC_F10) And self.tic > 60 Then
                if ctx.action_edit and self.tic > 60:
                    ctx.sound_unpause()  # SoundManager.instance.UnPause();
                    self.status = RedcrabLander.game_status.GS_START
                    self.tic = 0
                    self.SaveLevel(self.safeland, self.sublevelx, self.sublevely)
                #  DRAW GROUND
                if self.bm == 1:
                    if 0 <= int(self.xm) < 320:
                        self.scene.ground[int(self.xm)] = int(240 - self.ym)
                        if self.scene.ground[int(self.xm)] < 20:
                            self.scene.ground[int(self.xm)] = -20
                        if self.scene.ground[int(self.xm)] > 220:
                            self.scene.ground[int(self.xm)] = 220
                        if self.scene.ground[int(self.xm)] > self.scene.sky[int(self.xm)]:
                            self.scene.sky[int(self.xm)] = self.scene.ground[int(self.xm)]
                #  DRAW SKY
                if self.bm == 2:
                    if 0 <= int(self.xm) < 320:
                        self.scene.sky[int(self.xm)] = int(240 - self.ym)
                        if self.scene.sky[int(self.xm)] < 20:
                            self.scene.sky[int(self.xm)] = 20
                        if self.scene.sky[int(self.xm)] > 220:
                            self.scene.sky[int(self.xm)] = 250
                        if self.scene.ground[int(self.xm)] > self.scene.sky[int(self.xm)]:
                            self.scene.ground[int(self.xm)] = self.scene.sky[int(self.xm)]
                if self.status == RedcrabLander.game_status.GS_EDIT_TEXT:  # change text
                    if st != "":
                        isBackSpace = ctx.action_key_backspace
                        isEnter = (st == '\n' or st == '\r')
                        isCharacter = not isBackSpace and not isEnter
                        if isCharacter:
                            self.msg[self.safeland] += st
                        if isBackSpace:
                            self.msg[self.safeland] = self.msg[self.safeland][:-1]
                        if isEnter:
                            self.status = RedcrabLander.game_status.GS_EDIT
                else:
                    #  SWITCH TO EDIT LEVEL MESSAGE MODE
                    if ctx.action_key_backspace:  # == '\b':
                        self.status = RedcrabLander.game_status.GS_EDIT_TEXT
                    #  INSERT LAND PAD
                    if st == " " and not ctx.action_key_lshift:  # !Input.GetKey(KeyCode.LeftShift))
                        self.xm = np.clip(self.xm, 10, 309)
                        self.scene.padLocation.x = self.xm
                        self.scene.padLocation.y = 240 - self.ym
                        for i in range(int(self.xm - 10), int(self.xm + 11)):
                            self.scene.ground[i] = self.scene.padLocation.y
                    #  INSERT FUEL PAD
                    # If st = " " And MultiKey(FB.SC_LSHIFT) Then
                    if st == " " and ctx.action_key_lshift:  # Input.GetKey(KeyCode.LeftShift))
                        self.xm = np.clip(self.xm, 10, 309)
                        self.scene.fuelLocation.x = self.xm
                        self.scene.fuelLocation.y = 240 - self.ym
                        for i in range(int(self.xm - 10), int(self.xm + 11)):
                            self.scene.ground[i] = self.scene.fuelLocation.y
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
                        self.sublevely += 1
                    if st == "B":
                        self.sublevely -= 1
                    if st == "L":
                        self.sublevelx -= 1
                    if st == "R":
                        self.sublevelx += 1
                    #  SWITCH TO ONE LEVEL MORE
                    if st == "+" and self.safeland < 22:
                        self.safeland += 1
                    #  SWITCH TO ONE LEVEL LESS
                    if st == "-" and self.safeland >= 0:
                        self.safeland -= 1
                    #  SAVE LEVEL
                    if self.tic > 60 and ctx.action_key_f2:  # Input.GetKey(KeyCode.F2)
                        self.tic = 0
                        self.SaveLevel(self.safeland, self.sublevelx, self.sublevely)
                    #  LOAD LEVEL
                    if self.tic > 60 and ctx.action_key_f3:  # Input.GetKey(KeyCode.F3)
                        self.tic = 0
                        self.SaveLevel(999)
                        self.ship.init()
                        if self.sublevelx == 0 and self.sublevely == 0:
                            if self.LoadLevel(self.safeland) == 0:
                                self.LoadLevel(999)
                        else:
                            if self.LoadLevel(self.safeland, self.sublevelx, self.sublevely) == 0:
                                self.LoadLevel(999)
                    #  ALLOW / DISALLOW TAKE OFF after landing
                    if self.tic > 60 and ctx.action_key_f5:  # Input.GetKey(KeyCode.F5)
                        self.scene.allowtakeoff = 1 if self.scene.allowtakeoff == 0 else 0
                        self.tic = 0
                    #  REMOVE LANDPAD
                    if ctx.action_key_f6:
                        self.scene.padLocation.x = -100
                    #  REMOVE FUELPAD
                    if ctx.action_key_f7:
                        self.scene.fuelLocation.x = -100
                    #  GENERATE LEVEL
                    if self.tic > 3 and ctx.action_key_f4:
                        self.tic = 0
                        self.scene.init(self.safeland)
                    #  ADD ONE MORE ENERGY SUCKET AT MOUSE POSITION
                    if self.tic > 15 and ctx.action_key_insert:
                        self.tic = 0
                        self.nbSucker += 1
                        self.Sucker[self.nbSucker - 1].location.x = self.xm
                        self.Sucker[self.nbSucker - 1].location.y = 240.0 - self.ym
                    #  REMOVE LAST ADDED ENERGY SUCKER
                    if self.tic > 15 and ctx.action_key_delete:
                        self.tic = 0
                        if self.nbSucker > 0:
                            self.nbSucker -= 1
                    #  ADD MORE FUEL
                    if self.tic > 3 and ctx.action_key_pageup:
                        self.tic = 0
                        if self.ship.fuel < 100:
                            self.ship.fuel += 1
                    #  REMOVE FUEL
                    if self.tic > 3 and ctx.action_key_pagedown:
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
            if self.status == RedcrabLander.game_status.GS_RUN:
                if self.ship.fuel <= 0:
                    if self.scene.gravity < 0.0025:
                        self.scene.gravity = 0.0025
                if self.playerAct == RedcrabLander.player_action.PA_PAUSE and self.tic > 30:
                    self.status = RedcrabLander.game_status.GS_PAUSE
                    self.playerAct = RedcrabLander.player_action.PA_NOTHING
                    ctx.sound_pause()  # SoundManager.instance.Pause()
                    self.tic = 0
                if self.playerAct == RedcrabLander.player_action.PA_THRUST:
                    self.ship.status = RedcrabLander.lander_status.LS_THRUST
                else:
                    if self.ship.status != RedcrabLander.lander_status.LS_CRASH:
                        self.ship.status = RedcrabLander.lander_status.LS_NORMAL
                if self.playerAct == RedcrabLander.player_action.PA_LEFT and self.ship.fuel > 0:
                    self.ship.angle -= np.pi / 180
                if self.playerAct == RedcrabLander.player_action.PA_RIGHT and self.ship.fuel > 0:
                    self.ship.angle += np.pi / 180
                if self.ship.angle > np.pi:
                    self.ship.angle -= 2 * np.pi
                if self.ship.angle < -np.pi:
                    self.ship.angle += 2 * np.pi
                if self.playerAct == RedcrabLander.player_action.PA_THRUST and self.ship.fuel > 0:
                    self.ship.Speed.x += math.sin(self.ship.angle) * 0.03
                    self.ship.Speed.y += math.cos(self.ship.angle) * 0.03
                    if self.tic % 4 == 0:
                        self.ship.fuel -= 1
                self.ship.Speed.y -= self.scene.gravity
                self.ship.location.x += self.ship.Speed.x
                self.ship.location.y += self.ship.Speed.y

                if self.ship.location.x < 0:
                    if self.scene.go_left != 0:
                        if self.LoadLevel(self.safeland, self.sublevelx - 1, self.sublevely) != 0:
                            self.sublevelx -= 1
                            self.ship.location.x = 320 - 5
                        else:
                            self.ship.location.x = 0
                            self.ship.Speed.x = -self.ship.Speed.x / 2.0
                    else:
                        self.ship.location.x = 0
                        self.ship.Speed.x = -self.ship.Speed.x / 2.0
                if self.ship.location.x >= 319:
                    if self.scene.go_right != 0:
                        if self.LoadLevel(self.safeland, self.sublevelx + 1, self.sublevely) != 0:
                            self.sublevelx += 1
                            self.ship.location.x = 5
                        else:
                            self.ship.location.x = 319
                            self.ship.Speed.x = -self.ship.Speed.x / 2.0
                    else:
                        self.ship.location.x = 319
                        self.ship.Speed.x = -self.ship.Speed.x / 2.0
                if self.ship.location.y < 20:
                    if self.scene.go_down != 0:
                        if self.LoadLevel(self.safeland, self.sublevelx, self.sublevely - 1) != 0:
                            self.sublevely -= 1
                            self.ship.location.y = 240 - 5
                        else:
                            self.ship.location.y = 20
                            self.ship.Speed.y = -self.ship.Speed.y / 2.0
                    else:
                        self.ship.location.y = 20
                        self.ship.Speed.y = -self.ship.Speed.y / 2.0
                if self.ship.location.y > 240:
                    if self.scene.go_up != 0:
                        if self.LoadLevel(self.safeland, self.sublevelx, self.sublevely + 1) != 0:
                            self.sublevely += 1
                            self.ship.location.y = 25
                        else:
                            self.ship.location.y = 239
                            self.ship.Speed.y = -self.ship.Speed.y / 2.0
                    else:
                        self.ship.location.y = 239
                        self.ship.Speed.y = -self.ship.Speed.y / 2.0
                if self.ship.location.y <= self.scene.ground[int(self.ship.location.x)] + self.ship.size * 0.80 or \
                        self.ship.location.y >= self.scene.sky[int(self.ship.location.x)] - self.ship.size * 0.80:
                    speed = int(self.ship.Speed.x ** 2 + self.ship.Speed.y ** 2) * 1000
                    angle = int(abs(self.ship.angle / (np.pi / 180)))
                    if (speed <= 60 and angle < 10 and
                        self.ship.location.y <= self.scene.ground[
                            int(self.ship.location.x)] + self.ship.size * 0.80) and \
                            ((self.scene.padLocation.x - 10 < self.ship.location.x < self.scene.padLocation.x + 10) or
                             (self.scene.fuelLocation.x - 10 < self.ship.location.x < self.scene.fuelLocation.x + 10)):
                        if self.scene.padLocation.x - 10 < self.ship.location.x < self.scene.padLocation.x + 10:
                            self.safeland += 1
                            self.score += int(self.ship.fuel)
                            self.ship.status = RedcrabLander.lander_status.LS_LANDED
                            if self.scene.sky[int(self.ship.location.x)] <= 240 or self.scene.allowtakeoff == 0:
                                self.ship.status = RedcrabLander.lander_status.LS_LANDED_NOSKY
                            if self.safeland >= 23:
                                self.status = RedcrabLander.game_status.GS_FINISH
                            else:
                                ctx.sound_play_landed()  # SoundManager.instance.PlaySingle(ctx.dl.landedSound)
                                self.status = RedcrabLander.game_status.GS_LANDED
                            self.tic = 0
                        else:
                            if self.tic % 3 == 0 and self.ship.fuel < 100:
                                self.ship.fuel += 1
                            self.ship.location.y = self.scene.ground[int(self.ship.location.x)] + self.ship.size * 0.80
                    else:
                        self.status = RedcrabLander.game_status.GS_CRASHED
                        self.ship.status = RedcrabLander.lander_status.LS_CRASH
                        ctx.sound_play_explosion()  # SoundManager.instance.PlaySingle(ctx.dl.crashSound)
                        if self.life == 0:
                            self.status = RedcrabLander.game_status.GS_GAMEOVER
                            ctx.sound_play_gameover()  # SoundManager.instance.PlaySingle(ctx.dl.gameOverSound,1,0.25f)
                        else:
                            self.life -= 1
                        self.tic = 0
                    self.tic2 = 0
                    self.ship.Speed.x = 0
                    self.ship.Speed.y = 0
            self.Draw(ctx)

            if ctx.action_quit:
                if self.bestscore < self.score:
                    self.bestscore = self.score
                    self.bestsafeland = self.safeland
                    try:
                        fi = open(RedcrabLander.data_path + "LANDER.SCO", "wt")
                        print(self.bestscore, file=fi)
                        print(self.bestsafeland, file=fi)
                        fi.close()
                    except Exception as n:
                        print(n)
                self.safeland = 99
                self.tic = 0
                self.showMessage = True
                return False
            return True

        def LoadLevel(self, lvl, sublvlx=-100, sublvly=-100):
            vv = "." + str(sublvlx) + "." + str(sublvly)
            if sublvlx <= -100 and sublvly <= -100:
                vv = ".0.0"
            levelFilename = RedcrabLander.data_path + "l" + str(lvl) + vv + ".lvl"
            if os.path.exists(levelFilename):
                fi = open(levelFilename)
            else:
                return 0
            # Check file structure version
            vv = fi.readline().rstrip('\n')
            if vv != "version=1":
                fi.close()
                return 0
            for i in range(320):
                self.scene.sky[i] = float(fi.readline())
                self.scene.ground[i] = float(fi.readline())
            self.scene.go_up = int(fi.readline())
            self.scene.go_down = int(fi.readline())
            self.scene.go_left = int(fi.readline())
            self.scene.go_right = int(fi.readline())
            self.scene.inverse = int(fi.readline())
            self.scene.allowtakeoff = int(fi.readline())
            self.scene.landedmsg = fi.readline().rstrip('\n')
            #  get pad location
            self.scene.padLocation.x = float(fi.readline())
            self.scene.padLocation.y = float(fi.readline())
            #  get fuel location
            self.scene.fuelLocation.x = float(fi.readline())
            self.scene.fuelLocation.y = float(fi.readline())
            #  get gravity
            self.scene.gravity = float(fi.readline())
            if (sublvlx <= -100 and sublvly <= -100) or self.status == RedcrabLander.game_status.GS_EDIT or \
                    self.status == RedcrabLander.game_status.GS_EDIT_TEXT:
                #  get lander location
                self.ship.location.x = float(fi.readline())
                self.ship.location.y = float(fi.readline())
                self.scene.startLocation.x = self.ship.location.x
                self.scene.startLocation.y = self.ship.location.y
                #  get lander speed
                self.ship.Speed.x = float(fi.readline())
                self.ship.Speed.y = float(fi.readline())
                #  get lander angle
                self.ship.angle = float(fi.readline())
                #  get fuel
                self.ship.fuel = int(fi.readline())
            else:
                #  read ship info to ignore
                for _ in range(6):
                    fi.readline()
            #  get enemies quantity of "Energy sucker"
            self.nbSucker = int(fi.readline())
            for i in range(self.nbSucker):
                #  get enemy location
                self.Sucker[i].location.x = float(fi.readline())
                self.Sucker[i].location.y = float(fi.readline())
            # get message of level

            if 0 <= lvl < self.msg.__len__():
                self.msg[lvl] = fi.readline().rstrip('\n')
            fi.close()
            return 1

        def SaveLevel(self, lvl, sublvlx=-100, sublvly=-100):
            vv = "." + str(sublvlx) + "." + str(sublvly)
            if sublvlx <= -100 and sublvly <= -100:
                vv = ".0.0"
            levelFilename = RedcrabLander.data_path + "l" + lvl + vv + ".lvl"
            if os.path.exists(levelFilename):
                fi = open(levelFilename, "wt")
            else:
                return 0
            print("version=1", file=fi)

            for i in range(320):
                print(self.scene.sky[i], file=fi)
                print(self.scene.ground[i], file=fi)
            print(self.scene.go_up, file=fi)
            print(self.scene.go_down, file=fi)
            print(self.scene.go_left, file=fi)
            print(self.scene.go_right, file=fi)
            print(self.scene.inverse, file=fi)
            print(self.scene.allowtakeoff, file=fi)
            print(self.scene.landedmsg, file=fi)
            #  put pad location
            print(self.scene.padLocation.x, file=fi)
            print(self.scene.padLocation.y, file=fi)
            #  put fuel location
            print(self.scene.fuelLocation.x, file=fi)
            print(self.scene.fuelLocation.y, file=fi)
            # put gravity
            print(self.scene.gravity, file=fi)
            #  put lander location
            print(int(self.ship.location.x * 1000.0) / 1000.0, file=fi)
            print(int(self.ship.location.y * 1000.0) / 1000.0, file=fi)
            #  put lander speed
            print(int(self.ship.Speed.x * 100000.0) / 100000.0, file=fi)
            print(int(self.ship.Speed.y * 100000.0) / 100000.0, file=fi)
            #  put lander angle
            print(self.ship.angle, file=fi)
            #  put fuel
            print(self.ship.fuel, file=fi)
            #  put enemies quantity of "Energy sucker"
            print(self.nbSucker)
            for i in range(self.nbSucker):
                print(self.Sucker[i].location.x, file=fi)
                print(self.Sucker[i].location.y, file=fi)
            # put message of level
            if 0 <= lvl < self.msg.__len__():
                print(self.msg[lvl], file=fi)
            else:
                print("Msg" + str(lvl), file=fi)
            fi.close()
            return 1

        def showmessage(self, ctx):
            if self.showMessageHelp and self.showMessage:
                m = ("EDITOR COMMAND",
                     "--------------",
                     " F1 .....................: This help",
                     " F2 .....................: Save current Level",
                     " F3 .....................: Load current Level",
                     " F4 .....................: Generate a Lanscape (current level)",
                     " F5 .....................: Allow/disallow launch after landing (end level anim)",
                     " F6 .....................: Remove landpad",
                     " F7 .....................: Remove fuelpad",
                     " F10 ....................: Enter / Leave Level Editor",
                     " INSERT .................: Add an Energy Sucker at mouse position",
                     " DELETE .................: Remove Last Added Energy Sucker",
                     " HOME/END ...............: + / - Gravity",
                     " PGUP/DOWN ..............: + / - Energy",
                     " SPACE ..................: Place Land Pad at mouse position",
                     " SHIFT + SPACE ..........: Place Energy Reload Pad at mouse position",
                     " BACK-SPC ...............: Enter Title Edit Mode",
                     " ENTER ..................: Valid Title(Edit Mode)",
                     " LEFT/RIGHT/UP/DOWN .....: Move Lander",
                     " LEFT Sft+LEFT/RIGHT ....: Rotate Lander",
                     " CTRL+UP/DOWN/LEFT/RIGHT : Shift landscape ",
                     " t,b,l,r ................: allow/disallow sublevel top/bottom/left/right",
                     " T,B,L,R ................: move to sublevel top/bottom/left/right",
                     " + / - ..................: Change Level Up/Down",
                     " LEFT MOUSE BUTTON ......: Draw Ground (slowy please to avoid picks)",
                     " RIGHT MOUSE BUTTON .....: Draw Sky (slowy please to avoid picks)",
                     " ",
                     " Auto-save level when leaving Editor (F10)",
                     " Auto-load level when entering Editor (F10)",
                     " ",
                     " TIP : You may use Landscape generator (F4) and use the land pad command",
                     "  (keep space key down) and move mouse to have a quick landscape design",
                     "",
                     "Press Any Key to continue")
            else:
                messageFilename = RedcrabLander.data_path + "m" + str(self.safeland) + ".lvl"
                if os.path.exists(messageFilename):
                    fi = open(messageFilename)
                    m = fi.readlines()
                    fi.close()
                else:
                    self.tic = 0
                    self.showMessage = self.showMessageHelp = False
                    return
            lmax = 0
            for aline in m:
                lmax = aline.__len__() if aline.__len__() > lmax else lmax
            ctx.Cls()
            ctx.text.scaleRot(4.0 * ctx.KW, 0)
            i = 0
            colour = 10
            for aline in m:
                if not self.showMessageHelp:
                    tt = int(self.tic/2)
                    colour = 10
                    if int(tt / lmax) == (i+1):
                        aline = aline[:tt % lmax]
                        colour = 15
                    elif int(tt / lmax) < (i+1):
                        aline = ""
                aline = " " + aline + (" " * (lmax - aline.__len__()))
                if self.showMessageHelp:
                    ctx.smalltxt.drawText(ctx, aline, ctx.G_WIDTH / 2.0, (i * 4.5 + 6.0) * ctx.KH, 10)
                else:
                    ctx.text.drawText(ctx, aline.rstrip('\n'), ctx.G_WIDTH / 2.0, (i * 9.0 + 6.0) * ctx.KH, colour)
                i += 1
            self.tic += 1
            if self.tic > ctx.fps * 25 or (ctx.anyKey() and self.tic > ctx.fps * 3):
                self.tic = 0
                self.showMessage = self.showMessageHelp = False
            return

    class VectrexMemory:
        def __init__(self):
            self.p1 = pg.math.Vector2(0, 0)
            self.p2 = pg.math.Vector2(0, 0)
            self.colour = pg.Color(0, 0, 0)

    class GameContext:
        def __init__(self):
            self.data_path = "data/"
            self.action_mouse_button1 = False
            self.action_mouse_button2 = False
            self.action_mouse_button3 = False
            self.action_mouse_position_y = 0
            self.action_mouse_position_x = 0
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
            self.action_key_pagedown = False
            self.action_key_pageup = False
            self.action_key_end = False
            self.action_key_home = False
            self.action_key_downarrow = False
            self.action_key_uparrow = False
            self.action_key_rightarrow = False
            self.action_key_leftarrow = False
            self.action_key_shit = False
            self.action_key_rshit = False
            self.action_key_lshift = False
            self.action_key_ctrl = False
            self.action_key_rctrl = False
            self.action_key_lctrl = False
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
            pg.display.set_caption('Redcrab Lander')
            self.circleSeg = 16
            self.inkey = ""
            self.Vmem = tuple(RedcrabLander.VectrexMemory() for _ in range(10000))
            self.VmemSize = 0
            self.text = RedcrabLander.TinyVectrex()
            self.boardtxt = RedcrabLander.TinyVectrex()
            self.text2 = RedcrabLander.TinyVectrex()
            self.smalltxt = RedcrabLander.TinyVectrex()
            self.bigtxt = RedcrabLander.TinyVectrex()
            self.palette = (
                pg.Color("black"), pg.Color("blue"), pg.Color("green"), pg.Color("cyan"), pg.Color("red"),
                pg.Color("magenta"), pg.Color("yellow"), pg.Color("white"),
                pg.Color("grey"), pg.Color("blue"), pg.Color("green"), pg.Color("cyan"), pg.Color("red"),
                pg.Color("magenta"), pg.Color("yellow"), pg.Color("white"))
            self.sound = (
                pg.mixer.Sound(RedcrabLander.data_path + "andrea-baroni.ogg"),
                pg.mixer.Sound(RedcrabLander.data_path + "game_over.ogg"),
                pg.mixer.Sound(RedcrabLander.data_path + "thrust.ogg"),
                pg.mixer.Sound(RedcrabLander.data_path + "explosion.ogg"),
                pg.mixer.Sound(RedcrabLander.data_path + "landed.ogg"),
                pg.mixer.Sound(RedcrabLander.data_path + "SE-Gun-001.ogg")
            )
            self.music_channel = None
            self.KW = self.G_WIDTH / 320.0
            self.KH = self.G_HEIGHT / 240.0
            self.smalltxt.scaleRot(2 * self.KW, 0)
            self.bigtxt.scaleRot(5 * self.KW, 0)
            self.text.scaleRot(4 * self.KW, 0)
            self.text2.scaleRot(4 * self.KW, 0)
            self.boardtxt.scaleRot(3.5 * self.KW, 0)
            self.boardtxt.setCenterText(0)

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

        def sound_play_gameover(self):
            self.sound[1].play()

        def sound_play_thrust(self):
            self.sound[2].play()

        def sound_play_explosion(self):
            self.sound[3].play()

        def sound_play_landed(self):
            self.sound[4].play()

        def sound_play_title(self):
            self.sound[5].play()

        def Line(self, x1, y1, x2, y2, colour):
            if self.VmemSize >= self.Vmem.__len__():
                print("Out of Vertex memory (max " + str(self.VmemSize) + ")")
                return
            self.Vmem[self.VmemSize].p1.x = float(x1)
            self.Vmem[self.VmemSize].p1.y = float(y1)
            if x1 == x2 and y1 == y2:
                self.Vmem[self.VmemSize].p2.x = float(x2) + 1  # self.pixelSize.x
                self.Vmem[self.VmemSize].p2.y = float(y2)
            else:
                self.Vmem[self.VmemSize].p2.x = float(x2)
                self.Vmem[self.VmemSize].p2.y = float(y2)
            self.Vmem[self.VmemSize].colour = self.palette[colour]
            self.VmemSize += 1

        def LineBF(self, x1, y1, x2, y2, colour):
            self.LineB(x1, y1, x2, y2, colour)
            xx1 = x1 if (x1 < x2) else x2
            xx2 = x2 if (x1 < x2) else x1
            yy1 = y1 if (y1 < y2) else y2
            yy2 = y2 if (y1 < y2) else y1
            yy = yy1
            while yy <= yy2:
                self.Line(xx1, yy, xx2, yy, colour)
                yy += 1

        def LineB(self, x1, y1, x2, y2, colour):
            self.Line(x1, y1, x2, y1, colour)
            self.Line(x1, y2, x2, y2, colour)
            self.Line(x1, y1, x1, y2, colour)
            self.Line(x2, y1, x2, y2, colour)

        def Circle(self, x, y, radius, colour):
            # double x1, y1, x2, y2, angle1, angle2, deltaAngle;

            deltaAngle = np.pi * 2 / self.circleSeg
            for i in range(self.circleSeg):
                angle1 = deltaAngle * i
                angle2 = angle1 + deltaAngle
                x1 = x + math.cos(angle1) * radius
                y1 = y + math.sin(angle1) * radius
                x2 = x + math.cos(angle2) * radius
                y2 = y + math.sin(angle2) * radius
                self.Line(x1, y1, x2, y2, colour)

        def Cls(self):
            self.VmemSize = 0

        def anyKey(self):  # return True or False
            return self.action_key_any

        def input(self):
            self.inkey = ""
            self.action_quit = False
            self.last_event = None
            for self.last_event in pg.event.get():
                if self.last_event.type == QUIT or \
                        (self.last_event.type == KEYDOWN and self.last_event.key == K_ESCAPE):
                    self.action_quit = True
                if self.last_event.type == KEYDOWN or self.last_event.type == KEYUP:
                    self.action_key_any = self.last_event.type == KEYDOWN
                    self.action_key_lctrl = (self.last_event.mod | KMOD_LCTRL) != 0
                    self.action_key_rctrl = (self.last_event.mod | KMOD_RCTRL) != 0
                    self.action_key_ctrl = (self.last_event.mod | KMOD_CTRL) != 0
                    self.action_key_lshift = (self.last_event.mod | KMOD_LSHIFT) != 0
                    self.action_key_rshit = (self.last_event.mod | KMOD_RSHIFT) != 0
                    self.action_key_shit = (self.last_event.mod | KMOD_SHIFT) != 0
                    if self.last_event.key == K_LEFT:
                        self.action_rotate_left = self.last_event.type == KEYDOWN
                        self.action_key_leftarrow = self.action_rotate_left
                    elif self.last_event.key == K_RIGHT:
                        self.action_rotate_right = self.last_event.type == KEYDOWN
                        self.action_key_rightarrow = self.action_rotate_right
                    elif self.last_event.key == K_UP:
                        self.action_thrust = self.last_event.type == KEYDOWN
                        self.action_key_uparrow = self.action_thrust
                    elif self.last_event.key == K_DOWN:
                        self.action_key_downarrow = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_HOME:
                        self.action_key_home = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_END:
                        self.action_key_end = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_PAGEUP:
                        self.action_key_pageup = self.last_event.type == KEYDOWN
                    elif self.last_event.key == K_PAGEDOWN:
                        self.action_key_pagedown = self.last_event.type == KEYDOWN
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
                        self.inkey = self.last_event.unicode
                        print("Event key down", self.inkey, ", object", self.last_event)
                elif self.last_event.type == MOUSEMOTION or \
                        self.last_event.type == MOUSEBUTTONUP or \
                        self.last_event.type == MOUSEBUTTONDOWN:
                    self.action_mouse_position_x = self.last_event.pos[0]
                    self.action_mouse_position_y = self.last_event.pos[1]
                    if self.last_event.type == MOUSEMOTION:
                        self.action_mouse_button1 = self.last_event.buttons[0] != 0
                        self.action_mouse_button2 = self.last_event.buttons[1] != 0
                        self.action_mouse_button3 = self.last_event.buttons[2] != 0
                    elif self.last_event.type == MOUSEBUTTONDOWN:
                        if self.last_event.button == 1:
                            self.action_mouse_button1 = True
                        elif self.last_event.button == 2:
                            self.action_mouse_button2 = True
                        elif self.last_event.button == 3:
                            self.action_mouse_button3 = True
                    elif self.last_event.type == MOUSEBUTTONUP:
                        if self.last_event.button == 1:
                            self.action_mouse_button1 = False
                        elif self.last_event.button == 2:
                            self.action_mouse_button2 = False
                        elif self.last_event.button == 3:
                            self.action_mouse_button3 = False

        def render(self):
            self.screen.fill(pg.Color(192, 192, 192), special_flags=BLEND_RGB_MULT)
            maxVM = self.VmemSize
            iVM = 0
            for vm in self.Vmem:
                if iVM >= maxVM:
                    break
                pg.draw.aaline(self.screen, vm.colour, vm.p1, vm.p2)
                iVM += 1
            pg.display.update()
            self.clock.tick(int(self.fps))

    data_path = "data/"

    def __init__(self):
        self.fps = 50.0
        self.run = True
        self.agame = RedcrabLander.game()
        self.gamectx = RedcrabLander.GameContext()
        self.timer = 0.0
        self.gamectx.fps = self.fps
        print("Lander  Started")
        self.gamectx.sound_play_score()
        # SoundManager.instance.Noise(thrustSound);

    def play(self):
        self.run = True
        while self.run or self.agame.showMessage:
            self.gamectx.input()
            if self.agame.showMessage:
                self.agame.showmessage(self.gamectx)
            else:
                self.run = self.agame.tick(self.gamectx)
            self.gamectx.render()
        pg.quit()


if __name__ == '__main__':
    print("Get ready")
    RedcrabLander().play()
    print("Bye bye")
