#!/bin/sh
perl -pe 's/[[:space:]]/\n/g' | perl -pe 's/[[:punct:]]/\n/g' | perl -pe 's/[^[:ascii:]]]/\n/g' | grep -v -e '^$'
