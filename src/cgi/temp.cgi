#!/bin/sh
# enable httpd in rc.conf:
# httpd=YES httpd_flags="-c /var/cgi/"
echo "Content-type: text/html"
echo
echo "<html><body>"
echo "<center><font size=10>Microchip MCP980x</font>"
echo "<table border=1>"
echo "<tr><th bgcolor=yellow><font size=6>Sensor</font></th><th bgcolor=yellow><font size=6>Value</font></th></tr>"
echo "<tr>"
echo "<td><font size=6>Ambient temperature</font></td>"
echo "<td><font size=6>"
/usr/sbin/envstat | grep -i "^.*Ambient" | awk '{ print $3 }'
echo "C </font></td> <br/>"
echo "</tr>"
done 
echo "</table></center>"
echo "</body></html>"
