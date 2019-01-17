from random import choice


class Random_walk():

    def __init__(self, rw_number=5000):
        """初始化随机漫步的属性"""
        self.rw_number = rw_number

        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        rw_number_point = 1
        x_new_point = 0
        y_new_point = 0
        while rw_number_point < self.rw_number:
            rw_x_direction = [1,-1]
            rw_x_distance = [0, 1, 2, 3, 4]
            x_step = choice(rw_x_direction) * choice(rw_x_distance)

            rw_y_direction = [1, -1]
            rw_y_distance = [0, 1, 2, 3, 4]
            y_step = choice(rw_y_direction) * choice(rw_y_distance)

            if x_step == 0 and y_step == 0:
                continue

            #计算一次漫步的位置
            x_new_point = x_new_point + x_step
            y_new_point = y_new_point + y_step

            self.x_value.append(x_new_point)
            self.y_value.append(y_new_point)

            rw_number_point += 1





