param ($duration)
(python analyze.py) > tmp.txt

$text = Get-Content tmp.txt -Raw 

Write-Output $text
$result=$text
$result = $result -split "\r?\n|\r" #1 splitting on newline to know how many unique ips are there
$no=$result.Length
$no=$no - 2 #1 is for the header and the other is for the newline to_string adds.
echo $no
#1 if we have potential attacks, send an email
If ($no -gt 0)  { 

$intro="Dear Admin, `r`n"+ $no +" ip address(es) have(s) tried logging in more than 3 times in the past $duration seconds. Find details below. `r`n"
$end=" `r`nBest regards, `r`nThe Powershell script you wrote"
$message=$intro+$text+$end
$username = "perezogayo@gmail.com"
$emailTo="pogayo17@alustudent.com"
$password = '12345Dawaber14'
$securestring = $password | ConvertTo-SecureString -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $userName, $securestring

Send-MailMessage -Body $message -From $username -SmtpServer smtp.gmail.com -Subject "Possible Brute Force Attacks" -To $emailTo -UseSsl -Port 587 -Credential $cred

  }
Else {

  echo "No attack"

} 




