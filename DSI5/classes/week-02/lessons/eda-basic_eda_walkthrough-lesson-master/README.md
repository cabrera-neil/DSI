<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Walkthrough of basic EDA Procedure

> Unit 2, Lesson 15

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Interactive jupyter notebook with structured lesson content | [Link](./basic-eda-walkthrough.ipynb)|
| Data | Boston housing data| [Link](./datasets/housing.csv)|
| Solutions | Solution code to Jupyter notebook | [Link](./solution-code/basic-eda-walkthrough-solutions.ipynb)|
|| Alternate solutions notebook | [Link](./solution-code/instructor-alternates/Ram\ EDA\ basic\ walkthrough\ lesson\ Workbook.ipynb)|

> **Dataset description:** The boston housing dataset is a small dataset consisting of 506 observations and 14 columns. It contains information on housing in the Boston area from the 1970s. Students will use the dataset to practice the EDA workflow.

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

> This lesson uses Boston housing data to walk through a basic exploratory data analysis procedure, starting at the beginning with loading the data.

*After this lessons, students will be able to:*

1. Have an intuition for how to go about exploring data

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

*Before this lesson(s), students should already be able to:*

1. Explore data using Pandas
2. Perform basic visualizations of data

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> **Total Time: 130 mins**

- Opening: Description of the Boston Housing Data (10 mins.)
- Loading the Data (5 mins.)
- Describing the Basic Format of the Data and the Columns (5 mins.)
- Dropping Unwanted Columns (5 mins.)
- Cleaning Corrupted Data (10 mins.)
- Counting Null Values and Dropping Rows (5 mins.)
- Renaming Columns (10 mins.)
- Describing Summary Statistics for Columns (10 mins.)
- Investigating Potential Outliers With Box Plots (10 mins.)
- Plotting All Variables Together (10 mins.)
- Standardizing Variables (20 mins.)
- Plotting the Standardized Variables Together (10 mins.)
- Looking at the Covariance or Correlation Between Variables (20 mins.)


---

<!--- If a repo contains any additional practice files or supplementary resources (PDFs, etc) describe them here  --->
<!---
> OPTIONAL: Practice/Resources
- Item 1 description
- Item 2 description

---
--->

## Additional Resources

<!--- This section lists useful reference materials that can inform, extend, or deepen a student's understanding of the material. While this may seem like a "nice to have" feature, we normally see a range of advanced and remedial students in our classes. Curating these resources allows us to provide targeted materials and suggestions that instructors can use to support different student needs. --->

*For more information on this topic, check out the following resources:*

- [EDA Techniques](http://www.itl.nist.gov/div898/handbook/eda/section3/eda3.htm)
- [Medium Post on how to perform EDA](https://medium.com/@InDataLabs/why-start-a-data-science-project-with-exploratory-data-analysis-f90c0efcbe49)
- [Spurious Correlations](http://www.tylervigen.com/spurious-correlations)

---