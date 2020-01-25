<!---
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Robust Regression Lab

> Lab activity to be paired with Robust Regression Lesson

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide
<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab Activity | Two-Part Robust Regression Activity using Baltimore Salary Data | [Link](./baltimore-salaries-lab.ipynb)|
| Dataset | Baltimore city employee salaries | [Link](./datasets/Baltimore_City_Employee_Salaries_2011.csv)|
| Solutions | Sample solutions to lesson demo code and any practice files | [Link](./solution-code/baltimore-salaries-lab-solutions.ipynb)|


> **Data Description**: What data we are using in this activity and why? Provide a brief description of what it is and how it is used. This is intended to be a helpful, quick reference for instructors.

---

## Prerequisites
<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:
- Split a dataset into train and test parts
- Create a linear model using sklearn.linear_model.LinearRegression
- Create a scatter plot using Matplotlib
- Understand the concept of error in a prediction
- Know when to use robust regression methods instead of OLS
- Understand how Theil-Sen, RANSAC and Huber work, and what they are optimising for
- Understand the advantages of using median absolute error as a scoring function
- Create a scoring function appropriate for different business scenarios

---

## Objectives
<!--- This section lists the learning objectives of the activity or lab.  --->

Brief high level summary sentence of the topic and purpose of the lab/activity. 

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  --->
#### Requirements
1. Complete Section 1
   1. Read dataset
   1. Preprocess the data (convert strings to numbers)
   1. Perform EDA
   1. Create training and test sets
   1. Plot OLS
   1. Plot results from linear vs OLS
   1. Calculate metrics for comparison
   1. Repeat analysis using alternate methods: 
      - Theil-sen
      - RANSAC
    - Huber
1. Complete Section 2
   1. Create a scoring function
   1. Score the four models

**BONUS**
1. Find the optimal coefficient
1. Improve the model


<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

---

## Suggested Timing

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each section --->

> Total Time Required: 90 min. 

- **Section 1** (estimated: 50 mins)
- **Section 2** (estimated: 40 mins)

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
- [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/)
- [The more advanced book: Elements of Statistical Learning](http://web.stanford.edu/~hastie/ElemStatLearn/)
- [Spurious Correlations](http://www.tylervigen.com/spurious-correlations)
- Wikipedia pages on [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance), [Welch's t-test](https://en.wikipedia.org/wiki/Welch's_t-test), [Mann-Whitney test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)
