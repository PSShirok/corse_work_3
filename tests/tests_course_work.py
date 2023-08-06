from utils import get_date_sort, format_from, print_operations


def test_get_date_sort():
    assert get_date_sort() == ['2019-11-13T17:38:04.800051',
                               '2019-11-19T09:22:25.899614',
                               '2019-12-03T04:27:03.427014',
                               '2019-12-07T06:17:14.634890',
                               '2019-12-08T22:46:21.935582']


def test_format_from():
    assert format_from("Maestro 7810659855785568") == "Maestro 7810** **** 5568"
    assert format_from("Счет 659855785568") == "Счет **5568"


def test_print_operations():
    assert print_operations() is None
