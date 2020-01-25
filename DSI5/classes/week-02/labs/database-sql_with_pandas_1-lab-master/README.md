<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Practice SQL with pandas pt. 1

> Unit 2, Activity 9

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity |  Structured Jupyter notebook with activity requirements and prompts | [Link](./practice-sql-via-pandas-pt1.ipynb)|
| Data | Car Makers (CSV) | [Link](./datasets/csv/car-makers.csv)|
|      | Car Names (CSV) | [Link](./datasets/csv/car-names.csv)|
|      | Cars Data (CSV) | [Link](./datasets/csv/cars-data.csv)|
|      | Model List (CSV) | [Link](./datasets/csv/model-list.csv)|
|      | Cars DB (sqlite) | [Link](./datasets/sql/Cars.db.sqlite)|
|      | Test DB (sqlite) | [Link](./datasets/sql/test_db.sqlite)|
| Solutions | Sample solutions to lesson demo code and any practice files | [Link](./solution-code/practice-sql-via-pandas-pt1-solutions.ipynb)|
| Assets | Images, graphs, or files linked in lab, as needed | [Link](./assets)|

> Dataset(s) description:

All four CSV files are different datasets related to cars. All the datasets are fairly small. They are used in the lab for students to load into the Cars DB database.

Test DB does not seem to be used in the lab.

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:

- Load in data using Pandas
- Use Pandas interface with SQL

---

## Objectives

<!--- This section lists the learning objectives of the activity or lab.  --->

This lab is meant to give students practice writing SQL commands and using Pandas to interact with SQL databases.

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  It also offers estimated times for how long each requirement will take to complete.--->

### Requirements and Suggested Timimg

### Total Time: 70 mins.

1. Create a SQL DB and tables using `pandas` DFs and `.csv`s (10 mins.)
    - Connect to the SQLite database (5 mins.)
    - Convert the loaded `.csv` to a SQL file (5 mins.)
2. Create a table in the `cars` database for car makers. (5 mins.)
3. Create a table in the `cars` database for the car data (5 mins.)
4. Using a query string, read the entire `car_names` table from your SQL database into a DataFrame (5 mins.)
5. Write a Python function to query a database using `pandas` and return a DataFrame (10 mins.)
6. Select the first five rows of the `car_names` table (5 mins.)
7. Add the cars into the `car_names` table. (5 mins.)
8. Query the `car_names` table for all columns where `'Model' = 'Tesla.'` (5 mins.)
9. Select the first five rows of the `car_makers` table. (5 mins.)
10. Select the first five rows of the `car_data` table. (5 mins.)
11. Practice INNER JOINs (5 mins.)
12. Practice LEFT JOINs (5 mins.)

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

- [Pydata Video](https://www.youtube.com/watch?v=1uVWjdAbgBg)  
- [Associated GitHub Repo](https://github.com/gjreda/pydata2014nyc/tree/master/data)
- [`pandas` Merge, JOIN, and Concatenate](http://pandas.pydata.org/pandas-docs/stable/merging.html)
