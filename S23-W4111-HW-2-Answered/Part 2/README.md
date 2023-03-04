# W4111 - Intro. to Databases (S23):<br> Course Projects and Homework Assignments

## Introduction

This repository/project defines and supports homework assignments in W4111 - Intro. to Databases,
sections 002/V02 for the spring 2023 semester. There are three folders:
1. ```/HW2``` contains the definition and starter files for HW2.
2. ```/HW3``` contains the definition and starter files for HW3.
3. ```/HW4``` contains the definition and starter files for HW3.

Cumulatively the homework assignments define a course project that students will implement. Once
completed, students can finalize the final results in one of the following folders:
- ```/programming_track```
- ```/non_programming_track```


## Initial Setup

Students should copy the directories (and content) ```HW2, HW3, HW4, programming_track``` and
```non_programming track``` into the directory ```student_work```. Students will do their work
and implementations in the subdirectories of ```student_work```. This approach enables the instructor
to add and update the HW/project definition and files without creating merge conflicts for students.

The [Ed discussion for HW2](https://edstem.org/us/courses/32981/discussion/2617289):
- Defines additional setup steps and projects to clone.
- It is important that students follow the instructions in the Ed post, including configuring the
referenced projects and loading the starting database.

There is a Jupyter notebook ```s23_w4111_project.ipynb``` that contains configuration and setup tests.
Students should copy the notebook into ```/student_work``` and run the tests. We will update and extend
the notebook during HW and project implementation.

## Corrections

- The folder ```/corrections``` contains some files that correct setup mistakes:
  - ```hw2_v2.sql``` is a correction on data loading. Please drop your previous loaded schema, if you have
loaded it and replace with running this SQL script. __Remember to rename__ the schema at the
beginning of the file by replace ```dff3``` with your UNI.



