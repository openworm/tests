export OPENWORM_HOME=`pwd`
echo $OPENWORM_HOME
sudo /opt/conda/bin/pip install -e . --process-dependency-links
# Comment out clones when done
git clone https://github.com/openworm/ChannelWorm.git
#
git clone https://github.com/openworm/CElegansNeuroML.git
sudo /opt/conda/bin/pip install -e . --process-dependency-links
