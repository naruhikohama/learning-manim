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
        
