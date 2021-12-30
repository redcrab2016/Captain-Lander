using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Text;
using UnityEngine;
using Random = System.Random;

public class DrawLines : MonoBehaviour
{

    class TV_Polar2D
    {
        public double radius = 0;
        public double angle = 0;
    }

    class TV_vertex2D
    {
        public double x = 0;
        public double y = 0;
    }

    class TinyVectrex
    {
        public double boom = 0;
        public TV_Polar2D[] plot = {new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(),
                                    new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(),
                                    new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D(), new TV_Polar2D() };
        public TV_vertex2D[] plotxy = {new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(),
                                    new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(),
                                    new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D(), new TV_vertex2D() };
        public double size = 0;
        public double angle = 0;
        public double cx = 0;
        public string[] alphabet = new string[356];

        public int asc(String s)
        {
            if (s == null) return 0;
            return (int)Encoding.ASCII.GetBytes(s)[0];
        }

        public TinyVectrex()
        {
            double i; // Dim i As Double
            int j; // Dim j As Integer
            //int k; // Dim k As Integer
            //int x, y; // dim As Integer x, y
            boom = 1;
            setCenterText(0.5);
            j = 0;
            this.plot[j].angle = 0; this.plot[j].radius = 0; // this.plot(j) = Type<TV_Polar2D>(0, 0)
            j += 1;
            for (i = 0; i <= 2 * Math.PI - Math.PI / 4; i += Math.PI / 4) // For i = 0 To 2 * PI - PI / 4 Step PI/ 4
            {
                this.plot[j].radius = 1; this.plot[j].angle = i; // this.plot(j) = Type<TV_Polar2D>(1, i)
                this.plot[j + 8].radius = Math.Sqrt(2) / 2; this.plot[j + 8].angle = i;//this.plot(j + 8) = Type<TV_Polar2D>(Sqr(2) / 2, i)
                j += 1;
            } // Next
            scaleRot(4, 0);
            //' sign
            this.alphabet[asc("+")] = "PL NJ"; this.alphabet[asc("-")] = "NJ"; this.alphabet[asc("*")] = "OK MQ NJ";
            this.alphabet[asc("/")] = "IE"; this.alphabet[asc(":")] = "PP LL"; this.alphabet[asc("!")] = "PA LL";
            this.alphabet[asc(".")] = "LL"; this.alphabet[asc(",")] = "LD";
            this.alphabet[asc("'")] = "HP"; this.alphabet[asc("(")] = "HGED"; this.alphabet[asc(")")] = "HICD";
            this.alphabet[asc("_")] = "EC";
            this.alphabet[asc("~")] = "2E0D2C 2HCBDFEH";  //'small ship with thrust
            this.alphabet[asc("^")] = "2HCBDFEH"; //' small ship without thrust
            this.alphabet[asc("$")] = "HCBDFEH"; //' normal sized ship
            this.alphabet[asc("&")] = "2HCBDFEH 0BCDEFGHIB"; //' rounded lander
            this.alphabet[asc("#")] = "JKLMNOPQJ BJ CK DL EM FN GO HP IQ"; //' sun
            this.alphabet[asc("~")] = "GICEG BDFHB"; //' star
            this.alphabet[asc("§")] = "0H3I0B3C0D3E0F3G0H 3I0I 3C0C 3E0E 3G0G"; //' Energy sucker
            this.alphabet[asc("%")] = "BHFNECJB"; //' Arrow

            //' Digit
            this.alphabet[asc("0")] = "EIHGEDCI";
            this.alphabet[asc("1")] = "GHL";
            this.alphabet[asc("2")] = "GHIEC";
            this.alphabet[asc("3")] = "GHIACDE";
            this.alphabet[asc("4")] = "LHNJ";
            this.alphabet[asc("5")] = "IGNJCDE";
            this.alphabet[asc("6")] = "IHGEDCJN";
            this.alphabet[asc("7")] = "GIL";
            this.alphabet[asc("8")] = "NGHICDENJ";
            this.alphabet[asc("9")] = "JNGHICDE";
            //' Alphabet Upercase

            this.alphabet[asc("A")] = "ENOPQJC NJ";
            this.alphabet[asc("B")] = "EGPQAKLE NA";
            this.alphabet[asc("C")] = "KLMNOPQ";
            this.alphabet[asc("D")] = "EGPQJKLE";
            this.alphabet[asc("E")] = "IGEC NA";
            this.alphabet[asc("F")] = "IGE NA";
            this.alphabet[asc("G")] = "AJKLMNOPQ";
            this.alphabet[asc("H")] = "GE IC NJ";
            this.alphabet[asc("I")] = "PL";
            this.alphabet[asc("J")] = "QKLM";
            this.alphabet[asc("K")] = "GE NP NC";
            this.alphabet[asc("L")] = "GEC";
            this.alphabet[asc("M")] = "EGAIC";
            this.alphabet[asc("N")] = "EGCI";
            this.alphabet[asc("O")] = "JKLMNOPQJ";
            this.alphabet[asc("P")] = "EGPQAN";
            this.alphabet[asc("Q")] = "AKLMNOPQJK";
            this.alphabet[asc("R")] = "EGPQAN AC";
            this.alphabet[asc("S")] = "QPOKLM";
            this.alphabet[asc("T")] = "PL GI";
            this.alphabet[asc("U")] = "GNMLKJI";
            this.alphabet[asc("V")] = "GLI";
            this.alphabet[asc("W")] = "GEACI";
            this.alphabet[asc("X")] = "GC EI";
            this.alphabet[asc("Y")] = "GAI AL";
            this.alphabet[asc("Z")] = "GIEC";

            //'Alphabet lower case
            this.alphabet[asc("a")] = "1ENOPQJC NJ";
            this.alphabet[asc("b")] = "1EGPQAKLE NA";
            this.alphabet[asc("c")] = "1KLMNOPQ";
            this.alphabet[asc("d")] = "1EGPQJKLE";
            this.alphabet[asc("e")] = "1IGEC NA";
            this.alphabet[asc("f")] = "1IGE NA";
            this.alphabet[asc("g")] = "1AJKLMNOPQ";
            this.alphabet[asc("h")] = "1GE IC NJ";
            this.alphabet[asc("i")] = "1PL";
            this.alphabet[asc("j")] = "1QKLM";
            this.alphabet[asc("k")] = "1GE NP NC";
            this.alphabet[asc("l")] = "1GEC";
            this.alphabet[asc("m")] = "1EGAIC";
            this.alphabet[asc("n")] = "1EGCI";
            this.alphabet[asc("o")] = "1JKLMNOPQJ";
            this.alphabet[asc("p")] = "1EGPQAN";
            this.alphabet[asc("q")] = "1AKLMNOPQJK";
            this.alphabet[asc("r")] = "1EGPQAN AC";
            this.alphabet[asc("s")] = "1QPOKLM";
            this.alphabet[asc("t")] = "1PL GI";
            this.alphabet[asc("u")] = "1GNMLKJI";
            this.alphabet[asc("v")] = "1GLI";
            this.alphabet[asc("w")] = "1GEACI";
            this.alphabet[asc("x")] = "1GC EI";
            this.alphabet[asc("y")] = "1GAI AL";
            this.alphabet[asc("z")] = "1GIEC";
        }

        public void setCenterText(double cenx)
        {
            this.cx = cenx;
        }

        public void scaleRot(double psize, double pangle)
        {
            int i;
            for (i = 0; i < 18; i++)
            {
                plotxy[i].x = psize * Mathf.Cos((float)(pangle + plot[i].angle)) * plot[i].radius;
                plotxy[i].y = psize * Mathf.Sin((float)(pangle + plot[i].angle)) * plot[i].radius;
            }
            size = psize;
            angle = pangle;
        }

        public void drawScript(GameContext ctx, string s, double xc, double yc, int colour)
        {
            drawScript(ctx, s, xc, yc, colour, this.boom);
        }

        public void drawScript(GameContext ctx, string s, double xc, double yc, int colour, double explode)
        {
            int i; // Dim i As Integer
            string ss; // Dim ss As String
            string c; // Dim c As String
            int b; // Dim b As integer
            int a; // Dim a As Integer
            int defaultColour = colour;
            double x, y, xo = 0, yo = 0, x1, y1, x2, y2, xx, yy, k; // Dim As Double x, y, xo, yo, x1, y1, x2, y2, xx, yy, k
            k = 1; b = 0; 
            if (s == null) return;
            ss = " " + s.ToUpper();// UCase(" " + s)
            //int idx; // Dim idx As integer
            for (i = 0; i < ss.Length; i++) // For i = 1 To Len(ss)
            {
                c = ss.Substring(i, 1); // c = Mid(ss, i, 1)
                if (c.Equals("$"))
                {
                    i++;
                    c = ss.Substring(i, 1).ToUpper(); ;
                    a = (int)Encoding.ASCII.GetBytes(c)[0];
                    if ( a >= 48 && a <= 57)
                    {
                        a -= 48;
                    } else if ((a >= 65 && a <= 70))
                    {
                        a -= 55;
                    } else
                    {
                        a = defaultColour;
                    }
                    colour = a;
                }
                else if (c.Equals(" ")) //If c = " " Then
                {
                    b = 1;
                }
                else
                {
                    a = (int)Encoding.ASCII.GetBytes(c)[0]; // a = Asc(c)
                    if (a >= 65 && a < (65 + 17)) //If a>= 65 And a<(65 + 17) Then
                    {
                        a -= 65;
                        if (k == 1) //If k = 1 Then
                        {
                            x = plotxy[a].x + xc;
                            y = plotxy[a].y + yc;
                        }
                        else
                        { // Else
                            x = plotxy[a].x * k + xc;
                            y = plotxy[a].y * k + yc;
                        }
                        if (b == 0) //If b = 0 Then
                        {
                            if (explode == 1) //If explode = 1 Then
                            {
                                ctx.Line(xo, yo, x, y, colour);// Line(xo, yo) - (x, y),colour
                            }
                            else
                            { // Else
                                xx = (xo + x) / 2 - xc; yy = (yo + y) / 2 - yc;
                                xx = xx * explode - xx; yy = yy * explode - yy;
                                x1 = xo + xx; y1 = yo + yy;
                                x2 = x + xx; y2 = y + yy;
                                ctx.Line(x1, y1, x2, y2, colour);// Line(x1, y1) - (x2, y2),colour
                            } // End If
                        } // End If
                        xo = x; yo = y;
                        b = 0;
                    }
                    else
                    { // Else
                        if (a >= 48 && a <= 57) //If a >= 48 And a <= 57 Then
                        {
                            switch (a)  //  Select Case a
                            {
                                case 48:
                                    k = 1;
                                    break;
                                case 49:
                                    k = 0.70710678118654752440084436210485;
                                    break;
                                default:
                                    k = Math.Pow(0.70710678118654752440084436210485, (a - 48));
                                    break;
                            } // End Select
                        } // EndIf
                    } // EndIf
                } // EndIf
            } // Next i
        }

        public void drawText(GameContext ctx, string s, double xc, double yc, int colour)
        {
            drawText(ctx, s, xc, yc, colour, this.angle);
        }

        public void drawText(GameContext ctx, string s, double xc, double yc, int colour, double txtAngle)
        {
            int i; // Dim i As Integer
            int a; // Dim a As Integer
            double c; // Dim c As integer
            double dx, dy; // Dim As Double dx, dy
            c = (double)(s.Length * this.cx); // c = Int(Len(s) * this.cx)
            dx = this.size * Math.Cos(txtAngle) * 1.80;
            dy = this.size * Math.Sin(txtAngle) * 1.80;
            for (i = 0; i < s.Length; i++) // For i = 1 To Len(s)
            {
                a = (int)Encoding.ASCII.GetBytes(s.Substring(i, 1))[0]; //a = Asc(Mid(s, i, 1))
//                this.drawScript(ctx, alphabet[a], (xc + dx * (i - 1 - c)), (yc + dy * (i - 1 - c)), colour);
                this.drawScript(ctx, alphabet[a], (xc + dx * (i - c)), (yc + dy * (i - c)), colour);
            } // Next
        }
    }

    enum game_status
    {
        GS_START = 0,
        GS_INTRO,
        GS_RUN,
        GS_PAUSE,
        GS_CRASHED,
        GS_LANDED,
        GS_GAMEOVER,
        GS_FINISH,
        GS_EDIT,
        GS_EDIT_TEXT
    }

    enum player_action
    {
        PA_NOTHING = 0,
        PA_LEFT,
        PA_RIGHT,
        PA_THRUST,
        PA_QUIT,
        PA_PAUSE,
    }

    enum lander_status
    {
        LS_NORMAL = 0,
        LS_THRUST,
        LS_LANDED,
        LS_LANDED_NOSKY,
        LS_CRASH
    }

    enum EnergySucker_Status
    {
        SS_NORMAL = 0,
        SS_EXPLODED
    }

    class Vertex2D
    {
        public double x = 0;
        public double y = 0;
    }

    class Lander
    {
        const string LANDER_NORMAL = "$F2HCBDFEH";
        const string LANDER_LANDED = "$F2HCBDFEH";
        const string LANDER_THRUST = "$E2E0D2C$$ $F2HCBDFEH";
        public TinyVectrex model = new TinyVectrex();
        public Vertex2D location = new Vertex2D();
        public Vertex2D Speed = new Vertex2D();
        public double fuel = 0;
        public double angle = 0;
        public double size = 0;
        public lander_status status = lander_status.LS_NORMAL;
        public int crash_tic = 0;
        public int noise_tic = 0;
        public int tic = 0;
        public Lander()
        {
            this.init();
        }

        public Lander(double x, double y)
        {
            this.init();
            this.location.x = x;
            this.location.y = y;
        }

        public void init()
        {
            this.location.x = 160;
            this.location.y = 230;
            this.fuel = 100;
            this.angle = 0;
            this.size = 7;
            this.status = lander_status.LS_NORMAL; //  LS_NORMAL
            this.crash_tic = 0;
            this.tic = 0;
            this.noise_tic = 0;
            this.model.boom = 1;
        }

