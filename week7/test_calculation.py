from calculation import calculate_shipping_fee

def test_calculation_01():
    weight_unit = 'Pounds'
    weight = 1.0
    distance_unit = 'Kilometers'
    distance = 10
    selected_method = 'Standard'

    expected = 5.545
    actual = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert expected == actual


def test_calculation_02():
    weight_unit = 'Pounds'
    weight = -1.0
    distance_unit = 'Kilometers'
    distance = 10
    selected_method = 'Standard'

    try:
        actual = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
        assert False
    except ValueError as e:
        assert True
        assert e.args[0] == 'Weight must be greater than 0'