<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Practice loading and describing data lab

> Unit 1, Activity 10

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity | Jupyter Notebook with sequential prompts for loading and exploring data | [Link](./loading-and-describing-data.ipynb)|
| Data | Boston Housing data | [Link](./datasets/housing.data)|
| Solutions | Solutions to lab notebook| [Link](./solution-code/loading-and-describing-data-solution.ipynb)|

> Dataset(s) description: The Boston Housing Dataset is a small, famous dataset containing info collected by the U.S. Census Bureau about housing in the Boston, Mass area in 1970.

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:

- Define and interepret measures of central tendency
- Calculate measures of central tendency using `numpy`
- Evaluate skew of a distribution
- Iterate through values using a `for loop`

---

## Objectives

<!--- This section lists the learning objectives of the activity or lab.  --->

This lab has students practice loading data using python (this time they load from a remote url source and save as a local file, then practice reading files with python). This covers basic statistical measures and asks questions related to concepts in the fundamentals of statistics introduction lesson.

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  --->

### Requirements

1. Load the Boston housing data
2. Load the `housing.data` file with python
3. Conduct a brief integrity check of your data
4. Answer: For what two attributes does it make the *least* sense to calculate mean and median? Why?
5. Answer: Which two variables have the strongest linear association?
6. Look at distributional qualities of variables

    Answer the following questions:

    - Which variable has the most symmetric distribution?
    - Which variable has the most left-skewed (negatively skewed) distribution?
    - Which variable has the most right-skewed (positively skewed) distribution?

7. Repeat question 6 but scale the variables by their range first
8. Univariate analysis of your choice

    Conduct a full univariate analysis on MEDV, CHAS, TAX, and RAD. 

    For each variable, you should answer the three questions generally asked in a univariate analysis using the most appropriate metrics.
    - A measure of central tendency
    - A measure of spread
    - A description of the shape of the distribution (plot or metric based)
9. Answer: Have you been using inferential statistics, descriptive statistics, or both?
10. Reducing the number of observations
    - Use the `random.sample()` function to select 50 observations from `'AGE'`.
    - Identify the type of sampling we just used


<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

### Bonus

11. Of the remaining types of sampling, describe (but do not execute) how you might implement at least one of these types of sampling

---

## Suggested Timing

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each section --->

> Total Time Required: 90 min

- **Objective 1** (estimated: 1 min)
- **Objective 2** (estimated: 4 mins)
- **Objective 3** (estimated: 10 mins)
- **Objective 4** (estimated: 5 mins)
- **Objective 5** (estimated: 10 mins)
- **Objective 6** (estimated: 15 mins)
- **Objective 7** (estimated: 10 mins)
- **Objective 8** (estimated: 15 mins)
- **Objective 9** (estimated: 5 mins)
- **Objective 10** (estimated: 10 mins)
- **Objective 11** (estimated: 5 mins)

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

- [Inferential vs Descriptive Statistics](https://www.thoughtco.com/understanding-descriptive-vs-inferential-statistics-3026698) This is a nice overview of the difference between inferential and descriptive statistics.
- [NumPy Statistics Documentation](https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.statistics.html) Here's a list of the statistics functions in NumPy.