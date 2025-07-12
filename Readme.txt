Mail Sender Project
===================

A simple Python-based email sender tool that allows users to send emails via SMTP. 
This is great for learning Python automation and understanding email protocols.

Features
--------
- Send emails with subject and message
- Secure login using your email credentials
- Works with Gmail, Outlook, and other SMTP-supported services
- CLI interface for quick and simple use

Technologies Used
-----------------
- Python
- smtplib
- email.message

Project Files
-------------
mail_sender/
│
├── mail_sender.py      -> Main Python script
├── requirements.txt    -> (Optional) List of dependencies
├── README.txt          -> Project overview (this file)

How to Use
----------
1. Make sure Python 3 is installed.
2. Clone or download this project to your system.
3. (Optional) Install required packages:
       pip install -r requirements.txt

4. Run the script:
       python mail_sender.py

5. Enter the following details when prompted:
   - Your email address and password (or app password)
   - Receiver email address
   - Email subject
   - Email body/message

Security Note
-------------
Never hardcode your email password in the script. For better security,
use environment variables or app passwords (especially with Gmail).

Sample Output
-------------
Enter your email: yourname@gmail.com
Enter your password: ********
Enter receiver email: friend@example.com
Enter subject: Hello from Python!
Enter message: Just testing this mail sender project.
Email sent successfully ✅

Author
------
Created by Pavan Anish

License
-------
MIT License

