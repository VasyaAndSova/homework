import pytest

from src.masks import get_mask_card, get_mask_account

@pytest.mark.parametrize("numbers, mask_card", [("7000792289606361", "7000 79** **** 6361"),
                                                      ("8009793285601321", "8009 79** **** 1321"),
                                                      ("9357714289605810", "9357 71** **** 5810")])
def test_get_mask_card(numbers, mask_card):
    assert get_mask_card(numbers) == mask_card


@pytest.mark.parametrize("numbers, mask_account", [("73654108430135874305", "**4305"),
                                                      ("93655108530135140301", "**0301"),
                                                      ("5613918484285873792", "**3792")])
def test_get_mask_account(numbers, mask_account):
    assert get_mask_account(numbers) == mask_account