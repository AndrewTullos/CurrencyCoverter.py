# Currency Converter (Python Script)

## Description:

This Python script provides a user-friendly command-line interface for currency conversion. It leverages the currency_converter library to perform accurate conversions between various currencies.

## Features:

- Supports conversion between popular currencies (USD, EUR, GBP, JPY, CHF, MXN, CAD).
- Offers interactive prompts for selecting starting currency, desired currency, and amount.
- Handles invalid user input and provides error messages.
- Allows users to perform multiple conversions in a loop.

## Installation:

1. Make sure you have Python installed on your system (https://www.python.org/downloads/).
2. Open a terminal or command prompt.
3. Install the required library using pip:

### Bash

```
pip install currency_converter prompt_toolkit
```

## Usage:

1. Run the script from your terminal:

```
python currency_converter.py
```

2. Follow the interactive prompts to select currencies and enter the amount.
3. The script will display the converted amount.
4. You can choose to perform another conversion or exit the program.

## Example:

```
*** Menu ***
Choose from the following options below:
USD EUR GBP JPY CHF MXN CAD

What is your starting currency? USD
What is your new desired currency? JPY
Enter amount: 100
You entered 100.0 USD. The converted amount is 11383.12 JPY.

Would you like to convert another amount? (Y/N) Y

*** Menu ***
Choose from the following options below:
USD EUR GBP JPY CHF MXN CAD

What is your starting currency? EUR
What is your new desired currency? GBP
Enter amount: 50
You entered 50.0 EUR. The converted amount is 43.74 GBP.

Would you like to convert another amount? (Y/N) N
See you later!
```

## Dependencies:

- currency_converter: <https://pypi.org/project/CurrencyConverter/>
- prompt_toolkit: https://pypi.org/project/prompt_toolkit/

### Contributing:

Feel free to fork this repository and make improvements! We welcome pull requests for bug fixes, new features, or enhancements to the user experience.

## License:

This project is licensed under the MIT License (see LICENSE file for details).

### Enjoy using the Currency Converter!
