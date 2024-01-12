# README

## How to run my GroupMe bot - ReeBot

    python3 bot.py

## Features of my GroupMe bot

### Responds to me
Via my sender_id, 40293401, ReeBot only responds to me for messages that do not include good morning/night, stickers, or translation.
So, for any messages besides the features that I have implemented for everyone, ReeBot only responds to me.

### Good morning/good night
If anyone says "good morning" or "good night", with any capitalization, ReeBot responds with "Good morning" or "Good night" followed by the sender's name.
However, this feature is not active for any sender who has "bot" as their sender_type in order to prevent ReeBot from responding to other bots.

### Sends a sticker about anything (1st additional feature)
Asking ReeBot to send a sticker about anything, such as cats, dogs, cars, planes, Maryland, food, etc., results in a Giphy sticker being sent as a reply.
The format for a sticker request must currently be any of the following, with any capitalization:
1. Send me a sticker about [INSERT CONTENT HERE]
2. Sticker about [INSERT CONTENT HERE]
3. Sticker [INSERT CONTENT HERE]

### Translates text from English to any other language (2nd additional feature, Extra-Credit)
Via the [Google Translate API for Python](https://pypi.org/project/googletrans/), ReeBot translates any English text into any of 6 languages (Spanish, French, Japanese, Mandarin, Korean, or Hindi) based on a user's request. 
The format for translation requests must currently be either of the following, with any capitalization:
1. Translate "[INSERT ENGLISH TEXT HERE]" to [INSERT LANGUAGE HERE], or
2. Please Translate "[INSERT ENGLISH TEXT HERE]" to [INSERT LANGUAGE HERE]