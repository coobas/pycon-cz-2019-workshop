# The Data Trinity – Practical Numpy, Pandas and Matplotlib (Course Instructions)

Welcome to workshop instructions. Please, read them carefully.

## Prerequisites

- Bring your own computer and have required software ready.

- Understand Python language.

- Understand how Jupyter notebooks work.

## Required software

- **Python**. With Windows or MacOS, we strongly recommend using the anaconda distribution. With Linux, you can use Python provided by your package manager. However, minimum version 3.6 is required (and 3.7 recommended).

- The basic Python scientific stack libraries: **numpy** (1.15+), **matplotlib** (2.2+), **pandas** (0.24+), **seaborn** (0.8+)

- The Jupyter notebook environment: **jupyter**

We will not cover installation of any of these libraries in the course. We have no capacity to give support to people who will come
with incomplete environment.

### Installation guide using Anaconda (recommended)

1) Download and install Python from the anaconda website: https://www.anaconda.com/distribution/. Follow the instructions on the web page.

2) Once you have the anaconda installation ready, create a virtual environment for our course:

```bash
conda create -n pycon-workshop python=3.7
conda activate pycon-workshop
conda install pandas matplotlib seaborn
conda install jupyter
conda install jupyterlab   # Optional
```

## Help

If you have problems with any of the previous steps, please contact us
**before** the conference. We will gladly help in the [\#workshop-data](https://pyconcz2019.slack.com/messages/CJRQSN0FL) channel
of the conference slack.