        public void Draw(GameContext ctx)
        {
            //'	Static tic As Integer
            int v1; //, v2; // Dim As Integer v1, v2
            this.model.scaleRot(this.size * 2 * ctx.KW, this.angle);
            this.tic += 1;
            switch (this.status) //Select Case this.status
            {
                case lander_status.LS_NORMAL:
                    this.crash_tic = 0;
                    this.model.boom = 1;
                    this.model.drawScript(ctx, LANDER_NORMAL, (this.location.x * ctx.KW), ((240 - this.location.y) * ctx.KH), 10);
                    if (this.fuel <= 0) //If this.fuel <= 0 then
                    {
                        ctx.smalltxt.drawText(ctx, "I'M CRASHING!", (this.location.x * ctx.KW), ((240 - this.location.y - this.size - 7) * ctx.KH), 15);
                    } //End If
                    break;
                case lander_status.LS_LANDED:
                case lander_status.LS_LANDED_NOSKY:
                    //v1 = rs._channel(1).volume
                    //v1 = v1 - 1
                    //v2 = rs._channel(1).frequency
                    //v2 = v2 - 1
                    //If v2< 30 Then v2 = 30
                    //If v1< 0 Then v1 = 0
                    //rs.keyonoff(1, 15, v2, v1, 100)
                    this.crash_tic = 0;
                    this.model.boom = 1;
                    this.model.drawScript(ctx, LANDER_NORMAL, (this.location.x * ctx.KW), ((240 - this.location.y) * ctx.KH), 10);
                    ctx.Circle(this.location.x * ctx.KW, (240 - this.location.y) * ctx.KH, (this.size + 5 + 3 * Math.Sin(this.tic / 10.0)) * ctx.KW, 8);
                    if (this.fuel >= 70 && this.fuel <= 99)  //if this.fuel >= 70  And this.fuel <= 99 Then
                    {
                        if (this.status == lander_status.LS_LANDED)  //If this.status = LS_LANDED then
                        {
                            ctx.smalltxt.drawText(ctx, "Launch To " + (int)(3 - ((this.fuel - 70.0) / 30 * 4)), (this.location.x * ctx.KW), ((240 - this.location.y - this.size - 7) * ctx.KH), 15);
                        }
                        else
                        { // Else
                            ctx.smalltxt.drawText(ctx, "DAPI Ready !", (this.location.x * ctx.KW), ((240 - this.location.y - this.size - 7) * ctx.KH), 15);
                        } // End If
                    } // End if
                    if (this.fuel >= 100 && this.location.y < 300 && this.status == lander_status.LS_LANDED) //If this.fuel >= 100 And this.location.y < 300 And this.status = LS_LANDED Then
                    {
                        if (this.location.y < 255) //If this.location.y < 255 Then
                        {
                            v1 = (int)(128 - this.location.y / 2);
                        }
                        else
                        { // Else
                            v1 = 0;
                        } // EndIf
                        // rs.keyon(1, 15, this.location.y * 10, v1)
                        this.angle = 0;
                        this.location.y *= 1.01;
                    } // EndIf
                    break;
                case lander_status.LS_CRASH:
                    this.crash_tic += 1;
                    //if (this.crash_tic == 1) SoundManager.instance.PlaySingle(ctx.dl.crashSound);

                    if (this.crash_tic < 60) //If crash_tic< 60 Then
                    {
                        // rs.keyonoff(1, 15, 20 + crash_tic / 10, 255 - 255 * crash_tic / 60, 100)
                        // rs.keyonoff(2, 15, 25 + crash_tic / 10, 255 - 255 * crash_tic / 60, 100)
                        // rs.keyonoff(3, 15, 22 + crash_tic / 10, 255 - 255 * crash_tic / 60, 100)
                        this.model.boom = 1 - crash_tic / 15.0;
                        this.model.drawScript(ctx, LANDER_NORMAL, (this.location.x * ctx.KW), ((240 - this.location.y) * ctx.KH), 10);
                    }
                    else
                    { // Else
                      // rs.keyoff(1):rs.keyoff(2): rs.keyoff(3)
                    } // End if
                    break;
                case lander_status.LS_THRUST:
                    //SoundManager.instance.PlaySingle(ctx.dl.thrustSound);
                    this.noise_tic = 0;
                    SoundManager.instance.NoiseStart();
                    // rs.keyonoff(1, 15, this.fuel * 20, 40, 100)
                    if (tic % 20 < this.fuel / 5 && this.fuel > 0)   //If(tic Mod 20) < this.fuel / 5 And this.fuel > 0 Then
                    {
                        this.model.drawScript(ctx, LANDER_THRUST, (this.location.x * ctx.KW), ((240 - this.location.y) * ctx.KH), 10);
                    }
                    else
                    { // Else
                        this.model.drawScript(ctx, LANDER_NORMAL, (this.location.x * ctx.KW), ((240 - this.location.y) * ctx.KH), 10);
                    } // EndIf
                    break;
            } // End Select
            if (status != lander_status.LS_THRUST)
            {
                this.noise_tic++;
                if (this.noise_tic>5) SoundManager.instance.NoiseStop();
            }
        }
    }

    class EnergySucker
    {
        const string EnergySucker_NORMAL = "$C0H3I0B3C0D3E0F3G0H $E3I0I 3C0C 3E0E 3G0G";
        public TinyVectrex model = new TinyVectrex();
        public Vertex2D location = new Vertex2D();
        public Vertex2D Speed = new Vertex2D();
        public double angle = 0;
        public double size = 0;
        public int tic = 0;
        public EnergySucker_Status status = EnergySucker_Status.SS_NORMAL;

        public EnergySucker()
        {
            this.init();
        }

        public void Draw(GameContext ctx)
        {
            this.tic += 1;
            switch (this.status) //Select Case this.status
            {
                case EnergySucker_Status.SS_NORMAL:
                    this.model.scaleRot(this.size * ctx.KW, this.tic * Math.PI / 90.0);
                    this.model.drawScript(ctx, EnergySucker_NORMAL, (this.location.x * ctx.KW), ((240 - this.location.y) * ctx.KH), 10);
                    break;
                case EnergySucker_Status.SS_EXPLODED:
                    break;
            } // End Select
        }

        public void init()
        {
            this.tic = 0;
            this.status = EnergySucker_Status.SS_NORMAL;
            this.location.x = 0;
            this.location.y = 0;
            this.Speed.x = 0;
            this.Speed.y = 0;
            this.angle = 0;
            this.size = 7;
            this.model.boom = 1;
        }

        public void init(double x, double y)
        {
            this.init();
            this.location.x = x;
            this.location.y = y;
        }
    }

    class Landscape
    {
        public double[] ground = new double[320];
        public double[] sky = new double[320];
        public Vertex2D padLocation = new Vertex2D();
        public Vertex2D fuelLocation = new Vertex2D();
        public double gravity = 0;
        public Vertex2D startLocation = new Vertex2D();
        public int inverse = 0;
        public int tic = 0;
        public int go_up = 0;
        public int go_down = 0;
        public int go_left = 0;
        public int go_right = 0;
        public int allowtakeoff = 0;
        public string landedmsg = "";

        public Landscape()
        {
            this.init();
        }

        public void Draw(GameContext ctx)
        {
            tic++;
            string energy = "Energy";
            int i, lb, ub; //Dim As Integer i, lb, ub
            lb = 0; // lb = LBound(this.ground)
            ub = this.ground.Length - 1; // ub = UBound(this.ground)
            for (i = lb; i < ub; i++) // For i = lb To ub-1
            {
                if (this.ground[i] != this.sky[i] || this.ground[i + 1] != this.sky[i + 1]) //If this.ground(i) <> this.sky(i) or this.ground(i + 1) <> this.sky(i + 1)   Then
                {
                    // PSet(i * KW, (240 - Int(this.ground(i))) * KH),11
                    if (this.ground[i] >= 20 && this.ground[i + 1] >= 20)  //If(this.ground(i) >= 20) and this.ground(i + 1) >= 20 then
                    {
                        ctx.Line(i * ctx.KW, (240 - (int)(this.ground[i])) * ctx.KH, (i + 1) * ctx.KW, (240 - (int)(this.ground[i + 1])) * ctx.KH, 13);
                    } // End if
                    ctx.Line(i * ctx.KW, (240 - (int)(this.sky[i])) * ctx.KH, (i + 1) * ctx.KW, (240 - (int)(this.sky[i + 1])) * ctx.KH, 13);
                } // End if
            } //Next
            ctx.LineBF((int)(this.padLocation.x - 10) * ctx.KW, (240 - (int)(this.padLocation.y)) * ctx.KH, (int)(this.padLocation.x + 10) * ctx.KW, (245 - (int)(this.padLocation.y)) * ctx.KH, 11);
            ctx.smalltxt.drawText(ctx, "DCTSC", ((this.padLocation.x + 1) * ctx.KW), ((240 - this.padLocation.y + 8) * ctx.KH), 11);
            ctx.LineBF((int)(this.fuelLocation.x - 10) * ctx.KW, (240 - (int)(this.fuelLocation.y)) * ctx.KH, (int)(this.fuelLocation.x + 10) * ctx.KW, (245 - (int)(this.fuelLocation.y)) * ctx.KH, 11);
            if (this.tic % 240 < 120)
            {
                energy = "Energy";
            } else
            {
                energy = "Coffee";
            }    
            
            ctx.smalltxt.drawText(ctx, energy, ((this.fuelLocation.x + 1) * ctx.KW), ((240 - this.fuelLocation.y + 8) * ctx.KH), 11);
        }

        public void init()
        {
            this.init(0);
        }

        public void init(int Glevel)
        {
            tic = 0;
            int i, j, k, lb, cnt, ub, level; //Dim As Integer i, j, k, lb, cnt, ub, level
            double cur, prev, slope, delta, mini, maxi, ground; // Dim As Double cur, prev, slope, delta, mini, maxi, ground
            this.gravity = 0.0025 * ((int)(Glevel / 10.0) / 3.0 + 1.0);
            inverse = 0;
            allowtakeoff = 1;
            go_up = 0;
            go_down = 0;
            go_left = 0;
            go_right = 0;
            landedmsg = "LANDED";
            level = Glevel % 10;
            lb = 0; //LBound(this.ground)
            ub = this.ground.Length - 1; // Ubound(this.ground)
            this.startLocation.x = 160;
            this.startLocation.y = 230;
            Random rnd = new Random();
            prev = rnd.NextDouble() * 200 + 20;
            for (i = lb; i <= ub; i++)//For i = lb To ub
            {
                this.sky[i] = 250;
                this.ground[i] = prev;
            } // Next i
            for (j = 1; j <= 6; j++) // For j = 1 To 6
            {
                slope = rnd.NextDouble() * (level + 1) * 250 / j - ((level + 1) * 250 / 2 / j);
                cnt = 0;
                for (i = lb; i <= ub; i++) // For i = lb To ub
                {
                    cur = this.ground[i] + slope * cnt;
                    this.ground[i] = cur;
                    cnt += 1;
                    if (cnt > 320 / Math.Pow(2, j)) //If cnt > 320 / (2 ^ j) Then
                    {
                        slope = rnd.NextDouble() * (level + 1) * 250 / j - ((level + 1) * 250 / 2 / j);
                        cnt = 0;
                        if (i < ub) //If i<ub Then
                        {
                            delta = cur - this.ground[i + 1];
                        }
                        else
                        { // Else
                            delta = 0;
                        } // EndIf
                        for (k = i + 1; k <= ub; k++) // For k = i + 1 To ub
                        {
                            this.ground[k] += delta;
                        } // Next
                    } // EndIf
                } // Next i
            } // Next j
            delta = 0;
            mini = 1000;
            maxi = 0;
            for (i = lb; i <= ub; i++) //For i = lb To ub
            {
                mini = (this.ground[i] < mini) ? this.ground[i] : mini;
                maxi = (this.ground[i] > maxi) ? this.ground[i] : maxi;
                delta += this.ground[i];
            } // Next i
            ground = (maxi - mini) / 5 * level;
            mini = maxi - ground;
            for (i = lb; i <= ub; i++) // For i = lb To ub
            {
                this.ground[i] = (this.ground[i] < mini) ? mini : this.ground[i];
                this.ground[i] = (this.ground[i] - mini) / (maxi - mini) * (level / 8.0) * 200 + 20;
            } // Next i
              //'	delta = (delta / ub-lb+1)/((level+1)*10)
            for (i = lb; i <= ub; i++) // For i = lb To ub
            {
                //' this.ground(i)/=delta
                //'		this.ground(i)+= 10
                this.ground[i] = (this.ground[i] < 20) ? 20 : this.ground[i];//  If this.ground(i) < 20 Then this.ground(i) = 20
                this.ground[i] = (this.ground[i] > 220) ? 220 : this.ground[i];//  If this.ground(i) > 220 Then this.ground(i) = 220
            } // Next

            this.fuelLocation.x = -100.0;
            this.fuelLocation.y = -100;
            this.padLocation.x = ((int)(rnd.NextDouble() * 2) * 300 - 150) * (level / 10.0) + 160;
            this.padLocation.y = (this.ground[(int)(this.padLocation.x) - 10] + this.ground[(int)(this.padLocation.x) + 10]) / 2;
            this.padLocation.y = (this.padLocation.y < 20) ? 20 : this.padLocation.y;  //If this.padlocation.y < 20 Then this.padlocation.y = 20
            lb = (int)(this.padLocation.x) - 10;
            ub = (int)(this.padLocation.x) + 10;
            for (i = lb; i <= ub; i++) // For i = lb To ub
            {
                this.ground[i] = this.padLocation.y;
            } //Next
        }
    }

    class game
    {
        public int tic = 0;
        public int tic2 = 0;
        public int life = 0;
        public int bestsafeland = 0;
        public int safeland = 0;
        public int sublevelx = 0;
        public int sublevely = 0;
        public int bestscore = 0;
        public int score = 0;
        public bool showMessage = true;
        public Lander ship = new Lander();
        public EnergySucker[] Sucker = new EnergySucker[101];
        public int nbSucker = 0;
        public Landscape scene = new Landscape();
        public player_action playerAct = player_action.PA_NOTHING;
        public game_status status = game_status.GS_INTRO;
        public string[] msg = new string[201];
        public double xm = 0;
        public double ym = 0;
        public int bm = 0;
        Random rnd = new Random();
        // prev = rnd.NextDouble() * 200 + 20;
        public game()
        {
            int i; // Dim i As Integer
            for (i=0; i < this.Sucker.Length; i++)
            {
                this.Sucker[i] = new EnergySucker();
            }
            
            //Dim fi As Integer
            //fi = FreeFile
            //this.initGfx
            this.init();
            this.bestsafeland = 0;
            this.bestscore = 0;
            //https://support.unity3d.com/hc/en-us/articles/115000341143-How-do-I-read-and-write-data-from-a-text-file-

            //If Open("lander.sco" For Input As #fi)=0 Then
            //    Input #fi,this.bestscore
            //    Input #fi,this.bestsafeland
            //    Close #fi
            //EndIf
            BasicTextFile btf = BasicTextFile.openRead("LANDER.SCO"); //yuy
            if (btf != null)
            {
                btf.input(out this.bestscore);
                btf.input(out this.bestsafeland);
            }
            for (i = 0; i < this.msg.Length; i++) // For i = LBound(this.msg) To UBound(this.msg)
            {
                this.msg[i] = "Press Any Key to Start";
            } // Next i
            this.msg[1] = "Another easy one,";
            this.msg[2] = "Looks to be the same";
            this.msg[3] = "Detecting FOE not far away";
            this.msg[4] = "ALERT ! § Energy sucker ! Avoid it !";
            this.msg[5] = "It was easy... ! But it still here !";
            this.msg[6] = "1 more § !";
            this.msg[7] = "Enegy Sucker Engine Enhanced !";
            this.msg[8] = "BEWARE ! They fly a bit faster!";
            this.msg[9] = "§ speed linit ! But they are 3 !";
            this.msg[10] = "New planet with higher gravity";
            this.msg[11] = "Hope you're not tired";
            this.msg[12] = "He he ! 4 suckers now !";
            this.msg[13] = "Again !";
            this.msg[14] = "Again !";
            this.msg[15] = "Again !";
            this.msg[16] = "Oooh ! 5 Energy Suckers Now";
            this.msg[17] = "Again !";
            this.msg[18] = "Again !";
            this.msg[19] = "One more sucker ! ";
            this.msg[20] = "New planet with higher gravity and 6 § !";
            this.msg[21] = "Keep going almost finished !";
            this.msg[22] = "Grr ! Here come another one";
            this.msg[23] = "----------";
        }

