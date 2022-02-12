from fractions import Fraction

class RepresentableFraction(Fraction):
    def __init__(self, numerator: int, denominator: int) -> None:
        self.base_numerator = numerator
        self.base_denominator = denominator

    def to_LO_format(self, use_mixed: bool, answers_mode: bool = False):
        if answers_mode:
            numerator, denominator = self.numerator, self.denominator
        else:
            numerator, denominator = self.base_numerator, self.base_denominator

        negative = False
        if numerator * denominator < 0:
            negative = True
        numerator, denominator = abs(numerator), abs(denominator)

        if use_mixed and numerator > denominator:
            int_part = numerator // denominator
            numerator = numerator % denominator
            if numerator == 0:
                result = f'{{ {int_part} }}'
            else:
                result = f'{{ {{ {int_part} }} {{ {{ {numerator} }} over {{ {denominator} }} }} }}'
        else:
            result = f'{{ {{ {numerator} }} over {{ {denominator} }} }}'

        if negative:
            return f'( - {result} )'
        else:
            return result

    def __add__(self, other):
        res = super().__add__(other)
        return RepresentableFraction(res.numerator, res.denominator)

    def __sub__(self, other):
        res = super().__sub__(other)
        return RepresentableFraction(res.numerator, res.denominator)

    def __mul__(self, other):
        res = super().__mul__(other)
        return RepresentableFraction(res.numerator, res.denominator)

    def __truediv__(self, other):
        res = super().__truediv__(other)
        return RepresentableFraction(res.numerator, res.denominator)
