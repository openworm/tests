FROM jupyter/scipy-notebook

USER root
RUN apt-get update
RUN apt-get install -y default-jre
USER jovyan

WORKDIR /home/jovyan/work
RUN mkdir openworm
ENV OPENWORM_HOME /home/jovyan/work/openworm

# SciUnit
WORKDIR $OPENWORM_HOME
RUN wget http://github.com/scidash/sciunit/tarball/dev -O out.tar.gz
RUN mkdir sciunit
RUN tar -xvzf out.tar.gz --strip-components=1 -C sciunit
WORKDIR sciunit
RUN pip install -e . --process-dependency-links

# NeuronUnit
WORKDIR $OPENWORM_HOME
RUN wget http://github.com/scidash/neuronunit/tarball/dev -O out.tar.gz
RUN mkdir neuronunit
RUN tar -xvzf out.tar.gz --strip-components=1 -C neuronunit
WORKDIR neuronunit
RUN pip install -e . --process-dependency-links

# ChannelWorm
WORKDIR $OPENWORM_HOME
RUN wget http://github.com/openworm/ChannelWorm/tarball/sciunit -O out.tar.gz
RUN mkdir ChannelWorm
RUN tar -xvzf out.tar.gz --strip-components=1 -C ChannelWorm
WORKDIR ChannelWorm
RUN pip install -e . --process-dependency-links

# CElegansNeuroML
WORKDIR $OPENWORM_HOME
RUN wget http://github.com/openworm/CElegansNeuroML/tarball/sciunit -O out.tar.gz
RUN mkdir CElegansNeuroML
RUN tar -xvzf out.tar.gz --strip-components=1 -C CElegansNeuroML
WORKDIR CElegansNeuroML
RUN pip install -e . --process-dependency-links

# open-worm-analysis-toolbox
WORKDIR $OPENWORM_HOME
RUN wget http://github.com/rgerkin/open-worm-analysis-toolbox/tarball/sciunit -O out.tar.gz
RUN mkdir open-worm-analysis-toolbox
RUN tar -xvzf out.tar.gz --strip-components=1 -C open-worm-analysis-toolbox
WORKDIR open-worm-analysis-toolbox
RUN pip install -e . --process-dependency-links
# One level deeper
WORKDIR open_worm_analysis_toolbox 
RUN cp user_config_example.txt user_config.py
WORKDIR $OPENWORM_HOME/open-worm-analysis-toolbox
RUN mkdir example_data
WORKDIR example_data
#RUN wget "https://drive.google.com/uc?export=download&id=0B7to9gBdZEyGWVAzUlYwbk1ad0E" -O example_contour_and_skeleton_info.mat
#RUN wget "https://drive.google.com/uc?export=download&id=0B7to9gBdZEyGX2tFQ1JyRzdUYUE" -O example_video_feature_file.mat
#RUN wget "https://drive.google.com/uc?export=download&id=0B7to9gBdZEyGakg5U3loVUktRm8" -O example_video_norm_worm.mat

# cache bust
RUN ls 

# wcon
WORKDIR $OPENWORM_HOME
RUN wget http://github.com/rgerkin/tracker-commons/tarball/master -O out.tar.gz
RUN mkdir tracker-commons
RUN tar -xvzf out.tar.gz --strip-components=1 -C tracker-commons
WORKDIR tracker-commons/src/Python
RUN pip install -e . --process-dependency-links

RUN pip install -U nbconvert IPython

# This tests package
WORKDIR $OPENWORM_HOME
#VOLUME $OPENWORM_HOME/tests
#RUN git clone http://github.com/openworm/tests
WORKDIR tests
COPY --chown=jovyan:users . $OPENWORM_HOME/tests
USER root
RUN chown jovyan:users $OPENWORM_HOME/tests
USER jovyan
#USER root
#RUN chown -R jovyan .
#USER jovyan
RUN pip install -e . --process-dependency-links
#RUN pip install -e .[channels,cells] --process-dependency-links


#RUN python -m unittest -b owtests

#ENTRYPOINT /bin/bash
#WORKDIR $HOME/work
ENTRYPOINT start-notebook.sh --NotebookApp.token=''

RUN cp $OPENWORM_HOME/tracker-commons/wcon_schema.json $OPENWORM_HOME/tracker-commons/src/Python/wcon/wcon_schema.json