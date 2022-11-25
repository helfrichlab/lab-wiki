.. include:: /Includes.rst.txt

======
Cluster
======

.. autosummary::
   :toctree: generated

Contents
------
| :ref:`details`
| :ref:`programs`
| :ref:`mountingCluster`
| :ref:`connect`
| :ref:`config`
| :ref:`matlab`
| :ref:`parallelizing`
| :ref:`qsub_workflow`
| :ref:`clusterEtiquette`
| :ref:`disconnect_reconnect`
| :ref:`commands`
| :ref:`howTo`
| :ref:`example`


.. _details:

1. Details
------
:IP address:
    | 192.168.7.189

:Resources:
    | **HIH-HN1 (headnode):**
    | - 2x20 cores 2.1Ghz -> 80 threads (192GB RAM)
    | **HIH1-HIH4 (compute nodes) (headnode):**
    | - 2x20 cores 2.1Ghz -> 80 threads (768GB RAM)
    |
    | All nodes have data storage mounted with 10GbE GPFS client (r/w up to 1400MB/s)

.. warning::
    | * 160 CPUs available (=parallel jobs/threads)
    | * 3072 GB RAM, ~19.2 GB per jobs
    | * **Keep these numbers in mind!**


.. _programs:

2. Required programs
------

**Windows**
* Ubuntu 20.04.4 LTS

    "Install Windows Subsystem for Linux (WSL) by entering this command in an administrator (!!)
		PowerShell or Windows Command Prompt and then restarting your machine:

		`>> wsl --install`

		This command will enable the required optional components, download the latest Linux kernel, set
		WSL 2 as your default, and install a Linux distribution for you (Ubuntu by default, see below
		to change this).

		The first time you launch a newly installed Linux distribution, a console window will open and
		you'll be asked to wait for files to de-compress and be stored on your machine. All future
		launches should take less than a second. `source <https://docs.microsoft.com/en-us/windows/wsl/install>`_ "

**MAC OS**
* Has integrated software (Shell/Terminal)


.. _mountingCluster:

3. Mounting cluster as a local drive
------

:Windows:
    1. >> File Explorer >> \\192.168.7.189
    2. Right click \\192.168.7.189\helfrich_data -> Map network drive
    3. Right click \\192.168.7.189\[username] -> Map network drive
    4. Assign drive letters for the connections


:MAC OS:
    1. >> Finder >> Go >> Connect to server
    2. smb://192.168.7.189/helfrich_data (data folder)
    3. smb://192.168.7.189/[username]    (user folder)
    4. Enter name and password to verify


.. _connect:

4. Connecting to the cluster
------

:Windows:
    1. Start Ubuntu
    2. ssh [username]@192.168.7.189
    3. enter password


:MAC OS:
    1. Start Shell/Terminal
    2. ssh -X [username]@192.168.7.189
    3. enter password

.. code-block::
  |          .--,       .--,
  |         ( (  \.---./  ) )
  |          '.__/o   o\__.'
  |             {=  ^  =}
  |              >  -  <
  |      _______.""`-------`"".______
  |      /                            \
  |      \ Welcome to the CIN-Cluster /
  |      /        HIH-Headnode 1      \
  |      \____________________________/
  |           ___)( )(___
  |          (((__) (__)))


.. _config:

5. One-time configurations
------

**Set up SSH keys**
This is to ensure that you can utilize qsub and are authorized to write to your personal folder (check)

1. Connect to the cluster

.. code-block::
  >> ssh-keygen -t distance

Accept all defaults by pressing enter

Afterwards type:

.. code-block::
  >> cat ~/.ssh/id_dsa.pub > ~/.ssh/authorized_keys

Now you should be ready to run MATLAB


**Set up Matlab shortcut**
This is to make it easier to start Matlab (instead of stating Matlab's path every time)

1. Connect to the cluster
2. Navigate to your home folder (default) and type:  >> vi .bashrc
3. Press `i` to edit and add the last line (without the leftward-facing arrow)

.. code-block::
  # .bashrc

  # Source global definitions
  if [ -f /etc/bashrc ]; then
        . /etc/bashrc
  fi

  # Uncomment the following line if you don't like systemctl's auto-paging feature:
  # export SYSTEMD_PAGER=

  # User specific aliases and functions
  export PATH=$PATH:/usr/local/MATLAB/R2021b/bin  <-
  ~
  ~
  ~
  ~
  ~
  ~
  ~
4. To save, press `escape` and type :wq
5. You have now added Matlab to the default path

.. Note::
  Different text editors have different comments. The command to save may vary.


.. _matlab:

6. Starting MATLAB
------
You have multiple options to start Matlab:

** Without a GUI (recommended):**
  - without the shortcut
    .. code-block::
      >> /usr/local/MATLAB/R2021b/bin/matlab -nodesktop -nojvm
  - With the shortcut
    .. code-block::
      >> matlab -nodesktop -nojvm

**With a GUI (not recommended):**
- without the shortcut
  .. code-block::
    >> /usr/local/MATLAB/R2021b/bin/matlab
- With the shortcut
  .. code-block::
    >> matlab


.. _parallelizing:

7. Parallelizing jobs
------
To parallelize jobs, you need to add qsub to Matlab's path AFTER adding Fieldtrip

1. Add Fieldtrip
.. code-block::
  >> addpath /gpfs01/helfrich/data/Toolboxes/fieldtrip/fieldtrip-20210205
2. Run ft_defaults
3. Add QSUB
.. code-block::
  >> addpath /gpfs01/helfrich/data/Toolboxes/fieldtrip/fieldtrip-20210205/qsub/

.. Note::
  Different versions of Fieldtrip will be available over time in /Toolboxes/fieldtrip/


.. _qsub_workflow:

8. Creating an efficient work flow for QSUB
------

.. _clusterEtiquette:

9. Cluster etiquette
------

.. _disconnect_reconnect:

10. Disconnect and reconnect
------


.. _commands:

11. Other commands
------

.. _howTo:

12. How to's
------

.. _example:

13. Step-by-step example
------
