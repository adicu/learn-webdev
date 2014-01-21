#!/bin/bash

cp -R build/* .
cp webdev_curriculum.css webdev_python_curriculum.css
python md2html.py webdev_curriculum.md
python md2html.py webdev_python_curriculum.md
rm *.css *.js *.py
rm -r markdown