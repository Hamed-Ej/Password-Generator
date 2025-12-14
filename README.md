# Password Generator

A flexible and user-friendly password generator with multiple generation modes, built with Python and Streamlit.

## Features

- **Random Password Generation**: Create secure passwords with customizable length and character types
- **Memorable Password Generation**: Generate easy-to-remember passphrases using real words
- **PIN Code Generation**: Create numeric PIN codes of any length
- **Interactive Web Interface**: Built with Streamlit for a smooth user experience

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
```

2. Install required dependencies:
```bash
pip install streamlit nltk
```

3. Download NLTK words corpus (required for memorable passwords):
```python
python -c "import nltk; nltk.download('words')"
```

## Usage

### Web Interface

Launch the Streamlit app:
```bash
streamlit run run.py
```

Then open your browser to the provided local URL (typically `http://localhost:8501`).

### Command Line

You can also use the password generation functions directly in your Python code:

```python
from password_generator import generate_random_password, generate_memorable_password, generate_pin

# Generate a random password
password = generate_random_password(length=12, include_numbers=True, include_symbols=True)

# Generate a memorable password
memorable = generate_memorable_password(no_of_words=4, separator="-", capitalization=True)

# Generate a PIN
pin = generate_pin(length=6)
```

## Password Types

### Random Password
- Customizable length (5-50 characters)
- Optional numbers inclusion
- Optional symbols inclusion
- Uses uppercase and lowercase letters

### Memorable Password
- Customizable word count (5-50 words)
- Choose separator (-, ., or space)
- Optional capitalization
- Uses real English words from NLTK corpus

### PIN Code
- Customizable length (5-50 digits)
- Numeric only

## Project Structure

```
password-generator/
│
├── password_generator.py    # Core password generation logic
├── run.py                   # Streamlit web interface
├── images/
│   └── banner.jpeg         # App banner image
└── README.md
```

## Requirements

- Python 3.7+
- streamlit
- nltk

## Testing

Run the built-in tests:
```bash
python password_generator.py
```

This will execute test cases for all three password generation modes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Security Note

This tool generates passwords using Python's `random` module, which is suitable for general password generation. For cryptographically secure applications, consider using the `secrets` module instead.