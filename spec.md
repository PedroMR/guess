# Guess What?

Party-game that can be played using just a phone's browser, similar to Monikers or 63.

It's implemented in Javascript and HTML5. The database of cards is a CSV (see cards.csv). There are cards in different languages so we can filter them as we create a game (All, English, Brazilian Portuguese). Each card has a title, description and a number of points they are worth when guessed in teams mode. The game should render in portrait so we can play in a phone with is standing vertically.

We will first implement the co-operative version of the game where everyone is working together.

## Game Setup

Choose which languages to include. Then the game (secretly) selects 3 cards from the cards available to make up the game's deck.

## Playing the Game

When it's a player's turn, they take the phone and press "Start Turn". They then see a card from the deck. They have to describe the character/item without using the words in the title of the card.

The game is played in three rounds:

In Round 1, players can say anything they want as long as they don't use a word in the title.
In Round 2, players can only say a single word, and it can't be in the card's title.
In Round 3, players can only mime content relevant to the card.

Whenever a different player guesses what the card is, the player with the phone presses the "Guessed!" button. They can also press the "Skip" button if they don't think he can get it across.

Whenever a card is guessed it stays out of the deck until the next round.

Turns last at most 60 seconds. When the turn is over (because the player ran out of time or because the deck ran out of cards) we show a summary screen confirming how many cards were guessed. Then after a confirm press we show a "Ready for Next Turn!" screen that shows how many cards remain in the deck out of the original number of cards and what round it is.

After the round is over (because all cards were guessed) we move to the next round, reshuffling all the guessed cards into the deck again.
