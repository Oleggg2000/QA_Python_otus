from src.main import Figure
from src.Triangle import Triangle, sqrt
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
import pytest


class TestTriangle:
    def test_attr_figure_class(self):
        fig = Figure("tr1")
        assert fig.name == "tr1"

    @pytest.mark.parametrize("name, side1, side2, side3", [("tr1", 10, 5, 13), ("tr2", 23, 11, 17)])
    def test_triangle_positive(self, name, side1, side2, side3):
        tr = Triangle(name, side1, side2, side3)
        assert tr is not None and tr.side1 == side1 and tr.side2 == side2 and tr.side3 == side3

    @pytest.mark.xfail(raises=ValueError)
    @pytest.mark.parametrize("name, side1, side2, side3", [("tr1", 2, 3, 6), ("tr2", 5, 7, 13)])
    def test_triangle_negative(self, name, side1, side2, side3):
        assert Triangle(name, side1, side2, side3)

    @pytest.mark.parametrize("name, side1, side2, side3", [("tr1", 10, 5, 13), ("tr2", 23, 11, 17)])
    def test_triangle_perimeter(self, name, side1, side2, side3):
        assert Triangle(name, side1, side2, side3).perimeter == side1 + side2 + side3

    # @pytest.mark.skipif(test_triangle_perimeter, reason="test's based on object perimeter method (Triangle.perimeter)")
    @pytest.mark.parametrize("name, side1, side2, side3", [("tr1", 10, 5, 13), ("tr2", 23, 11, 17)])
    def test_triangle_area(self, name, side1, side2, side3):
        fig = Triangle(name, side1, side2, side3)
        half_perimeter = (side1 + side2 + side3) / 2
        assert fig.area == sqrt(half_perimeter * (half_perimeter - fig.side1) * (half_perimeter - fig.side2) *
                                (half_perimeter - fig.side3))
