from entity.flower import Flower


class Bouquet:
    def __init__(self, flowers=None):
        if flowers:
            self.__flowers = flowers
        else:
            self.__flowers = []

    @property
    def size(self):
        return len(self.__flowers)

    def get_flower(self, index):
        if (isinstance(index, int) and index >= 0
                and index < self.size):
            return self.__flowers[index]

    def add(self, flower):
        if isinstance(flower, Flower):
            self.__flowers.append(flower)

    def __str__(self):
        msg = "List of flowers:"

        for i in range(self.size):
            msg += f"\n{i + 1}) " + str(self.__flowers[i])

        return msg

