#!/bin/sh
perl -pe 's/[^[:ascii:]]//g' | tr '" \t.,(){}[]:;?!<>' '\n' | sed 's/^[a-z].*$//g' | tr -s '\n'
