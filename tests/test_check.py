from src.masks import get_mask_card_number
import pytest


def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'

    with pytest.raises(AssertionError):
        assert get_mask_card_number('70007922896063611')
        assert get_mask_card_number('700079228960636')
        assert get_mask_card_number(' ')