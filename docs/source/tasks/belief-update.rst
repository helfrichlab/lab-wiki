.. include:: /Includes.rst.txt

=============
Belief Update
=============

.. autosummary::
   :toctree: generated

| **From: HelfrichLab**
| **Authors:** Gabriela Iwama
| **Run on:** Psychtoolbox
| **Abbreviation:** BU

Contents
--------

 | :ref:`description`
 | :ref:`setup`
 | :ref:`scripts`
 | :ref:`instructions-exp`
 | :ref:`instructions-pat`

.. _description:

1. Task description
-------------------

:Recording Session:
    | **Structure:**  0. Coherence calibration (up to 5 min) - Usually run as a standalone experiment before.
    |                 1. Training session (up to 8 min)
    |                 2. Main task (up to 70 min)
    |                 3. Localizer (5 min) 
    | **Duration:**   From 1h to 1h30
    | **Blocks:**     4 of 80 trials
    | **Trials:**     320
    | **Pause:**      Press ``P`` during random dots response or self-paced start
    | **Abort:**      Press ``ESC`` during random dots response or self-paced start
    | **Equipment:**  Stimulus laptop, Photodiode

.. _setup:

1. Setup
--------

  **Important**: Enable graphics card and vertical synchronization!

  In the first section of the master script you will find the following required variables that have to be manually updated:
  *	``subID``- Subject identification code (e.g., "TUE08")
  *	``cfg.checkside`` - Photodiode location (1=bottom-left corner; 2=bottom-right corner)

  When you run ``config_exp.m``, a confirmation of the subject ID will be prompted. To confirm subject ID, enter ``true`` in the command line. 
  You also must define a recording type. If you are running this task for patients, enter ``ECoG`` in the second prompt.

..  code-block:: matlab
    :caption: PATH:~\\belief-update\\code\\config_exp.m

     ------ Confirm subID or type new subID ---- TUE08 ----  [true/newID]: [user_input]

     ------ Recording Type [training/behavioral/EEG/ECoG/debug]: [user_input]

If 

.. _scripts:

1. Scripts
------

| **Repository**: `GitHub <https://github.com/GabrielaIwama/belief-update>`_
| **Dependencies**: `QuestPlus <https://github.com/petejonze/QuestPlus>`_
| **Master Script**: ``config_exp.m``


.. _instructions-exp:

1. Experimenter instructions
------

**Checklist prior to the experiment:**
  * Verify that graphics card and vertical synchronization are enabled.
  * Verify that the **subject ID** is set correctly (``subID``).
  *	Verify that the **photodiode location** is set correctly (``cfg.checkside``; 1=left; 2=right).


**Running the complete experiment:**
      [...Instructions...]


**Running individual sections:**
      The calibration must be completed in a single session. Otherwise, the calibration will start over.



**How to PAUSE, RESUME, or ABORT the paradigm:**
  * Pause/Resume by pressing ``P``
  * Abort by pressing ``ESC``
  If the experiment was aborted, run ``config_exp.m`` again with the same subID and recording type as before. The experiment will continue according to a predefine rule. The calibration session will start over. Other components will resume from the trial where it stopped.

.. note::
  Data are stored automatically, also when you abort.


.. _instructions-pat:

1. Patient instructions
-----------------

**Instructions for** ``config_exp.m``:



