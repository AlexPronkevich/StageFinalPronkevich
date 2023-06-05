from entity.chrysanthemum import Chrysanthemum
from entity.gerbera import Gerbera
from entity.rose import Rose
from entity.alstroemeria import Alstroemeria
from entity.gypsophila import Gypsophila
from container.bouquet import Bouquet
from logic.shop_flower import ShopFlower


def main():
    bouquet = Bouquet()

    r = Rose("Pink", 55.0, 3.0)
    gerb = Gerbera("Yellow", 35.0, 6.0)
    chr = Chrysanthemum("Green", 30.0, 6.5)
    alst = Alstroemeria("Pink", 25.0, 8.5)
    gyp = Gypsophila("White", 10.0, 7.5)

    bouquet.add(r)
    bouquet.add(gerb)
    bouquet.add(chr)
    bouquet.add(alst)
    bouquet.add(gyp)

    print(bouquet)

    total_weight = ShopFlower.calculate_total_weight(bouquet)
    total_price = ShopFlower.calculate_total_price(bouquet)
    # max.price = ShopFlower.get_max_price(bouquet)
    # min.price = ShopFlower.get_min_price(bouquet)

    print(f"Total weight bouquet is {total_weight} gramm")
    print(f"Total price bouquet is {total_price} BYN")
    # print(f"The most expensive flower is {max.price} BYN")
    # print(f"The cheapest flower is {min.price} BYN")

if __name__ == "__main__":
    main()