        public void init()
        {
            this.safeland = 0;
            this.score = 0;
            this.life = 3;
            this.status = game_status.GS_INTRO;
            this.tic = 0;
            this.tic2 = 0;
            this.nbSucker = 0;
            this.initLevel(0);
        }

        public void Draw(GameContext ctx)
        {
            int i; //, lb, ub; // Dim As Integer i, lb, ub
            Lander aLife = new Lander(); // Dim aLife As lander
            int speed; // Dim speed As Integer
            double destx; // Dim destx As Double
            double desty; // Dim desty As Double
            string m = "";// Dim m As string
            ctx.Cls();
            //' Lanscape
            this.scene.Draw(ctx);
            //' Lander
            this.ship.Draw(ctx);
            //' Sucker
            for (i = 0; i < this.nbSucker; i++) // For i = 0 To this.nbSucker - 1
            {
                this.Sucker[i].Draw(ctx);
            } // Next
            //'Safe landing
            //'boardtxt.DrawText(" Safe "+Str( this.safeland),0,234*KH,10)
            //'Score
            if (this.status != game_status.GS_EDIT && this.status != game_status.GS_EDIT_TEXT) //If this.status <> GS_EDIT And this.status <> GS_EDIT_TEXT Then
            {
                ctx.boardtxt.drawText(ctx, " & " + this.safeland + "  # " + this.score, 0, (234 * ctx.KH), 10);
            }
            else
            {
                if (this.scene.allowtakeoff == 0) //If this.scene.allowtakeoff = 0 Then
                {
                    m = "L";
                }
                else
                { // Else
                    m = "T";
                } // EndIf
                ctx.boardtxt.drawText(ctx, " & " + this.safeland + " (" + this.sublevelx + "," + this.sublevely + ")" + m, 0, (234 * ctx.KH), 10);
            } // EndIf

            //'Life
            if (this.status != game_status.GS_EDIT && this.status != game_status.GS_EDIT_TEXT) //If this.status <> GS_EDIT And this.status <> GS_EDIT_TEXT then
            {
                aLife.size = 5;
                aLife.status = lander_status.LS_NORMAL; // LS_NORMAL
                aLife.location.y = 6;
                for (i = 1; i <= this.life; i++) // For i = 1 To this.life
                {
                    aLife.location.x = 88 + 25 + (i - 1) * 12;
                    aLife.angle = this.tic * Math.PI / 180;
                    aLife.Draw(ctx);
                } // Next i
            } // End If

            //'Arrow to show possible direction
            if (this.scene.go_up != 0) //If this.scene.go_up Then
            {
                ctx.boardtxt.scaleRot(ctx.boardtxt.size, 0);
                ctx.boardtxt.drawText(ctx, "%", (88 * ctx.KW), (229 * ctx.KH), 10);
            } //EndIf
            if (this.scene.go_down != 0) //If this.scene.go_down Then
            {
                ctx.boardtxt.scaleRot(ctx.boardtxt.size, Math.PI);
                ctx.boardtxt.drawText(ctx, "%", (88 * ctx.KW), (235 * ctx.KH), 10);
            } // EndIf
            if (this.scene.go_left != 0) //If this.scene.go_left Then
            {
                ctx.boardtxt.scaleRot(ctx.boardtxt.size, -Math.PI / 2);
                ctx.boardtxt.drawText(ctx, "%", (85 * ctx.KW), (232 * ctx.KH), 10);
            } // EndIf
            if (this.scene.go_right != 0)  //If this.scene.go_right Then
            {
                ctx.boardtxt.scaleRot(ctx.boardtxt.size, Math.PI / 2);
                ctx.boardtxt.drawText(ctx, "%", (91 * ctx.KW), (232 * ctx.KH), 10);
            } // EndIf

            //'Fuel	
            ctx.boardtxt.scaleRot(ctx.boardtxt.size, this.tic * Math.PI / 180);
            ctx.boardtxt.drawText(ctx, " ~", (150 * ctx.KW), (235 * ctx.KH), 14, 0);
            ctx.boardtxt.scaleRot(ctx.boardtxt.size, 0);
            ctx.LineBF(161 * ctx.KW, 231 * ctx.KH, (161 + this.ship.fuel) * ctx.KW, 239 * ctx.KH, 14);
            ctx.LineB(161 * ctx.KW, 231 * ctx.KH, 261 * ctx.KW, 239 * ctx.KH, 15);

            //'Speed
            if (this.ship.Speed.y < 0) //If this.ship.speed.y < 0 Then
            {
                speed = (int)((Math.Pow(this.ship.Speed.x, 2) + Math.Pow(this.ship.Speed.y, 2)) * 1000);
                speed = ((int)(Math.Abs(this.ship.angle / (Math.PI / 180))) >= 10) ? 100 : speed; // If Int(Abs(this.ship.angle/ (PI / 180))) >= 10 Then speed = 100
                speed = (speed > 100) ? 100 : speed; //If speed > 100 Then speed = 100
                ctx.LineBF(265 * ctx.KW, 231 * ctx.KH, (265 + speed / 2) * ctx.KW, 239 * ctx.KH, 14);
            } // EndIf
            ctx.LineB(265 * ctx.KW, 231 * ctx.KH, (265 + 60 / 2) * ctx.KW, 239 * ctx.KH, 15);
            ctx.LineB(265 * ctx.KW, 231 * ctx.KH, (265 + 50) * ctx.KW, 239 * ctx.KH, 15);
            switch (this.status) //Select Case this.status
            {
                case game_status.GS_START:
                    //' START
                    if (this.tic2 < 200) //If this.tic2 < 200 Then
                    {
                        ctx.text.drawText(ctx, this.msg[this.safeland], ctx.G_WIDTH / 2.0, (120 * ctx.KH * (this.tic2 - 10) / 190.0), 10);
                    }
                    else
                    {
                        if (this.tic2 > 500) //If this.tic2 > 500 Then
                        {
                            ctx.text.scaleRot(4 * ctx.KW, Math.Sin((this.tic2 - 500) * Math.PI / 180 / 2) * Math.PI / 4.0);
                        } // EndIf
                        ctx.text.drawText(ctx, this.msg[this.safeland], ctx.G_WIDTH / 2.0, (120.0 * ctx.KH), 10);
                        ctx.text.scaleRot(4.0 * ctx.KW, 0);
                    } // End if
                    break;
                case game_status.GS_INTRO:
                    //' INTRO
                    if (this.tic2 == 1) SoundManager.instance.PlaySingle(ctx.dl.titleSound,0.10f,1.25f);
                    if (this.tic2 <= 200) //If this.tic2 <= 200 Then
                    {
                        ctx.bigtxt.scaleRot(1.0*this.tic2 / 200.0 * 5.0 * ctx.KW, 1.0*this.tic2 / 100.0 * Math.PI);
                    } // EndIf
                    ctx.bigtxt.drawText(ctx, "$ Captain DAPI $", ctx.G_WIDTH / 2.0, (95 * ctx.KH), 10);
                    // If this.tic2 >= 200 then text.DrawText("Left   : Turn left ", G_WIDTH / 2, (105 + 9) * KH, 10)
                    if (this.tic2 >= 200) ctx.text.drawText(ctx, "Left   : Turn left ", ctx.G_WIDTH / 2.0, ((105 + 9) * ctx.KH), 10);
                    //If this.tic2 >= 230 then text.DrawText("Right  : Turn right", G_WIDTH / 2, (105 + 18) * KH, 10)
                    if (this.tic2 >= 230) ctx.text.drawText(ctx, "Right  : Turn right", ctx.G_WIDTH / 2.0, ((105 + 18) * ctx.KH), 10);
                    //If this.tic2 >= 260 then text.DrawText("Up     : Thrust    ", G_WIDTH / 2, (105 + 27) * KH, 10)
                    if (this.tic2 >= 260) ctx.text.drawText(ctx, "Up     : Thrust    ", ctx.G_WIDTH / 2.0, ((105 + 27) * ctx.KH), 10);
                    //If this.tic2 >= 290 then text.DrawText("Space  : Pause     ", G_WIDTH / 2, (105 + 36) * KH, 10)
                    if (this.tic2 >= 290) ctx.text.drawText(ctx, "Space  : Pause     ", ctx.G_WIDTH / 2.0, ((105 + 36) * ctx.KH), 10);
                    //If this.tic2 >= 320 Then text.DrawText("Escape : Quit      ", G_WIDTH / 2, (105 + 45) * KH, 10)
                    if (this.tic2 >= 320) ctx.text.drawText(ctx, "Escape : Quit      ", ctx.G_WIDTH / 2.0, ((105 + 45) * ctx.KH), 10);
                    // If this.tic2 >= 320 And this.bestscore <> 0 Then text.DrawText("Best score " + Str(this.bestscore) + " with " + Str(this.bestsafeland) + " safe landing", G_WIDTH / 2, (105 + 62) * KH, 10)
                    if (this.tic2 >= 320 && this.bestscore != 0) ctx.text.drawText(ctx, "Best score " + this.bestscore + " with " + this.bestsafeland + " completed project", ctx.G_WIDTH / 2.0, ((105 + 62) * ctx.KH), 10);
                    //If this.tic2 >= 320 And this.bestscore = 0 Then text.DrawText("No Best Score Yet !", G_WIDTH / 2, (105 + 62) * KH, 10)
                    if (this.tic2 >= 320 && this.bestscore == 0) ctx.text.drawText(ctx, "No Best Score Yet !", ctx.G_WIDTH / 2.0, ((105 + 62) * ctx.KH), 10);
                    if (this.tic2 >= 200 && this.tic2 <= 350) //If this.tic2 <= 350 And this.tic2 > = 200 Then
                    {
                        ctx.text.drawText(ctx, this.msg[this.safeland], ctx.G_WIDTH / 2.0, ((110.0 + 72) * ctx.KH * (this.tic2 - 300.0) / (350 - 300.0)), 10);
                    }
                    else
                    { //  Else
                        //If  this.tic2 > = 350 Then text.DrawText(this.msg(this.safeland), G_WIDTH / 2, (110 + 72) * KH, 10)
                        if (this.tic2 >= 350) ctx.text.drawText(ctx, this.msg[this.safeland], ctx.G_WIDTH / 2.0, ((110 + 72) * ctx.KH), 10);
                    } // EndIf
                    break;
                case game_status.GS_PAUSE:
                    //' PAUSE	
                    if (this.tic % 60 < 30) //If this.tic mod 60 < 30 Then
                    {
                        ctx.bigtxt.scaleRot(5 * ctx.KW, 0);
                        ctx.bigtxt.drawText(ctx, "Pause", ctx.G_WIDTH / 2.0, (120 * ctx.KH), 12);
                    } //EndIf
                    break;
                case game_status.GS_RUN:
                    //' RUNNING 	
                    if (this.ship.fuel <= 0) //If this.ship.fuel <= 0 then
                    {
                        if (this.tic % 30 < 15) // If this.tic mod 30 < 15 Then
                        {
                            ctx.bigtxt.scaleRot(5 * ctx.KW, 0);
                            ctx.bigtxt.drawText(ctx, "NO ENERGY !", ctx.G_WIDTH / 2.0, (120 * ctx.KH), 12);
                        } //EndIf
                    }//  End If
                    break;
                case game_status.GS_CRASHED:
                    //' CRASHED
                    //' "Life request" animation
                    if (this.tic2 <= 60) //If this.tic2 <= 60 Then
                    {
                        aLife.location.x = 88 + 25 + (this.life) * 12;
                        aLife.angle = this.tic * Math.PI / 180;
                        aLife.Draw(ctx);
                    } //EndIf
                    if (this.tic2 == 60) //If this.tic2 = 60 Then
                    {
                        this.LoadLevel(this.safeland, 0, 0);
                    } // EndIf
                    if (this.tic2 > 60) //If this.tic2 > 60 Then
                    {
                        destx = this.scene.startLocation.x;
                        desty = this.scene.startLocation.y;
                        if (this.tic2 < 60 + 200) //If this.tic2 < 60 + 200 Then
                        {
                            aLife.location.x = (destx - (88 + 25 + (this.life) * 12)) / 200.0 * (this.tic2 - 60) + 88 + 25 + (this.life) * 12;
                            aLife.location.y = (desty - 6.0) / 200.0 * (this.tic2 - 60) + 6;
                            aLife.size = (7.0 - 5.0) / 200.0 * (this.tic2 - 60) + 5;
                            aLife.angle = this.tic * Math.PI / 180;
                        }
                        else
                        { // Else
                            ctx.smalltxt.drawText(ctx, "DAPI is Ready", (destx * ctx.KW), (((240.0 - desty) + 7 + 4) * ctx.KW), 15);
                            aLife.location.x = destx;
                            aLife.location.y = desty;
                            aLife.size = 7;
                            aLife.angle = this.tic * Math.PI / 180;
                        } // End If
                        aLife.Draw(ctx);
                    } // End If
                    if (this.tic2 < 200) //If this.tic2 < 200 Then
                    {
                        //'text2.boom = (10/200.0*this.tic2)-9
                        if (this.tic2 % 4 == 0) //If this.tic2 Mod 4 = 0 Then
                        {
                            ctx.text2.scaleRot((15.0 + rnd.NextDouble() * 2.0) * ctx.KW, (rnd.NextDouble() * 0.2) - 0.1);
                        } // End If
                    }
                    else
                    { // Else
                        ctx.text2.boom = 1;
                    } // End If

                    ctx.text2.drawText(ctx, "CRASH!", ctx.G_WIDTH / 2.0, (120.0 * ctx.KH), 14);
                    ctx.text2.boom = 1;
                    break;
                case game_status.GS_GAMEOVER:
                    //' GAME OVER
                    if (this.tic2 < 200) //If this.tic2 < 200 Then
                    {
                        ctx.text2.boom = 10 - (9 / 200.0 * this.tic2);
                        ctx.text2.scaleRot(5 * ctx.KW * this.tic2 / 60, 0);
                    } // EndIf
                    ctx.text2.drawText(ctx, "GAME OVER", ctx.G_WIDTH / 2.0, (120 * ctx.KH), 15);
                    ctx.text2.boom = 1;
                    break;
                case game_status.GS_FINISH:
                    //' FINISH THE GAME
                    if (this.tic2 < 200) //If this.tic2 < 200 Then
                    {
                        ctx.text2.boom = 10 - (9 / 200.0 * this.tic2);
                        ctx.text2.scaleRot(5 * ctx.KW * this.tic2 / 60.0, 0);
                    } // EndIf
                    ctx.text2.drawText(ctx, "YOU WIN", ctx.G_WIDTH / 2.0, (120.0 * ctx.KH), 15);
                    ctx.text2.boom = 1;
                    break;
                case game_status.GS_LANDED:
                    //' LANDED
                    if (this.tic2 <= 180) //If this.tic2 <= 180 Then
                    {
                        ctx.text2.scaleRot(5 * ctx.KW * this.tic2 / 60.0, this.tic2 * 1.0 / 90 * Math.PI);
                    } // End If
                    ctx.text2.drawText(ctx, this.scene.landedmsg, ctx.G_WIDTH / 2.0, (120 * ctx.KH), 15);
                    break;

                case game_status.GS_EDIT:
                case game_status.GS_EDIT_TEXT:
                    //LEVEL editor
                    /*
                    If MultiKey(FB.SC_F1) Then
                        Cls
                        Locate 2,1
                        Color 10
                        Print "EDITOR COMMAND"
                        Print "--------------"
                        Print " F1 .....................: This help"
                        Print " F2 .....................: Save current Level"
                        Print " F3 .....................: Load current Level"
                        Print " F4 .....................: Generate a Lanscape (current level)"
                        Print " F5 .....................: Allow/disallow launch after landing (end level anim)"
                        Print " F6 .....................: Remove landpad"
                        Print " F7 .....................: Remove fuelpad"
                        Print " F10 ....................: Enter / Leave Level Editor"
                        Print " INSERT .................: Add an Energy Sucker at mouse position"
                        Print " DELETE .................: Remove Last Added Energy Sucker"
                        Print " HOME/END ...............: + / - Gravity"
                        Print " PGUP/DOWN ..............: + / - Energy"
                        Print " SPACE ..................: Place Land Pad at mouse position"
                        Print " SHIFT + SPACE ..........: Place Energy Reload Pad at mouse position"
                        Print " BACK-SPC ...............: Enter Title Edit Mode"
                        Print " ENTER ..................: Valid Title(Edit Mode)"
                        Print " LEFT/RIGHT/UP/DOWN .....: Move Lander"
                        Print " LEFT Sft+LEFT/RIGHT ....: Rotate Lander"
                        Print " CTRL+UP/DOWN/LEFT/RIGHT : Shift landscape "
                        Print " t,b,l,r ................: allow/disallow sublevel top/bottom/left/right"
                        Print " T,B,L,R ................: move to sublevel top/bottom/left/right"
                        Print " + / - ..................: Change Level Up/Down"
                        Print " LEFT MOUSE BUTTON ......: Draw Ground (slowy please to avoid picks)"
                        Print " RIGHT MOUSE BUTTON .....: Draw Sky (slowy please to avoid picks)"
                        Print " "
                        Print " Auto-save level when leaving Editor (F10)"
                        Print " Auto-load level when entering Editor (F10)"
                        Print " "
                        Print " TIP : You may use Landscape generator (F4) and use the land pad command  (keep space key down) and move mouse to have a quick landscape design"
                        Print ""
                        Print "Press Any Key to continue"
                        Flip
                        Sleep
                        Sleep 100,1
                        While InKey<> "" : Wend
                        Sleep 100,1
                    EndIf
                    */
                    if (this.scene.go_up != 0)
                    {
                        ctx.LineB(0, 0, 319.0 * ctx.KW, 5.0 * ctx.KH, 09);//,B,&hFF00
                    } // EndIf
                    if (this.scene.go_down != 0) //Then
                    {
                        ctx.LineB(0, (239.0 - 20.0) * ctx.KH,319.0 * ctx.KW, (240.0 - 20.0 - 5.0) * ctx.KH, 09); //,B,&hFF00
                    } // EndIf
                    if (this.scene.go_left != 0) //Then
                    {
                        ctx.LineB(0, 0, 5.0 * ctx.KW, (240.0 - 20.0) * ctx.KH, 9); //,B,&hFF00
                    }// EndIf
                    if (this.scene.go_right != 0) // Then
                    {
                        ctx.LineB((320.0 - 5.0) * ctx.KW, 0, (319.0) * ctx.KW, (240.0 - 20.0) * ctx.KH, 9); //,B,&hFF00
                    } // EndIf
                    ctx.boardtxt.drawText(ctx,"G", 80.0 * ctx.KW, 234.0 * ctx.KH, 10);
                    ctx.LineB(88.0 * ctx.KW, 230.0 * ctx.KH, (88.0 + 50.0) * ctx.KW, 239.0 * ctx.KH, 10); //,B
                    ctx.LineBF(88.0 * ctx.KW, 230.0 * ctx.KH, (88.0 + (this.scene.gravity * 2000.0)) * ctx.KW, 239.0 * ctx.KH, 10); //,BF
                    ctx.boardtxt.drawText(ctx, "LEVEL EDITOR", 246.0 * ctx.KW, 226.0 * ctx.KH, 9);
                    if (this.status == game_status.GS_EDIT_TEXT) // Then
                    {
                        string pst = "";// ;  Dim pst As String
                        if (this.tic % 30 < 15) //If this.tic Mod 30 < 15 Then
                        {
                            pst = " ";
                        } else { // Else
                            pst = "_";
                        } // EndIf
                        pst = this.msg[this.safeland] + pst;
                        ctx.text.scaleRot(4.0 * ctx.KW, 0);
                        ctx.text.drawText(ctx, pst, ctx.G_WIDTH / 2.0, 120.0 * ctx.KH, 10);
                    } // End If
                    ctx.boardtxt.drawText(ctx, "X", this.xm * ctx.KW, this.ym * ctx.KH, 10);
                break;
            } // End Select

            //' Screen sync delay and show drawing result
            //screensync
            //Flip
        }

