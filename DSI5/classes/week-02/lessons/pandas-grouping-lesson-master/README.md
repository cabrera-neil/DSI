<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Pandas Grouping

> Unit 2, Lesson 6

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Interactive jupyter notebook with structured lesson content | [Link](./intro-to-grouping-pandas-lesson.ipynb)|
| Data | Titanic Dataset | [Link](./datasets/titanic_clean.csv)|
|| UFO dataset | [Link](./datasets/ufo.csv)|
| Solutions | Solution code for lesson notebook | [Link](./solution-code/intro-to-grouping-pandas-lesson-solutions.ipynb)|
|| Solution code for practice notebook | [Link](./solution-code/practice-pandas-grouping-solutions.ipynb)|
| Practice | Independent practice Jupyter notebook to be completed after the lesson | [Link](./practice/practice-pandas-grouping.ipynb)|

> **Dataset description:** 

The Titanic dataset contains information on passengers aboard the Titanic. It has 713 observations. Used in the lesson notebook.

The UFO dataset contains information on times and locations of UFO sitings from 1930 to 2014. It has approximately 80,500 observations. Used in the practice notebook.

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

*After this lessons, students will be able to:*

- Identify the situations in which **grouping** is useful.
- Explain and use the **`.groupby()`** function in `pandas`.
- Demonstrate aggregation and plotting methods by groups in `pandas`.

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

*Before this lesson(s), students should already be able to:*

1. Execute basica Pandas commands

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> **Total Time: 90 mins**

- Opening: Overview of Multi-Dimensional Data Analysis (5 mins.)
- Analyzing Data by Group: Examples (10 mins.)
  - Subset aggregation (5 mins.)
  - Hierarchical aggregation (5 mins.)
- Exploring the Titanic Data Set with Grouping (5 mins.)
- Introducing `pandas` `.groupby()` Function (10 mins.)
- Grouping by Multiple Variables (10 mins.)
- Applying Basic Functions to Groups (10 mins.)
- Removing the Hierarchical Index (10 mins.)
- Applying Custom Functions with `.apply()` (10 mins.)
- Plotting Basic Histograms with Groups (10 mins.)
- Grouped Histograms with `pandas` (10 mins.)

---

<!--- If a repo contains any additional practice files or supplementary resources (PDFs, etc) describe them here  --->

> OPTIONAL: Practice/Resources
- Practice notebook containing seven prompts for students to practice using `.groupby()` on the UFO dataset.

---

## Additional Resources

<!--- This section lists useful reference materials that can inform, extend, or deepen a student's understanding of the material. While this may seem like a "nice to have" feature, we normally see a range of advanced and remedial students in our classes. Curating these resources allows us to provide targeted materials and suggestions that instructors can use to support different student needs. --->

*For more information on this topic, check out the following resources:*

- [Pandas Documentation: split-apply-combine](https://pandas.pydata.org/pandas-docs/stable/groupby.html)

---