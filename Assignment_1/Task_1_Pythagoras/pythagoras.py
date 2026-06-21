from manim import *

class PythagoreanProofAnimation(Scene):
    def construct(self):
        # 1. Setup the triangle's corner points
        pt_origin = ORIGIN
        pt_base = RIGHT * 4
        pt_height = UP * 3

        # 2. Draw the three edges
        base_edge = Line(pt_origin, pt_base, color=BLUE)
        height_edge = Line(pt_origin, pt_height, color=RED)
        hypotenuse_edge = Line(pt_height, pt_base, color=GREEN)

        # 3. Build the core right-triangle shape
        main_triangle = Polygon(pt_origin, pt_base, pt_height, stroke_width=2, fill_opacity=0.1, fill_color=WHITE)

        # 4. Add the 90-degree corner marker
        corner_sq = RightAngle(base_edge, height_edge, length=0.3, color=YELLOW)

        # 5. Label the edges (Native Text used to prevent LaTeX compiler errors)
        text_a = Text("a", color=RED).next_to(height_edge, LEFT, buff=0.2)
        text_b = Text("b", color=BLUE).next_to(base_edge, DOWN, buff=0.2)
        text_c = Text("c", color=GREEN).next_to(hypotenuse_edge, UR, buff=0.1)

        # 6. Create the area squares for each side
        # Square extending from the base (b)
        sq_base = Square(side_length=4, stroke_color=BLUE, fill_color=BLUE, fill_opacity=0.3)
        sq_base.next_to(base_edge, DOWN, buff=0)

        # Square extending from the height (a)
        sq_height = Square(side_length=3, stroke_color=RED, fill_color=RED, fill_opacity=0.3)
        sq_height.next_to(height_edge, LEFT, buff=0)

        # Square attached to the hypotenuse (c)
        sq_hypotenuse = Square(side_length=5, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.3)
        tilt_angle = hypotenuse_edge.get_angle()
        sq_hypotenuse.rotate(tilt_angle)
        
        # Snapping the rotated square perfectly to the diagonal line
        sq_hypotenuse.move_to(hypotenuse_edge.get_center()).shift(UP * 1.2 + RIGHT * 1.6)

        # 7. Display the main formula at the top left
        main_formula = Text("a² + b² = c²", t2c={"a²": RED, "b²": BLUE, "c²": GREEN})
        main_formula.to_corner(UL)

        # 8. Render the animation sequence
        self.play(Write(main_formula))
        self.wait(0.6)

        self.play(Create(main_triangle), Create(corner_sq))
        self.play(Write(text_a), Write(text_b), Write(text_c))
        self.wait(1.2)

        self.play(FadeIn(sq_height, shift=LEFT), run_time=1.4)
        self.play(FadeIn(sq_base, shift=DOWN), run_time=1.4)
        self.play(FadeIn(sq_hypotenuse), run_time=1.4)
        
        self.wait(3)
