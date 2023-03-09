.. include:: /Includes.rst.txt

======
Inhibition of Return
======

.. autosummary::
   :toctree: generated

| **From: HelfrichLab**
| **Authors:** Isabel Raposo
| **Run on:** Psychtoolbox
| **Abbreviation:** IOR
| **Contact:** isa.1528@hotmail.com

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

:Recording session:
    | **Structure:**  [...Pending...]
    | **Duration:**   [...Pending...]
    | **Blocks:**     [...Pending...]
    | **Trials:**     [...Pending...]
    | **Pause:**      [...Pending...]
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

  :Scripts:
    | - ``script1.m`` -> Link to Git
    | - ``script2.m`` -> Link to Git
    | - ``script3.m`` -> Link to Git
    | - ``script4.m`` -> Link to Git
    | - ``script5.m`` -> Link to Git 

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
