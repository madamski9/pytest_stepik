#!/env/usr/bin python3

def czy_parzysta(liczba):
    return liczba % 2 == 0

def test_czy_parzysta():
	assert czy_parzysta(3) == False
	assert czy_parzysta(2) == True



