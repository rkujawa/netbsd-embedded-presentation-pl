#!/bin/sh
/usr/pkg/bin/rrdtool update /var/www/rrd/temp.rrd `date +%s`:`envstat | grep Ambient | awk '{ print $3 }' # | sed 's/\..*//'`
