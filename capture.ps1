tshark -i 7 -f "tcp port 21 or tcp port 20"  -a duration:60 -w real.pcap
tshark  -r real.pcap -Y "ftp" -T fields -e frame.number -e frame.time  -e ip.src -e ip.dst -e _ws.col.Protocol -e _ws.col.Info -e data.data -E header=y -E separator="," -E quote=d -E occurrence=f  > real.csv
copy-item -path real.csv -destination ftp-packets-test
./analyze-notify