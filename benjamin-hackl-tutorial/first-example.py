from manim import *

class FirstExample(Scene):
    def construct(self):
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
        curve = ax.plot(lambda x: (x + +2)*x*(x-2)/2, color=RED)
        area = ax.get_area(curve, x_range=(-2, 0))

        self.play(Create(ax, run_time = 2)) # run_time inside can be inside Create() and is optional
        self.wait(0.75)
        self.play(Create(curve), run_time=3) # run_time outside Create(), and inside play(). Also optional
        self.wait(0.75)
        self.play(FadeIn(area))
        self.wait(2)
        # self.add(ax, curve, area)

class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(ReplacementTransform(green_square, blue_circle))
        self.play(Indicate(blue_circle))
        self.play(FadeOut(blue_circle))
        self.wait(2)


class SquareToCircle2(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))