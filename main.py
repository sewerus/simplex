from math import sqrt

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from numpy import linspace, meshgrid

from surface_chart import SurfaceChart
from simplex import Simplex

import os, sys

def resource_path(relative_path):
  if hasattr(sys, '_MEIPASS'):
      return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath('.'), relative_path)


class WidgetSimplexTest(QDialog):
    def __init__(self, parent=None):
        super(WidgetSimplexTest, self).__init__(parent)

        self.steps = []
        self.current_step = 0

        self.originalPalette = QApplication.palette()

        layout = QHBoxLayout()

        # TOP LABELS

        chart_group_box = QGroupBox("Wykres funkcji i kolejne kroki metody")
        chart_box = QVBoxLayout()
        chart_group_box.setLayout(chart_box)

        menu_group_box = QGroupBox("Menu")
        menu_box = QVBoxLayout()
        menu_group_box.setLayout(menu_box)

        # GROUP BY SPLITTERS

        splitter_1 = QSplitter(Qt.Horizontal)
        splitter_1.addWidget(chart_group_box)
        splitter_1.addWidget(menu_group_box)
        splitter_1.setSizes([900, 200])
        layout.addWidget(splitter_1)

        # CHART

        chart_draw_group_box = QGroupBox("Wizualizacja:")
        chart_draw_box = QVBoxLayout()
        chart_draw_group_box.setLayout(chart_draw_box)
        chart_box.addWidget(chart_draw_group_box)

        self.chart = SurfaceChart()
        chart_draw_box.addWidget(self.chart)
    
        steps_group_box = QGroupBox("Etapy poszukiwania ekstremum:")
        steps_form = QVBoxLayout()
        steps_group_box.setLayout(steps_form)
        chart_box.addWidget(steps_group_box)

        data_steps_group_box = QWidget()
        steps_box = QHBoxLayout()
        data_steps_group_box.setLayout(steps_box)
        steps_form.addWidget(data_steps_group_box)

        point_0_column = QWidget()
        point_0_box = QVBoxLayout()
        point_0_column.setLayout(point_0_box)
        steps_box.addWidget(point_0_column)

        point_0_x_group_box = QWidget()
        point_0_x_layout = QHBoxLayout()
        point_0_x_group_box.setLayout(point_0_x_layout)
        point_0_box.addWidget(point_0_x_group_box)

        point_0_x_label = QLabel("x<sub>0</sub> = ")
        point_0_x_layout.addWidget(point_0_x_label)

        self.point_0_x = QLineEdit()
        self.point_0_x.setText("")
        self.point_0_x.setDisabled(True)
        point_0_x_layout.addWidget(self.point_0_x)

        point_0_y_group_box = QWidget()
        point_0_y_layout = QHBoxLayout()
        point_0_y_group_box.setLayout(point_0_y_layout)
        point_0_box.addWidget(point_0_y_group_box)

        point_0_y_label = QLabel("y<sub>0</sub> = ")
        point_0_y_layout.addWidget(point_0_y_label)

        self.point_0_y = QLineEdit()
        self.point_0_y.setText("")
        self.point_0_y.setDisabled(True)
        point_0_y_layout.addWidget(self.point_0_y)

        point_0_z_group_box = QWidget()
        point_0_z_layout = QHBoxLayout()
        point_0_z_group_box.setLayout(point_0_z_layout)
        point_0_box.addWidget(point_0_z_group_box)

        point_0_z_label = QLabel("f(x<sub>0</sub>y<sub>0</sub>) = ")
        point_0_z_layout.addWidget(point_0_z_label)

        self.point_0_z = QLineEdit()
        self.point_0_z.setText("")
        self.point_0_z.setDisabled(True)
        point_0_z_layout.addWidget(self.point_0_z)

        point_1_column = QWidget()
        point_1_box = QVBoxLayout()
        point_1_column.setLayout(point_1_box)
        steps_box.addWidget(point_1_column)

        point_1_x_group_box = QWidget()
        point_1_x_layout = QHBoxLayout()
        point_1_x_group_box.setLayout(point_1_x_layout)
        point_1_box.addWidget(point_1_x_group_box)

        point_1_x_label = QLabel("x<sub>1</sub> = ")
        point_1_x_layout.addWidget(point_1_x_label)

        self.point_1_x = QLineEdit()
        self.point_1_x.setText("")
        self.point_1_x.setDisabled(True)
        point_1_x_layout.addWidget(self.point_1_x)

        point_1_y_group_box = QWidget()
        point_1_y_layout = QHBoxLayout()
        point_1_y_group_box.setLayout(point_1_y_layout)
        point_1_box.addWidget(point_1_y_group_box)

        point_1_y_label = QLabel("y<sub>1</sub> = ")
        point_1_y_layout.addWidget(point_1_y_label)

        self.point_1_y = QLineEdit()
        self.point_1_y.setText("")
        self.point_1_y.setDisabled(True)
        point_1_y_layout.addWidget(self.point_1_y)

        point_1_z_group_box = QWidget()
        point_1_z_layout = QHBoxLayout()
        point_1_z_group_box.setLayout(point_1_z_layout)
        point_1_box.addWidget(point_1_z_group_box)

        point_1_z_label = QLabel("f(x<sub>1</sub>y<sub>1</sub>) = ")
        point_1_z_layout.addWidget(point_1_z_label)

        self.point_1_z = QLineEdit()
        self.point_1_z.setText("")
        self.point_1_z.setDisabled(True)
        point_1_z_layout.addWidget(self.point_1_z)

        point_2_column = QWidget()
        point_2_box = QVBoxLayout()
        point_2_column.setLayout(point_2_box)
        steps_box.addWidget(point_2_column)

        point_2_x_group_box = QWidget()
        point_2_x_layout = QHBoxLayout()
        point_2_x_group_box.setLayout(point_2_x_layout)
        point_2_box.addWidget(point_2_x_group_box)

        point_2_x_label = QLabel("x<sub>2</sub> = ")
        point_2_x_layout.addWidget(point_2_x_label)

        self.point_2_x = QLineEdit()
        self.point_2_x.setText("")
        self.point_2_x.setDisabled(True)
        point_2_x_layout.addWidget(self.point_2_x)

        point_2_y_group_box = QWidget()
        point_2_y_layout = QHBoxLayout()
        point_2_y_group_box.setLayout(point_2_y_layout)
        point_2_box.addWidget(point_2_y_group_box)

        point_2_y_label = QLabel("y<sub>2</sub> = ")
        point_2_y_layout.addWidget(point_2_y_label)

        self.point_2_y = QLineEdit()
        self.point_2_y.setText("")
        self.point_2_y.setDisabled(True)
        point_2_y_layout.addWidget(self.point_2_y)

        point_2_z_group_box = QWidget()
        point_2_z_layout = QHBoxLayout()
        point_2_z_group_box.setLayout(point_2_z_layout)
        point_2_box.addWidget(point_2_z_group_box)

        point_2_z_label = QLabel("f(x<sub>2</sub>y<sub>2</sub>) = ")
        point_2_z_layout.addWidget(point_2_z_label)

        self.point_2_z = QLineEdit()
        self.point_2_z.setText("")
        self.point_2_z.setDisabled(True)
        point_2_z_layout.addWidget(self.point_2_z)

        steps_buttons_column = QWidget()
        steps_buttons_box = QVBoxLayout()
        steps_buttons_column.setLayout(steps_buttons_box)
        steps_box.addWidget(steps_buttons_column)

        step_count_box = QWidget()
        step_count_layout = QHBoxLayout()
        step_count_box.setLayout(step_count_layout)
        steps_buttons_box.addWidget(step_count_box)

        step_count_label = QLabel("Krok: ")
        step_count_layout.addWidget(step_count_label)

        self.step_count = QLabel("")
        step_count_layout.addWidget(self.step_count)

        operation_title_box = QWidget()
        operation_title_layout = QHBoxLayout()
        operation_title_box.setLayout(operation_title_layout)
        steps_buttons_box.addWidget(operation_title_box)

        operation_title_label = QLabel("Operacja: ")
        operation_title_layout.addWidget(operation_title_label)

        self.operation_title = QLabel("")
        operation_title_layout.addWidget(self.operation_title)

        founded_min_box = QWidget()
        founded_min_layout = QHBoxLayout()
        founded_min_box.setLayout(founded_min_layout)
        steps_buttons_box.addWidget(founded_min_box)

        founded_min_label = QLabel("Minimum: ")
        founded_min_layout.addWidget(founded_min_label)

        self.founded_min = QLabel("")
        founded_min_layout.addWidget(self.founded_min)

        self.previous_step_button = QPushButton("Poprzedni krok")
        self.previous_step_button.setCheckable(False)
        self.previous_step_button.setDisabled(True)
        self.previous_step_button.clicked.connect(self.draw_previous_step)
        steps_buttons_box.addWidget(self.previous_step_button)

        self.next_step_button = QPushButton("Następny krok")
        self.next_step_button.setCheckable(False)
        self.next_step_button.setDisabled(True)
        self.next_step_button.clicked.connect(self.draw_next_step)
        steps_buttons_box.addWidget(self.next_step_button)

        self.steps_slider = QSlider(Qt.Horizontal)
        self.steps_slider.setMinimum(0)
        self.steps_slider.setMaximum(0)
        self.steps_slider.setSingleStep(1)
        self.steps_slider.setDisabled(True)
        self.steps_slider.setTickInterval(True)
        self.steps_slider.setTickPosition(QSlider.TicksBelow)
        self.steps_slider.sliderReleased.connect(self.draw_by_slider)
        steps_form.addWidget(self.steps_slider)

        # MENU

        # f

        f_group_box = QGroupBox("Funkcja celu:")
        f_layout = QHBoxLayout()
        f_group_box.setLayout(f_layout)
        menu_box.addWidget(f_group_box)

        f_label = QLabel("f(x, y) = ")
        f_layout.addWidget(f_label)

        self.f_text = QLineEdit()
        self.f_text.setText("x*x + y*y - 3/2*x*y")
        f_layout.addWidget(self.f_text)

        # x0, y0

        x0y0_group_box = QGroupBox("Arbitralnie wybrany punkt startowy:")
        x0y0_layout = QVBoxLayout()

        x0y0_group_box.setLayout(x0y0_layout)
        menu_box.addWidget(x0y0_group_box)

        x0_group_box = QWidget()
        x0_layout = QHBoxLayout()
        x0_group_box.setLayout(x0_layout)
        x0y0_layout.addWidget(x0_group_box)

        y0_group_box = QWidget()
        y0_layout = QHBoxLayout()
        y0_group_box.setLayout(y0_layout)
        x0y0_layout.addWidget(y0_group_box)

        x0_label = QLabel("x<sub>0</sub> = ")
        x0_label.setFixedWidth(30)
        x0_layout.addWidget(x0_label)

        self.x0 = QDoubleSpinBox()
        self.x0.setValue(5)
        self.x0.setMinimum(-1000.0)
        self.x0.setMaximum(1000.0)
        self.x0.setSingleStep(0.01)
        x0_layout.addWidget(self.x0)

        y0_label = QLabel("y<sub>0</sub> = ")
        y0_label.setFixedWidth(30)
        y0_layout.addWidget(y0_label)

        self.y0 = QDoubleSpinBox()
        self.y0.setValue(45)
        self.y0.setMinimum(-1000.0)
        self.y0.setMaximum(1000.0)
        self.y0.setSingleStep(0.01)
        y0_layout.addWidget(self.y0)

        # d

        d_group_box = QGroupBox("Początkowa odległość pomiędzy wierzchołkami Simplexu:")
        d_layout = QHBoxLayout()
        d_group_box.setLayout(d_layout)
        menu_box.addWidget(d_group_box)

        d_label = QLabel("d = ")
        d_label.setFixedWidth(30)
        d_layout.addWidget(d_label)

        self.d = QDoubleSpinBox()
        self.d.setMinimum(0)
        self.d.setValue(15)
        self.d.setSingleStep(0.01)
        d_layout.addWidget(self.d)

        # alpha

        alpha_group_box = QGroupBox("Współczynnik odbicia (\u03B1 > 0):")
        alpha_layout = QHBoxLayout()
        alpha_group_box.setLayout(alpha_layout)
        menu_box.addWidget(alpha_group_box)

        alpha_label = QLabel("\u03B1 = ")
        alpha_label.setFixedWidth(30)
        alpha_layout.addWidget(alpha_label)

        self.alpha = QDoubleSpinBox()
        self.alpha.setMinimum(0)
        self.alpha.setValue(1)
        self.alpha.setSingleStep(0.01)
        alpha_layout.addWidget(self.alpha)

        # beta

        beta_group_box = QGroupBox("Współczynnik kontrakcji (0 < \u03B2 < 1):")
        beta_layout = QHBoxLayout()
        beta_group_box.setLayout(beta_layout)
        menu_box.addWidget(beta_group_box)

        beta_label = QLabel("\u03B2 = ")
        beta_label.setFixedWidth(30)
        beta_layout.addWidget(beta_label)

        self.beta = QDoubleSpinBox()
        self.beta.setMinimum(0)
        self.beta.setMaximum(1)
        self.beta.setValue(0.5)
        self.beta.setSingleStep(0.01)
        beta_layout.addWidget(self.beta)

        # gamma

        gamma_group_box = QGroupBox("Współczynnik ekspansji (\u03B3 > 1):")
        gamma_layout = QHBoxLayout()
        gamma_group_box.setLayout(gamma_layout)
        menu_box.addWidget(gamma_group_box)

        gamma_label = QLabel("\u03B3 = ")
        gamma_label.setFixedWidth(30)
        gamma_layout.addWidget(gamma_label)

        self.gamma = QDoubleSpinBox()
        self.gamma.setMinimum(1)
        self.gamma.setValue(2)
        self.gamma.setSingleStep(0.01)
        gamma_layout.addWidget(self.gamma)

        # epsilon

        epsilon_group_box = QGroupBox("Wymagana dokładność:")
        epsilon_layout = QHBoxLayout()
        epsilon_group_box.setLayout(epsilon_layout)
        menu_box.addWidget(epsilon_group_box)

        epsilon_label = QLabel("\u03B5 = ")
        epsilon_label.setFixedWidth(30)
        epsilon_layout.addWidget(epsilon_label)

        self.epsilon = QDoubleSpinBox()
        self.epsilon.setValue(1)
        self.epsilon.setSingleStep(0.01)
        epsilon_layout.addWidget(self.epsilon)

        make_research_test_group_box = QGroupBox("Zastosuj podane parametry i przeprowadź badanie:")
        research_test_box = QVBoxLayout()
        make_research_test_group_box.setLayout(research_test_box)
        menu_box.addWidget(make_research_test_group_box)

        make_research_test_button = QPushButton("Przeprowadź badanie")
        make_research_test_button.setCheckable(False)
        make_research_test_button.clicked.connect(self.make_research)
        research_test_box.addWidget(make_research_test_button)

        self.setLayout(layout)
        self.setWindowTitle("Metoda Neldera-Meada")
        self.showMaximized()
        self.setFocus()
        self.draw_graph()
        systray_icon = QIcon(resource_path("icon.png"))
        systray = QSystemTrayIcon(systray_icon, self)
        menu = QMenu()
        close = QAction("Close", self)
        menu.addAction(close)
        systray.setContextMenu(menu)
        systray.show()
        # systray.showMessage("Simplex", "Program powstał w czasie pandemii 2020.", QSystemTrayIcon.Information)
        close.triggered.connect(self.close)

    def f(self, a, b):
        x = a
        y = b
        return eval(self.f_text.text())

    def draw_graph(self):
        x_min, x_max, y_min, y_max = self.x0.value(), self.x0.value(), self.y0.value(), self.y0.value()
        for simplex in self.steps:
            x_arr = [simplex.x1, simplex.x2, simplex.x3]
            simplex_x_min = min(x_arr)
            simplex_x_max = max(x_arr)
            y_arr = [simplex.y1, simplex.y2, simplex.y3]
            simplex_y_min = min(y_arr)
            simplex_y_max = max(y_arr)
            if simplex_x_min < x_min:
                x_min = simplex_x_min
            if simplex_x_max > x_max:
                x_max = simplex_x_max
            if simplex_y_min < y_min:
                y_min = simplex_y_min
            if simplex_y_max > y_max:
                y_max = simplex_y_max
        x = linspace(x_min-5, x_max+5, 80)  # X coordinates
        y = linspace(y_min-5, y_max+5, 80)  # Y coordinates
        X, Y = meshgrid(x, y)  # Forming MeshGrid
        Z = self.f(X, Y)
        self.chart.draw_graph(X, Y, Z)  # call Fun for Graph plot

    def is_end(self):
        epsilon = self.epsilon.value()
        if self.steps == 0:
            return False
        [x1, y1, z1, x2, y2, z2, x3, y3, z3] = self.steps[-1].all_xyz()
        if (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2) > epsilon*epsilon:
            return False
        elif (x1 - x3)*(x1 - x3) + (y1 - y3)*(y1 - y3) > epsilon*epsilon:
            return False
        elif (x2 - x3)*(x2 - x3) + (y2 - y3)*(y2 - y3) > epsilon*epsilon:
            return False
        else:
            return True

    def make_research(self):
        self.current_step = 0
        self.steps.clear()
        alpha = self.alpha.value()
        beta = self.beta.value()
        gamma = self.gamma.value()

        # 1 # calc first vertices
        d = self.d.value()
        delta1 = (sqrt(3)+1)/2/sqrt(2)*d
        delta2 = (sqrt(3)-1)/2/sqrt(2)*d
        x0 = self.x0.value()
        y0 = self.y0.value()
        x1 = x0 + delta2
        y1 = y0 + delta1
        x2 = x0 + delta1
        y2 = y0 + delta2

        # 2 # calc f in each points
        self.steps.append(Simplex(x0, y0, self.f(x0, y0), x1, y1, self.f(x1, y1), x2, y2, self.f(x2, y2), "start"))
        self.steps[-1].draw(self.chart)

        # reflection
        while not(self.is_end()):
            simplex = self.steps[-1]

            # 3 # find h and l
            x_h, y_h = simplex.p_h()
            f_h = simplex.f_p_h()
            x_l, y_l = simplex.p_l()
            f_l = simplex.f_p_l()

            # 4 # calc cen
            cen_x, cen_y = simplex.p_cen()

            # 5 # make reflection
            ref_x, ref_y = simplex.reflection_point(alpha)

            # 6 # calc f_s and f_o
            f_s = self.f(cen_x, cen_y)
            f_o = self.f(ref_x, ref_y)

            # 7 #
            if f_o < f_l:
                # 7.1 # calc expansion point
                exp_x, exp_y = simplex.expansion_point(gamma, alpha)
                f_exp = self.f(exp_x, exp_y)
                # 7.2 #
                if f_exp < f_h:
                    # 7.2.1 #
                    self.steps.append(simplex.new_point_instead_p_h(exp_x, exp_y, f_exp, "expansion"))
                    self.steps[-1].draw(self.chart)
                # 7.3 #
                else:
                    # 7.3.1 #
                    self.steps.append(simplex.new_point_instead_p_h(ref_x, ref_y, f_o, "reflection"))
                    self.steps[-1].draw(self.chart)
                # 7.4 #
                continue
            # 8 #
            else:
                # 8.1 #
                z_no_zh_1, z_no_zh_2 = simplex.z_without_zh()
                if not(f_o >= z_no_zh_1 and f_o >= z_no_zh_2):
                    self.steps.append(simplex.new_point_instead_p_h(ref_x, ref_y, f_o, "reflection"))
                    self.steps[-1].draw(self.chart)
                    continue

                # 8.2 #
                if f_o < f_h:
                    # 8.2.1 #
                    simplex = simplex.new_point_instead_p_h(ref_x, ref_y, f_o, "reflection")
                    x_h, y_h = simplex.p_h()
                    f_h = simplex.f_p_h()
                    x_l, y_l = simplex.p_l()
                    f_l = simplex.f_p_l()

                    # 4 # calc cen
                    cen_x, cen_y = simplex.p_cen()

                    # 5 # make reflection
                    ref_x, ref_y = simplex.reflection_point(alpha)

                    # 6 # calc f_s and f_o
                    f_s = self.f(cen_x, cen_y)
                    f_o = self.f(ref_x, ref_y)
                # 8.3 #
                contr_x, contr_y = simplex.contraction_point(beta)
                f_k = self.f(contr_x, contr_y)
                # 8.4 #
                if f_k >= simplex.f_p_h():
                    # 8.4.1 #
                    simplex.reduction(self.f)
                    # 8.4.2 #
                    # 8.6 #
                    continue
                # 8.5 #
                else:
                    # 8.5.1 #
                    self.steps.append(simplex.new_point_instead_p_h(contr_x, contr_y, f_k, "contraction"))
                    self.steps[-1].draw(self.chart)
                    continue

        self.draw_graph()
        self.prepare_steps()

    # it works but with wrong result
    def old_make_research(self):
        self.current_step = 0
        self.steps.clear()
        alpha = self.alpha.value()
        beta = self.beta.value()
        gamma = self.gamma.value()

        # 1 # calc first vertices
        d = self.d.value()
        delta1 = (sqrt(3)+1)/2/sqrt(2)*d
        delta2 = (sqrt(3)-1)/2/sqrt(2)*d
        x0 = self.x0.value()
        y0 = self.y0.value()
        x1 = x0 + delta2
        y1 = y0 + delta1
        x2 = x0 + delta1
        y2 = y0 + delta2

        # 2 # calc f in each points
        self.steps.append(Simplex(x0, y0, self.f(x0, y0), x1, y1, self.f(x1, y1), x2, y2, self.f(x2, y2), "start"))
        self.steps[-1].draw(self.chart)

        # reflection
        while not(self.is_end()):
            simplex = self.steps[-1]

            # 3 # find h and l
            x_h, y_h = simplex.p_h()
            f_h = simplex.f_p_h()
            x_l, y_l = simplex.p_l()
            f_l = simplex.f_p_l()

            # 4 # calc cen
            cen_x, cen_y = simplex.p_cen()

            # 5 # make reflection
            ref_x, ref_y = simplex.reflection_point(alpha)

            # 6 # calc f_s and f_o
            f_s = self.f(cen_x, cen_y)
            f_o = self.f(ref_x, ref_y)

            # 7 #
            if f_o < f_l:
                # 7.1 # calc expansion point
                exp_x, exp_y = simplex.expansion_point(gamma, alpha)
                f_exp = self.f(exp_x, exp_y)
                # 7.2 #
                if f_exp < f_h:
                    # 7.2.1 #
                    self.steps.append(simplex.new_point_instead_p_h(exp_x, exp_y, f_exp, "expansion"))
                    self.steps[-1].draw(self.chart)
                # 7.3 #
                else:
                    # 7.3.1 #
                    self.steps.append(simplex.new_point_instead_p_h(ref_x, ref_y, f_o, "reflection"))
                    self.steps[-1].draw(self.chart)
                # 7.4 #
                continue
            # 8 #
            else:
                # 8.1 #
                z_no_zh_1, z_no_zh_2 = simplex.z_without_zh()
                if not(f_o >= z_no_zh_1 and f_o >= z_no_zh_2):
                    # 8.2 #
                    if f_o < f_h:
                        # 8.2.1 #
                        simplex = simplex.new_point_instead_p_h(ref_x, ref_y, f_o, "reflection")
                # 8.3 #
                contr_x, contr_y = simplex.contraction_point(beta)
                f_k = self.f(contr_x, contr_y)
                # 8.4 #
                if f_k >= simplex.f_p_h():
                    # 8.4.1 #
                    simplex.reduction(self.f)
                    # 8.4.2 #
                    # 8.6 #
                    if f_o < simplex.f_p_l():
                        # 8.6.1 #
                        self.steps.append(simplex.new_point_instead_p_h(ref_x, ref_y, f_o, "reflection"))
                        self.steps[-1].draw(self.chart)
                # 8.5 #
                else:
                    # 8.5.1 #
                    self.steps.append(simplex.new_point_instead_p_h(contr_x, contr_y, f_k, "contraction"))
                    self.steps[-1].draw(self.chart)

            print(self.steps[-1].all_xyz())
            print(self.steps[-1].f_p_l())
        self.draw_graph()
        self.prepare_steps()

    def prepare_steps(self):
        self.previous_step_button.setDisabled(False)
        self.next_step_button.setDisabled(False)
        self.steps_slider.setDisabled(False)
        self.steps_slider.setMaximum(len(self.steps)-1)
        self.draw_to_step(len(self.steps) - 1)

    def draw_to_step(self, step_number):
        self.draw_graph()
        self.current_step = step_number
        self.steps_slider.setValue(step_number)

        for n in range(step_number+1):
            self.steps[n].draw(self.chart)
        self.update_visualisation_form(step_number)

    def update_visualisation_form(self, step_number):
        last_step_simplex = self.steps[step_number]
        self.point_0_x.setText(str(round(last_step_simplex.x1, 2)))
        self.point_0_y.setText(str(round(last_step_simplex.y1, 2)))
        self.point_0_z.setText(str(round(last_step_simplex.z1, 2)))
        self.point_1_x.setText(str(round(last_step_simplex.x2, 2)))
        self.point_1_y.setText(str(round(last_step_simplex.y2, 2)))
        self.point_1_z.setText(str(round(last_step_simplex.z2, 2)))
        self.point_2_x.setText(str(round(last_step_simplex.x3, 2)))
        self.point_2_y.setText(str(round(last_step_simplex.y3, 2)))
        self.point_2_z.setText(str(round(last_step_simplex.z3, 2)))
        self.step_count.setText(str(self.current_step+1))
        if last_step_simplex.operation == "start":
            self.operation_title.setText("Start")
        elif last_step_simplex.operation == "reflection":
            self.operation_title.setText("Odbicie")
        elif last_step_simplex.operation == "contraction":
            self.operation_title.setText("Kontrakcja")
        elif last_step_simplex.operation == "expansion":
            self.operation_title.setText("Ekspansja")
        self.founded_min.setText(str(round(last_step_simplex.f_p_l(), 2)))
        if self.current_step == len(self.steps)-1:
            self.next_step_button.setDisabled(True)
        else:
            self.next_step_button.setDisabled(False)
        if self.current_step == 0:
            self.previous_step_button.setDisabled(True)
        else:
            self.previous_step_button.setDisabled(False)



    def draw_next_step(self):
        self.current_step += 1
        self.steps_slider.setValue(self.current_step)
        self.steps[self.current_step].draw(self.chart)
        self.update_visualisation_form(self.current_step)

    def draw_previous_step(self):
        self.current_step -= 1
        self.steps_slider.setValue(self.current_step)
        self.draw_graph()
        self.draw_to_step(self.current_step)

    def draw_by_slider(self):
        if self.current_step > self.steps_slider.value():
            self.current_step = self.steps_slider.value()
            self.draw_to_step(self.current_step)
        else:
            for n in range(self.current_step+1, self.steps_slider.value()):
                self.draw_next_step()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    simplex_test = WidgetSimplexTest()
    simplex_test.show()
sys.exit(app.exec_())
