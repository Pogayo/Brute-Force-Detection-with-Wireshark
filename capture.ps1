param ($path,$duration=3600, $interface=7)
#$duration specifies in seconds how long the capture should run
#$interface is the network interface to listen to
#$path is the file path - this is required.
cd $path
$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8' #making sure the csv file is saved in utf-8 encoding
tshark -i $interface -f "tcp port 21 or tcp port 20"  -a duration:$duration -w real.pcap
tshark  -r real.pcap -Y "ftp" -T fields -e frame.number -e frame.time  -e ip.src -e ip.dst -e _ws.col.Protocol -e _ws.col.Info -E header=y -E separator="," -E bom=y -E quote=d -E occurrence=f  > real.csv
copy-item -path real.csv -destination ftp-packets-real.csv
./analyze-notify.ps1 