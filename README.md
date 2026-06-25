# Simple AI Chatbot

A lightweight, rule-based Python chatbot that interacts with users in the terminal. It recognizes basic greetings, expressions of gratitude, and exit commands, responding dynamically using randomized variations.

## Features

* **Pattern Matching:** Responds to specific user keywords (greetings, thanks, exits).
* **Dynamic Responses:** Uses `random.choice` so the bot rarely gives the exact same reply twice in a row.
* **User-Friendly Interface:** Built-in string cleaning (`.lower()` and `.strip()`) ensures the bot understands inputs regardless of accidental spaces or capitalization.

---

## How It Works

The chatbot loops continuously, waiting for user input. It maps the input against a predefined dictionary of responses:

| User Input Type | Example Keywords | Bot Response Style |
| --- | --- | --- |
| **Greetings** | `hello`, `hi`, `hey` | Friendly greetings with emojis |
| **Gratitude** | `thanks`, `thank you`, `ty` | Polite, welcoming replies |
| **Exits** | `bye`, `exit`, `quit` | Parting words (breaks the loop) |
| **Unrecognized** | *Anything else* | Helpful fallback/clarification prompts |

---

## Getting Started

### Prerequisites

* Python 3.x

### Running the Chatbot

1. Clone or download the `ai-chatbot.py` file to your local machine.
2. Open your terminal and navigate to the directory containing the file.
3. Run the following command:

```bash
python ai-chatbot.py

```

---

## Future Enhancements

* Add more complex keyword structures or partial phrase matching.
* Integrate an external API for advanced natural language processing.
* Expand the dictionary to handle a wider variety of conversation topics.
