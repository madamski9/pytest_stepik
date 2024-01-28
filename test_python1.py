#!/usr/bin/env python3

def dodawanie(liczba1, liczba2):
	return liczba1+liczba2


def test_dodawanie():
	assert dodawanie(1,4) == 5
	assert dodawanie(2,-2) == 0



