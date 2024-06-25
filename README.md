 Caesar Cipher

## Overview

The Caesar Cipher is a simple and widely known encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet. This Python-based implementation provides a command-line interface to encrypt and decrypt messages using the Caesar Cipher technique.

## Features

- Encrypt messages by shifting letters a specified number of places.
- Decrypt messages by reversing the shift.
- Supports both uppercase and lowercase letters.
- Ignores non-alphabetic characters (e.g., numbers, punctuation).

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/Caesar-Cipher.git
    cd caesar-cipher
    ```

## Usage

1. Run the tool to encrypt or decrypt a message:
    ```bash
    python caesar_cipher.py -m <mode> -t <text> -s <shift>
    ```

    Replace `<mode>`, `<text>`, and `<shift>` with the actual values.

### Example

Encrypt a message with a shift of 3:

```bash
python caesar_cipher.py -m encrypt -t "Hello, World!" -s 3
```

Decrypt a message with a shift of 3:

```bash
python caesar_cipher.py -m decrypt -t "Khoor, Zruog!" -s 3
```

## Options

- `-m, --mode`: Mode of operation (encrypt or decrypt).
- `-t, --text`: Text to be encrypted or decrypted.
- `-s, --shift`: Number of places to shift the letters.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact me at www.linkedin.com/in/aravinth-aj.
