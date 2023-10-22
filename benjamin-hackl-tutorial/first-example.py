from manim import *

class FirstExample(Scene):
    def construct(self):
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
        curve = ax.plot(lambda x: (x + +2)*x*(x-2)/2, color=RED)
        area = ax.get_area(curve, x_range=(-2, 0), color=LIGHT_GRAY, opacity=0.2)
        self.add(ax, curve, area)