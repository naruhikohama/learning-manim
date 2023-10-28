from manim import * 

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        # next_to
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)
        self.add(red_dot, green_dot)

        # shift
        square = Square(color=ORANGE)
        square.shift(2*UP + 4*RIGHT)
        self.add(square)

        # move_to
        circle = Circle(color=PURPLE)
        circle.move_to([-3, -2, 0])
        self.add(circle)

        # align_to
        circle2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        circle3 = circle2.copy().set_color(YELLOW)
        circle4 = circle2.copy().set_color(ORANGE)
        circle2.align_to(square, UP)
        circle3.align_to(square, RIGHT)
        circle4.align_to(square, UP + RIGHT)
        self.add(circle2, circle3, circle4)

class CriticalPoints(Scene):
    def construct(self):
        c = Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)

        for d in [(0, 0, 0), UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))
        
        s = Square(color=RED, fill_opacity=0.5)
        s.move_to([1, 0, 0], aligned_edge=LEFT)
        self.add(s)

from manim.utils.unit import Percent, Pixels

class UsefulUnits(Scene):
    def construct(self):
        for perc in range(5, 51, 5):
            self.add(Circle(radius=perc * Percent(X_AXIS)))
            self.add(Square(side_length=2*perc * Percent(Y_AXIS), color=YELLOW))

        d = Dot()
        d.shift(100 * Pixels * RIGHT)
        self.add(d)

class Grouping(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN).next_to(red_dot, RIGHT)
        blue_dot = Dot(color=BLUE).next_to(red_dot, UP)
        dot_group = VGroup(red_dot, green_dot, blue_dot)

        dot_group.to_edge(RIGHT)
        self.add(dot_group)

        circles = VGroup(*[Circle(radius=0.2) for _ in range(10)])
        circles.arrange(UP)
        self.add(circles)

        stars = VGroup(*[Star(color=YELLOW, fill_opacity=1).scale(0.5) for _ in range(20)])
        stars.arrange_in_grid(5, 4, buff = 0.2)
        self.add(stars)