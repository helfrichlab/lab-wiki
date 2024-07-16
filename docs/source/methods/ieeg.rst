.. include:: /Includes.rst.txt

======
iEEG
======

.. autosummary::
   :toctree: generated


 Contents
 ------
 .. code-block::

   1. Manual
   2. Documents



 Contents
 ------
 | :ref:`iEEG_manual`
 | :ref:`iEEG_documents`


.. _iEEG_manual:

1. Manual
---------

:Channels:
    | ``DC1`` (purple trace): photodiode
    | ``DC2`` (red trace):    audio 3.5mm
    | ``DC3`` (green trace):  manual pedal/response box

.. note::
  Adding DC channels to the iEEG montage:

  1. Click on ``Bearbeiten`` and select ``Einstellungen``
  2. Scroll down the list of currently added electrodes. On the right hand side, select the button labeled ``Kanal anhängen``. This creates a new line at the bottom of the channel list
  3. Set the following characteristics in the newly created channel line:
    * Right click on the first column labeled ``Eingabe`` and select the desired channel (``DC1``, ``DC2``, or ``DC3``)
    * Right click on the first column labeled ``Ref`` and select ``keine``/empty
    * Set ``Type`` to EEG
    * Set ``LFF`` to 1 Hz (default)
    * Set ``HFF`` to “Aus”/off
  4. Click ``OK`` and close the window
  5. You can manually change amplitudes of individual channels by left clicking the signal label and pressing the up/down arrows on the keyboard
  6. Verify that signal is OK using the photodiode plugged into DC1

  .. note::
    Activating channels:

    1. Go to ``Einstellungen`` -> ``Datenerfassung``
    2. Select DC channel and click on ``Kanalstatus``
    3. Select ``Kanal ein``
    4. Select ``Uebernahme``
    5. Repeat per DC channel


**Room descriptives**

* Recording station located on the left or right side of the bed. Assign photodiode position accordingly.
* Screen is turned off as you enter and should be turned off as you leave.
* Keyboard is tucked into cupboard and should be stowed away when you leave.


**Manual markers**

* As soon as you start typing, a pop-up window will appear where you can type your manual marker
* Mark experiment start and end using manual markers
* Naming convention: ``RH exp # start``; ``RH exp # end``. Experiment nr. relative for each recording session


.. warning::
  * Communication with your subject is key. Be clear, patient, and friendly. It is preferable to come back another time than to force them to do a task against their perference.
  * Always adhere to COVID guidelines if applicable (i.e., wear an FFP2 mask)


.. _iEEG_documents:

2. Documents
---------
* `TUE iEEG patient consent form <https://drive.google.com/file/d/1_dV9Btn5-0i_N6mfswm3epMOpcqRnI95/view?usp=drive_link>`_
* `TUE iEEG patient information sheet <https://drive.google.com/file/d/1nFo9Jwfeh9eFXFikPNcH9_3wWDJ-PNRb/view?usp=drive_link>`_
* `TUE iEEG electrode information sheet <https://drive.google.com/file/d/1me4D_UT2YULn823p5ozVYnNfzrn9KacC/view?usp=drive_linkg>`_
* `TUE iEEG recording sheet <https://drive.google.com/file/d/1C2RIVT56SW-NAZHh8nHHQVft2VepwKpR/view?usp=sharing>`_
* `TUE iEEG task overiew <https://docs.google.com/spreadsheets/d/1bObFexVnTqAx4LjixtlGUuJBR6R3__Ur/edit?usp=drive_link&ouid=104327315070915086176&rtpof=true&sd=true>`_
* `TUE iEEG adding DC channels to montage <https://docs.google.com/document/d/11HqtePjqnUermh8BEfqPlsxvXU4SOy56XU9lBe0auRI/edit?usp=drive_link>`_
