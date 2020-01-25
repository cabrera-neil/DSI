<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Long, wide, pivot, melt lab on humor styles dataset

> Unit 2, Activity 13

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity |  Structured Jupyter notebook with activity requirements and prompts | [Link](./pandas-data-transformation-lab.ipynb)|
| Data | Local copy of any datasets used | [Link](./datasets/hsq_data.csv)|
| Solutions | Sample solutions to lesson demo code and any practice files | [Link](./solution-code/pandas-data-transformation-lab-solutions.ipynb)|

> Dataset(s) description: This data was collection with an interactive online version of the Humor Styles Questionnaire.

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:

- Use `.pivot_table()` and `.melt()` in Pandas

---

## Objectives

<!--- This section lists the learning objectives of the activity or lab.  --->

In this lab, students will practice going between long and wide formats in `pandas`, dive deeper into `.melt()` and `.pivot_tables()`, and explore the pitfalls of hierarchical indices that we covered in the lesson.

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity as well as an estimation of the amount of time required for each section.  --->

### Requirements and Suggested Timing

> Total Time Required: 100 mins.

1. Read data description and load in data (5 mins.)
2. Print the data shape ( < 1 min.)
3. Describe the data (15 mins.)
    - Use `.rename()` function to rename column
    - Use `.describe()` to look at data
    - Calculate and print standard deviation of columns
    - Plot distribution of `Q15` for `aggressive`
4. Convert data from Wide to Long format (5 mins.)
    - Change column names
    - Print column names
5. Add `subject_id` column (5 mins.)
    - Create an ID array
    - Add new column
6. Transform data to long format (15 mins.)
    - Change column names
    - Print shape of DataFrame and unique values of `variable` column
    - Print the entire subset of the DataFrame where `subject_id == 10`
    - Figure out a way to order the index by `subject_id`
7. Clean the data and transform variables (25 mins.)
    - Convert gender column to string representation
    - Removing subjects from dataset
      - Find users who responded `-1` on any questions
      - Remove all rows from the data sets that correspond to the bad users.
      - Check if any entered 0 for accuracy and remove them.
      - Find the subjects who reported an age older than 100 and remove them
    - Transform variables, inverting some
    - Write a function that will accept a score value and "invert" the score
    - Apply the score inverter function to the values where the variable is included in the inverted_question list, reassigning the value column at those locations.
8. Transforming the dataset back to Wide Format (30 mins.)
    - Use pd.pivot_table() to re-widen your data
      - Create a new widened DataFrame from your long data set
      - Reset the index and turn the data into long format
      - Merge the `count` long data set into the full long data set
      - Use the `.pivot_table()` function to calculate the mean of both the original values and the counts by `gender` and `age` across variables.
    - Understanding the MultiIndex
      - Print out the columns of the `means` DataFrame you created in the previous question
      - Print out the ```.columns.names``` property
      - Print out the ```.index.names``` property of your wide data
    - Indexing With a MultiIndex: Alternative Methods
      - Type command in lab, replacing `value_count_means` with your wide DataFrame name.
      - First, remove the value column index, making the columns non-hierarchical. Then type command in notebook.
      - Try `.query()` examples in notebook
    - Flattening a MultiIndex DataFrame
      - Try commands in notebook
      - Check `.columns`

<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

<!---
### Bonus

4. Objective 4
5. Objective 5

---

--->
<!--->
## Suggested Timing
--->
<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each section --->
<!---
> Total Time Required: 90 min

- **Objective 1** (estimated: 20 mins)
- **Objective 2** (estimated: 30 mins)
- **Objective 3** (estimated: 40 mins)
--->
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

- [Working with data using Pandas](https://www.digitalocean.com/community/tutorials/working-with-data-using-pandas-and-python-3) This is a great deep dive into Pandas.
- [Pandas documentation: `.wide_to_long()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.wide_to_long.html) 
- [Pandas documentation: `pandas.melt()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.melt.html)