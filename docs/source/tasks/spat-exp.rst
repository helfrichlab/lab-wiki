.. include:: /Includes.rst.txt

======
Spatial Exploration task (SpatExpl)
======

.. autosummary::
   :toctree: generated

 .. Descriptives:
 ------
**From HelfrichLab** \
**Authors:** Frank van Schalkwijk & Randolph Helfrich \
**Run on:** Psychtoolbox \
**Age:** \
**Contact:** frank.schalkwijk@uni-tuebingen.de \

.. Learning session::
    **Structure**: Training, Learning (2x consecutive repetitions), immediate recall (2x), free recall\

    **Duration**: ca. 40m\

    **Blocks**: 3\

    **Trials**: 30\

    **Pause**: NA. Pause is self-implemented\

    **Abort**: Enabled. Press 'esc' to abort\

    **Skip trial**: Enabled. Press 's' to skip to the next trial\

.. Recall session::
    **Structure**: Recall (1x repetition), free recall\

    **Duration**: ca. 40m\

    **Blocks**: 3\

    **Trials**: 30\

    **Pause**: NA. Pause is self-implemented\

    **Abort**: Enabled. Press 'esc' to abort\

    **Skip trial**: Enabled. Press 's' to skip to the next trial\

Contents
 ------
 ::
  1. Equipment
  2. Set Up
  3. Scripts
  4. Instructions
  5. Timing

Equipment
------
1. Stimulus laptop
2. Photodiode

Set up
------
1.	Identify participant ID (e.g., ‘TUE01’) and session type (1=learning; 2 = recall).
    Logfiles will be dynamically and uniquely named based on patient ID, so no files will be overwritten.

2.	In the first section of the master script you will find the following required variables that have to be manually updated:
  *	**“init.ID”** 		      - Participant ID (as string [e.g., ‘TUE01’])
  *	**“init.sessionType”** 	- Session type [1 = learning; 2 = recall])
  *	**“init.nSquares”**     - Maze dimension (NxN; define as number [e.g., 5]; range: 4-6)
  *	**“init.PDlocation”**   - Photodiode location (1=bottom-left corner; 2=bottom-right corner)
  *	**“init.audioTrigger”** - Audio triggers (1=yes; 0=no)

3.	In case of photodiode scaling being too large/small: the photodiode size can be scaled in the task script (“spatialExploration_task_v3.m”) under settings [“settings.PDscaling”]).

Script
------
*	Master script that runs all sub-scripts/functions [“spatialExploration_MASTER_v3.m”]
*	4 subscripts (will run in the same order as listed)
    - *spatialExploration_paths_v3.m* \
      Determine paths relevant to the paradigm
    - *spatialExploration_instruction_v3.m*
      Provides general task instructions and a demo task to familiarize the patient with the task \
      (note: only applicable for learning session)
	  - *spatialExploration_task_v3.m* \
	    Main experiment
    - *spatialExploration_recollection_v3.m* \
      Free recollection of main experiment

Instructions
------
**Experimenter Instructions**

1. Checklist prior to the experiment:
  * Verify that **patient ID** is correct (“init.ID”)
  * Verify **session type** is defined (“init.sessionType”)
  *	Verify **maze size** is defined (“init.nSquares”; range 4-6)
  *	Verify that the **photodiode location** is set correctly (“init.PDlocation”; 1=left; 2=right)
  *	Verify that utilization of **audio trigger** is defined (“init.audioTrigger”; 1=on; 2=off)

2. General checklist for experiment:
  * Verify that the **paths** are defined correctly (“spatialExploration_paths_v3.m”):


"testing"


''testing

''testing''

Subheading 2
------