        public void initLevel(int level)
        {
            int i; // Dim i As Integer
            this.playerAct = player_action.PA_NOTHING;
            this.ship.init();
            this.nbSucker = 0;
            this.sublevelx = 0;
            this.sublevely = 0;
            i = this.LoadLevel(level);
            if (i == 0) //If i = 0 then
            {
                this.scene.init(level);
                if (this.safeland > 3) //If this.safeland > 3 Then
                {
                    this.nbSucker = (int)(this.safeland / 3.0);
                    this.nbSucker = (this.nbSucker > this.Sucker.Length) ? this.Sucker.Length : this.nbSucker; // IIf(this.nbSucker > UBound(this.Sucker) + 1, UBound(this.Sucker), this.nbSucker)
                    for (i = 0; i < this.nbSucker; i++) // For i = 0 To this.nbSucker - 1
                    {
                        this.Sucker[i].location.x = 160 + 160 - this.scene.padLocation.x + rnd.NextDouble() * 30 - 15;
                        if (Math.Abs(this.Sucker[i].location.x - this.scene.padLocation.x) < 100) //If Abs(this.Sucker(i).location.x -this.scene.padLocation.x) < 100 Then
                        {
                            this.Sucker[i].location.x *= 2.0;
                            //If this.Sucker(i).location.x > 319 Then this.Sucker(i).location.x = 319
                            this.Sucker[i].location.x = (this.Sucker[i].location.x > 319) ? 319 : this.Sucker[i].location.x;
                        } // endif
                        this.Sucker[i].location.y = this.scene.ground[(int)(this.Sucker[i].location.x)] + 20 + (220 - this.scene.ground[(int)(this.Sucker[i].location.x)]) * rnd.NextDouble();
                    } // Next i
                } // EndIf
            } // End If
            this.ship.location.x = this.scene.startLocation.x;
            this.ship.location.y = this.scene.startLocation.y;
        }

        public void EnergySuckerAction(GameContext ctx)
        {
            int i; // Dim i As Integer
            double xs, ys, xm, ym, d, dx, dy, k, cur_alt, new_alt, cur_skydist, new_skydist; // Dim As Double xs, ys, xm, ym, d
            double perTicSpeed = 14.0/ ctx.fps;

            //int level; // Dim level As Integer
            //level = (this.safeland > 10) ? 10 : this.safeland;//iif(this.safeland > 10, 10, this.safeland)
            //level += 4;

            xs = this.ship.location.x;
            ys = this.ship.location.y;
            if (this.status == game_status.GS_RUN) //If this.status = GS_RUN then
            {
                for (i = 0; i < this.nbSucker; i++) // For i = 0 To this.nbSucker - 1
                {
                    if (this.Sucker[i].status == EnergySucker_Status.SS_NORMAL) //If this.Sucker(i).status = SS_NORMAL Then
                    {
                        //rs.setDefault((i Mod 4) + 2,0,(this.Sucker(i).tic Mod 60)/ 2)
                        //rs.sound(60 - (this.Sucker(i).tic Mod 60))*2 + 80,100,0
                        xm = this.Sucker[i].location.x;
                        ym = this.Sucker[i].location.y;
                        d = Math.Sqrt(Math.Pow(xs - xm, 2) + Math.Pow(ys - ym, 2)); // Sqr((xs - xm) ^ 2 + (ys - ym) ^ 2)
                        dx = xs - xm;
                        dy = ys - ym;
                        k = perTicSpeed / d;
                        // detect collision to ship, if so then still ship energy
                        if (d < this.ship.size + this.Sucker[i].size) //If d< (this.ship.size+this.Sucker(i).size) Then
                        {
                            if ((this.tic + i) % 10 == 0) //If(this.tic + i) Mod 10 = 0 Then
                            {
                                if (this.ship.fuel > 0) //If this.ship.fuel > 0 Then
                                {
                                    this.ship.fuel -= 1;
                                    //rs.setDefault((i Mod 4) + 2,15,255)
                                    //rs.sound 30,250,0
                                } // EndIf
                            } // EndIf
                        } // EndIf

                        this.Sucker[i].Speed.x = k * dx;
                        this.Sucker[i].Speed.y = k * dy;
                        cur_alt = ym - this.scene.ground[(int)xm];
                        cur_skydist = this.scene.sky[(int)xm] - ym;
                        xm += this.Sucker[i].Speed.x;
                        ym += this.Sucker[i].Speed.y;
                        xm = (xm > 319) ? 319 : xm;
                        xm = (xm < 0) ? 0 : xm;
                        new_alt = ym - this.scene.ground[(int)xm];
                        new_skydist = this.scene.sky[(int)xm] - ym;
                        // ground detection
                        if ((new_alt >= 0 && new_alt <= 10) || (new_skydist >= 0 && new_skydist <= 10)) //in  altitude below 10 (ground or sky)
                        {
                            this.Sucker[i].Speed.y = 0; // avoid penetrte but keep horizontal speed
                            this.Sucker[i].Speed.x = perTicSpeed * Math.Sign(this.Sucker[i].Speed.x);
                        }

                        if (new_alt <= 0 && new_skydist <= 0)
                        {
                            this.Sucker[i].Speed.y = 0;
                            this.Sucker[i].Speed.x = 0;
                        }
                        else
                        {
                            if (new_alt < 0) // in  ground
                            {
                                this.Sucker[i].Speed.y = perTicSpeed; // Math.Abs(this.Sucker[i].Speed.y);
                                this.Sucker[i].Speed.x = 0;
                            }

                            if (new_skydist < 0) // in  sky
                            {
                                this.Sucker[i].Speed.y = -perTicSpeed; // Math.Abs(this.Sucker[i].Speed.y);
                                this.Sucker[i].Speed.x = 0;
                            }
                        }

                        this.Sucker[i].location.x += this.Sucker[i].Speed.x;
                        this.Sucker[i].location.y += this.Sucker[i].Speed.y;

                        /*
                        if (d * 0 < 10 * level) // If d * 0 < 10 * level Then
                        {
                            If Abs(xs -xm) < 0.0001 Then xm+= 0.001
                            this.Sucker(i).angle = ATan2((ys - ym), (xs - xm))
                            this.Sucker(i).speed.x = Cos(this.Sucker(i).angle) * 7 / 60.0
                            this.Sucker(i).speed.y = sin(this.Sucker(i).angle) * 7 / 60.0
                        } // EndIf

                        If this.Sucker(i).location.y - this.scene.ground(Int(this.Sucker(i).location.x)) + 10 > 3 Then
                            this.Sucker(i).location.x += this.Sucker(i).speed.x
                        EndIf

                        this.Sucker(i).location.y += this.Sucker(i).speed.y
                        If this.Sucker(i).location.y < this.scene.ground(Int(this.Sucker(i).location.x)) + 10 Then
                            this.Sucker(i).location.x -= this.Sucker(i).speed.x
                            this.Sucker(i).location.y -= this.Sucker(i).speed.y
                            this.Sucker(i).location.y += 0.1'Abs(this.Sucker(i).speed.y)
                            //'this.Sucker(i).location.y = this.scene.ground(Int(this.Sucker(i).location.x))+20
                        EndIf
                        If this.Sucker(i).location.y - this.scene.sky(Int(this.Sucker(i).location.x)) - 10 < -3 Then
                            this.Sucker(i).location.x += this.Sucker(i).speed.x
                        EndIf
                        this.Sucker(i).location.y += this.Sucker(i).speed.y
                        If this.Sucker(i).location.y > this.scene.sky(Int(this.Sucker(i).location.x)) - 10 Then
                            this.Sucker(i).location.x -= this.Sucker(i).speed.x
                            this.Sucker(i).location.y -= this.Sucker(i).speed.y
                            this.Sucker(i).location.y -= 0.1'Abs(this.Sucker(i).speed.y)
                            'this.Sucker(i).location.y = this.scene.ground(Int(this.Sucker(i).location.x))+20
                        EndIf
                        */
                    } // EndIf
                } // Next i
            } // End If
        }

