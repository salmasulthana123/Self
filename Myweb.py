from ftplib import FTP

ftp_host = "your_ftp_server"
ftp_user = "your_username"
ftp_pass = "your_password"

file_to_upload = "index.html"        # file on your computer
upload_path_on_server = "/public_html/index.html"   # where to upload on server

ftp = FTP(ftp_host)
ftp.login(ftp_user, ftp_pass)

with open(file_to_upload, 'rb') as f:
    ftp.storbinary(f"STOR {upload_path_on_server}", f)

ftp.quit()
print("File uploaded successfully!")
