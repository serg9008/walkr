0. get this installed on local machine
install python (2.6 is fine)
install easy_install (http://pypi.python.org/pypi/setuptools#files)
        or $ python ez_setup.py 
	or $ sudo apt-get install python-setuptools
install python virtualenv
	$ sudo apt-get install python-virtualenv
	or $ sudo easy_install virtualenv

0.x: get this installed on the burrow
  module load python/2.6
  put this file in ~/bin:  http://peak.telecommunity.com/dist/virtual-python.py
  put this in .bash_profile:  export PYTHONPATH=/u/<username>/bin
  easy_install -d ~/bin virtualenv


Create Site
===============
1.  Create Python sandbox:: 

        virtualenv --no-site-packages sandbox

2.  Activate sandbox:: [before you start developing!!]
    
        source sandbox/bin/activate

3.  Install Pylons and PasteScript (the web server):: [get pylons dependencies]

        easy_install Pylons

4.  Create the project:: [this is done]

        paster create -t pylons walkr
        Enter template_engine (mako/genshi/jinja2/etc: Template language)['mako']: mako
        Enter sqlalchemy (True/False: Include SQLAlchemy 0.5 configuration)[False]: True

5.  Configure the project for development:: [get other dependencies]

        cd walkr
        python setup.py develop

6. Serve the site
        paster serve --reload development.ini


You might need to do some of the following:
$ sudo apt-get install python-mysqldb
$ sudo apt-get build-dep python-mysqldb
$ sudo apt-get install python-dev
$ sudo apt-get install libmysqlclient15-dev

