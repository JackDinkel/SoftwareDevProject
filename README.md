# SoftwareDevProject
This repo contains the development code and files for the BuyBack Revolution team in the Software Development Methods and Tools class


Project:
BuyBack Revolution


Team Members:
Jack Dinkel
Derek Gorthy
Michael Swisher


Website:
buybackrevolution.com


Repository Structure:
This repository is split into three sections, Documents, Scripts, and Web.

The Documents directory contains all the documents for the project. Competitors contains various tests and notes about scraping our competitor's websites, such as Gazelle.com. Legal contains a document discussing the legality of our project. Miscellaneous contains various random documents and notes. Reports contains all the submissions for this project, namely Part1, Part3, Part5, and Part6. Lastly, Systems contains various notes made during the development of our server.

Scripts contains several different Python scripts written for the project. This includes an initial test script, our web scrapers, and automated unit tests.

Web contains the source files for our website and notes about them. Design contains some notes on the general layout of the website as well as some templates and themes. HTML contains the actual source files from the website. There are many main php files as well as some css and js helper files. Also included are fonts, error pages, and images. Changing these files will change the look of the website. Lastly, misc contains several old files that were used in the development of the website, but are not in the final version.


Deployment:
The website can be found at www.buybackrevolution.com and accessed using a standard web browser as you would any other website. Refer to the video in VIDEO for a demonstration of its functionality.


Testing:
The automated unit testing script can be found in Scripts/test.py. It was written using the Python UnitTest module. To run the tests simply use the command python test.py and the tests will run. If the test is run on a local machine, it is possible the tests will fail due if the MySQLdb module is not installed. If this is the case, simply open Scripts/main.py and comment out line 3 (import MySQLdb). After this, the test script should be able to run and pass 31/31 tests.

The User Acceptance Tests are located in Documents/Reports/user_acceptance_tests.pdf.

For more information on testing, see the Part 3 document in Documents/Reports/BuyBackRevolution_Part_3.pdf


Auto-documentation:
The auto-documentation is done using the PyDoc module for python. The documentation itself is in Documents/Reports/auto-documentation.txt and is generated from the python file main.py, where the comments are written. The file was created by navigating to Scripts/ and running the command
pydoc main ../Documents/Reports/auto-documentation.txt