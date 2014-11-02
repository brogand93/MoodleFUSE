==========
MoodleFUSE
==========

Moodle filesystem sync with FUSE
################################

.. image:: https://magnum.travis-ci.com/BroganD1993/MoodleFUSE.svg?token=A11YYSj4ZhksVqqEC7xW&branch=master
    :target: https://magnum.travis-ci.com/BroganD1993/MoodleFUSE
 
 
Moodle is WIT`s online learning platform used in schools and universitys all around the world. 
Uploading and downloading files from Moodle can take time for lecturers and students because it 
first involves logging into a web interface and uploading files individually.

MoodleFUSE would aim to provide a simplified way to sync Moodle resources to a local filesystem. 
MoodleFUSE watches the local Moodle filesystm waiting for changes or modifications. 
When a change is detected (addition / deletion / modification) MoodleFUSE performs the corresponding 
operation to the remote Moodle file. Similarly MoodleFUSE will download assignments automatically 
onto the local filesystem after the deadline for the assignment has passed grading of the assignments 
can be performed locally by adding grades to an auto generated CSV file. 
