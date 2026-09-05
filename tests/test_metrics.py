from datetime import date

from analise_eleitoral.metrics import age_at, age_bin, distribution, gini


def test_age_at_respects_birthday():
    assert age_at(date(1988, 8, 12), date(2026, 8, 11)) == 37
    assert age_at(date(1988, 8, 12), date(2026, 8, 12)) == 38


def test_age_bins():
    assert age_bin(29) == "<30"
    assert age_bin(30) == "30-39"
    assert age_bin(70) == "70+"
    assert age_bin(None) == "não informado"


def test_distribution_percentages():
    rows = distribution(["A", "A", "B"])
    assert rows[0]["categoria"] == "A"
    assert rows[0]["total"] == 2
    assert abs(sum(r["percentual"] for r in rows) - 100) < 0.01


def test_gini_boundaries():
    assert gini([10, 10, 10]) == 0
    value = gini([0, 0, 100])
    assert value is not None
    assert 0 < value < 1
