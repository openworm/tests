FROM jupyter/scipy-notebook
RUN git clone https://github.com/openworm/ChannelWorm.git
WORKDIR ChannelWorm 
RUN pip install . 
WORKDIR $HOME
RUN pip install git+https://github.com/OpenSourceBrain/osb-model-validation
RUN pip install git+https://github.com/openworm/CElegansNeuroML@sciunit
RUN git clone -b sciunit https://github.com/openworm/CElegansNeuroML.git
WORKDIR CElegansNeuroML
RUN python setup.py install
ENV OPENWORM_HOME pwd
# over looked
ENV OW_HOME pwd
# over looked
RUN pip install quantities sciunit django
WORKDIR $HOME 
RUN git clone http://github.com/openworm/tests.git
WORKDIR tests 
RUN pip install -e . --process-dependency-links
WORKDIR $HOME

