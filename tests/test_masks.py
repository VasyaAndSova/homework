from src.masks import get_mask_card, get_mask_account


def test_get_mask_card(numbers_card):
    assert get_mask_card("7000792289606361") == numbers_card


def test_get_mask_account(numbers_account):
    assert get_mask_account("73654108430135874305") == numbers_account
