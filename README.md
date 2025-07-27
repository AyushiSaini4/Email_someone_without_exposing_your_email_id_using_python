# Email_someone_without_exposing_your_email_id_using_python
This project allows you to send emails using Python without revealing your actual email credentials in the code. It uses Gmail's SMTP server, along with environment variables to keep your email and app password secure using the python-dotenv package.
Here’s a concise and clear **GitHub README description** for your project `email_someone_without_showing_your_email_id.py`:

---

 🔐 Features

* Send anonymous or masked emails via Python
* Keeps your email ID and password safe using `.env`
* Works with Gmail SMTP over SSL
* Easy to customize: add recipients, subject, attachments, or HTML

---

🛠️ Technologies Used

* Python 3
* `smtplib`, `email.message`
* `python-dotenv` for credential management

---

 📦 Setup Instructions

1. Clone the repo

   ```bash
   git clone https://github.com/your-username/email-anonymous-python.git
   cd email-anonymous-python
   ```

2. Install dependencies

   ```bash
   pip install python-dotenv
   ```

3. Create a `.env` file in the same directory:

   ```
   EMAIL_ADDRESS=your_email@gmail.com
   APP_PASSWORD=your_app_password_here
   ```

   > You must enable **2-Step Verification** on your Gmail account and generate an [App Password](https://myaccount.google.com/apppasswords).

4. Run the script

   ```bash
   python email_someone_without_showing_your_email_id.py
   ```

---

💡 Use Cases

* Anonymous feedback systems
* Automated email alerts
* Personal email bots
* Secure email automation in projects

---

 ⚠️ Important

* Never share your `.env` file publicly
* Always add `.env` to `.gitignore`

---

 📩 Output Example

```bash
✅ Email sent successfully.
```

---
