from main import Figure
from Triangle import Triangle, sqrt
from Rectangle import Rectangle
from Square import Square
from Circle import Circle, pi
import pytest

triangle_test_params = [(10, 5, 13), (23, 11, 17)]
rectangle_test_params = [(5, 5), (12, 1)]
square_test_params = [100, 53]
circle_test_params = [123, 9]


class Test:
    pass


def test_attr_figure_class():
    fig = Figure("tr1")
    assert fig.name == "tr1"


@pytest.mark.parametrize("fig1", [Triangle("fig", 7, 3, 5), Rectangle("fig", 4, 8), Square("fig", 3), Circle("fig", 8)])
@pytest.mark.parametrize("fig2", [Triangle("fig", 7, 3, 5), Rectangle("fig", 4, 8), Square("fig", 3), Circle("fig", 8)])
def test_adding_positive(fig1, fig2):
    if isinstance(fig1, Figure) and isinstance(fig2, Figure):
        assert (fig1 + fig2) == (fig1.area + fig2.area)
    else:
        raise ValueError("One of operand isn't an instance of Figure class!")


@pytest.mark.xfail(raises=ValueError)
@pytest.mark.parametrize("fig1", [Triangle("fig", 7, 3, 5), Test(), Square("fig", 3), Test()])
@pytest.mark.parametrize("fig2", [Test(), Rectangle("fig", 4, 8), Square("fig", 3), Test()])
def test_adding_negative(fig1, fig2):
    if not isinstance(fig1, Figure):
        raise ValueError("Left operand isn't an instance of Figure class!")
    elif not isinstance(fig2, Figure):
        raise ValueError("Right operand isn't an instance of Figure class!")
    else:
        raise ValueError("Both operands aren't instances of Figure class!")


class TestTriangle:
    @pytest.mark.parametrize("side1, side2, side3", triangle_test_params)
    def test_triangle_positive(self, side1, side2, side3):
        tr = Triangle("tr1", side1, side2, side3)
        assert tr is not None and tr.side1 == side1 and tr.side2 == side2 and tr.side3 == side3

    @pytest.mark.xfail(raises=ValueError)
    @pytest.mark.parametrize("side1, side2, side3", [(2, 3, 6), (-10, 10, 13), (10, -10, 13), (10, 10, -13),
                                                     (-10, -10, -13), (0, 5, 13), (10, 0, 13), (10, 5, 0)])
    def test_triangle_negative(self, side1, side2, side3):
        assert Triangle("tr1", side1, side2, side3)

    @pytest.mark.parametrize("side1, side2, side3", triangle_test_params)
    def test_triangle_perimeter(self, side1, side2, side3):
        assert Triangle("tr1", side1, side2, side3).perimeter == side1 + side2 + side3

    # @pytest.mark.skipif(test_triangle_perimeter, reason="test's based on object perimeter method (Triangle.perimeter)")
    @pytest.mark.parametrize("side1, side2, side3", triangle_test_params)
    def test_triangle_area(self, side1, side2, side3):
        fig = Triangle("tr1", side1, side2, side3)
        half_perimeter = (side1 + side2 + side3) / 2
        assert fig.area == sqrt(half_perimeter * (half_perimeter - fig.side1) * (half_perimeter - fig.side2) *
                                (half_perimeter - fig.side3))


class TestRectangle:
    @pytest.mark.parametrize("side1, side2", rectangle_test_params)
    def test_rectangle_positive(self, side1, side2):
        rec = Rectangle("rec1", side1, side2)
        assert rec is not None

    @pytest.mark.xfail(raises=ValueError)
    @pytest.mark.parametrize("side1, side2", [(-3, 2), (3, -2), (-3, -2), (0, 2), (3, 0)])
    def test_rectangle_negative(self, side1, side2):
        assert Rectangle("rec1", side1, side2)

    @pytest.mark.parametrize("side1, side2", rectangle_test_params)
    def test_rectangle_perimeter(self, side1, side2):
        assert Rectangle("rec1", side1, side2).perimeter == side1 * 2 + side2 * 2

    @pytest.mark.parametrize("side1, side2", rectangle_test_params)
    def test_rectangle_area(self, side1, side2):
        assert Rectangle("rec1", side1, side2).area == side1 * side2


class TestSquare:
    @pytest.mark.parametrize("side", square_test_params)
    def test_square_positive(self, side):
        sq = Square("rec1", side)
        assert sq is not None

    @pytest.mark.xfail(raises=ValueError)
    @pytest.mark.parametrize("side", [-1, -800, 0])
    def test_square_negative(self, side):
        assert Square("rec1", side)

    @pytest.mark.parametrize("side", square_test_params)
    def test_square_perimeter(self, side):
        assert Square("rec1", side).perimeter == side * 4

    @pytest.mark.parametrize("side", square_test_params)
    def test_square_area(self, side):
        assert Square("rec1", side).area == side ** 2


class TestCircle:
    @pytest.mark.parametrize("radius", circle_test_params)
    def test_square_positive(self, radius):
        fig = Circle("fig1", radius)
        assert fig is not None

    @pytest.mark.xfail(raises=ValueError)
    @pytest.mark.parametrize("radius", [-1, -800, 0])
    def test_square_negative(self, radius):
        assert Circle("fig1", radius)

    @pytest.mark.parametrize("radius", circle_test_params)
    def test_square_perimeter(self, radius):
        assert Circle("fig1", radius).perimeter == 2 * pi * radius

    @pytest.mark.parametrize("radius", circle_test_params)
    def test_square_area(self, radius):
        assert Circle("fig1", radius).area == pi * radius ** 2
