#!/bin/bash

cp -R build/* .
python md2html.py "An Accelerated Introduction to Web Development.md"
rm *.css *.js *.py
rm -r markdown tweaks