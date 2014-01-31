DevFest Web Development Curriculum
==================================

http://adicu.com/intro-webdev

http://adicu.com/intro-webdev/python

#### Building

Run the following in the root directory:

    ./build.sh

This generates `.html` files to be viewed in a browser.

#### Solutions

All solutions are available by section in the `webdev-solutions/` and `python-solutions/` folders.

#### Using Vagrant

We support running with vagrant!  [Install and setup Vagrant], and then:

    $ vagrant up # launches the box
    $ vagrant ssh # ssh into the box
    # You are now in the vagrant instance
    $ cd /vagrant # go to the code
    $ cd <solutions folder> # Ex: cd webdev-solutions/1.3.2\ Dynamic\ Routes
    # Run the solution # Ex: python app.py

#### Directory Structure

##### build/

This is where all the extra files needed to convert from markdown to HTML go. `build.sh` uses the files from this folder.

##### img/ 

All images for the project should be put in here.

##### 
