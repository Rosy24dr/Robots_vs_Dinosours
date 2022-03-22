from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_one = Robot('Roberto')
        self.robots.append(robot_one)

        robot_two = Robot('Lin')
        self.robots.append(robot_two)

        robot_three = Robot('Zef')
        self.robots.append(robot_three)


# robot_list = Fleet()
# robot_list.create_fleet()
# print(robot_list.robots[0].name)
