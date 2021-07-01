class Simplex:
    def __init__(self, x1, y1, z1, x2, y2, z2, x3, y3, z3, operation):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.x3 = x3
        self.y3 = y3
        self.z3 = z3
        self.operation = operation

    def all_xyz(self):
        return [self.x1, self.y1, self.z1, self.x2, self.y2, self.z2, self.x3, self.y3, self.z3]

    def which_p_h(self):
        if self.z1 >= self.z2 and self.z1 >= self.z3:
            return 1
        elif self.z2 >= self.z1 and self.z2 >= self.z3:
            return 2
        elif self.z3 >= self.z1 and self.z3 >= self.z2:
            return 3

    def p_h(self):
        which_p_h = self.which_p_h()
        if which_p_h == 1:
            return self.x1, self.y1
        elif which_p_h == 2:
            return self.x2, self.y2
        elif which_p_h == 3:
            return self.x3, self.y3

    def z_without_zh(self):
        which_p_h = self.which_p_h()
        if which_p_h == 1:
            return self.z2, self.z3
        elif which_p_h == 2:
            return self.z1, self.z3
        elif which_p_h == 3:
            return self.z1, self.z2

    def f_p_h(self):
        which_p_h = self.which_p_h()
        if which_p_h == 1:
            return self.z1
        elif which_p_h == 2:
            return self.z2
        elif which_p_h == 3:
            return self.z3

    def which_p_l(self):
        if self.z1 <= self.z2 and self.z1 <= self.z3:
            return 1
        elif self.z2 <= self.z1 and self.z2 <= self.z3:
            return 2
        elif self.z3 <= self.z1 and self.z3 <= self.z2:
            return 3

    def p_l(self):
        which_p_l = self.which_p_l()
        if which_p_l == 1:
            return self.x1, self.y1
        elif which_p_l == 2:
            return self.x2, self.y2
        elif which_p_l == 3:
            return self.x3, self.y3

    def f_p_l(self):
        which_p_l = self.which_p_l()
        if which_p_l == 1:
            return self.z1
        elif which_p_l == 2:
            return self.z2
        elif which_p_l == 3:
            return self.z3

    def p_cen(self):
        if self.z1 >= self.z2 and self.z1 >= self.z3:
            return (self.x2 + self.x3) / 2, (self.y2 + self.y3) / 2
        elif self.z2 >= self.z1 and self.z2 >= self.z3:
            return (self.x1 + self.x3) / 2, (self.y1 + self.y3) / 2
        elif self.z3 >= self.z1 and self.z3 >= self.z2:
            return (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2

    def draw(self, surface):
        if self.operation == "start":
            surface.draw_simplex(self.all_xyz() + ["y"])
        elif self.operation == "reflection":
            surface.draw_simplex(self.all_xyz() + ["r"])
        elif self.operation == "contraction":
            surface.draw_simplex(self.all_xyz() + ["black"])
        elif self.operation == "expansion":
            surface.draw_simplex(self.all_xyz() + ["black"])

    def reflection_point(self, alpha):
        x_h, y_h = self.p_h()
        cen_x, cen_y = self.p_cen()
        new_x = (1 + alpha) * cen_x - alpha * x_h
        new_y = (1 + alpha) * cen_y - alpha * y_h
        return new_x, new_y

    def expansion_point(self, gamma, alpha):
        ref_x, ref_y = self.reflection_point(alpha)
        cen_x, cen_y = self.p_cen()
        new_x = (1 - gamma) * ref_x - gamma * cen_x
        new_y = (1 - gamma) * ref_y - gamma * cen_y
        return new_x, new_y

    def contraction_point(self, beta):
        x_h, y_h = self.p_h()
        cen_x, cen_y = self.p_cen()
        new_x = beta * x_h + (1 - beta) * cen_x
        new_y = beta * y_h + (1 - beta) * cen_y
        return new_x, new_y

    def new_point_instead_p_h(self, new_x, new_y, new_z, action):
        which_p_h = self.which_p_h()
        if which_p_h == 1:
            return Simplex(new_x, new_y, new_z, self.x2, self.y2, self.z2, self.x3, self.y3, self.z3, action)
        elif which_p_h == 2:
            return Simplex(self.x1, self.y1, self.z1, new_x, new_y, new_z, self.x3, self.y3, self.z3, action)
        elif which_p_h == 3:
            return Simplex(self.x1, self.y1, self.z1, self.x2, self.y2, self.z2, new_x, new_y, new_z, action)

    def reduction(self, f):
        x_l, y_l = self.p_l()
        self.x1 = (self.x1 + x_l) / 2
        self.x2 = (self.x2 + x_l) / 2
        self.x3 = (self.x3 + x_l) / 2
        self.y1 = (self.y1 + x_l) / 2
        self.y2 = (self.y2 + x_l) / 2
        self.y3 = (self.y3 + x_l) / 2
        self.z1 = f(self.x1, self.y1)
        self.z2 = f(self.x2, self.y2)
        self.z3 = f(self.x3, self.y3)