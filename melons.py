"""Classes for melon orders."""
from random import randint
import datetime


class AbstractMelonOrder():
    """An abstract melon order class"""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.currentdate = datetime.datetime.now()

    def get_total(self):
        base_price = self.get_base_price()
        if self.species == "Christmas":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        self.shipped = True

    def get_base_price(self):
        base_price = randint(5, 9)
        if self.is_rush_hour():
            return base_price + 4
        return base_price

    def is_rush_hour(self):
        if self.currentdate.weekday() < 5:
            if self.currentdate.hour >= 8 and self.currentdate.hour <= 11:
                return True
        return False


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        return self.country_code

    def get_total(self):
        total = super().get_total()
        if self.qty < 10:
            total += 3
        return total


class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0.0
    passed_inspection = False
    order_type = "government"

    def mark_inspection(passed):
        if passed:
            self.passed_inspection = True


order = DomesticMelonOrder("crenshaw", 100)
print(order.get_total())