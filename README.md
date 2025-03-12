# Auto Quotable Bot 📝

A Python script that automatically retrieves random quotes, every day at 9am.

## 📌 Features
- Retrieves a random joke from an API.
- Updates a `joke.txt` file.
- Automatically commits the quote and pushes it to GitHub.

## 🚀 Installation
1. Clone this repository:
   ``sh
   git clone https://github.com/datagucc/auto-quotable-project.git

2. Install (recommended to install in a virtual environment)
   ``sh
   pip install requests

3. Run the script:
   python auto_commit.py

4. Automate the script:
     - On Mac/Linux with cron:
         a. Open the cron task manager : 
         crontab -e
         b. Replace path/to/auto-quotable.py with the actual location of your script
         0 9 * * * /usr/bin/python3 /path/to/auto-quotable.py
     - On Windows: with the Task Scheduler:
         a. Open the Task Scheduler (taskschd.msc in “Run”).
         b. Create a new task.
         c. Define a daily run.
         d. In “Actions” → “Start a program”, enter :
               Program: python
               Argument: /path/to/auto-quotable.py
