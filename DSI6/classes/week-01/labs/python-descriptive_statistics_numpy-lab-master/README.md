<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Descriptive statistics with Numpy lab

> Unit 1, Activity 9

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity | Jupyter Notebook with prompts for students to perform measures of central tendency and practice python Python functions | [Link](./describe-sales-data.ipynb)|
| Data | Sales Info Dataset | [Link](./datasets/sales_info.csv)|
| Solutions | Sample solutions to lab | [Link](./solution-code/describe-sales-data-solutions.ipynb)|
| Archive | Old lab in markdown file | [Link](./archive/LAB.md) |

> Dataset(s) description: Sales Info dataset containing 4 columns of sales data from 2015 and 2016. Meant for students to create summary statistics of and plot distributions.

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be familiar with**:

- Fundamental Python concepts
- Iteration and looping
- Manipulation of dictionaries and lists
- Functions
- Numpy and Scipy statistics functions
- List comprehensions
- Reading in csv files with Python
- Basic statistical concepts on descriptive statistics and distributions

---

## Objectives

<!--- This section lists the learning objectives of the activity or lab.  --->

Apply measures of central tendency and spread while practicing python functions. Has students practice the loading of data from a csv and gives them demo code to do it. There are optional bonus questions to explore seaborn plotting of data.

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  --->

### Requirements

1. Load Data
2. Separate header and data
3. Create a dictionary with the data
    - Print out the first 10 items of the 'volume_sold' column
4. Convert data from string to float
5. Write function to print summary statistics
    - Using your function, print the summary statistics for volume_sold
    - Using your function, print the summary statistics for 2015_margin
    - Using your function, print the summary statistics for 2015_q1_sales
    - Using your function, print the summary statistics for 2016_q1_sales

<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

### Bonus

6. Plot Distributions
    - Explain whether distributions are skewed and explain why they might be skewed.
7. Explore the `seaborn` gallery

---

## Suggested Timing

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each section --->

> Total Time Required: 90 min

- **Objective 1** (estimated: 5 mins)
- **Objective 2** (estimated: 5 mins)
- **Objective 3** (estimated: 20 mins)
- **Objective 4** (estimated: 10 mins)
- **Objective 5** (estimated: 30 mins)
- **Objective 6** (estimated: 10 mins)
- **Objective 6** (estimated: 10 mins)

> Note: If this lab or activity is not finished in-class, we recommend completing it as homework.

---

## Rubric

For this activity, required objectives will be evaluated on a simple point scale of 1-3.

Score | Expectations
:--- | :---
**0** | _Incomplete._
**1** | _Does not meet expectations._
**2** | _Meets expectations._
**3** | _Exceeds expectations!_

> Note: Bonus objectives = exceed expectations.

---

## Additional Resources

<!--- List of potential sources that may help or inform the students' ability to complete the tasks required. This might include reference sites, examples, or tutorials for "getting started." --->

For more information on this topic, check out the following resources:

- [Numpy Statistics Tutorial](https://www.tutorialspoint.com/numpy/numpy_statistical_functions.htm) This is a simple tutorial for using basic numpy statistics functions.