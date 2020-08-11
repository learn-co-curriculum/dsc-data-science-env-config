
# Setting up a Professional Data Science Environment - Setup

## Introduction

In this lesson, you'll continue setting up your professional data science environment by making a virtual environment. 

## Objectives

You will be able to:

* Use basic commands to navigate the command line
* Summarize why virtual environments are used
* Use a virtual environment

## Cloning this Repository

To finish this setup process, you’re going to need to download a copy of the files in this repository. To do that, you need to start by opening a terminal window.

If you’re on a Windows machine, select “Git Bash” from either the start menu or the search bar and it’ll open up a terminal (don’t use the default Windows terminal - it will not work for this).

If you’re working on a mac, open the “Terminal” app in the “Utilities” folder within your “Applications” folder.

Let’s type `pwd` to “print the working directory. It should be somewhere you are OK downloading files to. If not, feel free to use the “cd” command to change directory to one you’d like to work from.

Then type (or better still, copy and paste) `git clone https://github.com/learn-co-curriculum/dsc-data-science-env-setup-v2-1.git`

*In Windows, in git bash, to paste from the clipboard the shortcut should be `ctrl-shift-insert`*

This will create a new subdirectory whose name starts with "dsc-data-science-env-setup-v2-1" which will contain a copy of all of the files from this repository. Go into that directory using the `cd`, or change directory, command (after typing `cd dsc` you should be able to hit the **tab** key to "tab complete" so you don't need to type the whole directory name). That should work on both Windows and Macs.

## Setting Up Virtual Environments

As you do data science projects, you will spend a lot of your time using pre-written libraries to speed up your development. Examples include NumPy, Pandas and scikit-learn. As you work on different projects, you may also find that you end up using different versions of different libraries for different projects. The most common versioning issue is that some projects will run in Python 2 whereas others will run in Python 3, but you may also find that different projects depend on different versions of libraries like Tensorflow.

Occasionally, code that works in an old version of a library won’t work in a newer version. So if you open up a new project and install the dependencies, it’s possible that your old project won’t work anymore.

To avoid that problem, a best practice is to use “virtual environments”. Virtual environments allow you to have different versions of Python and different versions of the various libraries you use, so you can install a new version of a library for one project but still use the old version for another project. It’s almost as if you have multiple computers that you can swap between, each having a different setup and configuration, just by running a couple of commands.

There is a built-in virtual environment feature in Python, but we’re going to use the more flexible virtual environments provided by Conda as part of the Anaconda distribution you installed.

To use a new virtual environment, there are two steps you need to complete. The first step is to create the virtual environment. That may take a couple of minutes as your computer has to download the necessary version of Python and all of the libraries that you want to be able to use in that environment. The next step then is to “use” the virtual environment by activating it.

If you want to learn more about Conda environments, have a look at the [documentation](https://conda.io/docs/user-guide/tasks/manage-environments.html), otherwise, let’s give this a try.

You need to start by navigating into the root of this project folder, so you’re going to want to type `cd dsc-data-science-env-setup-v2-1` in your terminal if you didn't already.

Then to create the environment, on a mac, type `conda env create -f environment.yml`. On windows, type `conda env create -f windows.yml`. Depending on the speed of your computer and your internet connection it may take up to five minutes for this to complete. While it does you should see output similar to that displayed below start to appear in your terminal.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-47.png' width="750">

Next, try activating the environment. Whether you're on a Mac or using git bash on a windows machine, type `conda activate learn-env` (if you have an issue with running git bash, the command to activate Conda within the Conda shell on windows is `activate learn-env`).

To confirm that it worked, type `conda info --envs` and confirm that the output in the terminal ends with /learn-env - e.g. *  /Users/peterbell/anaconda3/envs/learn-env

#### Troubleshooting
If you see a message that states “WARNING: A newer version of Conda exists”, run `conda update -n base conda` and then try again to create the environment using `conda env create -f environment.yml`.

If you see a message that states "file not found", double check that you are running this command from the directory that contains the .yml file. If you type `ls` you should see the .yml file. If you don't see it, you likely forgot to run `cd dsc-data-science-env-setup-v2-1` to change into the right directory.

## Setting your Default Environment

You have successfully created your virtual environment! To be sure that you are using the learn-env, it's helpful to set it as your default environment so that you don't need to remember to manually switch to it every time you open terminal. This step is suggested but not required.

### Mac
On a Mac, run `echo "conda activate learn-env" >> ~/.bash_profile` to add the configuration to your bash profile and then run `source ~/.bash_profile` to activate the changes you just made.
</details>

### Windows
To follow these instructions on a Windows machine you must be using the Git Bash shell it was suggested to install above.
Run `touch ~/.bash_profile` to create a new file. Next, run `echo "conda activate learn-env" >> ~/.bash_profile` to add the configuration to your bash profile and then run `source ~/.bash_profile` to activate the changes you just made.

## Updating your Virtual Environment

Every so often we create new versions of the virtual environment and we'll ask you to update your virtual environment. To do that, download the latest version of this repository with the latest changes. Then go into a terminal window and:

```
conda activate base # To make sure you're not in the learn-env environment
conda remove -n learn-env --all # To get rid of the environment
conda env list # Make sure it doesn't list learn-env - if it does, try the last step again
# Then to re-create the environment from the latest environment file
# On a Mac
conda env create -f environment.yml
# Or in Windows
conda env create -f windows.yml

```

## Configuring your Kernel

Jupyter Notebooks run "kernels" - the computational engine used for executing your code. It's important to be running the right kernel within your notebook, otherwise you may get errors stating that you don't have a particular package or have the wrong version of it or even complaints about the version of Python you're running (some packages that work with Python 3.6.6 don't currently support Python 3.7, for example).

It is essential to run `conda activate learn-env` (if you have an issue with running git bash, the command to activate Conda within the Conda shell on windows is `activate learn-env`) every time you start a new terminal window that you are going to use to either run a Jupyter Notebook or your tests. If you don't do this you **will** get errors, so please check this first. If you are not sure whether you have activated the environment, in the terminal type `conda list -f obscure` and it should show you that you have v1.0.1 of the "obscure" package. If it doesn't show that, (re)run (`conda`) `activate learn-env`.

However, there is one more step you need to perform. Firstly you need to ensure your terminal is running the learn-env virtual environment so you have the necessary packages. Then you need to go into your Jupyter Notebook and when viewing a notebook, click on "Kernel" in the top bar, then "Change Kernel" and then pick the learn-env kernel. You must make sure you're running the learn-env kernel whenever you're working in a Jupyter Notebook.

If for any reason you don't see the learn-env option in the drop-down list of kernels, exit the notebook in the browser, close down the notebook server, and in the terminal type `python -m ipykernel install --user --name=learn-env` - that will add the learn-env to your list of kernels and when you restart the Jupyter Notebook server and then open a notebook, you'll be able to select the learn-env option from the list of kernels.

## Summary

Congratulations! If you've gotten this far and everything has worked, you have successfully set up a virtual environment which will serve as a great baseline setup for working as a professional data scientist!