        public bool tick(GameContext ctx)
        {
            string st; // dim st as String
            double xxm, yym;
            int speed, angle, i;//, xxm, yym; // Dim As Integer speed, angle, fi, i, xxm, yym
            BasicTextFile fi;
            //int y1, y2; // Dim As Integer v1, v2
            //rs.setDefault(0, 2, 128)
            //showmessage(); // very first message
            do
            {
                this.tic += 1;
                this.tic2 += 1;
                // st = InKey
                st = ctx.inkey; // (ctx.anyKey()) ? "+" : "";
                //rs.tick
                //' Player action
                this.playerAct = player_action.PA_NOTHING; // PA_NOTHING
                //' Lander sound diming
                //v1 = rs._channel(1).volume
                //v2 = rs._channel(1).frequency
                //'If tic Mod 2 = 0 Then	
                //    v1 = v1 - 2
                //    v2 = v2 - 2
                //    If v2< 30 Then v2 = 30
                //    If v1< 0 Then v1 = 0
                //    If v1 > 40 Then v1 = 40
                //'End If
                //rs.keyonoff(1, 15, v2, v1, 100)

                //If MultiKey(FB.SC_LEFT) Then this.playeract = PA_LEFT
                if (Input.GetAxis("Horizontal") < 0) this.playerAct = player_action.PA_LEFT;
                // If MultiKey(FB.SC_RIGHT) Then this.playeract = PA_RIGHT
                if (Input.GetAxis("Horizontal") > 0) this.playerAct = player_action.PA_RIGHT;
                //If MultiKey(FB.SC_UP) Then this.playeract = PA_THRUST
                if (Input.GetAxis("Vertical") > 0) this.playerAct = player_action.PA_THRUST;
                //if Multikey(FB.SC_SPACE) then this.playeract = PA_PAUSE
                if (Input.GetAxis("Jump") > 0) this.playerAct = player_action.PA_PAUSE;
                //If MultiKey(FB.SC_ESCAPE) Then this.playeract = PA_QUIT
                if (Input.GetAxis("Cancel") > 0) this.playerAct = player_action.PA_QUIT;
#if (UNITY_EDITOR)                
                //If MultiKey(FB.SC_F10) And this.status <> GS_EDIT And this.tic > 60 Then
                if (Input.GetKey(KeyCode.F10) && this.status != game_status.GS_EDIT && this.tic > 60) 
                {
                    //  # If  __FB_DEBUG__=0
                    //              If Left(Trim(UCase(Command)), Len("-EDIT")) = "-EDIT" Then
                    //   #endif	
                    SoundManager.instance.Pause();
                    this.status = game_status.GS_EDIT;
                    this.ship.Speed.x = 0;
                    this.ship.Speed.y = 0;
                    this.ship.status = lander_status.LS_NORMAL;
                    this.tic = 0;
                    this.tic2 = 0;
                    this.LoadLevel(this.safeland, this.sublevelx, this.sublevely);
                     //   #If __FB_DEBUG__ = 0
                     //               End If
                     //   #endif			
                } // EndIf


                //        # Ifdef CHEAT		
                //' Cheat keys (Debugging purpose)		
                //'If st="-" Then this.ship.status = LS_CRASH
                //'If st="+" Then this.ship.status = LS_NORMAL
                if (st.Equals("*")) this.ship.fuel = 100;
                if (st.Equals("/")) //If st = "/" Then
                {
                    this.tic = 0;
                    this.life = 0;
                    this.tic2 = 0;
                    this.status = game_status.GS_GAMEOVER;
                } // End If
                //        #endif
#endif
                //'Enemy action
                this.EnergySuckerAction(ctx);

                if (this.status == game_status.GS_GAMEOVER || this.status == game_status.GS_FINISH) //If this.status = GS_GAMEOVER Or this.status = GS_FINISH then
                {
                    if (this.bestscore < this.score) //If this.bestscore < this.score Then
                    {
                        //fi = freefile
                        this.bestscore = this.score;
                        this.bestsafeland = this.safeland;
                        fi = BasicTextFile.openWrite("LANDER.SCO");
                        if (fi != null)
                        {
                            //If Open("lander.sco" For Output As #fi)=0 Then
                            fi.print(this.bestscore);// print #fi,this.bestscore
                            fi.print(this.bestsafeland); // print #fi,this.bestsafeland
                            fi.close(); // Close #fi
                        } // EndIf
                    } //EndIf
                } // EndIf

                //' Process player action
                if (this.status == game_status.GS_START) //If this.status = GS_START Then
                {
                    /*
                                        If this.tic = 1 Then
                                            rs.setDefault(0, 1, 64)
                                            rs.sound 220,300.1,2
                                            rs.setDefault(0, 1, 0)
                                            rs.sound 0,300.1,2
                                            rs.setDefault(0, 1, 64)
                                            rs.sound 220,300.1,2
                                            rs.setDefault(0, 1, 128)
                                            rs.sound 440,400.1,2
                                        EndIf
                    */
                    this.ship.location.x = this.scene.startLocation.x;
                    this.ship.location.y = this.scene.startLocation.y;
                    if (ctx.anyKey() && this.tic > 30) //If st<> "" And this.tic > 30 Then
                    {
                        this.status = game_status.GS_RUN;
                        this.tic = 0;
                    } // End If
                } // EndIf
                if (this.status == game_status.GS_INTRO) //If this.status = GS_INTRO  Then
                {
                    /*
                    If this.tic = 1 Then
                        rs.setDefault(0, 3, 128)
                        rs.sound - 60 - 6,700.2,2
                        rs.sound - 60 - 7,800.2,2
                        rs.setDefault(0, 3, 128)
                        rs.sound - 60 - 3,1400.1,2
                    EndIf
                    */
                    this.ship.location.x = this.scene.startLocation.x;
                    this.ship.location.y = this.scene.startLocation.y;
                    if (ctx.anyKey() && this.tic > 30) //If st<> "" And this.tic > 30 Then
                    {
                        this.status = game_status.GS_RUN;
                        SoundManager.instance.Stop();
                        this.tic = 0;
                    } // EndIf
                } // EndIf

                if (this.status == game_status.GS_LANDED && this.tic > 120) //If this.status = GS_LANDED And this.tic > 120 Then
                {
                    if (this.ship.fuel < 100 && this.tic % 3 == 0) //If this.ship.fuel < 100 And this.tic Mod 3 = 0 Then
                    {
                        this.ship.fuel += 1;
                    } // EndIf
                    if (ctx.anyKey() || this.ship.location.y > 280 || this.tic > 60 * 10) //If st <> "" or this.ship.location.y > 280 Or this.tic > 60 * 10 Then
                    {
                        this.tic = 0; this.showMessage = true;
                        this.status = game_status.GS_START;
                        this.initLevel(this.safeland);
                        this.tic = 0;
                        this.tic2 = 0;
                    } // End if
                } // EndIf

                if (this.status == game_status.GS_CRASHED && this.tic > 120) //If this.status = GS_CRASHED And this.tic > 120 Then
                {
                    if (ctx.anyKey() || this.tic2 > 260 + 180) // If st<> "" Or this.tic2 > 260 + 180 Then
                    {
                        this.status = game_status.GS_START;
                        this.ship.init();
                        this.initLevel(this.safeland);
                        this.tic = 0;
                        this.tic2 = 0;
                    } // End if
                } //EndIf

                if (this.status == game_status.GS_GAMEOVER && this.tic > 120) // If this.status = GS_GAMEOVER And this.tic > 120 Then
                {
                    if (ctx.anyKey() || this.tic > 800) //If st<> "" Or this.tic > 800 Then
                    {
                        this.init();
                        this.tic = 0;
                        this.tic2 = 0;
                    } // End if
                } // EndIf

                if (this.status == game_status.GS_FINISH && this.tic > 120) //If this.status = GS_FINISH And this.tic > 120 Then
                {
                    if (ctx.anyKey() || this.tic > 800) //  If st<> "" Or this.tic > 800 Then
                    {
                        this.init();
                        this.tic = 0;
                        this.tic2 = 0;
                    } // End if
                } // EndIf

                if (this.status == game_status.GS_PAUSE && this.tic > 60) //if this.status = GS_PAUSE And this.tic > 60 Then
                {
                    if (this.playerAct == player_action.PA_PAUSE) //if this.playeract = PA_PAUSE then
                    {
                        this.status = game_status.GS_RUN;
                        //while inkey <> "" : sleep 1,1 :wend
                        // sleep 100,1
                        this.playerAct = player_action.PA_NOTHING;
                        this.tic = 0;
                        SoundManager.instance.UnPause();
                    } // end if
                } // end If
#if (UNITY_EDITOR)
                //If this.status = GS_EDIT Or this.status = GS_EDIT_TEXT Then
                if (this.status == game_status.GS_EDIT || this.status == game_status.GS_EDIT_TEXT)
                {
                    //'If this.safeland = 0 Then this.safeland = 1
                    //GetMouse xxm, yym,,this.bm
                    xxm = Input.mousePosition.x/Screen.width;
                    yym = Input.mousePosition.y/Screen.height;
                    int mbutton = Input.GetKey(KeyCode.Mouse0)?1:0;
                    mbutton += Input.GetKey(KeyCode.Mouse1) ? 2 : 0;
                    mbutton += Input.GetKey(KeyCode.Mouse2) ? 4 : 0;
                    this.bm = mbutton;
                    this.xm = xxm / ctx.KW * 1.0;
                    this.ym = 240.0 - (yym / ctx.KH * 1.0);
                    this.scene.startLocation.x = this.ship.location.x;
                    this.scene.startLocation.y = this.ship.location.y;
                    
                    //If MultiKey(FB.SC_CONTROL)= 0 then
                    if (!Input.GetKey(KeyCode.LeftControl) && !Input.GetKey(KeyCode.RightControl))
                    {
                        //If MultiKey(FB.SC_UP) And MultiKey(FB.SC_LSHIFT)= 0 Then this.ship.location.y += 1 / KH
                        if (!Input.GetKey(KeyCode.LeftShift) && Input.GetKey(KeyCode.UpArrow)) this.ship.location.y += 1.0;// / ctx.KH;
                        //If MultiKey(FB.SC_DOWN) And MultiKey(FB.SC_LSHIFT)= 0 Then   this.ship.location.y -= 1 / KH
                        if (!Input.GetKey(KeyCode.LeftShift) && Input.GetKey(KeyCode.DownArrow)) this.ship.location.y -= 1.0;// / ctx.KH;
                        //If MultiKey(FB.SC_LEFT) And MultiKey(FB.SC_LSHIFT)= 0 Then this.ship.location.x -= 1 / KW
                        if (!Input.GetKey(KeyCode.LeftShift) && Input.GetKey(KeyCode.LeftArrow)) this.ship.location.x -= 1.0;// / ctx.KW;
                        //If MultiKey(FB.SC_RIGHT) And MultiKey(FB.SC_LSHIFT)= 0 Then this.ship.location.x += 1 / KW
                        if (!Input.GetKey(KeyCode.LeftShift) && Input.GetKey(KeyCode.RightArrow)) this.ship.location.x += 1.0;// / ctx.KW;
                        //If MultiKey(FB.SC_LEFT) And MultiKey(FB.SC_LSHIFT) Then
                        if (Input.GetKey(KeyCode.LeftShift) && Input.GetKey(KeyCode.LeftArrow))
                        {
                            this.ship.angle -= Math.PI / 100.0;
                            if (this.ship.angle < -Math.PI) this.ship.angle += 2.0 * Math.PI;
                        } // End if
                        //If MultiKey(FB.SC_RIGHT) And MultiKey(FB.SC_LSHIFT) Then
                        if (Input.GetKey(KeyCode.LeftShift) && Input.GetKey(KeyCode.RightArrow))
                        {
                            this.ship.angle += Math.PI / 100.0;
                            if (this.ship.angle > Math.PI) this.ship.angle -= 2.0 * Math.PI;
                        } // End if
                    } else { // Else
                        //If MultiKey(FB.SC_UP) Then
                        if (Input.GetKey(KeyCode.UpArrow))
                        {
                            //For i = LBound(this.scene.ground) To UBound(this.scene.ground)
                            
                            for (i = 0; i < this.scene.ground.Length; i++)
                            {
                                this.scene.ground[i] += 1;
                                this.scene.sky[i] += 1;
                            } // Next
                            //For i = lbound(this.Sucker) To UBound(this.sucker)
                            for (i = 0; i < this.Sucker.Length; i++)
                            {
                                this.Sucker[i].location.y += 1;
                            } // Next
                            this.scene.padLocation.y += 1;
                            this.scene.fuelLocation.y += 1;
                            this.ship.location.y += 1;
                        } // End If
                        //If MultiKey(FB.SC_DOWN) Then
                        if (Input.GetKey(KeyCode.UpArrow))
                        {
                            //For i = LBound(this.scene.ground) To UBound(this.scene.ground)
                            for (i = 0; i < this.scene.ground.Length; i++)
                            {
                                this.scene.ground[i] -= 1;
                                this.scene.sky[i] -= 1;
                            } //Next
                            //For i = lbound(this.Sucker) To UBound(this.sucker)
                            for (i = 0; i < this.Sucker.Length;i++)
                            {
                                this.Sucker[i].location.y -= 1;
                            } // Next
                            this.scene.padLocation.y -= 1;
                            this.scene.fuelLocation.y -= 1;
                            this.ship.location.y -= 1;
                        } // End If

                        //If MultiKey(FB.SC_LEFT) Then
                        
                        if (Input.GetKey(KeyCode.LeftArrow))
                        {
                            double tg,ts;//Dim As Double tg, ts
                            
                            //tg = this.scene.ground(UBound(this.scene.ground))
                            tg = this.scene.ground[this.scene.ground.Length-1];
                            // ts = this.scene.sky(UBound(this.scene.ground))
                            ts = this.scene.sky[this.scene.sky.Length-1];
                            //For i = UBound(this.scene.ground) To LBound(this.scene.ground)+1 Step - 1
                            for (i = this.scene.ground.Length - 1; i > 0; i--)
                            {
                                this.scene.ground[i] = this.scene.ground[i - 1];
                                this.scene.sky[i] = this.scene.sky[i - 1];
                            } // Next
                            //this.scene.ground(LBound(this.scene.ground)) = tg
                            this.scene.ground[0] = tg;
                            //this.scene.sky(LBound(this.scene.ground)) = ts
                            this.scene.sky[0] = ts;

                            //For i = lbound(this.Sucker) To UBound(this.sucker)
                            for (i = 0; i < this.Sucker.Length; i++)
                            {
                                this.Sucker[i].location.x += 1;
                                //If this.Sucker(i).location.x >= 320 Then this.Sucker(i).location.x -= 320
                                if (this.Sucker[i].location.x >= 320) this.Sucker[i].location.x -= 320;
                            } // Next
                            if (this.scene.padLocation.x > -100)
                            {
                                this.scene.padLocation.x += 1;
                                if (this.scene.padLocation.x >= 320) this.scene.padLocation.x -= 320;
                            } //End if
                            if (this.scene.fuelLocation.x > -100)
                            {
                                this.scene.fuelLocation.x += 1;
                                if (this.scene.fuelLocation.x >= 320) this.scene.fuelLocation.x -= 320;
                            } // End if
                            this.ship.location.x += 1;
                            if (this.ship.location.x >= 320) this.ship.location.x -= 320;
                        } // End If
                        //If MultiKey(FB.SC_RIGHT) Then
                        if (Input.GetKey(KeyCode.RightArrow))
                        {
                            double tg, ts; // Dim As Double tg, ts
                            tg = this.scene.ground[0];
                            ts = this.scene.sky[0];
                            //For i = LBound(this.scene.ground) To UBound(this.scene.ground)-1
                            for (i = 0; i < this.scene.ground.Length - 1; i++)
                            {
                                this.scene.ground[i] = this.scene.ground[i + 1];
                                this.scene.sky[i] = this.scene.sky[i + 1];
                            } // Next
                            this.scene.ground[this.scene.ground.Length - 1] = tg;
                            this.scene.sky[this.scene.sky.Length - 1] = ts;

                            //For i = lbound(this.Sucker) To UBound(this.sucker)
                            for (i = 0; i < this.Sucker.Length; i++)
                            {
                                this.Sucker[i].location.x -= 1;
                                if (this.Sucker[i].location.x < 0) this.Sucker[i].location.x += 320;
                            } // Next
                            if (this.scene.padLocation.x > -100)
                            {
                                this.scene.padLocation.x -= 1;
                                if (this.scene.padLocation.x < 0) this.scene.padLocation.x += 320;
                            } // End If
                            if (this.scene.fuelLocation.x > -100)
                            {
                                this.scene.fuelLocation.x -= 1;
                                if (this.scene.fuelLocation.x < 0) this.scene.fuelLocation.x += 320;
                            } // End if
                            this.ship.location.x -= 1;
                            if (this.ship.location.x < 0)  this.ship.location.x += 320;
                        } // End If
                    } // End If

                    //If MultiKey(FB.SC_F10) And this.tic > 60 Then
                    if (Input.GetKey(KeyCode.F10) && this.tic > 60)
                    {
                        SoundManager.instance.UnPause();
                        this.status = game_status.GS_START;//game_status.GS_RUN;
                        this.tic = 0;
                        this.SaveLevel(this.safeland, this.sublevelx, this.sublevely);
                    } // EndIf
                    //' DRAW GROUND
                    if (this.bm == 1) // Then
                    {
                        if ((int)(this.xm) >= 0 && (int)(this.xm) < 320)
                        {
                            this.scene.ground[(int)(this.xm)] = (int)(240 - this.ym);
                            if (this.scene.ground[(int)(this.xm)] < 20) this.scene.ground[(int)(this.xm)] = -20;
                            if (this.scene.ground[(int)(this.xm)] > 220) this.scene.ground[(int)(this.xm)] = 220;
                            if (this.scene.ground[(int)(this.xm)] > this.scene.sky[(int)(this.xm)])// Then
                            {
                                this.scene.sky[(int)(this.xm)] = this.scene.ground[(int)(this.xm)];
                            } //End if
                        }
                    } // End If
                    //' DRAW SKY
                    if (this.bm == 2) // Then
                    {
                        if ((int)(this.xm) >= 0 && (int)(this.xm) < 320)
                        {
                            this.scene.sky[(int)(this.xm)] = (int)(240 - this.ym);
                            if (this.scene.sky[(int)(this.xm)] < 20) this.scene.sky[(int)(this.xm)] = 20;
                            if (this.scene.sky[(int)(this.xm)] > 220) this.scene.sky[(int)(this.xm)] = 250;
                            if (this.scene.ground[(int)(this.xm)] > this.scene.sky[(int)(this.xm)]) //Then
                            {
                                this.scene.ground[(int)(this.xm)] = this.scene.sky[(int)(this.xm)];
                            } // End if
                        }
                    } // End If
                    if (this.status == game_status.GS_EDIT_TEXT) //Then ' change text
                    {

                        if (!st.Equals(""))
                        {
                            bool isBackSpace = st.Equals("\b");
                            bool isEnter = st.Equals("\n") || st.Equals("\r"); 
                            bool isCharacter = !isBackSpace && !isEnter;
                            if (isCharacter) this.msg[this.safeland] += st;
                            //If Asc(st) > 31 And Asc(st)< 255 Then
                            //    msg(this.safeland) += st
                            // EndIf
                            if (isBackSpace) this.msg[this.safeland] = this.msg[this.safeland].Substring(0, this.msg[this.safeland].Length - 1);
                            //If Asc(st) = 8 Then msg(this.safeland) = Left(msg(this.safeland), Len(msg(this.safeland)) - 1)
                            if (isEnter) this.status = game_status.GS_EDIT;
                            //If st = Chr(13) Then this.status = GS_EDIT
                        } // End if
                    } else { // Else
                        //' SWITCH TO EDIT LEVEL MESSAGE MODE
                        if (st.Equals("\b")) this.status = game_status.GS_EDIT_TEXT;
                        //' INSERT LAND PAD
                        //If st = " " And MultiKey(FB.SC_LSHIFT)= 0 Then
                        if (st.Equals(" ") && !Input.GetKey(KeyCode.LeftShift))
                        {
                            if (this.xm < 10) this.xm = 10;
                            if (this.xm > 309) this.xm = 309;
                            this.scene.padLocation.x = this.xm;
                            this.scene.padLocation.y = 240 - this.ym;
                            for (i = (int)(this.xm - 10); i <= (int)(this.xm + 10); i++)
                            {
                                this.scene.ground[i] = this.scene.padLocation.y;
                            } // Next i
                        } // EndIf
                        //' INSERT FUEL PAD
                        //If st = " " And MultiKey(FB.SC_LSHIFT) Then
                        if (st.Equals(" ") && Input.GetKey(KeyCode.LeftShift))
                        {
                            if (this.xm < 10) this.xm = 10;
                            if (this.xm > 309) this.xm = 309;
                            this.scene.fuelLocation.x = this.xm;
                            this.scene.fuelLocation.y = 240 - this.ym;
                            //For i = this.xm - 10 To this.xm + 10
                            for (i = (int)(this.xm - 10); i <= (int)(this.xm + 10); i++)
                            {
                                this.scene.ground[i] = this.scene.fuelLocation.y;
                            }// Next i
                        } // EndIf
                        //' ENABLE/DISBALE UP/DOWN/LEFT/RIGHT PASS
                        if (st.Equals("t")) //If st = "t" Then
                        {
                            this.scene.go_up = this.scene.go_up == 0 ? 1 : 0;
                        } // end If
                        if (st.Equals("b")) //If st = "b" Then
                        {
                            this.scene.go_down = this.scene.go_down == 0 ? 1 : 0;
                        } // end If
                        if (st.Equals("l")) //If st = "l" Then
                        {
                            this.scene.go_left = this.scene.go_left == 0 ? 1 : 0;
                        } // end If
                        if (st.Equals("r")) //If st = "r" Then
                        {
                            this.scene.go_right = this.scene.go_right == 0 ? 1 : 0;
                        } // end If
                        //' CHANGE SUBLEVEL 
                        if (st.Equals("T"))//If st = "T" Then
                        {
                            this.sublevely += 1;
                        } // end If
                        if (st.Equals("B")) //If st = "B" Then
                        {
                            this.sublevely -= 1;
                        } // end If
                        if (st.Equals("L")) //If st = "L" Then
                        {
                            this.sublevelx -= 1;
                        } // end If
                        if (st.Equals("R")) //If st = "R" Then
                        {
                            this.sublevelx += 1;
                        } // end If
                        //' SWITH TO ONE LEVEL MORE
                        if (st.Equals("+") && this.safeland < 22) //If st = "+" And this.safeland < 22 Then
                        {
                            this.safeland += 1;
                        } //EndIf
                        //' SWITH TO ONE LEVEL LESS
                        if (st.Equals("-") && this.safeland >= 0) //If st = "-" And this.safeland >= 0 Then
                        {
                            this.safeland -= 1;
                        }// EndIf
                        //' SAVE LEVEL 
                        if (Input.GetKey(KeyCode.F2) && this.tic > 60)//If MultiKey(FB.SC_F2) And this.tic > 60 Then
                        {
                            this.tic = 0;
                            this.SaveLevel(this.safeland, this.sublevelx, this.sublevely);
                        } // EndIf
                        //' LOAD LEVEL
                        if (Input.GetKey(KeyCode.F3) && this.tic > 60) //If MultiKey(FB.SC_F3) And this.tic > 60 Then
                        {
                            this.tic = 0;
                            this.SaveLevel(999);
                            this.ship.init();
                            if (this.sublevelx == 0 && this.sublevely == 0) // Then
                            {
                                if (this.LoadLevel(this.safeland) == 0) // Then
                                {
                                    this.LoadLevel(999);
                                } //   EndIf
                            } else { // Else
                                if (this.LoadLevel(this.safeland, sublevelx, sublevely) == 0) // Then
                                {
                                    this.LoadLevel(999);
                                } //EndIf
                            } // EndIf
                        } //EndIf
                        //' ALLOW / DISALLOW TAKE OFF after landing
                        if (Input.GetKey(KeyCode.F5) && this.tic > 60) //If MultiKey(FB.SC_F5) And this.tic > 60 Then
                        {
                            this.scene.allowtakeoff = this.scene.allowtakeoff == 0 ? 1 : 0;
                            this.tic = 0;
                        } // End If
                          // ' REMOVE LANDPAD
                        if (Input.GetKey(KeyCode.F6)) //If MultiKey(FB.SC_F6) Then
                        {
                            this.scene.padLocation.x = -100;
                        } //End If
                        //' REMOVE FUELPAD
                        if (Input.GetKey(KeyCode.F7)) //If MultiKey(FB.SC_F7) Then
                        {
                            this.scene.fuelLocation.x = -100;
                        } //End If

                        //' GENERATE LEVEL
                        if (Input.GetKey(KeyCode.F4) && this.tic > 3) //If MultiKey(FB.SC_F4) And this.tic > 3 Then
                        {
                            this.tic = 0;
                            this.scene.init(this.safeland);
                        } // EndIf
                        //' ADD ONE MORE ENERGY SUCKET AT MOUSE POSITION
                        if (Input.GetKey(KeyCode.Insert) && this.tic > 15) //If MultiKey(FB.SC_INSERT) And this.tic > 15 Then
                        {
                            this.tic = 0;
                            this.nbSucker += 1;
                            this.Sucker[this.nbSucker - 1].location.x = this.xm;
                            this.Sucker[this.nbSucker - 1].location.y = 240.0 - this.ym;
                        } // End If
                        //' REMOVE LAST ADDED ENERGY SUCKER
                        if (Input.GetKey(KeyCode.Delete) && this.tic > 15) //If MultiKey(FB.SC_DELETE) And this.tic > 15 Then
                        {
                            this.tic = 0;
                            if (this.nbSucker > 0) this.nbSucker -= 1;
                        } // End If
                        //' ADD MORE FUEL
                        if (Input.GetKey(KeyCode.PageUp) && this.tic > 3) //If MultiKey(FB.SC_PAGEUP) And this.tic > 3 Then
                        {
                            this.tic = 0;
                            if (this.ship.fuel < 100) this.ship.fuel += 1;
                        } // End if
                        //' REMOVE FUEL
                        if (Input.GetKey(KeyCode.PageDown) && this.tic > 3) // MultiKey(FB.SC_PAGEDOWN) And this.tic > 3 Then
                        {
                            this.tic = 0;
                            if (this.ship.fuel > 0) this.ship.fuel -= 1;
                        } // End if
                        //' ADD MORE GRAVITY
                        if (Input.GetKey(KeyCode.Home) && this.tic > 3) // If MultiKey(FB.SC_HOME) And this.tic > 3 Then
                        {
                            this.tic = 0;
                            this.scene.gravity = ((int)(this.scene.gravity / 0.0025 + 0.5)) * 0.0025;
                            if (this.scene.gravity < 0.025) this.scene.gravity += 0.0025;
                        } // End if
                        //' REMOVE GRAVITY
                        if (Input.GetKey(KeyCode.End) && this.tic > 3) //If MultiKey(FB.SC_END) And this.tic > 3 Then
                        {
                            this.tic = 0;
                            this.scene.gravity = ((int)(this.scene.gravity / 0.0025 + 0.5)) * 0.0025;
                            if ( this.scene.gravity > 0) this.scene.gravity -= 0.0025;
                        } // End if
                    } // EndIf
                } // EndIf
#endif                               
                if (this.status == game_status.GS_RUN) //If this.status = GS_RUN Then
                {
                    if (this.ship.fuel <= 0) //If this.ship.fuel <= 0 Then
                    {
                        /*
                        i = this.tic Mod 60
                        i = i * 2
                        Select Case i
                            Case is< 60
                                rs.setDefault(0, 3, i * 3)
                                rs.Sound 110,100,0
                            Case is>= 60
                                rs.setDefault(0, 3, (i - 60) * 3)
                                rs.Sound 440,100,0
                        End Select
                        */
                        if (this.scene.gravity < 0.0025) this.scene.gravity = 0.0025; // If this.scene.gravity < 0.0025 then  this.scene.gravity = 0.0025
                    } // EndIf

                    if (this.playerAct == player_action.PA_PAUSE && this.tic > 30) //if this.playeract = PA_PAUSE then
                    {
                        //sleep 100,1
                        //st = inkey
                        this.status = game_status.GS_PAUSE;
                        this.playerAct = player_action.PA_NOTHING;
                        SoundManager.instance.Pause();
                        this.tic = 0;
                    } //end If
                    if (this.playerAct == player_action.PA_THRUST) //If this.playeract = PA_THRUST Then
                    {
                        this.ship.status = lander_status.LS_THRUST;
                    }
                    else
                    { // Else
                        if (this.ship.status != lander_status.LS_CRASH) //If this.ship.status <> LS_CRASH Then
                        {
                            this.ship.status = lander_status.LS_NORMAL;
                        } // EndIf
                    } // EndIf
                    // If this.playeract = PA_LEFT And this.ship.fuel > 0 Then this.ship.angle -= PI / 100
                    if (this.playerAct == player_action.PA_LEFT && this.ship.fuel > 0) this.ship.angle -= Math.PI / 180;
                    //If this.playeract = PA_RIGHT And this.ship.fuel > 0 Then this.ship.angle += PI / 100
                    if (this.playerAct == player_action.PA_RIGHT && this.ship.fuel > 0) this.ship.angle += Math.PI / 180;
                    if (this.ship.angle > Math.PI) //If this.ship.angle > PI Then
                    {
                        this.ship.angle -= 2 * Math.PI;
                    } // EndIf
                    if (this.ship.angle < -Math.PI) //If this.ship.angle < -PI Then
                    {
                        this.ship.angle += 2 * Math.PI;
                    } //EndIf
                    if (this.playerAct == player_action.PA_THRUST && this.ship.fuel > 0) //If this.playeract = PA_THRUST And this.ship.fuel > 0 Then
                    {
                        this.ship.Speed.x += Math.Sin(this.ship.angle) * 0.03;
                        this.ship.Speed.y += Math.Cos(this.ship.angle) * 0.03;
                        if (this.tic % 4 == 0) this.ship.fuel -= 1; // If this.tic Mod 4 = 0 Then this.ship.fuel -= 1
                    } // End If
                    this.ship.Speed.y -= this.scene.gravity;
                    this.ship.location.x += this.ship.Speed.x;
                    this.ship.location.y += this.ship.Speed.y;

                    if (this.ship.location.x < 0) //If this.ship.location.x < 0 Then
                    {
                        if (this.scene.go_left != 0) //If this.scene.go_left Then
                        {
                            if (this.LoadLevel(this.safeland, this.sublevelx - 1, this.sublevely) != 0) //If LoadLevel(this.safeland, this.sublevelx -1, this.sublevely) Then
                            {
                                this.sublevelx -= 1;
                                this.ship.location.x = 320 - 5;
                            }
                            else
                            { // Else
                                this.ship.location.x = 0;
                                this.ship.Speed.x = -this.ship.Speed.x / 2.0;
                            } // End if
                        }
                        else
                        { // Else
                            this.ship.location.x = 0;
                            this.ship.Speed.x = -this.ship.Speed.x / 2.0;
                        } // End if
                    } // End if
                    if (this.ship.location.x >= 319) // If this.ship.location.x >= 319 Then
                    {
                        if (this.scene.go_right != 0) //If this.scene.go_right Then
                        {
                            if (LoadLevel(this.safeland, this.sublevelx + 1, this.sublevely) != 0) //If LoadLevel(this.safeland, this.sublevelx +1, this.sublevely) Then
                            {
                                this.sublevelx += 1;
                                this.ship.location.x = 5;
                            }
                            else
                            { // Else
                                this.ship.location.x = 319;
                                this.ship.Speed.x = -this.ship.Speed.x / 2.0;
                            } //End if
                        }
                        else
                        { // Else
                            this.ship.location.x = 319;
                            this.ship.Speed.x = -this.ship.Speed.x / 2.0;
                        } // End if
                    } //End if
                    if (this.ship.location.y < 20) //If this.ship.location.y < 20 Then
                    {
                        if (this.scene.go_down != 0) //If this.scene.go_down Then
                        {
                            if (LoadLevel(this.safeland, this.sublevelx, this.sublevely - 1) != 0)
                            {
                                this.sublevely -= 1;
                                this.ship.location.y = 240 - 5;
                            }
                            else
                            { // Else
                                this.ship.location.y = 20;
                                this.ship.Speed.y = -this.ship.Speed.y / 2.0;
                            } //  End if
                        }
                        else
                        { // Else
                            this.ship.location.y = 20;
                            this.ship.Speed.y = -this.ship.Speed.y / 2.0;
                        } // End if
                    } // End if
                    if (this.ship.location.y > 240)
                    {
                        if (this.scene.go_up != 0)
                        {
                            if (LoadLevel(this.safeland, this.sublevelx, this.sublevely + 1) != 0)
                            {
                                this.sublevely += 1;
                                this.ship.location.y = 25;
                            }
                            else
                            { // Else
                                this.ship.location.y = 239;
                                this.ship.Speed.y = -this.ship.Speed.y / 2.0;
                            } // End if
                        }
                        else
                        { //Else
                            this.ship.location.y = 239;
                            this.ship.Speed.y = -this.ship.Speed.y / 2.0;
                        } // End if
                    } // End If
                    if (this.ship.location.y <= this.scene.ground[(int)(this.ship.location.x)] + this.ship.size * 0.80 ||
                        this.ship.location.y >= this.scene.sky[(int)(this.ship.location.x)] - this.ship.size * 0.80) // Then
                                                                                                                     //'this.ship.location.y = this.scene.ground(Int(this.ship.location.x))+this.ship.size*0.80
                    {
                        speed = (int)((Math.Pow(this.ship.Speed.x, 2) + Math.Pow(this.ship.Speed.y, 2)) * 1000);
                        angle = (int)(Math.Abs(this.ship.angle / (Math.PI / 180)));
                        if ((speed <= 60 && angle < 10 &&
                            this.ship.location.y <= this.scene.ground[(int)(this.ship.location.x)] + this.ship.size * 0.80) &&
                                ((this.scene.padLocation.x - 10 < this.ship.location.x &&
                                  this.scene.padLocation.x + 10 > this.ship.location.x) ||
                                 (this.scene.fuelLocation.x - 10 < this.ship.location.x &&
                                  this.scene.fuelLocation.x + 10 > this.ship.location.x)))
                        {
                            if (this.scene.padLocation.x - 10 < this.ship.location.x &&
                                this.scene.padLocation.x + 10 > this.ship.location.x)
                            {
                                this.safeland += 1;
                                this.score += (int)this.ship.fuel;
                                this.ship.status = lander_status.LS_LANDED;
                                if (this.scene.sky[(int)(this.ship.location.x)] <= 240 || this.scene.allowtakeoff == 0)
                                {
                                    this.ship.status = lander_status.LS_LANDED_NOSKY;
                                } // End if
                                if (this.safeland >= 23)
                                {
                                    this.status = game_status.GS_FINISH;
                                    //rs.setDefault(0, 3, 128)
                                    //For i = 1 To 10 Step 1
                                    //    rs.sound(-i - 40, 200, 2)
                                    //Next i
                                }
                                else
                                { // Else
                                    //rs.setDefault(0, 3, 128)
                                    //For i = 0 To 11 Step 3
                                    //    rs.sound(-i - 40, 600.2, 2)
                                    //Next i
                                    SoundManager.instance.PlaySingle(ctx.dl.landedSound);
                                    this.status = game_status.GS_LANDED;
                                } // End If
                                this.tic = 0;
                            }
                            else
                            { // Else
                                if (this.tic % 3 == 0 && this.ship.fuel < 100)
                                {
                                    this.ship.fuel += 1;
                                    //rs.setDefault(0, 3, 255)
                                    //rs.sound(30, 100, 0)
                                } // End If
                                this.ship.location.y = this.scene.ground[(int)(this.ship.location.x)] + this.ship.size * 0.80;
                            } //End If
                        }
                        else
                        { // Else
                            this.status = game_status.GS_CRASHED;
                            this.ship.status = lander_status.LS_CRASH;
                            SoundManager.instance.PlaySingle(ctx.dl.crashSound);
                            if (this.life == 0)
                            {
                                this.status = game_status.GS_GAMEOVER;
                                SoundManager.instance.PlaySingle(ctx.dl.gameOverSound,1,0.25f);
                                //rs.setDefault(0, 3, 0)
                                //rs.sound(-1, 1000, 2)
                                //rs.setDefault(0, 3, 128)
                                //For i = 10 To - 2 Step - 2
                                //    rs.sound(-i - 40, 800.2, 2)
                                //Next i
                            }
                            else
                            { // Else
                                this.life -= 1;
                            } // End If
                            this.tic = 0;
                        } // EndIf
                        this.tic2 = 0;
                        this.ship.Speed.x = 0;
                        this.ship.Speed.y = 0;
                    } //EndIf
                } // End If
                //Sleep 1,1
                this.Draw(ctx);
            } while (false);//while (Input.GetAxis("Cancel") == 0); //Loop While MultiKey(FB.SC_ESCAPE) = 0

            if (Input.GetAxis("Cancel") > 0)
            {
                if (this.bestscore < this.score)
                {
                    //fi = freefile
                    this.bestscore = this.score;
                    this.bestsafeland = this.safeland;
                    fi = BasicTextFile.openWrite("LANDER.SCO");
                    if (fi != null)
                    {
                        //If Open("lander.sco" For Output As #fi)=0 Then
                        fi.print(this.bestscore);
                        fi.print(this.bestsafeland);
                        fi.close();// #fi
                    } // EndIf
                } // EndIf
                this.safeland = 99;
                this.tic = 0;
                this.showMessage = true; ;
                return false;
            }
            return true;
        }

