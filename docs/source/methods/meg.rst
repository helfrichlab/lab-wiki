.. include:: /Includes.rst.txt

======
MEG
======

.. autosummary::
   :toctree: generated


| **From: HelfrichLab**
| **Authors:** Isabel Raposo, Jan Weber, and Frank van Schalkwijk
| **Contact:**

Contents
------
.. code-block::

  1. Contacts
  2. Equipment
  3. Supplies
  4. Scheduling recording time
  5. Checklist prior to a recording
  6. Participant preparation prior to recording
  7. Preparations prior to experiment
  8. Conducting an experiment
  9. Checklist after a recording
  10. Data export
  11. Cleaning
  12. Channel notes
  13. Other notes
  14. Alarms
  15. Open questions

1. Contacts
------
:Jürgen Dax:
    | **Tel:** 87706
    | **Workdays:** Mon, Wed, & Fri

:Gabi Walker-Dietrich:
    | **Tel:** 87706
    | **Workdays:** NA

:Timmo Larbig:
    | **Tel:** 87710
    | **Workdays:** NA

:Timmo Larbig:
    | **Tel:** 87705
    | **Workdays:** NA

:Markus Siegel:
    | **Tel:** 81200
    | **Workdays:** NA

2. Equipment
------
:MEG room:
  * MEG scanner
  * Response boxes (4x)
  * Eye-tracking
  * Electrooculogram electrodes (2x)

:Control room:
  * Beamer
  * Recording PC
  * Eye-tracking PC
  * Eye-tracking battery (table close to MEG entry)
  * Stimulus PC
  * Stimulus laptop
  * Intercom

:M/EEG prep. room:
  * Scrubs in gray cabinets in front of changing room (left)
  * Bedding in cabinet of M/EEG prep. room

3. Supplies
------

Supplies are found in M/EEG prep room #2 under the sink & large gray cabinet.
Covers are in cabinet of MEEG prep room #1

4. Scheduling recording time

------
.. code-block::

  1. Obtain access to M/EEG Google calendar
  2. Reserve a timeslot

5. Checklist prior to a recording
------

