#!/bin/bash
solution='BBRR'
echo $solution
echo -n $solution | md5sum | cut -f1 -d\ 
