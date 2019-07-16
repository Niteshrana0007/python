import smtplib
connection = smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo()
connection.starttls()
connection.login('niteshrana754@gmail.com','password')
connection.sendmail('niteshrana754@gmail.com','niteshrana754@gmail.com','this is message')
connection.quit()
