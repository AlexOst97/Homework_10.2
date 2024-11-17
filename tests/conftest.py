import pytest


# test_masks
@pytest.fixture()
def card_number():
    return "7000 79** **** 6361"


@pytest.fixture()
def mask_account():
    return "**4305"


# test_widget
@pytest.fixture()
def account_card():
    return "Счет **9589"


@pytest.fixture()
def date():
    return "05.06.2024"


# test_processing
@pytest.fixture()
def list_answer_1():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture()
def list_answer_2():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
