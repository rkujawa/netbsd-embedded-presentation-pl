#!/bin/sh
/usr/pkg/bin/rrdtool graph $1 -X 0 --end now --start end-$2 --width 600 \
DEF:temp=/var/www/rrd/temp.rrd:temp:AVERAGE \
LINE1:temp#0000FF:"MCP9801 ambient temperature\l"
