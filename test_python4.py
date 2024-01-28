#!/env/usr/bin python3
import pytest

def powitanie(imie):
    return f"Witaj, {imie}!"


def test_powitanie():
	assert powitanie("maciek") == "Witaj, maciek!"


