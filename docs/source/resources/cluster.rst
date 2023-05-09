.. include:: /Includes.rst.txt

======
Cluster
======

.. autosummary::
   :toctree: generated

Contents
------
| :ref:`cluster_details`
| :ref:`cluster_programs`
| :ref:`cluster_mountingCluster`
| :ref:`cluster_connect`
| :ref:`cluster_config`
| :ref:`cluster_matlab`
| :ref:`cluster_parallelizing`
| :ref:`cluster_qsub_workflow`
| :ref:`cluster_clusterEtiquette`
| :ref:`cluster_disconnect_reconnect`
| :ref:`cluster_vpn`
| :ref:`cluster_commands`
| :ref:`cluster_howTo`
| :ref:`cluster_example`
| :ref:`cluster_test_qsub`

.. _cluster_details:

1. Details
------

:IP address:
    | 192.168.7.189

**Resources:**

:HIH-HN1:
  * Head node
  * 2x20 cores 2.1Ghz
  * ~ 80 threads (192GB RAM)


:HIH1-HIH4:
  * Compute nodes
  * 2x20 cores 2.1Ghz
  * ~ 80 threads (768GB RAM)
  * All nodes have data storage mounted with 10GbE GPFS client (r/w up to 1400MB/s)

.. warning::
  * 160 CPUs available (=parallel jobs/threads)
  * 3072 GB RAM, ~19.2 GB per jobs
  * **Keep these numbers in mind!**


.. image:: /images/cluster/cluster1.png


.. _cluster_programs:

2. Required programs
------

**Windows**

* Ubuntu 20.04.4 LTS

"Install Windows Subsystem for Linux (WSL) by entering this command in an **administrator**  PowerShell or Windows Command Prompt and then restarting your machine:"

.. code-block::
  >> wsl --install

"This command will enable the required optional components, download the latest Linux kernel, set
WSL 2 as your default, and install a Linux distribution for you (Ubuntu by default, see below
to change this).

The first time you launch a newly installed Linux distribution, a console window will open and
you'll be asked to wait for files to de-compress and be stored on your machine. All future
launches should take less than a second." `source <https://docs.microsoft.com/en-us/windows/wsl/install>`_

**MAC OS**

* Has integrated software (Shell/Terminal)


.. _cluster_mountingCluster:

3. Mounting cluster as a local drive
------

:Windows:
  1. >> File Explorer >> \\\192.168.7.189
  2. Right click \\\192.168.7.189\\helfrich_data (data folder) -> Map network drive
  3. Right click \\\192.168.7.189\\[username] (user folder) -> Map network drive
  4. Assign drive letters for the connections


.. image:: /images/cluster/cluster2.png


:MAC OS:
  1. >> Finder >> Go >> Connect to server
  2. smb://192.168.7.189/helfrich_data (data folder)
  3. smb://192.168.7.189/[username]    (user folder)
  4. Enter name and password to verify


.. image:: /images/cluster/cluster3.png


