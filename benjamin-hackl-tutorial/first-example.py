from manim import *

class FirstExample(Scene):
    def construct(self):
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))

        self.add(ax)