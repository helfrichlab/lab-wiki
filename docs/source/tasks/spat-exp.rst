.. include:: /Includes.rst.txt

======
Spatial Exploration task
(SpatExpl)
======

.. autosummary::
   :toctree: generated

 Descriptives
 ------
| **From HelfrichLab**
| **Authors:** Frank van Schalkwijk & Randolph Helfrich
| **Run on:** Psychtoolbox
| **Age:**
| **Contact:** frank.schalkwijk@uni-tuebingen.de

Learning session
-----------
.. code-block::
    **Structure**: Training, Learning (2x consecutive repetitions), immediate recall (2x), free recall\
    **Duration**: ca. 40m\
    **Blocks**: 3\
    **Trials**: 30\
    **Pause**: NA. Pause is self-implemented\
    **Abort**: Enabled. Press 'esc' to abort\
    **Skip trial**: Enabled. Press 's' to skip to the next trial\

Recall session
-----------
.. code-block::

    **Structure**: Recall (1x repetition), free recall\

    **Duration**: ca. 40m\

    **Blocks**: 3\

    **Trials**: 30\

    **Pause**: NA. Pause is self-implemented\

    **Abort**: Enabled. Press 'esc' to abort\

    **Skip trial**: Enabled. Press 's' to skip to the next trial\

Contents
------
::.
  1. Equipment
  2. Set Up
  3. Scripts
  4. Instructions
  5. Timing

Equipment
------
::.
1. Stimulus laptop
2. Photodiode

Set up
------
1.	Identify participant ID (e.g., ‘TUE01’) and session type (1=learning; 2 = recall).
    Logfiles will be dynamically and uniquely named based on patient ID, so no files will be overwritten.
2.	In the first section of the master script you will find the following required variables that have to be manually updated:
  *	``init.ID`` 		      - Participant ID (as string [e.g., ‘TUE01’])
  *	``init.sessionType`` 	- Session type [1 = learning; 2 = recall])
  *	``init.nSquares``     - Maze dimension (NxN; define as number [e.g., 5]; range: 4-6)
  *	``init.PDlocation``   - Photodiode location (1=bottom-left corner; 2=bottom-right corner)
  *	``init.audioTrigger`` - Audio triggers (1=yes; 0=no)
3.	In case of photodiode scaling being too large/small: the photodiode size can be scaled in the task script (``spatialExploration_task_v3.m``) under settings [``settings.PDscaling``]).

Script
------
*	Master script that runs all sub-scripts/functions [“spatialExploration_MASTER_v3.m”]
*	4 subscripts (will run in the same order as listed)
    - ``spatialExploration_paths_v3.m``\
      Determine paths relevant to the paradigm
    - ``spatialExploration_instruction_v3.m``\
      Provides general task instructions and a demo task to familiarize the patient with the task \
      (note: only applicable for learning session)
	  - ``spatialExploration_task_v3.m``\
	    Main experiment
    - ``spatialExploration_recollection_v3.m``\
      Free recollection of main experiment

Instructions
------
**Experimenter Instructions**

1. Checklist prior to the experiment:
  * Verify that **patient ID** is correct (``init.ID``)
  * Verify **session type** is defined (``init.sessionType``)
  *	Verify **maze size** is defined (``init.nSquares``; range 4-6)
  *	Verify that the **photodiode location** is set correctly (``init.PDlocation``; 1=left; 2=right)
  *	Verify that utilization of **audio trigger** is defined (``init.audioTrigger``; 1=on; 2=off)

2. General checklist for experiment:
  * Verify that the **paths** are defined correctly (``spatialExploration_paths_v3.m``):


Settings for the main experiment
------
- ``settings.PDscaling`` 	  = Photodiode size (multiplication of settings.PDsize)
- ``settings.showTracker``  = Tracked stats (1=yes; 0=no; default=0). Optional display of progress
- ``settings.showBlocks``	  = Maze obstacles (1=yes; 0=no; default=0)

.. code-block::
  :caption: Running the complete experiment

  When everything is done and the participant is ready, simple press **“Run”** from
  Matlab’s Editor tab or type ``spatialExploration_MASTER_v3`` into the command window.
  The master script calls all the sub-functions and scripts automatically, so
  that there is no need to do anything once the paradigm has started. The
  participant will get a detailed instruction during the
  ``spatialExploration_instruction_v3.m`` and ``spatialExploration_task_v3.m`` scripts.


.. code-block::
  :caption: Running individual sections

  Scripts for the instruction/demo (``spatialExploration_instruction_v3.m``),
  main experiment (``spatialExploration_task_v3.m``), and recollection
  (``spatialExploration_recollection_v3.m``) can be run independently. You will
  be prompted for the relevant information in Matlab’s Command Window.

How to **PAUSE**, **RESUME**, **SKIP**, or **ABORT** the paradigm
------
* The participant can **PAUSE** at any time.
* You can **ABORT** at any time during the instructions, main experiment, or
  recollection by pressing ``Escape``
* You can **SKIP** any trial by pressing ``S``
* During free recall, you can make corrections using ``backspace`` and ``R``

.. note::
  Please make sure to only use the abort and stop options if the participant cannot continue the experiment.

.. note::
  Data are stored automatically, also when you abort.

Instructions
-----------------

.. topic:: Instructions for ``spatialExploration_instruction_v3.m``

    "Welcome to the spatial exploration task. The goal is to move the cursor to the
    target. You can use the arrow keys on the keyboard to move the cursor to the
    target. There are some hidden obstacles in your path. Try to remember their
    location to reach the target.\
    \
    You will see a variety of pictures. Each picture has its own layout. Try to
    remember the path required to move the cursor to the target. After you have
    completed the task, we will ask you to remember the path for each picture.\
    \
    We will first show you some examples. The task will begin when you press spacebar. Good luck!”

.. topic:: Instructions for ``spatialExploration_task_v3.m``

    “Welcome to the spatial exploration task. The goal is to move the cursor to the
    target. You can use the arrow keys on the keyboard to move the cursor to the target.
    There are some hidden obstacles in your path. Try to remember their location to
    reach the target. You will see a variety of pictures. Each picture has its own
    layout. Try to remember the path required to move the cursor to the target.
    After you have completed the task, we will ask you to remember the path for
    each picture. The task will begin when you press spacebar. Good luck!”

.. topic:: Instructions for ``spatialExploration_recollection_v3.m``:

      “We will now show you the same environments as before. Please follow the routes
      that you have learned. You can make corrections using the ``backspace`` and ``R``
      keys on the keyboard. We will now show you the same environments as before.
      Please follow the routes that you have learned and retrace your steps.”

Comments/issues
------------

Psychtoolbox related:
-------------
*	**Synchronization issues**. You can uncomment 'Screen('Preference', 'SkipSyncTests', 1);'
  in the “Psychtoolbox initialization” section (very top of the scripts) to alleviate
  this error. Note that this could potentially result in timing issues.
*	**Screen not cooperating (MEX error)**. Potential fix: restart script or restart Matlab.
