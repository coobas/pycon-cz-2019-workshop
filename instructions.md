# The Data Trinity – Practical Numpy, Pandas and Matplotlib (Course Instructions)

Welcome to workshop instructions. Please, read them carefully.

## Prerequisites

- Bring your own computer. Note that the Python distribution can easily eat 2 GB of disk space and that the repository with working data will occupy another ~1 GB. We also strongly recommend to have a computer with 8 GB of RAM (although 4 GB should be workable).

- Have the required software ready.

- Understand Python language.

- Understand how Jupyter notebooks work.


## Required software

- **Python**. With Windows or MacOS, we strongly recommend using the anaconda distribution. With Linux, you can use Python provided by your package manager. However, minimum version 3.6 is required (and 3.7 recommended).

- The basic Python [scientific stack libraries](https://www.scipy.org/about.html): **numpy**, **matplotlib**, **pandas**, **seaborn** (in their up to date versions)

- The Jupyter notebook environment: [**jupyter**](https://jupyter.org/)

- [**Git**](https://git-scm.com/) You will need to clone this repository.

We will not cover installation of any of these libraries in the course. We have no capacity to give support to people who will come
with incomplete environment.


### Cloning this repository

```bash
git clone https://github.com/coobas/pycon-cz-2019-workshop.git
```

*Not recommended:* If Git is not working, you can fall back to downloading the latest version from https://github.com/coobas/pycon-cz-2019-workshop/archive/master.zip.


### Python installation guide using Anaconda (recommended)

1) Download and install Python from the anaconda website: https://www.anaconda.com/distribution/. Follow the instructions on the web page.

2) Once you have the anaconda installation ready, create a virtual environment for our course:

Either from the provided `environment.yml` file:

```bash
# assuming the repository is in this directory
cd pycon-cz-2019-workshop

conda env create -f environment.yml
```

or manually:
```bash
conda create -n pycon-workshop python=3.7
conda activate pycon-workshop
conda install pandas matplotlib seaborn jupyter sqlalchemy html5lib beautifulsoup4 xlrd
conda install -c conda-forge -c plotly plotly plotly_express
conda install jupyterlab   # Optional
```


## Help

If you have problems with any of the previous steps, please contact us
**before** the conference. We will gladly help in the [\#workshop-data](https://pyconcz2019.slack.com/messages/CJRQSN0FL) channel
of the conference slack.
