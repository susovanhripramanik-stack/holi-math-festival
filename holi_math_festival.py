from manim import *
import numpy as np
import random

class HoliMathFestival(ThreeDScene):
    def construct(self):

        self.camera.background_color = "#111111"

        # ------------------------------------------------
        # 🌈 Color Burst Function
        # ------------------------------------------------
        def color_burst():
            dots = VGroup()
            colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
            for _ in range(150):
                dot = Dot(
                    point=[
                        random.uniform(-7, 7),
                        random.uniform(-4, 4),
                        0
                    ],
                    color=random.choice(colors),
                    radius=0.05
                )
                dots.add(dot)
            return dots

        # ------------------------------------------------
        # 1️⃣ Happy Holi Intro
        # ------------------------------------------------
        title = Tex(r"\textbf{Happy Holi @ Math}")
        title.scale(1.5)
        title.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.play(FadeIn(title), run_time=2)
        self.play(FadeIn(color_burst()), run_time=2)
        self.wait(2)
        self.play(FadeOut(title))

        # ------------------------------------------------
        # 2️⃣ Torus + Fundamental Group
        # ------------------------------------------------
        self.set_camera_orientation(phi=70*DEGREES, theta=-45*DEGREES)

        torus = Torus()
        torus.set_fill_by_checkerboard(RED, BLUE, opacity=0.9)

        self.play(Create(torus), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.2)

        formula = Tex(r"$\pi_1(T^2) = \mathbb{Z} \oplus \mathbb{Z}$")
        formula.to_edge(UP)
        self.add_fixed_in_frame_mobjects(formula)

        self.play(Write(formula))
        self.wait(3)

        self.play(FadeOut(torus), FadeOut(formula))
        self.stop_ambient_camera_rotation()

        # ------------------------------------------------
        # 3️⃣ Category Diagram
        # ------------------------------------------------
        self.move_camera(phi=0, theta=0)

        M = Tex("$M$").shift(LEFT*3)
        N = Tex("$N$").shift(RIGHT*3)
        arrow = Arrow(M.get_right(), N.get_left())
        f = Tex("$f$").next_to(arrow, UP)

        diagram = VGroup(M, N, arrow, f)

        self.play(FadeIn(diagram))
        self.wait(3)
        self.play(FadeOut(diagram))

        # ------------------------------------------------
        # 4️⃣ Möbius Strip (Correct Surface)
        # ------------------------------------------------
        self.set_camera_orientation(phi=70*DEGREES, theta=-30*DEGREES)

        mobius = Surface(
            lambda u, v: np.array([
                (1 + v*np.cos(u/2))*np.cos(u),
                (1 + v*np.cos(u/2))*np.sin(u),
                v*np.sin(u/2)
            ]),
            u_range=[0, TAU],
            v_range=[-0.3, 0.3],
            resolution=(32, 16)
        )

        mobius.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.play(Create(mobius), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.2)

        non_text = Tex(r"\textbf{Non-Orientable!}")
        non_text.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(non_text)

        self.play(Write(non_text))
        self.wait(3)

        self.play(FadeOut(mobius), FadeOut(non_text))
        self.stop_ambient_camera_rotation()

        # ------------------------------------------------
        # 5️⃣ Hyperbolic Surface Final
        # ------------------------------------------------
        self.set_camera_orientation(phi=65*DEGREES, theta=-45*DEGREES)

        surface = Surface(
            lambda u, v: np.array([u, v, u**2 - v**2]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(32, 32)
        )

        surface.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.play(Create(surface), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.2)

        final = Tex(r"\textbf{Explore the Infinite!}")
        final.to_edge(DOWN)
        final.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.add_fixed_in_frame_mobjects(final)

        self.play(Write(final))
        self.wait(4)