        public int LoadLevel(int lvl)
        {
            return LoadLevel(lvl, -100, -100);
        }

        public int SaveLevel(int lvl)
        {
            return SaveLevel(lvl, -100, -100);
        }

        public int LoadLevel(int lvl, int sublvlx, int sublvly)
        {
            BasicTextFile fi; // Dim fi As Integer
            int i; // Dim i As Integer
            string vv; // Dim vv As string
            //fi = FreeFile
            vv = "_" + sublvlx + "_" + sublvly;
            if (sublvlx <= -100 && sublvly <= -100) vv = "_0_0"; // If sublvlx <= -100 And sublvly <= -100 Then vv = "_0_0"
            //i = Open("l" + Str(lvl) + vv + ".lvl" For Input As #fi)
            fi = BasicTextFile.openRead("l" + lvl + vv + ".lvl");
            i = (fi != null) ? 0 : 1;
            if (i == 0) //If i = 0 Then
            {
                fi.input(out vv); // Input #fi,vv
                if (vv == null || !vv.Equals("version=1")) //If vv <> "version=1" Then
                {
                    fi.close(); // Close #fi
                    i = 1;
                } //EndIf
            } // EndIf
            if (i == 0) //If i = 0 Then
            {
                //' get ground landscape
                for (i = 0; i < 320; i++) // For i = 0 To 319
                {
                    fi.input(out this.scene.sky[i]); //  Input #fi,this.scene.sky(i)
                    fi.input(out this.scene.ground[i]); // Input #fi,this.scene.ground(i)
                }  //Next i
                fi.input(out this.scene.go_up); // Input #fi,this.scene.go_up
                fi.input(out this.scene.go_down); // Input #fi,this.scene.go_down
                fi.input(out this.scene.go_left); // Input #fi,this.scene.go_left
                fi.input(out this.scene.go_right); // Input #fi,this.scene.go_right
                fi.input(out this.scene.inverse); // Input #fi,this.scene.inverse
                fi.input(out this.scene.allowtakeoff); // Input #fi,this.scene.allowtakeoff
                fi.input(out this.scene.landedmsg); // Input #fi,this.scene.landedmsg

                //' get pad location
                fi.input(out this.scene.padLocation.x); // Input #fi,this.scene.padlocation.x
                fi.input(out this.scene.padLocation.y); // Input #fi,this.scene.padlocation.y

                //' get fuel location
                fi.input(out this.scene.fuelLocation.x); // Input #fi,this.scene.fuellocation.x
                fi.input(out this.scene.fuelLocation.y); // Input #fi,this.scene.fuellocation.y

                //' get gravity
                fi.input(out this.scene.gravity); // Input #fi,this.scene.gravity
                if ((sublvlx <= -100 && sublvly <= -100) || this.status == game_status.GS_EDIT || this.status == game_status.GS_EDIT_TEXT) //If(sublvlx <= -100 And sublvly <= -100) Or this.status = GS_EDIT Or this.status = GS_EDIT_TEXT then
                {
                    //' get lander location
                    fi.input(out this.ship.location.x); // Input #fi,this.ship.location.x
                    fi.input(out this.ship.location.y); // Input #fi,this.ship.location.y
                    this.scene.startLocation.x = this.ship.location.x;
                    this.scene.startLocation.y = this.ship.location.y;
                    //' get lander speed
                    fi.input(out this.ship.Speed.x); // Input #fi,this.ship.speed.x 
                    fi.input(out this.ship.Speed.y); // Input #fi,this.ship.speed.y

                    //' get lander angle
                    fi.input(out this.ship.angle); // Input #fi,this.ship.angle
                    //' get fuel
                    fi.input(out this.ship.fuel); // Input #fi,this.ship.fuel
                }
                else
                { // Else
                    //' read ship info to ignore
                    fi.input(out vv); // Input #fi, vv
                    fi.input(out vv); // Input #fi, vv
                    fi.input(out vv); // Input #fi, vv
                    fi.input(out vv); // Input #fi, vv
                    fi.input(out vv); // Input #fi, vv
                    fi.input(out vv); // Input #fi, vv
                } // End If

                //'	Print this.ship.angle,this.ship.fuel
                //'	Flip
                //'	sleep

                //' get enemies quantity of "Energy sucker"
                fi.input(out this.nbSucker); // Input #fi,this.nbSucker
                for (i = 0; i < this.nbSucker; i++) // For i = 0 To this.nbSucker - 1
                {
                    //' get enemy location
                    fi.input(out this.Sucker[i].location.x); // Input #fi,this.Sucker(i).location.x
                    fi.input(out this.Sucker[i].location.y); // Input #fi,this.Sucker(i).location.y
                } // Next
                // 'get message of level

                if (lvl >= 0 && lvl < this.msg.Length) //If lvl >= LBound(this.msg) And lvl <= UBound(this.msg) then
                {
                    fi.input(out this.msg[lvl]); // Input #fi,this.msg(lvl)
                } // End If
                  //'		If sublvlx<=-100 And sublvly<=-100 Then
                  //'		Else
                  //'		End if
                fi.close(); // Close #1 ' ?? shouldn't it be #fi instead of #1?
                return 1; // Return 1
            }
            else
            { // Else
                return 0;
            } // EndIf
            //return 0;
        }

