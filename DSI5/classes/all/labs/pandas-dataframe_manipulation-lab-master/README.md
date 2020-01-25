<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Pandas DataFrame Manipulation Lab

> Unit 2, Activity 25

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity |  Structured Jupyter notebook with activity requirements and prompts | [Link](./dataframe-manipulation-chipotle-data.ipynb)|
| Data | Chipotle | [Link](./datasets/chipotle.tsv)|
| Solutions | Sample solutions to notebook| [Link](./solution-code/dataframe-manipulation-chipotle-data-solutions.ipynb)|

> Dataset(s) description: Dataset on Chipotle orders that students will use to practice data manipulation with Pandas.

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:

- Explore data using Pandas.

---

## Objectives

<!--- This section lists the learning objectives of the activity or lab.  --->

This lab is intended to cover a variety of skills for data manipulation in pandas using a challenging data set from Chipotle.

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  --->

### Requirements and Suggested Timing

> Total Time Required: 70 mins.

1. Load the `chipotle.tsv` and examine the data. (<1 min.)
2. Create a `sub-id` for each `order-id`. (5 mins.)
3. Clean up the `price` column (5 mins.)
4. Make a new categorical column for broader item types (5 mins.)
5. Calculate the total price by `order_id` and add the results as a new column, `order_total_price`. (10 mins.)
6. Make an `adjusted_item_price` column to account for multiple orders per row. (5 mins.)
7. Answer: What is the `min`, `max`, `count`, ` mean`, and `std` of `price` for each unique item in  `item_name`? (15 mins.)
8. Plot the `mean` `price` of items against the `count` (popularity).(5 mins.)
9. Plot the `max` `price` of items against the `count` (popularity). (5 mins.)
10. Calculate the `mean` of adjusted `price` per `broad_type` category. (10 mins.)
11. Make a bar plot of your `mean` `price` by `broad_type` category. (5 mins.)

<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

### Bonus

12. Challenge: Parse the `choice_description` column into two new columns: `order_customizations` and `order_customization_id`.

---

<!--->

## Suggested Timing

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

- [Pandas documentation: split-apply-combine](https://pandas.pydata.org/pandas-docs/stable/groupby.html)
