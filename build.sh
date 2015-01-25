#!/bin/bash

cp -R build/* .
python md2html.py curriculum.md
rm *.css *.js *.py
rm -r markdown tweaks