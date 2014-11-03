==========
MoodleFUSE
==========

Moodle filesystem sync with FUSE
################################

.. image:: https://magnum.travis-ci.com/BroganD1993/MoodleFUSE.svg?token=A11YYSj4ZhksVqqEC7xW&branch=master
    :target: https://magnum.travis-ci.com/BroganD1993/MoodleFUSE
    :alt: 'Repository status'
.. image:: https://badge.waffle.io/brogand1993/moodlefuse.svg?label=ready&title=Ready 
   :target: https://waffle.io/brogand1993/moodlefuse 
   :alt: 'Stories in Ready'
 
 
Moodle is WIT`s online learning platform used in schools and universities all around the world. Uploading 
and downloading files from Moodle can take time for lecturers and students. It first involves logging into 
a web interface and uploading files individually.

MoodleFUSE aims to provide a simple way to map Moodle resources to a local filesystem. MoodleFUSE syncs a 
Moodle filesystem to a local FUSE filesystem.  It then watches the new filesystem waiting for changes or 
modifications. When a change is detected in the FUSE filesystem MoodleFUSE performs the same operation to 
the remote Moodle file. 

The list of supported operations is (Assuming appropriate user rights on Moodle):

-	Addition of courses
-	Addition of course sections
-	Deletion of course sections
-	Addition of course files
-	Deletion of course files
-	Modification of course files

MoodleFUSE will also download assignments automatically onto the FUSE filesystem after the assignment deadline. 
Grading of the assignments can be performed locally by adding grades to an auto generated CSV file.
