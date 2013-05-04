#!/bin/sh
# enable httpd in rc.conf:
# httpd=YES httpd_flags="-c /var/cgi/"
REGULATORS="LDO1 LDO2 LDO3 LDO4 DCDC1 DCDC2 DCDC3"
echo "Content-type: text/html"
echo
echo "<html><body>"
echo "<center><font size=10>Beaglebone TPS65217B status</font>"
echo "<table border=1>"
echo "<tr><th bgcolor=yellow><font size=6>Regulator</font></th><th bgcolor=yello
w><font size=6>Voltage</font></th></tr>"
for i in $REGULATORS
do
	echo "<tr>"
	echo "<td><font size=6>$i</font></td> <td><font size=6>"
	/usr/sbin/envstat | grep "^.*$i" | awk '{ print $2 }'
	echo "V </font></td> <br/>"
	echo "</tr>"
done
echo "</table></center>"
echo "</body></html>"
