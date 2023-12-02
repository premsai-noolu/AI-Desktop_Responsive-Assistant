# AI-Desktop_Responsive-Assistant

Python AI assistant is a basic AI assistant built in Python that can perform various tasks such as searching Wikipedia, opening websites, providing the current time, and sending emails. It uses the pyttsx3 library for text-to-speech, speech_recognition for speech recognition, and integrates with services like Wikipedia and Gmail.

## Features

* Voice Recognition: Jarvis can understand voice commands to perform tasks.
* Wikipedia Search: Retrieve information from Wikipedia by asking Jarvis about a topic.
* Web Browsing: Open YouTube, Google, Stack Overflow, or any website of your choice.
* Time Information: Ask Jarvis for the current time.
* Email Sending: Send emails using your Gmail account.


## Dependencies

Make sure to install the required libraries before running the code:

```
pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia-api
```

## Usage

Run the script.
Python AI assistant will greet you and wait for your command.
Speak clearly and wait for Python AI assistant to respond.

## Commands

*Wikipedia Search: Say "Wikipedia" followed by the topic you want to search.
* Open YouTube: Say "Open YouTube" to open the YouTube website.
* Open Google: Say "Open Google" to open the Google website.
* Open Stack Overflow: Say "Open Stack Overflow" to open the Stack Overflow website.
* Check Time: Say "What's the time" or "Tell me the time" to get the current time.
* Open Code: Say "Open Code" to open Visual Studio Code.
* Send Email: Say "Email to [recipient]" and provide the email content when prompted.

## Configuration

Set your Gmail username and password in the sendEmail function to enable email sending.

## Note

This is a basic AI assistant and can be extended with additional functionalities.
Make sure your microphone is set up and working correctly for voice commands.
