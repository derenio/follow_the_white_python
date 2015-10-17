#!/bin/sh

compare -fuzz 10% tweedledee_div-* diff.jpg
convert tweedledee.jpg -crop 4961x2789 +repage tweedledee_div.jpg 
