#!/env/usr/bin python3

def pole_kwadratu(bok):
    return bok * bok

def test_pole_kwadratu():
	assert pole_kwadratu(5) == 25
	assert pole_kwadratu(7) == 49

