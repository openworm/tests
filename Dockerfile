FROM jupyter/scipy-notebook
RUN git clone https://github.com/openworm/ChannelWorm.git
WORKDIR ChannelWorm 
RUN pip install . 
WORKDIR $HOME
RUN pip install git+https://github.com/OpenSourceBrain/osb-model-validation
RUN pip install git+https://github.com/openworm/CElegansNeuroML.git
#RUN sudo chown -R jovyan $HOME
WORKDIR $HOME 
WORKDIR openworm
#RUN sudo chown -R jovyan $HOME
ENV OPENWORM_HOME pwd
WORKDIR $HOME 
RUN git clone http://github.com/openworm/tests.git
WORKDIR tests 
RUN pip install -e . --process-dependency-links


