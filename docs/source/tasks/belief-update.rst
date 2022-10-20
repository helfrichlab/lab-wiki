.. include:: /Includes.rst.txt

======
Belief Update
======

.. autosummary::
   :toctree: generated

| **From: HelfrichLab**
| **Authors:** Gabriela Iwama
| **Run on:** Psychtoolbox
| **Abbreviation:** [...Abbreviation...]
| **Contact:** [...Contact...]

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

:##:
    | **Structure:**  Coherence calibration, localizer, training session, main task
    | **Duration:**   ca. 1h
    | **Blocks:**     4 of 80 trials
    | **Trials:**     320
    | **Pause:**      enabled during random dots response or ITI
    | **Abort:**      [...Pending...]


2. Equipment
------
:Hardware used:
  | Stimulus laptop
  | Photodiode
  | [...Pending...]

3. Set up
------
In the first section of the master script you will find the following required variables that have to be manually updated:
  *	``var1`` 	- Description
  *	``var2``  - Description
  *	``var3``  - Photodiode location (1=bottom-left corner; 2=bottom-right corner)

.. note::
  [...Pending...]

4. Scripts
------
*	**Master script** that runs all sub-scripts/functions (``spatialExploration_MASTER_v3.m``)
*	**# subscripts** (will run in the order listed)
    | - ``script1.m``: [Function description]
    | - ``script2.m``: [Function description]
    | - ``script3.m``: [Function description]

5. Experimenter instructions
------

**Checklist prior to the experiment:**
  * [Check1 description]
  * [Check2 description]
  *	Verify that the **photodiode location** is set correctly (``init.PDlocation``; 1=left; 2=right)


**Running the complete experiment:**
      [...Instructions...]


**Running individual sections:**
      [...Instructions...]


**How to PAUSE, RESUME, or ABORT the paradigm:**
    * Pause by pressing ``p``
    * Resume by pressing ``[key]``
    * Abort by pressing ``esc``

.. note::
  [...note...]

.. note::
  Data are stored automatically, also when you abort.

6. Patient instructions
-----------------

**Instructions for** ``[script1.m]``:
    *"[...instructions...]”*


**Instructions for** ``[script2.m]``:
    *“[...instructions...]”*


**Instructions for** ``[script3.m]``:
      *“[...instructions...]”*


7. Comments/issues
------------

:[Issue 1]:
  [...description + solution]

:[Issue 2]:
  [...description + solution]

:[Issue 2]:
  [...description + solution]
