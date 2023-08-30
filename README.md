## Introduction

This Git repository attempt so collect a range of code snippets used by the Kelly Hill Project
team to manipulate Survex data (SVX) files, export them to KML data and then into ArcGIS Pro.

This may expand over time to include other tasks to support our work.

### Who are the SA Speleo Council?
We are a bunch of cavers from South Australia, who visit, document and conserve cave and karst
around the state.  The Council is made up of representatives of the Cave Exploration Group of
South Australia (CEGSA), Flinders University Speleological Society Inc. (FUSSI) and the Scout 
Caving Group (SCG).

http://sasc.info/about/

### What is the Kelly Hill Project

## Script Info

### survey-group-to-layer.py

#### Problem
Caves grouped in different layers can't be published as a web layer, they need to be merged into one flat layer.  However this removes the ability to tweak individual points and lines.  

#### Resolution  
Write a Python script that will take all of the separate station and leg layers, and merge them into one publishable layer

#### Usage
Copy/paste script into ArcGIS Pro Python Console or Notebook.  Replace the constant names with relevant details