        public int SaveLevel(int lvl, int sublvlx, int sublvly)
        {
            BasicTextFile fi; // Dim fi As Integer
            int i; // Dim i As Integer
            string vv; // Dim vv As String
            //fi = FreeFile
            vv = "_" + sublvlx + "_" + sublvly;
            if (sublvlx <= -100 && sublvly <= -100) vv = "_0_0";
            fi = BasicTextFile.openWrite("l" + lvl + vv + ".lvl");
            i = fi == null ? 1 : 0;
            //i = Open("l" + Str(lvl) + vv + ".lvl" For Output As #fi)
            if (i == 0) // Then
            {
                //' level format version
                fi.print("version=1"); // Print #fi,"version=1"
                                       //' put ground landscape
                for (i = 0; i < 320; i++) // For i = 0 To 319
                {
                    fi.print(this.scene.sky[i]); // Print #fi,this.scene.sky(i)
                    fi.print(this.scene.ground[i]); // Print #fi,this.scene.ground(i)
		        } // Next i
                fi.print(this.scene.go_up);
		        fi.print(this.scene.go_down);
                fi.print(this.scene.go_left);
                fi.print(this.scene.go_right);
                fi.print(this.scene.inverse);
                fi.print(this.scene.allowtakeoff);
                fi.print(this.scene.landedmsg);

                //' put pad location
                fi.print(this.scene.padLocation.x);
                fi.print(this.scene.padLocation.y);
                //' put fuel location
                fi.print(this.scene.fuelLocation.x);
                fi.print(this.scene.fuelLocation.y);
                //'put gravity
                fi.print(this.scene.gravity);
		        //' put lander location
                fi.print((int)(this.ship.location.x*1000.0)/1000.0);
                fi.print((int)(this.ship.location.y*1000.0)/1000.0);

                //' put lander speed
                fi.print((int)(this.ship.Speed.x*100000.0)/100000.0);
                fi.print((int)(this.ship.Speed.y*100000.0)/100000.0);
                //' put lander angle
                fi.print(this.ship.angle);
                //' put fuel
                fi.print(this.ship.fuel);

                //' put enemies quantity of "Energy sucker"
                fi.print(this.nbSucker);
                //For i = 0 To this.nbSucker - 1
                for (i = 0; i < this.nbSucker; i++)
                {    //' put enemy location
                    fi.print(this.Sucker[i].location.x);
                    fi.print(this.Sucker[i].location.y);
                } // Next
                //'put message of level
                //If(lvl >= LBound(this.msg) And lvl <= UBound(this.msg)) then
                if (lvl >= 0 && lvl < this.msg.Length)
                {
                    fi.print(this.msg[lvl]);
                } else { // Else
                    fi.print("Msg" + (lvl));
                } // End If
                fi.close(); //Close #1
		        return 1; // Return 1
            } else { // Else
                return 0; 
            } // EndIf
            //return 0; 
        }