.. _cluster_connect:

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

        .--,       .--,
       ( (  \.---./  ) )
        '.__/o   o\__.'
           {=  ^  =}
            >  -  <
    _______.""`-------`"".______
    /                            \
    \ Welcome to the CIN-Cluster /
    /        HIH-Headnode 1      \
    \____________________________/
         ___)( )(___
        (((__) (__)))


.. _cluster_config:

5. One-time configurations
------

**Change your password**

1. Connect to the cluster with a GUI (e.g., Xquartz [MAC OS] or MobaXterm [Windows])
2. Start firefox (type 'firefox' in the terminal)
3. Change your password at: https://cin-ldap/lam/templates/selfService/selfServiceLogin.php?name=default&scope=user


**Set up SSH keys**
This is to ensure that you can utilize qsub and are authorized to write to your personal folder

**For Windows**
1. Connect to the cluster
2. Type the following command in the terminal window:

.. code-block::

  >> ssh-keygen -t distance

3. Accept all defaults by pressing enter
4. Type the following command:

.. code-block::

  >> cat ~/.ssh/id_dsa.pub > ~/.ssh/authorized_keys

5. You should now be ready to run MATLAB

**For MAC OS**
1. Connect to the cluster
2. Type the following command in the terminal window:

.. code-block::

  >> ssh-keygen

This starts the key generation process. When you execute this command, the ssh-keygen utility prompts you to indicate where to store the key.

2. Press the ENTER key to accept the default location. The ssh-keygen utility prompts you for a passphrase.
3. Type in a passphrase. You can also hit the ENTER key to accept the default (no passphrase). However, this is not recommended. You will need to enter passphrase a second time to continue. Remember the passphrase for future connection prompts
4. After you confirm the passphrase, the system generates the key pair.
5. Your private key is saved to the id_rsa file in the .ssh directory and is used to verify the public key you use
6. Type the following command:

.. code-block::

  >> cat ~/.ssh/id_dsa.pub > ~/.ssh/authorized_keys

7. You should now be ready to run MATLAB


**Set up a Matlab shortcut**

This is to make it easier to start Matlab (instead of defining Matlab's path every time)

1. Connect to the cluster
2. Navigate to your home folder (default) and type:

.. code-block::

  >> vi .bashrc

3. Press ``i`` to edit and add the last line (without the leftward-facing arrow)

.. code-block::

  # .bashrc

  # Source global definitions
  if [ -f /etc/bashrc ]; then
        . /etc/bashrc
  fi

  # Uncomment the following line if you don't like systemctl's auto-paging feature:
  # export SYSTEMD_PAGER=

  # User specific aliases and functions
  export PATH=$PATH:/usr/local/MATLAB/R2021b/bin/  # <-
  ~
  ~
  ~
  ~
  ~
  ~
  ~

4. To save, press ``escape`` and type:

.. code-block::

    >> :wq

5. You have now added Matlab to the default path

.. Note::
  The command to save may vary between text editors.


.. _cluster_matlab:

6. Starting MATLAB
------
You have multiple options to start Matlab:

.. code-block::

  % Without the shortcut (default):
  >> /usr/local/MATLAB/R2021b/bin/matlab -nodesktop -nojvm

  % With the shortcut:
  >> matlab -nodesktop -nojvm


.. Note::
  Remove the "-nodesktop -nojvm" to enable GUI (not recommended for speed)



.. _cluster_parallelizing:

7. Parallelizing jobs
------
To parallelize jobs, you need to add qsub to Matlab's path AFTER adding Fieldtrip. Note that different versions of Fieldtrip are available in /Toolboxes/fieldtrip/.

Add Fieldtrip, initialize, and add QSUB to Matlab's path:

.. code-block::

    >> addpath /gpfs01/helfrich/data/Toolboxes/fieldtrip/fieldtrip-20210205
    >> ft_defaults
    >> addpath /gpfs01/helfrich/data/Toolboxes/fieldtrip/fieldtrip-20210205/qsub/

**PARALLELIZING JOBS ON CLUSTER USING PYTHON**
1. Create a .pbs script that relays .py script to the cluster

Example script :

.. code-block::

    #===============================================================
    #
    #PBS -S /bin/bash                        # move to bash
    #PBS -A nbinish                          # account to which job is charged
    #PBS -N main                             # name of job
    #PBS -l walltime=12:00:00                # job will run at most
    #PBS -j oe                               # output and error is combined into the same file
    #PBS -q hih                              # job submitted to hih queue
    #PBS -m abe                              # begn end abort?
    #PBS -M neha.binish@uni-tuebingen.de     # job notifications send to e-mail
    #PBS -o main.out                         # name of outputfile
    #PBS -e main.err                         # name of error file
    #print the time and date at the beginning
    date
    echo " Started on `hostname`"

    cd /gpfs01/helfrich/user/nbinish/ecog_nb1/python_scripts/subspace_cluster
    module load python/conda/
    module load openmpi/1.2.8

    #run the python script main.py
    python3 main.py
    echo "Finished on `hostname`"

    #print the time and date at the end
    date

2. Submit the .pbs script to the cluster using the following command:
    >> qsub main.pbs

3. Check the status of the job using the following command:
    >> qstat -u nbinish

4. Check the output of the job using the following command:
    >> cat main.out

5. Check the error of the job using the following command:
    >> cat main.err

.. _cluster_qsub_workflow:

8. Creating an efficient work flow for QSUB
------

* Separate your project into different steps and associated functions.
* Separate analyses from plotting functions
* Bundle separate functions into a master script for easier referencing and documentation
* Note time and memory requirements per job. DO NOT plot on the cluster


.. image:: /images/cluster/cluster4.png


.. Note::
  * **Tip #1:** Have a master setpath script to add fieldtrip and all toolboxes in order to get the environment right
  * **Tip #2:** Have a function that initializes the subj automatically


.. _cluster_clusterEtiquette:

9. Cluster etiquette
------

* Typically every subject is one threat that runs in parallelize
  * max 160 parallel jobs, all others are in queue automatically
  * average 20 GB/threat - if you need more (e.g. source space MEG connectivity) you can go higher. Note that this will limit the number of CPUs being used (e.g., if 40GB per job are necessary -> 80 CPUs max)
* **ALWAYS** run it first for a single subject (educated guesses on time and memory requirement)
  * if e.g. time is too short, the job will just stop. Save iteratively within your script and not at the very end.
  * DO NOT set time to multiple days - it blocks others from the queue
  * DO NOT reserve more memory than needed. This slows others down, and 20GB is a lot for a job
* DO NOT use ``PARFOR`` within the QSUB loop (**never** use parfor on the cluster)
  * Every job runs on one separate CPU. If more resources are available, they get automatically assigned within QSUB

.. Note::
  Work and code locally, but keep ALL the data on the cluster. Mounted cluster folder can be accessed from your local machine like any other path


.. _cluster_disconnect_reconnect:

10. Disconnect and reconnect
------

* Use ``~`` + ``CTRL`` + ``z`` to close the connection (while job(s) are running)
* Use ``qstat`` command to see the status of the job(s)
* Use ``fg`` command to resume the connections

.. Warning::
  Closing the terminal without properly closing the connection kills your jobs!!

.. _cluster_vpn:

11. Remote access using Hertie VPN
------

 `Instructions <https://hih-docu.neurologie.uni-tuebingen.de/network-access/hih-vpn>`_

|   **Note:** Utilize 'openvpn hih pf 45 m udp4 1194'

.. _cluster_commands:

12. Other commands
------


.. list-table::
  :widths: auto
  :header-rows: 1

  * - Command
    - Description
  * - qsub
    - submit a job
  * - qdel jobid
    - will kill the specified job
  * - qdel -p jobid
    - will force purge the job if it is not killed by qdel
  * - qstat
    - list information about queues and jobs
  * - showq
    - calculated guess which job will run next
  * - xpbs
    - GUI to PBS commands
  * - qstat -q
    - list all queues on system
  * - qstat -Q
    - list queue limits for all queues
  * - qstat -a
    - list all jobs on system
  * - qstat -s
    - list all jobs with status comments
  * - qstat -r
    - list all running jobs
  * - qstat -f jobid
    - list full information known about jobid
  * - qstat -Qf queueid
    - list summary information about the PBS server
  * - qstat -B
    - list summary information about the PBS server
  * - qstat -iu userid
    -  get info for queued jobs of userid
  * - qstat -u userid
    - get info for all the jobs of userid
  * - qstat -n -1 jobid
    - will list nodes on which jobid is running in one line
  * - checkjob jobid
    - will list job details



**Example:** Using ``qstat`` to display jobs:

.. image:: /images/cluster/cluster5.png


.. _cluster_howTo:

13. How to's
------

* Separate functions for analysis from functions for visualization (i.e., plot locally, run computations on the cluster)
* Need to create a data and code base – shared folder / should probably be curated! How should we keep documentation? Slack is only short-term!

  * Frank: Tuebingen iEEG data (scan the notes, separate consent)
  * Jan/Randolph: code
  * Randolph: data (plus everyone ind. Projects w/ data identifier/documentation)
  * Frank/Isabel: How-To for Windows

.. _cluster_example:

14. Step-by-step example
------

|   **Note:** Subjects are defined as cell strings (e.g., {'TUE01','TUE02',...})

| 1. 	Start Ubuntu
| 2. 	ssh fvanschalkwijk@192.168.7.189
| 3. 	Enter password
| 4.  Start Matlab, define paths, initialize fieldtrip, add qsub, navigate to project folder, and define subjects:

.. code-block::


  >> matlab -nodesktop -nojvm % (when shortcut enabled
  >> cd /gpfs01/helfrich/user/fvanschalkwijk/2_Projects/Project4_Alpha-Spindles/Scripts/
  >> [fpath] = fjvs_startup_[PROJECT_ID] % Defines paths
  >> ft_defaults;
  >> addpath /gpfs01/helfrich/data/Toolboxes/fieldtrip/fieldtrip-20210205/qsub/
  >> subjects = project4_alphaSpindles_init_subjects(fpath);

| 5. 	Select the analysis you want to run using 'qsubcellfun' from the project's "Master_script"

.. code-block::

  qsubcellfun(@iEEG_popOut_detect_spindles,subjects,'memreq', 10*1024^3,...
                'timreq',10*3600,'StopOnError',false,'jvm','no','backend',...
                'torque','queue','hih','diary','always');

| 6. Execute your job
| 7. Closing the terminal while leaving the jobs running: sequentially type ``~`` + ``ctrl`` + ``z`` to close the connection (while job(s) are running)
| 8. Type "qstat" to determine status (while connected to the cluster)
| 9. Determine job completion from local machine using a dedicated script ``fjvs_check_clusterJob()``


.. _cluster_test_qsub:

15. Testing QSUB
------

1. Create a test function that will be applied to every subject/channel/variable:

.. code-block::

  function testscript(subj)
    pathname = '/gpfs01/helfrich/user/rhelfrich/';
    test = 1;
    save([pathname,subj,'_test'],'test');
  end

2. Create the subject ID vector (can also be scripted instead of hardcoded):

.. code-block::

  >> subj = {'S1','S2','S3'};

  subj =
    1x3 cell array
      {'S1'}  {'S2'}  {'S3'}
  >>

3. Run the test script through QSUB:

.. code-block::

  >> qsubcellfun(@testscript, subj, 'memreq', 10*1024^3,...
                'timreq',5*3600,'StopOnError',false,'jvm','no','backend',...
                'torque','queue','hih','diary','always');

Output:


.. image:: /images/cluster/cluster6.png


4. There should be three files in your mounted directory:


.. image:: /images/cluster/cluster7.png
