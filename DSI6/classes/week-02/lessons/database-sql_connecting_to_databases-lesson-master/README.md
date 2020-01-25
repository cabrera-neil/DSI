<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to SQL: connecting to databases

> Unit 2, Lesson 8

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Interactive jupyter notebook with structured lesson content | [Link](./intro-to-sql-connecting-to-databases.ipynb)|
| Data | Housing data (CSV) | [Link](./datasets/housing-data.csv)|
|| Test SQL database | [Link](./datasets/test_db.sqlite)|
|| Test SQL database backup | [Link](./datasets/test_db_backup.sqlite)|
| Solutions | Solution code to lessons notebook prompts | [Link](./solution-code/intro-to-sql-connecting-to-databases-solutions.ipynb)|
| Assets | Images, graphs, or files linked in lesson / notebook, as needed | [Link](./assets/)|

> **Dataset description:** 

The Housing data is a CSV that students will use load into the SQL database during the lesson.

The SQL database is the database that students will load data into and query.

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

*After this lessons, students will be able to:*

- Connect to a local or remote database using the command line, Python, or `pandas`.
- Connect to a local or remote database using SQLite Manager (for SQLite) or Postico (for POSTGRES).
- Perform queries using SELECT.
- Perform simple aggregations suing COUNT and MAX/MIN/SUM.

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

*Before this lesson(s), students should already be able to:*

1. Comfortably work with the Pandas library

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> **Total Time: 170 mins**

### Lesson Guide

- Connecting to a Local Database (60 mins.)
    - SQLite
    - Interacting with SQLite
    - Common SQL Command Patterns
    - SQLite Command Line Utility
    - Creating Tables and Adding Columns
    - Adding Data
    - Updating Records
    - Removing Records
- Connecting to a Remote Database (20 mins.)
    - PostgreSQL
- Comparison of SQL Commands (5 mins.)
- Intermission (10 mins.)
- SQLite from Python (20 mins.)
    - SQLite3 Package(5 mins.)
    - SQLite3: Adding Data (10 mins.)
    - Adding Data From a `.csv` File (5 mins.)
- `pandas` Connector (10 mins.)
    - Writing Data Into a Database (5 mins.)
    - Reading Data From a Database (5 mins.)
- SQL Syntax (20 mins.)
    - SELECT (5 mins.)
    - WHERE (5 mins.)
    - Aggregations (10 mins.)
- Independent Practice: Querying a Database (25 mins.)

---

<!--- If a repo contains any additional practice files or supplementary resources (PDFs, etc) describe them here

> OPTIONAL: Practice/Resources
- Item 1 description
- Item 2 description

---
--->

## Additional Resources

<!--- This section lists useful reference materials that can inform, extend, or deepen a student's understanding of the material. While this may seem like a "nice to have" feature, we normally see a range of advanced and remedial students in our classes. Curating these resources allows us to provide targeted materials and suggestions that instructors can use to support different student needs. --->

*For more information on this topic, check out the following resources:*

- [SQLite3's website](http://www.sqlite.org)  
- [SQLite — Python tutorial](http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html)  
- [SQL Zoo](http://www.sqlzoo.net)

---