        public void showmessage(GameContext ctx)
        {

            int i;// Dim i As Integer
            BasicTextFile fi; // Dim fi As Integer
            string[] m = new string[101]; // Dim m(0 To 100) As String
            int l; // Dim l As Integer
            //double t; // Dim t As double
            int lmax; // Dim lmax As Integer
            lmax = 0;
            //fi = FreeFile
            fi = BasicTextFile.openRead("m" + this.safeland + ".lvl");
            if (fi == null)
            {
                this.tic = 0;
                this.showMessage = false;
                return;
            }
            i = (fi == null ? 1 : 0);
            //i = Open("m" + Str(this.safeland) + ".lvl" For Input As #fi)
            l = 0;
            if (i == 0) //; // If i = 0 Then
            {

                //While(Not Eof(fi)) And l <= UBound(m)
                while (!fi.eof() && l < m.Length)
                {
                    fi.input(out m[l]); // Input #fi,m(l)
                    if (m[l].Length > lmax) lmax = m[l].Length; // If Len(m(l)) > lmax Then lmax = Len(m(l))
                    l += 1;
                } //Wend
                lmax += 1;
                fi.close();// Close #fi
                ctx.Cls(); // Cls
                ctx.text.scaleRot(4.0 * ctx.KW, 0);
                for (i = 0; i < l; i++) // For i = 0 To l -1
                {
                    // m(i) = " " + m(i) + pppc(Lmax - Len(m(i)))
                    m[i] = " " + m[i] + pppc(lmax - m[i].Length);
                    ctx.text.drawText(ctx,m[i], ctx.G_WIDTH / 2.0, (i * 9.0 + 6.0) * ctx.KH, 10);
                } // Next
               // Flip
               // Do
               // Loop While InKey<> ""
               // Sleep 100, 1
               // t = timer
               // Do
               //     Sleep 1, 1
               // Loop While InKey = "" And Timer -t < 25
            } // EndIf
            
            this.tic++;
            if (this.tic> ctx.fps*25 || (ctx.anyKey() && this.tic> ctx.fps*3))
            {
                this.tic = 0;
                this.showMessage = false;
            }
        }

        string pppc(int i) // As Integer) As String {
        {

            string s=""; // Dim s As String
            int j; // Dim j As Integer
            for (j = 1; j <= i; j++)// For j = 1 To i
            {
                s = s + " ";
            } // Next
            return s;
         }
    }

    class BasicTextFile
    {
        StreamReader sr;
        StreamWriter sw;
        //TextAsset taResource;
        string textResource;
        string assetName;
        string fileName;
        string fullPath;
        string dirPath;

        protected BasicTextFile()
        {
            sr = null;
            sw = null;
            //taResource = null;
            textResource = "";
        }

        protected static BasicTextFile getInstance(string assetName)
        {
            if (assetName == null) return null;
            BasicTextFile btf = new BasicTextFile();
            btf.assetName = assetName;
            btf.fileName = btf.assetName + ".txt";
            btf.dirPath = "Assets/Resources";
            btf.fullPath = btf.dirPath + "/" + btf.fileName;
            return btf;
        }

        public static BasicTextFile openRead(string assetName)
        {
            BasicTextFile btf = null;
            btf = getInstance(assetName);
            if (btf == null) return null;
#if (UNITY_EDITOR)
            try
            {
                btf.sr = new StreamReader(btf.fullPath);
            } catch (Exception e)
            { 
                Debug.Log("Can't read asset '" + assetName + "' :" + e.Message);
                return null;
            }
#else
            TextAsset taResource = Resources.Load<TextAsset>(btf.assetName);
            if (taResource == null)
            {
                try
                {
                    btf.sr = new StreamReader(btf.fullPath);
                } catch (Exception e)
                { 
                    Debug.Log("Can't read asset '" + assetName + "' :" + e.Message);
                    return null;
                }
               return btf;
            }
            btf.textResource =taResource.text;
            Resources.UnloadAsset(taResource);
            taResource = null;
            byte[] byteArray = Encoding.ASCII.GetBytes(btf.textResource);
            MemoryStream stream = new MemoryStream(byteArray);
            btf.sr = new StreamReader(stream);
#endif
            return btf;
        }

        public static BasicTextFile openWrite(string assetName)
        {
            BasicTextFile btf = getInstance(assetName);
            var dirInfo = Directory.CreateDirectory(btf.dirPath);
            if (btf == null) return null;

            btf.sw = new StreamWriter(btf.fullPath);
            return btf;
        }

        public void close()
        {
            if (sr != null) sr.Close();
            if (sw != null)
            {
                sw.Close();
#if (UNITY_EDITOR)
                UnityEditor.AssetDatabase.ImportAsset(fullPath);
#endif
            }
        }

        public bool input(out string aLine)
        {
            if (sr.Peek() >= 0)
            {
                string srLine = sr.ReadLine();
                aLine = srLine;
                return true;
            }
            aLine = null;
            return false;
        }

        public bool eof()
        {
            return !(sr.Peek() >= 0);
        }

        public bool input(out double aValue)
        {
            string aLine;
            if (input(out aLine))
            {
                aValue = double.Parse(aLine, CultureInfo.InvariantCulture);
                return true;
            }
            else
            {
                aValue = 0;
                return false;
            }
        }

        public bool input(out float aValue)
        {
            double dValue;
            if (input(out dValue))
            {
                aValue = (float)dValue;
                return true;
            }
            else
            {
                aValue = 0;
                return false;
            }
        }

        public bool input(out int aValue)
        {
            double dValue;
            if (input(out dValue))
            {
                aValue = (int)dValue;
                return true;
            }
            else
            {
                aValue = 0;
                return false;
            }
        }

        public void print(string str)
        {
            sw.WriteLine(str);
        }

        public void print(double aValue)
        {
           
            sw.WriteLine(aValue.ToString("G", CultureInfo.InvariantCulture));
        }

        public void print(float aValue)
        {
            sw.WriteLine(aValue.ToString("G", CultureInfo.InvariantCulture));
        }

        public void print(int aValue)
        {
            sw.WriteLine("" + aValue);
        }
    }

    class VectrexMemory
    {
        public Vector3 p1 = new Vector3();
        public Vector3 p2 = new Vector3();
        public Color colour = Color.black;
    }

    class GameContext
    {
        public double fps = 50.0;
        public double G_WIDTH = 1; //320;
        public double G_HEIGHT = 1; //240;
        public DrawLines dl;
        int circleSeg = 16;
        public double KW; 
        public double KH;
        public string inkey="";
        public VectrexMemory[] Vmem = new VectrexMemory[2000];
        public int VmemSize = 0;
        public TinyVectrex text = new TinyVectrex(); // Dim Shared text As TinyVectrex
        public TinyVectrex boardtxt = new TinyVectrex(); //Dim Shared boardtxt As TinyVectrex
        public TinyVectrex text2 = new TinyVectrex(); //Dim Shared text2 As TinyVectrex
        public TinyVectrex smalltxt = new TinyVectrex(); //Dim Shared smalltxt As TinyVectrex
        public TinyVectrex bigtxt = new TinyVectrex(); //Dim Shared bigtxt As TinyVectrex
        Vector2 pixelSize = new Vector2();
        //Dim Shared rs As RetroSound
        public Color[] palette = {Color.black, Color.blue, Color.green, Color.cyan, Color.red, Color.magenta, Color.yellow, Color.white,
                           Color.gray, Color.blue, Color.green, Color.cyan, Color.red, Color.magenta, Color.yellow, Color.white};

        public GameContext(DrawLines dl)
        {
            this.dl = dl;
            for (int i = 0; i < Vmem.Length; i++)
            {
                Vmem[i] = new VectrexMemory();
            }
            inkey = "";
            G_WIDTH = 1;// 320;, Open GL width
            G_HEIGHT = 1;// 240; Open GL height
            KW = G_WIDTH / 320.0; 
            KH = G_HEIGHT / 240.0;
            pixelSize.x = (float)(1.0*G_WIDTH / Screen.width); 
            pixelSize.y = (float)(1.0*G_HEIGHT / Screen.height);
            smalltxt.scaleRot(2 * KW, 0);
            bigtxt.scaleRot(5 * KW, 0);
            text.scaleRot(4 * KW, 0);
            text2.scaleRot(4 * KW, 0);
            boardtxt.scaleRot(3.5 * KW, 0);
            boardtxt.setCenterText(0);
        }

        public void Line(double x1, double y1, double x2, double y2, int colour)
        {
            if (VmemSize >= Vmem.Length)
            {
                Debug.LogWarning("Out of Vertex memory (max " + VmemSize + ")");
                return;
            }
            Vmem[VmemSize].p1.x = (float)x1;
            Vmem[VmemSize].p1.y = (float)(G_HEIGHT - y1);
            Vmem[VmemSize].p1.z = 0;
            if (x1 == x2 && y1 == y2)
            {
                Vmem[VmemSize].p2.x = (float)x2+pixelSize.x;
                Vmem[VmemSize].p2.y = (float)(G_HEIGHT - y2);
            }
            else
            {
                Vmem[VmemSize].p2.x = (float)x2;
                Vmem[VmemSize].p2.y = (float)(G_HEIGHT - y2);
            }
            Vmem[VmemSize].p2.z = 0;
            Vmem[VmemSize].colour = palette[colour];
            VmemSize++;
        }

        public void LineBF(double x1, double y1, double x2, double y2, int colour)
        {
            LineB(x1, y1, x2, y2, colour);
            double xx1, yy1, xx2, yy2, yy;
            xx1 = ((x1 < x2) ? x1 : x2); // + pixelSize.x;
            xx2 = ((x1 < x2) ? x2 : x1); // - pixelSize.x;
            yy1 = ((y1 < y2) ? y1 : y2); // + pixelSize.y;
            yy2 = ((y1 < y2) ? y2 : y1); // - pixelSize.y;
            yy = yy1;
            while (yy <= yy2)
            {
                Line(xx1, yy, xx2, yy, colour);
                yy += pixelSize.y;
            }
        }

        public void LineB(double x1, double y1, double x2, double y2, int colour)
        {
            Line(x1, y1, x2, y1, colour);
            Line(x1, y2, x2, y2, colour);
            Line(x1, y1, x1, y2, colour);
            Line(x2, y1, x2, y2, colour);
        }

        public void Circle(double x, double y, double radius, int colour)
        {
            double x1, y1, x2, y2, angle1, angle2, deltaAngle;

            deltaAngle = Math.PI * 2 / circleSeg;
            for (int i = 0; i < circleSeg; i++)
            {
                angle1 = deltaAngle * i;
                angle2 = angle1 + deltaAngle;
                x1 = x + Math.Cos(angle1) * radius;
                y1 = y + Math.Sin(angle1) * radius;
                x2 = x + Math.Cos(angle2) * radius;
                y2 = y + Math.Sin(angle2) * radius;
                Line(x1, y1, x2, y2, colour);
            }
        }

        public void Cls()
        {
            VmemSize = 0;
        }

        public bool anyKey()
        {
            return Input.anyKey;
        }
    }

    // Draws a line from "startVertex" var to the curent mouse position.
    public Material mat;
    public AudioClip thrustSound;
    public AudioClip crashSound;
    public AudioClip titleSound;
    public AudioClip landedSound;
    public AudioClip gameOverSound;
    public Color[] palette = {Color.black, Color.blue, Color.green, Color.cyan, Color.red, Color.magenta, Color.yellow, Color.white,
                           Color.gray, Color.blue, Color.green, Color.cyan, Color.red, Color.magenta, Color.yellow, Color.white};
    public double fps=50.0;
    private bool run = true;

    game agame;
    GameContext gamectx;
    double timer;
    

    void Start()
    {
        Debug.Log("Lander  Started");
        agame = new game();
        gamectx = new GameContext(this);
        gamectx.fps = this.fps;
        gamectx.palette = palette;
        SoundManager.instance.Noise(thrustSound);
        timer = 0;
        run = true;
    }

    void Update()
    {
        timer += Time.deltaTime;
        string inkey = Input.inputString;
        if (inkey == null) inkey = "";
        if (!inkey.Equals("")) gamectx.inkey = inkey;
        if (timer > 1.0 / gamectx.fps)
        {
            timer -= 1.0 / gamectx.fps;
            if (agame.showMessage)
            {
                agame.showmessage(gamectx);
            }
            else
            {
                if (!run)
                {
                    Application.Quit();
                }
                else
                {
                    run = agame.tick(gamectx);
                }
            }
            gamectx.inkey = "";
        }
    }

    void OnPostRender()
    {
        if (!mat)
        {
            Debug.LogError("Please Assign a material on the inspector");
            return;
        }
        GL.PushMatrix();
        mat.SetPass(0);
        GL.LoadOrtho();
        Color prev = Color.black;
        GL.Begin(GL.LINES);
        for (int i = 0; i < gamectx.VmemSize; i++)
        {
            if (prev != gamectx.Vmem[i].colour)
            {
                GL.Color(gamectx.Vmem[i].colour);
                prev = gamectx.Vmem[i].colour;
            }
            GL.Vertex(gamectx.Vmem[i].p1);
            GL.Vertex(gamectx.Vmem[i].p2);
        }
        GL.End();

        GL.PopMatrix();
    }
}