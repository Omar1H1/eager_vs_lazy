
from manim import *

class Lazy(Scene):
    def construct(self):
        code_block = MarkupText(
            '''
            boolean isAdmin = <span fgcolor="red">false</span>;
            boolean hasAccess = <span fgcolor="green">true</span>;

            if(<span fgcolor="red">isAdmin</span> &amp;&amp; <span fgcolor="green">hasAccess</span>) {
                 // logique métier
            }

            ...// le reste du programme
            ''',
            font="CaskaydiaCove Nerd Font"
        ).scale(0.5)

        admin_status_text = Text("isAdmin").set_color(WHITE)
        access_status_text = Text("hasAccess").set_color(WHITE)
        method_rectangle = Rectangle(width=2, height=1)
        business_logic_text = Text("logique métier")

        admin_status_text.to_edge(LEFT)
        method_rectangle.to_edge(RIGHT)

        self.play(Create(code_block), rate_func=linear, run_time=5)
        self.wait(3)

        self.play(FadeOut(code_block))
        self.play(FadeIn(admin_status_text), FadeIn(access_status_text), FadeIn(method_rectangle))
        business_logic_text.move_to(method_rectangle.get_center())
        business_logic_text.scale(0.3)
        self.play(FadeIn(business_logic_text))
        self.wait()

        arrow_to_access = Arrow(start=admin_status_text.get_right(), end=access_status_text.get_left(), stroke_width=3.0)
        self.play(Create(arrow_to_access))
        self.wait()

        arrow_to_method = Arrow(start=access_status_text.get_right(), end=method_rectangle.get_left(), stroke_width=3.0)
        self.play(Create(arrow_to_method))
        self.wait()

        cross_mark = Cross(stroke_color=RED, stroke_width=6.0, scale_factor=0.5)
        midpoint = (admin_status_text.get_right() + access_status_text.get_left()) / 2
        cross_mark.move_to(midpoint)

        self.play(admin_status_text.animate.set_color(RED))
        self.wait()
        self.play(FadeIn(cross_mark))
        self.play(access_status_text.animate.set_color(GREEN))
        self.wait()
        self.play(access_status_text.animate.set_color(GREY_E), method_rectangle.animate.set_color(GREY_E), arrow_to_method.animate.set_color(GREY_E), business_logic_text.animate.set_color(GREY_E))    
        self.wait()

        group1 = VGroup(access_status_text, arrow_to_access, cross_mark, arrow_to_method, method_rectangle, business_logic_text)
        self.play(FadeOut(group1))
        self.wait()

        self.play(admin_status_text.animate.move_to(ORIGIN))
        self.wait()
        self.play(admin_status_text.animate.shift(UP * 2))

        remaining_code_rectangle = Rectangle(width=2, height=1)
        self.wait()

        remaining_code_text = Tex("le reste du programme").scale(0.3)
        remaining_code_text.move_to(remaining_code_rectangle.get_center())
        self.add(remaining_code_rectangle, remaining_code_text)
        self.wait()

        arrow_to_remaining_code = Arrow(start=admin_status_text.get_bottom(), end=remaining_code_rectangle.get_top())
        self.play(Create(arrow_to_remaining_code), rate_func=linear, run_time=2)
        self.wait(2)

        group3 = VGroup(admin_status_text, arrow_to_remaining_code, remaining_code_rectangle, remaining_code_text)
        payment_text = Tex("On paie pour ce qu'on consomme !!")
        self.play(TransformMatchingShapes(group3, payment_text), rate_func=linear, run_time=1.3)
        self.wait(3)
        self.remove(payment_text)

        evaluation_code_block = MarkupText(
            '''
            public class Evaluation {
            public static boolean evaluate(final int value) {

                System.out.println("evaluating ..." + value);
                <span fgcolor="red">TimeUnit.SECONDS.sleep(2);</span>
                return value > 100;

             }
             //...
            }
            ''',
            font="CaskaydiaCove Nerd Font"
        ).scale(0.25)

        self.play(FadeIn(evaluation_code_block), run_time=1.3, rate_func=smooth)

        evaluation_box = RoundedRectangle(width=6, height=4, fill_color=BLUE_E, fill_opacity=0.3, corner_radius=0.3)
        self.play(Write(evaluation_box), run_time=1.5)

        final_group = VGroup(evaluation_box, evaluation_code_block)
        self.wait(5)

        self.play(ScaleInPlace(final_group, 0.2))
        self.wait()

        self.play(final_group.animate.to_corner(UL))
        self.wait()

        eager_evaluator_code = MarkupText(
            '''  public static void eagerEvaluator (boolean input1, boolean input2) {
      System.out.println("eagerEvaluator called...");
      System.out.println("accept?: " + (input1 &amp;&amp; input2));
  }
            ''',
            font="CaskaydiaCove Nerd Font", font_size=35
        ).scale(0.25)
        self.wait()

        self.play(FadeIn(eager_evaluator_code), run_time=1.3, rate_func=smooth)

        eager_evaluator_box = RoundedRectangle(width=6, height=3, fill_color=BLUE_E, fill_opacity=0.3, corner_radius=0.3)
        self.play(Write(eager_evaluator_box), run_time=1.5)

        final_group2 = VGroup(eager_evaluator_code, eager_evaluator_box)

        self.wait(3)

        self.play(ScaleInPlace(final_group2, 0.2))

        self.wait()

        self.play(final_group2.animate.move_to(final_group.get_bottom() + DOWN * 0.5))

        self.wait()


        method_call = MarkupText('''eagerEvaluator(evaluate(27), evaluate(163));''', font="CaskaydiaCove Nerd Font", font_size=25)


        self.play(Write(method_call), run_time=1.3, rate_func=smooth)




        self.wait(4)

        console = RoundedRectangle(width=6, height= 2.5, corner_radius=0.2, fill_color=GREY_E, fill_opacity=0.2).shift(DOWN *2)


        self.add(console)

        self.wait()


        output =  MarkupText('''console output:''', font="CaskaydiaCove Nerd Font", font_size=15)

        output.move_to(console.get_corner(UL) + RIGHT * 1.1 + DOWN * 0.3)


        self.add(output)

        self.wait()

        
        first = MarkupText('''evaluating ...27''', font="CaskaydiaCove Nerd Font", font_size=10)
        second = MarkupText('''evaluating ...163''', font="CaskaydiaCove Nerd Font", font_size=10)
        third = MarkupText('''eagerEvaluator called..''', font="CaskaydiaCove Nerd Font", font_size=10)
        fourth = MarkupText('''accept?: <span fgcolor="red">false</span>''', font="CaskaydiaCove Nerd Font", font_size=10)

        timer_circle = Circle(radius=0.3, color=WHITE).shift(RIGHT * 2 + DOWN * 2)
        timer_text = Text("0", font_size=20).move_to(timer_circle.get_center())
        self.add(timer_circle, timer_text)
        self.wait()

        for i in range(1, 5):
            self.wait(1)

            first.move_to(output.get_bottom() + DOWN * 0.3).align_to(output, LEFT)
            self.add(first)

            if i == 2 or i == 4:
                new_timer_text = Text(str(i), font_size=20, color=RED).move_to(timer_circle.get_center())
            else:
                new_timer_text = Text(str(i), font_size=20).move_to(timer_circle.get_center())
            self.play(Transform(timer_text, new_timer_text), run_time=0.5)

            if i == 2:
                timer_circle.animate.scale(1.3)
                second.move_to(first.get_bottom() + DOWN * 0.1).align_to(first, LEFT)
                self.add(second)
            elif i == 4:
                third.move_to(second.get_bottom() + DOWN * 0.1).align_to(first, LEFT)
                fourth.move_to(third.get_bottom() + DOWN * 0.1).align_to(first, LEFT)
                self.add(third)
                self.add(fourth)

        self.wait(4)
        self.play(FadeOut(timer_circle), FadeOut(timer_text))
        self.wait()
