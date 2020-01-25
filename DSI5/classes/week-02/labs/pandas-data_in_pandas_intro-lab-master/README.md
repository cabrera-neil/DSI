<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to Data in Pandas Lab

> Unit 2, Activity 2

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity |  Structured Jupyter notebook with activity requirements and prompts | [Link](./intro-to-pandas-review.ipynb)|
| Data | Mad Men Cast | [Link](./datasets/mad-men-cast-show-data.csv)|
|      | San Francisco Crime | [Link](./datasets/sf_crime.csv)|
| Solutions | Sample solutions to Jupyter Notebook | [Link](./solution-code/intro-to-pandas-review-solutions.ipynb)|

> Dataset(s) description:

The Mad Men Cast dataset is a CSV file with information on actors. The dataset name seems to be a misnomer, as most or all of the actors are not from the TV show Mad Men. The dataset is used in the first half of the lab for students to practice Pandas commands on.

The San Francisco Crime dataset is large dataset with 25,000 observations of crimes that occurred in the San Francisco area from the years 2003 to 2015. It contains information on the location, time, and type of crime.

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:

- Perform and understand basic commands using Pandas
- Understand Python coding fundamentals

---

## Objectives and Suggested Timing

<!--- This section lists the learning objectives of the activity or lab.  --->

This lab reinforces understanding of the Pandas library already introduced in the 'Introduction to Data in Pandas' lesson. Students will use Pandas to explore two datasets and utilize pandas plotting. The lab is comprised of fifteen asks

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity as well. It also provides the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each section --->

> Total Time Required: 80 mins

### Requirements

1. **Load the Mad Men cast data into a pandas DataFrame** (estimated: < 1 min.)
2. **Print the head and tail of the data** (estimated: 1 min.)
3. **Print the columns of the data** (estimated: 5 mins.)
4. **Rename any columns with spaces or special characters to not contain any** (estimated: 10 mins.)
5. **Subset the data where the status of the show is not "END" or "End."** (estimated: 5 mins.)
6. **Print out the performers where the show start is greater than 2005 and the score is greater than 7** (estimated: 5 mins.)
7. **Select the performer and show column for the 20th-25th LABELED rows.** (estimated: 10 mins.)
8. **Plot a histogram of score.** (estimated: 5 mins.)
9. **Load the San Francisco crime data set into a DataFrame** (estimated: < 1 min.)
10. **Look at the dimensions of the crime data** (estimated: 2 mins.)
11. **Look at the data types of the columns and print out the column names** (estimated: 5 mins.)
12. **Answer: How many distinct districts are there?** (estimated: 5 mins.)
13. **Answer: Which day of the week has the most crime?** (estimated: 5 mins.)
14. **Make a new DataFrame featuring the crime categories and the number of crimes per category.** (estimated: 10 mins.)
15. **Make a DataFrame that includes the districts and crime counts per district. Which district has the most crime?** (estimated: 10 mins.)

<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

> Note: If this lab or activity is not finished in-class, we recommend completing it as homework.

---

<!--- ## Suggested Timing >

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each section --->

<!---

> Total Time Required: 90 min

- **Objective 1** (estimated: 20 mins)
- **Objective 2** (estimated: 30 mins)
- **Objective 3** (estimated: 40 mins)

---

--->

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

- [Pandas Tutorials](https://www.tutorialspoint.com/python_pandas/) This sites has tutorials on how to perform a variety of Pandas commands.