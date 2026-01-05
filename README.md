Type Time ⌨️

Type Time is a simple desktop typing practice application built with Python and Tkinter. It helps users improve typing speed by timing their typing sessions, calculating words per minute (WPM) in real time, and providing randomized writing prompts.

Features

⏱ Live Timer – Tracks elapsed typing time in minutes and seconds

⚡ Real-Time WPM Calculation – Updates words-per-minute as you type

📝 Random Prompt Generator – Opens a separate window with a randomly selected typing prompt

🛑 Start / Stop Controls – Easily control typing sessions

🖥 Lightweight GUI – Built entirely with Tkinter, no external dependencies

How It Works

Click Generate Prompt to open a new window containing a random typing prompt.

Click Start to begin the timer and reset previous stats.

Start typing in the text box.

Your WPM updates automatically as time passes.

Click Stop to pause the timer.

WPM is calculated using the formula:

(words_typed / elapsed_seconds) * 60

Requirements

Python 3.8+

Tkinter (included with most Python installations)

No third-party packages required.

Installation & Usage

Clone the repository or copy the script:

git clone <your-repo-url>
cd type-time


Run the application:

python main.py


💡 If Tkinter is missing on Linux, install it with:

sudo apt install python3-tk

File Overview

main.py – Contains:

GUI layout and widgets

Timer logic

WPM calculation

Prompt generation logic

Future Improvements (Ideas)

Load prompts from a JSON file

Accuracy tracking (errors, corrections)

Session history and averages

Difficulty levels (short / long prompts)

Dark mode UI


License

This project is open-source and free to use for learning or personal projects.

Author

Created by Charmy
Built as a lightweight typing practice tool using Python and Tkinter.
