import smtplib

email_list = ("****@email.com", "****@gmail.com")

credentials = {"email": "Your email id here", "pwd": "password"}

for email in email_list:
  s = smtplib.SMTP("smtp.gmail.com", 587)
  s.starttls()
  s.login(credentials["email"], credentials['pwd'])
  message = "Your message"
  s.sendmail(credentials['email'], email, message)
	s.quit()
