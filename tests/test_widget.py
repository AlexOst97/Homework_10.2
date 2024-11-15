from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
