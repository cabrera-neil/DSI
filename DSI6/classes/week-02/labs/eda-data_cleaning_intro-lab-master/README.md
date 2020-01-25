<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Cleaning rock song data lab with pandas

> Unit 2, Activity 4

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity |  Structured Jupyter notebook with activity requirements and prompts | [Link](./pandas-cleaning-apply.ipynb)|
| Data | Rock songs dataset | [Link](./datasets/rock.csv)|
| Solutions | Sample solutions to lab notebook | [Link](./solution-code/pandas-cleaning-apply-solution.ipynb)|

> Dataset(s) description: The dataset is a CSV of 2230 Rock songs for students to explore using the Pandas library.

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:

- Perform basic Pandas commands
- Use the `.apply()` and `.map()` methods

---

## Objectives

<!--- This section lists the learning objectives of the activity or lab.  --->

This lab is meant to develop more advanced Pandas skills by having students use commands that actually modify the dataframe.

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  It also gives the suggested amount of time for each requirement.--->

### Requirements and Suggested Timing

> Total Time Required: 80 mins.

1. **Load rock.csv and do an initial examination of its data columns**
2. **Clean up the column names.** (10 mins.)
    - **Change the column names when you import the data using `pd.read_csv()`** (4 mins.)
    - **Change column names using the `.rename()` function.** (4 min.)
    - **Reassigning the `.columns` attribute of a DataFrame** (2 mins.)
3. **Subsetting data where null values exist** (5 mins.)
4. **Update slices of your DataFrame based on mask selection/slices** (10 mins.)
    - **Make all of the null values in release 0** (7 mins.)
    - **Verify that release contains no null values.** (3 mins.)
5. **Ensure that the data types of the columns make sense** (5 mins.)
    - **Look at the data types for the columns. Are any incorrect given what the data represents?** (5 mins.)
6. **Investigate and clean up the `release` column.** (15 mins.)
    - **Figure out what value(s) are causing the `release` column to be encoded as a string instead of an integer.** (5 mins.)
    - **Look at the rows in which there is incorrect data in the `release` column** (5 mins.)
    - **Clean up the data** (5 mins.)
7. **Get summary statistics for the `release` column using the `.describe()` function** (10 mins.)
    - **Print out the summary stats for the `release` column. What is the earliest and latest release date?** (5 mins.)
    - **Based on the summary statistics, is there anything else wrong with the release column?** (5 mins.)
8. **Make changes and investigate using custom functions with `.apply()`** (10 mins.)
    - **Write a function that will take a row of a DataFrame and print out the song, artist, and whether or not the release date is < 1970** (5 mins.)
    - **Using the `.apply()` function, apply the function you wrote to the first four rows of the DataFrame** (5 mins.)
9. **Write a function that converts cells in a DataFrame to float and otherwise replaces them with `np.nan`** (15 mins.)
    - **Write the function that takes a column and converts all of its values to float if possible and `np.nan` otherwise. The return value should be the converted Series.** (5 mins.)
    - **Try your function out on the rock song data and ensure the output is what you expected.** (5 mins.)
    - **Describe the new float-only DataFrame.** (5 mins.)

<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

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

- [Python Pandas Tutorials](https://www.tutorialspoint.com/python_pandas/) This site has a ton of tutorials on how to use Pandas.