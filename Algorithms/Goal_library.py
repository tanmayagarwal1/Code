from manimlib.imports import *
import math

###########################################################################################################################
                                        #BUILDERS 
################################################################################################################################
#This is a basic one sentence builder
class Basic_test_builder(Scene):
    def construct(self):
        t=TextMobject(self.value)
        t.scale(1)

        self.play(FadeIn(t))
        self.wait()

 ##This is used to build 3 text objects centered at the top
class builderForText_3(Scene):
    def construct(self):
        q=TextMobject(self.first)
        w=TextMobject(self.secon)
        e=TextMobject(self.third)
        q.scale(1)
        w.scale(1)
        e.scale(1)
        q.shift(2*UP)
        w.shift(2*UP)
        e.shift(2*UP)

        self.play(Write(q))
        self.wait(2)
        self.play(Transform(q,w))
        self.wait(2)
        self.play(Transform(q,e))
        self.wait(2)
        self.play(FadeOut(q))
        self.wait()
##This is used to build 3 latex equations
class latexfunc_builder_3(Scene):
    def construct(self):
        tex1=TexMobject(self.first)
        tex2=TexMobject(self.second)
        tex3=TexMobject(self.third)
        tex1.scale(1)
        tex2.scale(1)  
        tex3.scale(1)
        tex1.set_color_by_gradient(RED,YELLOW)
        tex2.set_color_by_gradient(BLUE,GREEN)
        tex3.set_color_by_gradient(BLUE,PURPLE)


        self.play(Write(tex1))
        self.wait(2)
        self.play(Transform(tex1,tex2))
        self.wait(2)
        self.play(Transform(tex1,tex3))
        self.wait(2)        
 #########################################################################################################################
                                   #A FEW TEST CASES
 #########################################################################################################################      

#very basic test scene 
class TestScene(Scene):
  def construct(self):  
    text = TextMobject("I literally h8 u.")
    text.scale(2)

    self.play(Write(text))
    self.wait()

# A quantum eq scene test 
class TestScene2(Scene):
  def construct(self):
    ex=TextMobject("This is a quantum harmoic oscillator")
    obj=TexMobject(r"\psi(x)=\int_{\infty}^{-\infty}{ \frac{1}{\sqrt{2\pi}}\cdot e^{ikx} \:\psi'(k)}")
    text = TexMobject(r"\phi (x)= 4\sqrt{\frac{mw}{\hbar\pi}} \cdot \frac{1}{\sqrt{2^n n!}} H_n(\sqrt{\frac{mw}{\hbar}}x)\cdot e^\frac{mwx^2}{2\hbar} ")
    text.scale(1)
    obj.scale(1)
    ex.scale(1)

    self.play(Write(ex))
    self.wait(2)
    self.play(Transform(ex,text))
    self.wait(2)
    self.play(Transform(ex,obj))
    self.wait(3)
    #self.play(FadeIn(obj))
    #self.wait()
    
#test for svgObjects
class TestScene3(Scene):
  def construct(self):
    bruh = SVGMobject("./thonk.svg")
    bruh.scale(2)

    self.play(Write(bruh))
    self.wait()

#some random test case 
class TestCase4(Scene):
    def construct(self):
        eq=TexMobject(r"\int_{a}^{b}{f(x)dx}")
        eq.scale(2)
        eq1=TexMobject(r"\sum_{n}{x^n}")
        eq1.scale(2)

        self.play(ShowCreation(eq))
        self.wait()
        self.play(Transform(eq,eq1))
        self.wait()
#some random test case part 2
class testcase(Scene):
    def construct(self):
        r=TextMobject("this is lower in case")
        r.scale(2)

        self.play(Write(r))
        self.wait()

#graphs
#To implement this create the two functions: func_to_graph and func_to_graph_2 and also create the necessary labels 
#will be disabling the lines and stuff #
class Graphing(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        #Make graph
        self.setup_axes(animate="TRUE")
        #in the get_graph method we pass our graphing function without any paranthesis 
        func_graph=self.get_graph(func_to_graph,self.function_color)
        func_graph.set_color_by_gradient(BLUE,PURPLE)
        #in the get_graph_label method we pass our label function with paranthesis 
        graph_lab = self.get_graph_label(func_graph, label =label_1())

        func_graph_2=self.get_graph(func_to_graph_2,self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label = label_2())


        #vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)
        #horz= self.get_vertical_line_to_graph(0,func_graph,color=YELLOW)

        #x = self.coords_to_point(1,self.func_to_graph(2))
        #y = self.coords_to_point(0,2)
        #horz_line = Line(x,y, color=YELLOW)

        #point = Dot(self.coords_to_point(2,2))

        #Display graph
        self.play(ShowCreation(func_graph),Write(graph_lab))
        self.wait(1)
        #self.play(ShowCreation(vert_line),ShowCreation(horz))
        #self.play(Write(point)) 

        self.play(Transform(func_graph, func_graph_2),Transform(graph_;ab,graph_lab_2))
        self.wait(2)



####################################################################################################################
                                        #BUILDERS AT WORK
####################################################################################################################        

#This is a basic one sentence builder
class builderclass(Basic_test_builder):
    CONFIG={
    "value":"this is  test for building using oop"

    } 
 ##This is used to build 3 text objects centered at the top       
class Text3Build(builderForText_3):
    CONFIG={
    "first":"this is equation one",
    "second":"this is equation to",  
    "third":"this is equation 3 "
    }

##This is used to build 3 latex equations
class buildlatex(latexfunc_builder_3):
    CONFIG={
    "first":r"\ket{\phi (x)}= 4\sqrt{\frac{mw}{\hbar\pi}} \cdot \frac{1}{\sqrt{2^n n!}} H_n(\sqrt{\frac{mw}{\hbar}}x)\cdot e^\frac{mwx^2}{2\hbar} ",
    "second":r"\int_{\infty}^{-\infty}{\frac{\tan(2x)\,\cos^4(2x)-\frac{\sin^4(2x)\,\cos^4(2x)}{\cos(2x)}}{e^{2\tan(x)\,\cos(4x)\,\sqrt{1-\sec^2(2x)}}}\sec^2(2x)dx}",
    "third":r"\psi_n(x)=\sum_{n}{C_n}{\phi_{e_n}}"


    }

 #############FUNCTIONS FOR THE GRAPHING CLASS########################################################################################   

def func_to_graph(x):
    return x**2

def func_to_graph_2(x):
    return x**3

def label_1():
    return "x^{2}"

def label_2():
    return "x^{3}"




  


