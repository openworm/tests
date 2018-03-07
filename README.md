# OpenWorm data-driven model validation hub

This repository represents a collection of SciUnit tests for various subprojects of OpenWorm.   

## Instructions:
- Set an environment variable for your openworm repositories. e.g. 

`export OPENWORM_HOME=/path/to/openworm`
- You should have at least one other open worm repository in this location e.g. 

`$OPENWORM_HOME/ChannelWorm`, `$OPENWORM_HOME/CElegansNeuroML`, etc.  
- Install each of those repositories, e.g. 

`cd $OPENWORM_HOME/ChannelWorm; pip install -e .`
- Clone this repository: 

`cd $OPENWORM_HOME; git clone http://github.com/openworm/tests; cd tests`
- Install it as a developer: 

`pip install -e . --process-dependency-links`
- Make sure you have the requirements for any part of the project you want to test by installing extras, e.g. 

`pip install -e .[channels,cells] --process-dependency-links`
- Launch and run any of the notebooks (owtests/\*.ipynb), or run `python -m unittest owtests` to run all of them in batch from the command line.  

## To Do:
- Add a lot more tests
- Allow tests to be run and output to be logged using SciUnit command line tools, e.g. `sciunit run`.  
- Create a Docker image to run all of these without configuration steps above.  
