.. include:: /Includes.rst.txt

======
Spatial Exploration task (SpatExpl)
======

.. autosummary::
   :toctree: generated

| **From: HelfrichLab**
| **Authors:** Frank van Schalkwijk & Randolph Helfrich
| **Run on:** Psychtoolbox
| **Abbreviation:** SpatExpl
| **Contact:** frank.schalkwijk<at>uni-tuebingen.de

Contents
------
.. code-block::

  1. Task descriptives
  2. Equipment
  3. Set Up
  4. Scripts
  5. Experimenter instructions
  6. Patient instructions
  6. Comments/issues

1. Task descriptives
------

:Learning session:
    | **Structure:** Training, Learning, immediate recall (2x), free recall
    | **Duration:** ca. 40m
    | **Blocks:** 3
    | **Trials:** 30
    | **Pause:** NA. Pause is self-implemented
    | **Abort:** Enabled. Press ``esc`` to abort
    | **Skip trial:** Enabled. Press ``s`` to skip to the next trial

:Recall session:
    | **Structure:** Recall (1x repetition), free recall
    | **Duration:** ca. 10m
    | **Blocks:** 1
    | **Trials:** 10
    | **Pause:** NA. Pause is self-implemented
    | **Abort:** Enabled. Press ``esc`` to abort
    | **Skip trial:** Enabled. Press ``s`` to skip to the next trial

2. Equipment
------
:Hardware used:
  | Stimulus laptop
  | Photodiode

3. Set up
------
In the first section of the master script you will find the following required variables that have to be manually updated:
  *	``init.ID`` 		      - Participant ID (as string [e.g., ‘TUE01’])
  *	``init.sessionType`` 	- Session type [1 = learning; 2 = recall])
  *	``init.nSquares``     - Maze dimension (NxN; define as number [default=5]; range: 4-6)
  *	``init.PDlocation``   - Photodiode location (1=bottom-left corner; 2=bottom-right corner)
  *	``init.audioTrigger`` - Audio triggers (1=yes; 0=no; default=0)

Settings for the main experiment:
   - ``settings.PDscaling`` 	 = Photodiode size (multiplication of settings.PDsize)
   - ``settings.showTracker``  = Tracked stats (1=yes; 0=no; default=0). Optional display of progress
   - ``settings.showBlocks``	 = Maze obstacles (1=yes; 0=no; default=0)

.. note::
  The photodiode size can be scaled (``settings.PDscaling``)

4. Script
------
*	**Master script** that runs all sub-scripts/functions (``spatialExploration_MASTER_v3.m``)
*	**Four subscripts** (will run in the order listed)
    | - ``spatialExploration_paths_v3.m``: sets path
    | - ``spatialExploration_instruction_v3.m``:  Task instructions and demo
    |     *(note: only applicable for learning session)*\
	  | - ``spatialExploration_task_v3.m``: Main experiment
    | - ``spatialExploration_recollection_v3.m``: Free recall

5. Experimenter instructions
------

**Checklist prior to the experiment:**
  * Verify that **patient ID** is correct (``init.ID``)
  * Verify **session type** is defined (``init.sessionType``)
  *	Verify **maze size** is defined (``init.nSquares``; range 4-6)
  *	Verify that the **photodiode location** is set correctly (``init.PDlocation``; 1=left; 2=right)
  *	Verify that utilization of **audio trigger** is defined (``init.audioTrigger``; 1=on; 2=off)
  * Verify that the **paths** are defined correctly (``spatialExploration_paths_v3.m``):

**Running the complete experiment:**

.. code-block::

    When everything is done and the participant is ready, simple press **“Run”** from
    Matlab’s Editor tab or type ``spatialExploration_MASTER_v3`` into the command window.
    The master script calls all the sub-functions and scripts automatically, so
    that there is no need to do anything once the paradigm has started. The
    participant will get a detailed instruction during the
    ``spatialExploration_instruction_v3.m`` and ``spatialExploration_task_v3.m`` scripts.

**Running individual sections:**

.. code-block::

    Scripts for the instruction/demo (``spatialExploration_instruction_v3.m``),
    main experiment (``spatialExploration_task_v3.m``), and recollection
    (``spatialExploration_recollection_v3.m``) can be run independently. You will
    be prompted for the relevant information in Matlab’s Command Window.

**How to PAUSE, RESUME, SKIP, or ABORT the paradigm:**
.. code-block::

    * The participant can **PAUSE** at any time.
    * You can **ABORT** at any time by pressing ``Escape``
    * You can **SKIP** any trial by pressing ``s``
    * During free recall, you can make **corrections** using ``backspace`` and ``R``

.. note::
  Please make sure to only use the abort and stop options if the participant cannot continue the experiment.

.. note::
  Data are stored automatically, also when you abort.

6. Patient instructions
-----------------

**Instructions for** ``spatialExploration_instruction_v3.m``:
    *"Welcome to the spatial exploration task. The goal is to move the cursor to the
    target. You can use the arrow keys on the keyboard to move the cursor to the
    target. There are some hidden obstacles in your path. Try to remember their
    location to reach the target. You will see a variety of pictures. Each picture
    has its own layout. Try to remember the path required to move the cursor to
    the target. After you have completed the task, we will ask you to remember
    the path for each picture. We will first show you some examples. The task
    will begin when you press spacebar. Good luck!”*

**Instructions for** ``spatialExploration_task_v3.m``:
    *“Welcome to the spatial exploration task. The goal is to move the cursor to the
    target. You can use the arrow keys on the keyboard to move the cursor to the target.
    There are some hidden obstacles in your path. Try to remember their location to
    reach the target. You will see a variety of pictures. Each picture has its own
    layout. Try to remember the path required to move the cursor to the target.
    After you have completed the task, we will ask you to remember the path for
    each picture. The task will begin when you press spacebar. Good luck!”*

**Instructions for** ``spatialExploration_recollection_v3.m``:
      *“We will now show you the same environments as before. Please follow the routes
      that you have learned. You can make corrections using the ``backspace`` and ``R``
      keys on the keyboard. We will now show you the same environments as before.
      Please follow the routes that you have learned and retrace your steps.”*

7. Comments/issues
------------

:Synchronization issues:
  You can uncomment 'Screen('Preference', 'SkipSyncTests', 1);' in the
  “Psychtoolbox initialization” section (very top of the scripts) to alleviate
  this error. Note that this could potentially result in timing issues.

:MEX error:
  Potential fix: restart script or restart Matlab.
