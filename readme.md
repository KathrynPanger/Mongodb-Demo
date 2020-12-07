# MongoDB Demo: Creating a Database from an API pull

## Summary:
This repository is designed to walk a user through the process of using MongoDB to pull and refer to JSON data. This readme will 1) Present a list of files which will be used in this demonstration, 2) Provide discrete steps that a user can follow in navigating these files for their learning, and 3) Provide snippets of sample code that the user can complete on their own in order to replicate the process with their own JSON data.

## The Files:

<b>What is MongoDB and why use it: </b>
[MongoDB Slideshow](https://docs.google.com/presentation/d/1CmRUm_FBiCf2ZhWJj3Chx8bdpD3bLOhqSQd9uQJBPQQ/edit?usp=sharing ).


- The nature and use of MongoDB
- Relational vs Non-Relational Databases
- How to set up MongoDB and MongoDB Compass
- How to insert records directly into MongoDB
- Using MongoDB Atlas

<b>Using Python to Create Collections</b>
(mongodb_insert.ipynb)
- Example code for importing Google Places API data and external JSON data into MongoDB
- Explanations of each portion of the code and its function

<b>Just the Code</b>
(mongod_insert.py)
- Code from mongodb_insert in a python file, in case you're not into notebooks.

<b>Resources Folder</b>
(contains zip_codes.csv)
- Folder contains a table of zip codes and their respective latitude and longitude coordinates
- Used for mongodb_insert.(ipynb/py) activity

<b>Extras Folder</b>
(contains plus_pygeocode.ipynb)
(contains sf_zips.csv)
- Folder contains a longer version of mongodb_insert using pygeocode to append latitude and longitude variables to zip code table.
- Folder contains original zip codes file.
- Not needed for the activity unless you want to know how to use pygeocode.

## Steps: 
1. View mongodb_explained and set up MongoDB on your computer.
2. View mongodb_insert.ipynb and follow the directions therein for each cell.
3. View practice.ipynb and fill in the commented out portions with your own code.
4. Celebrate! Now you can organize your JSON data.
