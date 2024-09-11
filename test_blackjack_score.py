from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == 7

# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  hand = ['Jack', 'Queen']
  score = blackjack_score(hand)
  assert score == 20

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = [3, 4, 'Ace']
  score = blackjack_score(hand)
  assert score == 18


# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand = [7, 6, 'Ace']
  score = blackjack_score(hand)
  assert score == 14

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  hand = [1, 3, 4, 7]
  score = blackjack_score(hand)
  assert score == 'Invalid'


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  hand = [2, 3, 4, 5, 6, 7]
  score = blackjack_score(hand)
  assert score == 'Invalid'

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  hand = ['Queen', 6, 7]
  assert blackjack_score(hand) == 'Bust'

@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  hand = ['Ace', 'Ace', 'King']
  assert blackjack_score(hand) == 12

@pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
    pass