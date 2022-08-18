import yagmail
import os

receiver = "shreyabamane21@gmail.com.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance_2020-09-30_19-13-43.csv"  # attach the file

# mail information
yag = yagmail.SMTP("bamanerani21@gmail.com", "Ranibamane@21")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
