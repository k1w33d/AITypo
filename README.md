# Text Correction with OpenAI Script README

## Overview

This Python application utilizes the OpenAI API to correct grammatical errors in text. It's designed to work with New Zealand English and focuses on making grammatical corrections without altering the original content's meaning or adding additional content.

## Features
- API Key Management: Securely manage your OpenAI API key through a simple GUI.
- Grammar Correction: Leverages OpenAI's text-davinci-002 engine to correct grammatical errors in the text.
- Clipboard Integration: Automatically copies corrected text to the clipboard and manages clipboard content.
- User-Friendly Interface: Built with Tkinter and ttkthemes for a clean and straightforward user experience.

## Usage
1. Enter Text: Input the text you want to correct in the text box.
2. Correct Text: The application processes the text using OpenAI's API and displays the corrected version.
3. Clipboard Management: The corrected text is appended to the clipboard, and users can clear or save clipboard content as needed.
4. API Key Setup: Users can enter their OpenAI API key through a dedicated window. Instructions are provided to obtain the key from OpenAI's platform.

## Requirements
- Python 3.x
- Tkinter and ttkthemes for the GUI.
- pyperclip for clipboard operations.
- openai Python package for interacting with the OpenAI API.

## Checking Python Installation

To check if Python is installed on your system, open a command prompt or terminal and type:

```sh
python --version
```
or

```sh
python3 --version
```

If Python is installed, you should see the version number. If not, you'll need to install it.

## Installing Python
Visit Python's official website (https://www.python.org/downloads/) and download the installer for your operating system. Run the installer and follow the on-screen instructions.

Make sure to check the option that says "Add Python to PATH" during installation.

## Setting Up the Script
1- Unpack Files: Create a new folder on your computer and unpack the contents of the zipped folder into it.

2- Install Dependencies: The script requires certain Python packages to run. These are listed in the requirements.txt file. To install these packages, navigate to the folder containing the unpacked files in your command prompt or terminal, and run:

```sh
pip install -r requirements.txt
```

This command will automatically install all the necessary packages.

4- API Key File: To use the OpenAI service, you need to obtain an API key from OpenAI. Once you have your API key, create a text file named api_key.txt in the same folder as the script and paste your API key there.

5- Running the Script: To run the script, navigate to the folder containing the script in your command prompt or terminal and execute:

```sh
python AITypo.py
```

or if your system requires:

```sh
python3 AITypo.py
```

The GUI should appear, where you can start using the script to correct text.

## Usage Notes
-Ensure your OpenAI API key remains confidential; do not share the api_key.txt file with others.
-If you encounter any issues with the GUI, such as multiple windows opening, ensure that no duplicate calls are made to initialize the interface.

## Troubleshooting
-If the GUI does not start, check that all required packages are installed and that Python is correctly added to your system's PATH.
-If you have problems with the OpenAI API, verify that your API key is valid and that you have not exceeded the usage limits.

## Feedback and Support
Since this script is shared personally with you, please reach out to me directly for support or feedback. Your input is greatly appreciated and will help improve the functionality of the script.

## Safety and Privacy
- The application includes features to securely manage the OpenAI API key, ensuring privacy and security.
- Users are advised not to use this tool for sensitive or confidential text, as the data is processed through OpenAI's servers.


