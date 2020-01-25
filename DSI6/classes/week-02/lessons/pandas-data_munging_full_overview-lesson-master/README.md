<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Review: pandas data munging full overview

> Unit 2, Lesson 20

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Interactive jupyter notebook with structured lesson content, part 1 | [Link](./pandas-data-munging-full-overview-prt1.ipynb)|
|| Interactive jupyter notebook with structured lesson content, part 2 | [Link](./pandas-data-munging-full-overview-prt2.ipynb)|
| Data | Drinks dataset | [Link](./datasets/drinks.csv)|
|| Updated drinks dataset| [Link](./datasets/drinks_updated.csv)|
|| UFOs dataset | [Link](./datasets/ufo.csv)|
|| Original users dataset| [Link](./datasets/users_original.txt)|
|| Updated users dataset | [Link](./datasets/users.txt)|
| Solutions | Solution code for part 1 | [Link](./solution-code/pandas-data-munging-full-overview-prt1-solutions.ipynb)|
|| Solution code for part 2 | [Link](./solution-code/pandas-data-munging-full-overview-prt2-solutions.ipynb)|
| Assets | Images, graphs, or files linked in lesson / notebook, as needed | [Link](./assets/)|
| Resources | Supplementary reading or reference materials, as needed | [Link](./resources/) |

### Dataset description

- Drinks: Small dataset of alcohol consumption by country
- Updated Drinks: same as Drinks dataset, with different column names
- UFOs: Large dataset of UFO sitings in the US from 1930 - 2014
- Original Users dataset: dataset of users on an unknown platform with information such as gender and occupation
- Users dataset: same as Original Users dataset, only with column names

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

*After this lessons, students will be able to:*

- Perform a wide range of commands in Pandas

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

*Before this lesson(s), students should already be able to:*

1. Work comfortably with the Pandas library

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

This covers the full breadth of data munging and manipulation features in pandas, covered thus far. It serves as a review and a nice reference. Can be walked through by the instructor calling on students to give the answers. Also covers some functionality not discussed up to this point.

> **Total Time: 180 mins (minimum)**

### Part 1

- The Basics of `pandas` DataFrames
    - Loading Data
    - A Basic Examination of DataFrames
    - Selecting Columns
    - Describing Data
- Exercise #1
- Filtering and Sorting DataFrames
    - Boolean Filtering
    - Sorting
- Exercise #2
- Renaming, Adding, and Removing Columns
    - Renaming Columns
    - Adding Columns)
    - Removing Columns
- Handling Missing Values
    - Finding Missing Values
    - Dropping Missing Values
    - Filling in Missing Values

### Part 2

- Exercise #3
- Split-Apply-Combine
    - `.groupby()`
    - Apply Functions to Groups and Combine
- Exercise #4
- Indexing
    - Location Indexing With `.loc()`
    - Position Indexing With `.iloc()`
- Other Frequently Used Features
    - Using Map Functions With Replacement Dictionaries
    - Encoding Strings as Integers With `.factorize()`
    - Determining Unique Values
    - Replacing Values With `.replace()`
    - Series String Methods With `.str`
    - Datetime Conversion and Arithmetic
    - Setting and Resetting the Index
    - Sorting by Index
    - Changing the Data Type of a Column
    - Creating Dummy-Coded Columns
    - Concatenating DataFrames
    - Detecting and Dropping Duplicate Rows
    - Writing a DataFrame to a `.csv`
    - Pickling a DataFrame
    - Randomly Sampling a DataFrame
- Infrequently Used Features
    - Creating DataFrames From Dictionaries and Lists of Lists
    - Performing Cross-Tabulations
    - Query-Filtering Syntax
    - Calculating Memory Usage
    - Converting Column to Category Type
    - Creating Columns With `.assign()`
    - Limiting the Number of Rows to Load in a File Read
    - Manually Setting the Number of Rows and Columns to Print

<!--- If a repo contains any additional practice files or supplementary resources (PDFs, etc) describe them here  --->

---

## Additional Resources

<!--- This section lists useful reference materials that can inform, extend, or deepen a student's understanding of the material. While this may seem like a "nice to have" feature, we normally see a range of advanced and remedial students in our classes. Curating these resources allows us to provide targeted materials and suggestions that instructors can use to support different student needs. --->

*For more information on this topic, check out the following resources:*

- [Medium Post: How to Learn Pandas](https://medium.com/dunder-data/how-to-learn-pandas-108905ab4955)

---