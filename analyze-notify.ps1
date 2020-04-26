(python analyze.py) > tmp.txt

$text = Get-Content C:\Users\Perez\Desktop\CS\Wireshark\tmp.txt -Raw 

Write-Output $text

$username = "perezogayo@gmail.com"
$emailTo="receiver_email"
$password = 'mygoodpassword12345'
$securestring = $password | ConvertTo-SecureString -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $userName, $securestring

Send-MailMessage -Body $text -From $username -SmtpServer smtp.gmail.com -Subject "Possible Brute Force Attacks" -To $emailTo -UseSsl -Port 587 -Credential $cred