:Control room:
  * Main lights on (2x)
  * Start console (CTF MEG; #51).
  * Turn on power switches/boxes (1x left of trigger box; 2x at desk level).
  * Recording PC (fo2-25) is on.
  * Set trigger box set appropriately (#13; e.g., ‘Laptop’)
  * Turn on stimulus PC (fo2-36 in the pc cabinet with the class door; right side of the desk).
  * Select Braun lab profile
  * Flip power switch on far left for eye-tracking PC
  * Turn on eye-tracking PC ([note:] located on the desk, not the pc labeled ‘eye-tracking’)
  * Select Eye-track OS
  * Setup stimulus laptop, connect HDMI & “USB triggers” cables, and power
  * Projector input to laptop (bottom of desk; radio console; #11)
  * Trigger output to laptop (bottom of desk; radio console; #12).
  * Set intercom to “listen” only
  * Volume levels for intercom (MEG room & speaker).
  * Obtain eye-tracking camera from the office of Gabi & Jürgen (gray cabinet).

.. Warning::
  PC fo2-25 should not be turned off or logged

.. Note::
  Press & hold to make sure both lights are switched (COM5 issue).

.. Note::
  Speaker volume is separate control (labeled grey box; top left).

:MEG room:
  * Lights in MEG room (small black box @ front right)
  * Power switch for beamer (next to MEG light box)
  * Beamer to “on” with the remote
  * Open door (button)
  * Photodiodes (4x) connected to switch box
  * Response boxes connected to switch box (1) (4 wires; 2 for each button)
  * Chair completely forward & down
  * Prepare covers for blanket & pillow
  * Check electrode plasters & leukopor are present
  * Install eye-tracking camera on left arm rest.
      Remove cushion & slide camera mount into outer railing. Ensure that camera
      is secure. Remove lens cap.
  * Obtain battery and associated power cables.
  * Connect eye-tracking camera to battery with power cables as well as MEG using the fiberoptics cable (orange) that is located in the cabinet from within the MEG room (left side of the door).
  * Turn on eye-tracking battery

.. Note::
  **Response boxes:** Port 1 = small amplitude; Port 2 = large amplitude.


6. Participant preparation prior to recording
------

:Participant:
  * Fully briefed on the procedures and experiment (in MEEG preparation room)
  * No makeup, piercings, or metal on/in the body
  * Changed into scrubs (utilize changing room).


7. Preparations prior to experiment
------

:MEG preparations:
  * Move chair completely forward before manipulation of MEG is possible
  * MEG position tilted backwards to enable vision of screen. Tilt further back for smaller heads.
  * Position participant in chair, provide blanket and cushion for back support.
  * Place localization coils/channels at two preauricular points & nasion. Cables facing downwards to avoid interference with MEG sensors. Fix with sticker + leukopor + nose + shoulder fix.
  * Move chair backwards and incrementally raise participant into MEG until top of head lightly touches MEG
  * Ask participant to slouch a bit (imagine sitting in this position for the next hour). Check position
  * Lower projection screen, flip mirror system, and check participant’s vision
  * Set projector size and focus using strings underneath beamer. [Emphasis:] Screen width = 52 cm
  * Apply foam rubbers + covers to fix head in place (located in MEG room next to stim box hub)
  * Setup eye tracking (see next section).

.. Note::
  If vision is compromised, reset and angle MEG further backwards

:Eye-tracking preparations:
  * Manipulate eye-tracking camera that both eyes are visible. Use camera focus ring to ensure image quality.
  * On eye-tracking PC:
  * Setup options according to those pictured (settings are displayed on the adjacent wall in the MEG control room & attached at the end of manual)
  * “Set options” -> mouse stim off -> select both eyes -> long-range mount -> Binoc|Monoc
  * Select both eyes & click on them to verify
  * Select “auto trigger”
  * Switch console (#11) to stimulus PC (fo2-36)
  * Start “Track” program
  * Overwrite “demo” recording.
  * Calibrate
  * Once calibrated: exit program
  * Switch to eye-tracking PC:
  * Select “validate” -> “Accept”
  * Shut down stimulus PC (fo2-36). Leave eye-tracking PC running!

:Recording preparations:
  * Provide response box
  * Check mirror angle for photodiode positioning
  * Photodiode(s) placement (bottom right)
  * Close door (final closing procedure by pressing the “close” button)

.. Note:
  Communicate with your participant


8. Conducting an experiment
------

.. Note::
  Take the time to ensure your participant is comfortable and data acquisition
  as good as it can be. This is far better than spending time cleaning low-quality
  data.

  .. Note:
    Communicate with your participant

:Starting your recording:
  * Start “Acq” program on the recording PC (Acq computer)
  * Select study (e.g., “Dual_task”)
  * Register patient -> TUE##
  * File -> protocol
  * Acquire data
  * Test -> close door, verify signal, and check if all OK.
  * Amp settings:
  * “ADC vol” 	(photodiode) 		= 5
  * “Stim” (response box(es)) 	= 2k-5k
  * All OK? -> start
  * Head localization
  * Start recording by clicking “start”
  * Set intercom to “listen”
  * Initiate block start & actual recording by sending a trigger through COM5 port

.. Note::
  *Stim response box:* Port 1 = lowest amplitude; port 2 = largest amplitude


.. Note::
  "Start recording" enables data acquisition. The actual recording starts by
  sending a trigger to the PC!


9. Checklist after a recording
------

  * Remove photodiode(s)
  * Remove response box
  * Mirror system to neutral (otherwise you blind the participant upon removal of the screen)
  * Screen position to neutral
  * Eye-tracking camera pivoted out of participant’s way
  * Lower MEG chair to lowest position
  * Move MEG chair fully forward
  * Take participant out of MEG room


10. Data export
------

  * Turn on fo2-53 PC
  * Switch console to data transfer PC (fo2-53)
  * Start program “file transfer from Acq”
  * Select correct recording & storage folders
  * Copy files through drag & drop. [Note:] Start this process early as copying takes ages.


11. Cleaning
------

:MEG room:
  * Photodiodes correctly placed in storage position (hanger on the left wall)
  * Sufficient supplies (electrode stickers & leukopor). Replenish if insufficient
  * MEG chair to neutral position (lowest & forward)
  * MEG to neutral position (forward)
  * Response box back to control room
  * Lens cap placed on eye-tracking camera, battery powered off, power cables disconnected, fiberoptics cable back in cabinet.
  * Eye-tracking battery + cables back on table next to MEG room entrance door.
  * Return eye-tracking camera to gray cabinet in office of Gabi & Jürgen
  * Disinfect MEG room with spray (i.e., head coil, chair, arm rests, etc.)

:Control room:
  * Intercom to “listen” only
  * Beamer to “off”
  * Switch off beamer (power switch)
  * Switch of lights for MEG room
  * Switch off eye-tracking PC
  * Disconnect stimulus laptop (HDMI & USB triggers)
  * Switch trigger output (bottom of desk; radio console) to stimulus PC
  * Beamer & trigger control to default settings (#11: fo2-35; #12: fo2-36)
  * All PCs off except recording PC (fo2-25)
  * Console off (CTF MEG; #51). Should show orange light as standby
  * Power switches/boxes (2x) off (left of trigger box)
  * Disinfect control room with wipes
  * Turn of main lights (2x)
  * Deposit laundry and sort if the bucket is full (located next to scrubs cabinets)

.. Warning::
  Leave recording PC (fo2-25) ON and logged in!


12. Channel notes
------

  * UDI0001 = response box; Amp settings: Stim = 2k-5k
  * UADC001 = photodiode #1; Amp settings: ADC vol = 5
  * UADC002 = photodiode #2; Amp settings: ADC vol = 5
  * UADC012 – UADC016 = eye-tracking channels
  * Trigger hub in MEG room: response box connected to ports #1 & #2
    |   o	Port #1 = Left button	- Has lowest amplitude (channel UDI0001)
    |   o	Port #2 = Right button	- Has highest amplitude (channel UDI0001)

13. Other notes
------

* If ACQ is turned off: login requires username (meg) and password (meglab). Page 1 of logbook.

* Signal recorded on UDI0001 shows response for both buttons of the response box. Note that the amplitude is larger for one button vs. the other (amp is also
really high, so rescale to see it).

* Hardware filters are offline filters and therefore influence your raw signal.
Can also apply visual filters in one of the menus under “display” during acquisition.


14. Alarms
------

:Alarm #1 - O2 sensor:
  * In case of helium leak inside MEG:
  * **Helium is non-toxic but competes with oxygen**. Ventilate helping participant!
  * Open MEG door, & all doors leading outside.
  * Get patient out & notify staff

:Alarm #2 - Helium recycling:
  * In case of helium recovery balloon being full
  * Alarm sounds like a bird
  * Vent valve located in MEG room emergency exit -> turn middle valve to the left
  * Open outer door & release on site. Notify staff

:Alarm #3 - Helium deliver:
  * Unrelated to us.
  * Takes place on *Wednesdays*
  * Responsible: Christoph Braun/Jürgen Dax.

:Alarm #4 - Helium recovery:
    * In case of a snag in the recovery cable
    * Right side out of MEG room, inspect cable.
    * If all OK, press “reset” button or do hard reset by replugging power cable


15. Open questions
------

1. Are data saved after every block?
2. How to pause a recording?
