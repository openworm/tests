# OpenWorm data-driven model validation hub

This repository represents a collection of SciUnit tests for various subprojects of OpenWorm.   

## Instructions:
- Set an environment variable for your openworm repositories. e.g. 
```
export OPENWORM_HOME=/path/to/openworm
```

- For each Open Worm subproject repository you wish to test (e.g. ChannelWorm, CElegansNeuroML):
```
cd $OPENWORM_HOME
git clone http://github.com/openworm/REPO_NAME # Replace REPO_NAME with e.g. ChannelWorm
cd REPO_NAME # Ditto
git pull # Retrieve all branches (in any recent version of the git client)
git checkout sciunit # Switch to the sciunit branch of the repo (which will contain updates for testing)
pip install -e . --process-dependency-links # Install as a developer
```

- Clone and install this repository: 
```
cd $OPENWORM_HOME
git clone http://github.com/openworm/tests
cd tests
pip install -e . --process-dependency-links`
```

- Launch and run any of the notebooks (`owtests/\*.ipynb`), or run:
```
cd $OPENWORM_HOME
python -m unittest owtests
``` 
to run all of them in batch from the command line.  

## To Do:
- Add a lot more tests
- Allow tests to be run and output to be logged using SciUnit command line tools, e.g. `sciunit run`.  
- Create a Docker image to run all of these without configuration steps above.  
