from fractions import Fraction

class RepresentableFraction(Fraction):

    answers_mode = False

    def __init__(self, numerator: int, denominator: int) -> None:
        super().__init__(numerator, denominator)
        self.base_numerator = numerator
        self.base_denominator = denominator

    def to_LO_format(self, use_mixed: bool):
        if RepresentableFraction.answers_mode:
            numerator, denominator = self.numerator, self.denominator
        else:
            numerator, denominator = self.base_numerator, self.base_denominator

        negative = False
        if numerator * denominator < 0:
            negative = True
        numerator, denominator = abs(numerator), abs(denominator)

        if use_mixed:
            int_part = numerator // denominator
            numerator = numerator % denominator
            if negative:
                return f'(- {{ {{ {int_part} }} {{ {{ {numerator} }} over {{ {denominator} }} }} }})'
            else:
                return f'{{ {{ {int_part} }} {{ {{ {numerator} }} over {{ {denominator} }} }} }}'
        else:
            if negative:
                return f'(- {{ {{ {numerator} }} over {{ {denominator} }} }})'
            else:
                return f'{{ {{ {numerator} }} over {{ {denominator} }} }}'
