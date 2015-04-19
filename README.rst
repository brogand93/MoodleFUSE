==========
MoodleFUSE
==========

Moodle filesystem sync with FUSE
################################

.. image:: https://badge.fury.io/py/moodlefuse.png
    :target: https://pypi.python.org/pypi/moodlefuse
.. image:: https://travis-ci.org/BroganD1993/MoodleFUSE.svg?branch=master
    :target: https://travis-ci.org/BroganD1993/MoodleFUSE
.. image:: https://coveralls.io/repos/BroganD1993/MoodleFUSE/badge.svg?branch=master 
    :target: https://coveralls.io/r/BroganD1993/MoodleFUSE?branch=master
.. image:: https://badge.waffle.io/brogand1993/moodlefuse.svg?label=ready&title=Ready 
    :target: https://waffle.io/brogand1993/moodlefuse

 
Moodle is WIT`s online learning platform used in schools and universities all around the world. Uploading 
and downloading files from Moodle can take time for lecturers and students. It first involves logging into 
a web interface and uploading files individually.

MoodleFUSE aims to provide a simple way to map Moodle resources to a local filesystem. MoodleFUSE syncs a 
Moodle filesystem to a local FUSE filesystem.  It then watches the new filesystem waiting for changes or 
modifications. When a change is detected in the FUSE filesystem MoodleFUSE performs the same operation to 
the remote Moodle file. 

The list of supported operations is (Assuming appropriate user rights on Moodle):

-   Listing of courses
-   Listing of course secctions
-	Addition of course sections
-	Renaming of course sections
-   Listing of course files
-	Addition of course files
-	Deletion of course files
-   Renaming of course files
-   Viewing of course files
-	Modification of course files
-   Listing of assignments
-   Listing of assignment submissions
-   Viewing of assignment submissions
-   Grading of assignment submissions

User guide for MoodleFUSE can be viewed on the `wiki 
<https://github.com/BroganD1993/MoodleFUSE/wiki/User-Guide/>`_.
