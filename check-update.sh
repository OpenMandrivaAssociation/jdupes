#!/bin/sh
curl -sL https://codeberg.org/jbruchon/jdupes/tags 2>/dev/null |sed -ne 's,.*/archive/v\(.*\).tar.gz.*,\1,p' |head -n1

