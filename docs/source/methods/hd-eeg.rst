.. include:: /Includes.rst.txt

======
HD-EEG
======

.. autosummary::
   :toctree: generated


Contents
------
.. code-block::

  1. Preparing for a recording
  2. Setup with participant
  3. Applying the EGI net
  4. Acquiring signal from the EGI net
  5. Starting and ending your recording
  6. Removing the EGI net
  7. Cleanup
  8. EGI electrode layout
  9. Scripts


.. note::
  Official EGI documentation can be found `here <https://www.egi.com/knowledge-center/net-application>`_


1. Preparing for a recording
---------

.. Note::
  Determine participant/patient ID

:Hardware:
  * Switch on EGI transformer box
  * Switch on the amplifier
  * Start recording device (Mac)
  * Start stimulus laptop (Windows)

:Software:
  * Start Netstation Acquisition software
  * Insert participant/patient ID
  * Select correct workspace

:HD-EEG net:
  * Prepare electrolyte solution in respective bucket
    (``# L`` water, ``# g`` potassium, ``# ml`` baby shampoo)

:Other:
  * Syringes for electrolyte solution
  * Towels & gloves
  * Clean recording & monitoring rooms; paradigm operational


2. Setup with participant
---------

1.	Explain to the participant what is about to happen. Explain cap placement and procedures.
2.	Obtain written informed consent before you do anything else
3.	Measure circumference of participant’s head. Measure around glabella (brow ridge) and 2.5 cm above the inion (bump on the back of the skull; Fig. 1). Select appropriate cap and submerge in electrolyte solution.

.. image:: /images/egi/EGI_fig1.JPG
**Figure 1.** Measuring skull circumference and determining cap size (image used from EGI manual)*

4.	Mark Vertex (Cz position). Measure nasion-inion distance and draw a perpendicular line at midpoint. Also mark midpoint between the two preauricular points. Vertex should be in the middle of the cross.

.. image:: /images/egi/EGI_fig2.JPG
**Figure 2.** Marking vertex (image used from EGI manual)*

.. Note::
   Full instructions can also be found `here <https://www.egi.com/knowledge-center/net-application>`_. This also contains some useful instruction videos for marking vertex position, applying, manipulating, and removing the EGI net.


3. Applying the EGI net
---------

1.	Place a towel around the participant’s neck and covering the shoulders. Explain again what will happen
2.	Shake the excess electrolyte from the net
3.	Give the connector to the patient.
4.	Stand directly in front of the patient when placing the net
5.	Ask the participant to keep the eyes closed
6.	Keep hold of the EGI cap using your thumbs and little fingers
7.	Gently apply the net onto the vertex
8.	Make sure the reference (REF/Cz) sensor is generally aligned over the vertex and that the nasion sensor is generally aligned over the nasion. If they are more than 1 cm off their marks, then reapply the net.
9.	Tighten the chin straps

.. warning::
  Ensure the connector **DOES NOT** get wet!

.. image:: /images/egi/EGI_fig3.JPG
**Figure 3.** Adjusting the EGI net (image used from EGI manual)

4. Acquiring signal from the EGI net
---------

1.  Connect the connector to the EGI beam.
2.	Start acquisition within Netstation
3.	Check the impedances of the electrodes (should be ``< 50 kOhm``.

.. note::
  If impedances are higher, you can improve the signal by ensuring good contact (push hair out of the way) and re-soaking the electrode with electrolyte solution.


5. Starting and ending your recording
---------

**Starting the recording:**

* [Option 1:] Click ``record`` in Netstation
* [Option 2:] Execute ``EGI_startRecording.m`` on the stimulus PC


**Ending your recording:**

* [Option 1:] Click ``end`` in Netstation
* [Option 2:] Execute ``EGI_stopRecording.m`` on the stimulus PC

.. Note::
  An active recording is indicated by a red background and running timer.

.. Warning::
  As soon as the recording ends, you have to reinsert the participant/patient ID!


6. Removing the EGI net
---------

1.  Stop the recording. Data are automatically saved in your workspace
2.  Make sure Netstation is no longer recording (i.e., white screen)
3.  Stop signal Acquisition
4.  Unplug the connector
5.  Have the participant/patient close their eyes
6.	Carefully remove the EGI cap by 'peeling' it back on itself

.. image:: /images/egi/EGI_fig4.JPG
**Figure 4.** Removing the EGI net (image used from EGI manual)*


7. Cleanup
---------

.. Warning::
  Make sure the connector **DOES NOT** get wet!!

**Cleaning the EEG cap:**

1.  Turn net inside out
2.  Soak the net for 10 minutes in the disinfectant. For first 2-3 minutes gently repeatedly plunge the net in disinfectant.
3.  Fill the rinse bucket with warm (not hot) tap water
4.  Repeatedly plunge the net in clean water (gently). Rinse water and repeat at least 4 times
5.  Use one of the foamboard head models to dry the EGI net. Place a towel on the head model and place the net onto the head model to dry.
6.  ``Alternative:`` Air dry the NetStation

.. Note::
  Refresh disinfectant regularly using the concentrated solution that is in the HD-EEG room (in a 1:4 ratio with solution & regular tap water; make solution of 2L).

**Shutting down the EGI system:**

1.	Close Netstation
2.	Start Firefox, click on “System” and select “Shutdown”
3.	Shut down the EGI recording device (Mac)
4.	Shut down the amplifier
5.	Shut down the transformer box
6.	Shut down the stimulus laptop

.. Note::
  Leave the HD-EEG room in a clean state (i.e. no dirty towels etc.) and make sure everything is set for the next recording (i.e. fresh towels, materials cleaned, etc.).


8. EGI electrode layout
---------


.. image:: /images/egi/EGI_fig5.JPG
**Figure 5.** EGI electrode layout (image used from EGI manual)*


9. Scripts
---------

:EGI scripts:
  | ``EGI_connect.m``         Connect stimulus PC to EGI NetStation
  | ``EGI_sendTrigger.m``     Send trigger to EGI NetStation
  | ``EGI_startRecording.m``  Start recording
  | ``EGI_stopRecording.m``   Stop recording
  | ``EGI_triggerDemo.m``     Demo script for sending triggers
