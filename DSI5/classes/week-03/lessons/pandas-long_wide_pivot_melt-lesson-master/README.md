<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Pandas data transformation: long format, wide format, pivoting, melting

> Unit 2, Lesson 12

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Interactive jupyter notebook with structured lesson content, part 1 | [Link](./long-wide-pivoting-melting-in-pandas.ipynb)|
| Data | NPAS parsed Trunc Demo Sample | [Link](./datasets/NPAS_parsed_trunc_demo_sample.csv)|
|| NPAS parsed Trunc Demos | [Link](./datasets/NPAS_parsed_trunc_demos.csv)|
|| NPAS parsed Trunc Long Missing | [Link](./datasets/NPAS_parsed_trunc_long_missing.csv)|
|| NPAS parsed Trunc Survey | [Link](./datasets/NPAS_parsed_trunc_survey.csv)|
|| NPAS parsed Trunc Wide Missing | [Link](./datasets/NPAS_parsed_trunc_wide_missing.csv)|
|| NPAS parsed Trunc | [Link](./datasets/NPAS_parsed_trunc.csv)|
|| NPAS parsed Data | [Link](./datasets/NPAS-data.csv)|
| Solutions | Solution code to lessons and practice activities | [Link](./solution-code/long-wide-pivoting-melting-in-pandas-solution.ipynb)|
| Resources | Small Jupyter notebook with examples of `.melt()` and `.pivot_table()` | [Link](./resources/simple-example-melt-pivot-table.ipynb) |

> **Dataset description:** This is a pre-cleaned and modified version of the full "Nerdy Personality Attributes" survey, which asked subjects to rate themselves based on questions related to "nerdiness" as well as more general personality traits such as openness and extraversion. Researchers also collected demographic information from the subjects.

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

*After this lessons, students will be able to:*

- Understand the differences between long and wide format data.
- Understand pivot tables.
- Practice transforming data between long and wide formats.
- Practice creating pivot tables.
- Learn how to avoid common pitfalls and obstacles in data transformation with `pandas`.

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

*Before this lesson(s), students should already be able to:*

1. Be able to use `.group_by()` statements in Pandas

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> **Total Time: 90 mins**

- Wide Format Data (5 mins.)
- Load and Examine the NPAS Data (5 mins.)
- Long Format Data (5 mins. )
- Using `pandas`' `.pivot_table()` Function: Long to Wide Format (10 mins.)
- MultiIndex/Hierarchical Indices in `pandas` (10 mins.)
- Using `pandas`' `.melt()` Function: Wide to Long Format (5 mins.)
- Summarizing Data With `.pivot_table()` and Aggregate  Functions (10 mins.)
- The Inner Workings of the MultiIndex (10 mins.)
- Getting Rid of the MultiIndex: "Flattening" Data (10 mins.)
- A Preface: Merging and Joining With Long and Wide Format Data (10 mins.)
- `pandas`' `.merge()` function: Joining Long Format vs. Wide Format Data (10 mins.)

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

- [Reshaping and Pivot Tables](https://pandas.pydata.org/pandas-docs/stable/reshaping.html)
- [`.melt()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.melt.html)

---