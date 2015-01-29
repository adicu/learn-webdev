#! /bin/bash

./build.sh
scp "An Accelerated Introduction to Web Development.html" adi-website:/srv/learn/public_html/webdev/index.html
scp -r img adi-website:/srv/learn/public_html/webdev/