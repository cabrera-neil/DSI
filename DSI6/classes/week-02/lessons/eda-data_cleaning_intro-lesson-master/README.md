<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to data representation and cleaning with pandas

> Unit 2, Lesson 3

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Jupyter notebook that can be rendered as slides to deliver lesson | [Link](./intro-to-data-representation-cleaning-with-pandas.ipynb)|
|| Interactive Jupyter Notebook for students to follow along on guided practice and do independent practice| [Link](./practice-inspecting-data-applying-functions.ipynb)|
| Data | Sales | [Link](./datasets/sales.csv)|
| Solutions | Solution code for guided and independent practive notebook | [Link](./solution-code/intro-to-data-cleaning-with-pandas-code-along-solution.ipynb)|
| Assets | Images, graphs, or files linked in lesson / notebook, as needed | [Link](./assets/)|
| Archive | Older versions & source materials, when applicable  | [Link](./archive/) |

> **Dataset description:** Small dataset of sales data with 200 observations. Features of the dataset are volume sold, 2015 profit margin, 2015 Q1 sales, and 2016 q_1 sales. This data is used in the independent practice portion of the lesson for students to practice using pandas attributes and methods on.

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

*After this lessons, students will be able to:*

- Inspect data types.
- Clean up a column using `df.apply()`.
- Recognize situations in which to use `.value_counts()` in your code.

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

*Before this lesson(s), students should already be able to:*

- **Execute** basic Pandas commands

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> **Total Time: 90 mins**

- Opening: Common Data Cleaning Strategies (20 mins)
- Data Quality Measures (10 mins)
- `pandas` Tools for Cleaning Data (10 mins)
  - Overview of commands (2 mins)
  - The `.apply()` function (4 mins)
  - The `.value_counts` attribute (4 mins)
- Common Operations on Data by Type (10 mins)
- Guided Practice: Inspecting Data Types and Applying Functions (15 mins)
- Independent Practice: Sales Data (25 mins)

---

<!--- If a repo contains any additional practice files or supplementary resources (PDFs, etc) describe them here  --->

## Additional Resources

<!--- This section lists useful reference materials that can inform, extend, or deepen a student's understanding of the material. While this may seem like a "nice to have" feature, we normally see a range of advanced and remedial students in our classes. Curating these resources allows us to provide targeted materials and suggestions that instructors can use to support different student needs. --->

*For more information on this topic, check out the following resources:*

- [Pandas Tutorial from Tutorials Point](https://www.tutorialspoint.com/python_pandas/)

---