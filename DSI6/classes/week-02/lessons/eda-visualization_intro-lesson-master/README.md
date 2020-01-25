<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Visualization principles and Python viz intro

> Unit 2, Lesson 5

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Jupyter notebook that can be converted into slide deck for lecture | [Link](./python-data-viz-principles.ipynb)|
| Data | Sales Info | [Link](./datasets/sales_info.csv)|
| Solutions | Solution code for practice notebook | [Link](./solution-code/explore-python-data-viz-solutions.ipynb)|
| Practice | Jupyter notebook with prompts for practice | [Link](./practice/explore-python-data-viz.ipynb)|
| Assets | Images, graphs, or files linked in lesson / notebook, as needed | [Link](./assets/)|

> **Dataset description:** Small dataset of sales data with 200 observations. Features of the dataset are volume sold, 2015 profit margin, 2015 Q1 sales, and 2016 q_1 sales. This data is used in the independent practice portion of the lesson for students to practice using pandas attributes and methods on.

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

*After this lessons, students will be able to:*

1. **Describe** the characteristics of a great data visualization.

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

*Before this lesson(s), students should already be able to:*

1. Execute Pandas commands

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> **Total Time: 180 mins**

I. **Lecture** (80 mins)

- Opening: Why Use Data Visualization? (20 mins.)
- Anscombe's Quartet (10 mins.)
- Attributes of Good Visualization (10 mins.)
- Choosing the Right Chart (40 mins.)
  - The Bar Chart (10 mins.)
  - The Pie Chart (10 mins.)
  - The Scatter Plot (10 mins.)
  - The Histogram (10 mins.)

II. **Guided Practice** (100 mins)

- Opening (5 mins)
- Pandas Plotting Documentation (5 mins)
- Line Plots (20 mins.)
  - Line Plot with a DataFrame
  - Line Plot with a Series
  - Change the size of a plot
  - Change the color of a plot
  - Change the style of individual lines
  - Create a line plot of ZN and INDUS in the housing data
- Bar Plots (30 mins.)
  - Bar plot from a series
  - Pandas + Matplotlib
  - Horizontal bar plots
  - Bar chart with two columns
  - Stacked bar charts
  - Stacked horizontal bar charts
  - Plotting `.value_counts()`
  - Stacked horizontal bar chart of all columns of `df`
- Histograms (10 mins.)
  - Single histogram
  - Adjusting bins
  - Histogram of `MEDV` feature
- Boxplots (5 mins.)
  - Create a boxplot
- Scatter Plots (5 mins.)
  - Scatter plot of two variables
  - List comprehension to change dot sizes
- Seaborn `pairplot` (5 mins.)
- Seaborn `heatmap` (5 mins.)
- Understanding figures, subplots, and axes (5 mins.)
- Extra Customization (5 mins.)

---

<!--- If a repo contains any additional practice files or supplementary resources (PDFs, etc) describe them here  --->

---

## Additional Resources

<!--- This section lists useful reference materials that can inform, extend, or deepen a student's understanding of the material. While this may seem like a "nice to have" feature, we normally see a range of advanced and remedial students in our classes. Curating these resources allows us to provide targeted materials and suggestions that instructors can use to support different student needs. --->

*For more information on this topic, check out the following resources:*

- [Pandas Plotting Documentation](https://pandas.pydata.org/pandas-docs/stable/visualization.html)

---