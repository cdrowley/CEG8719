FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm
ENV PYTHONUNBUFFERED 1

# Install Miniconda - Use the latest installer
ENV CONDA_DIR /opt/conda

# Download and install the latest version of Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && sh /tmp/miniconda.sh -b -p $CONDA_DIR \
    && rm /tmp/miniconda.sh \
    && $CONDA_DIR/bin/conda clean -t -i -p -y

# Add Conda to PATH
ENV PATH $CONDA_DIR/bin:$PATH

# Install the latest version of Mamba from Conda-Forge
RUN conda install -c conda-forge mamba

# [Optional] Uncomment to install additional packages or Conda environments using Mamba
RUN mamba create -n CEG8719 python=3.9 -y
RUN echo "source activate CEG8719" > ~/.bashrc
ENV PATH /opt/conda/envs/CEG8719/bin:$PATH

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>