Main file for detection is phish.py
===========================================================
Description - The project is a template. The real project needs an extraction of urls from the web and
train of ML algorithm. These phases


The implemented parts are taken from the report file:
1) white list
2) black list
3) ML detection algorithm simulation

=======================
Currently there is no prediction algorithm so mock class is added to simulate prediction probability
(see class LearnerWrapper). Also mock class for feature extractions class FeatureExtractor)

Class PhishDetector is configured by policy of config.py and allows to skip phases of detection if necessary.

