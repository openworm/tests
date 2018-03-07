FROM russelljarvis/neuronunit
USER jovyan
RUN sudo /opt/conda/bin/pip install psutil
ENV QT_QPA_PLATFORM offscreen
RUN sudo rm -rf /opt/conda/lib/python3.5/site-packages/neuronunit-0.1.8.8-py3.5.egg/neuronunit
RUN sudo rm -rf $HOME/neuronunit
#RUN sudo chown -R jovyan $HOME
COPY . $HOME/neuronunit


RUN sudo chown -R jovyan $HOME
RUN pip uninstall -y pyneuroml
#RUN pip uninstall -y pylems
RUN pip install -e $HOME/neuronunit --ignore-installed --process-dependency-links
#RUN pip install lazyarray pyNN
RUN pip install dask
ENV OPENWORM_HOME .

ENV OPENWORM_HOME `pwd`

ENV OPENWORM_HOME $pwd

RUN echo $OPENWORM_HOME
RUN sudo /opt/conda/bin/pip install -e . --process-dependency-links
# Comment out clones when done
RUN git clone https://github.com/openworm/ChannelWorm.git
#
RUN git clone https://github.com/openworm/CElegansNeuroML.git
RUN sudo /opt/conda/bin/pip install -e . --process-dependency-links
