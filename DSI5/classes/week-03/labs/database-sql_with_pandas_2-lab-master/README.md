<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Practice SQL with pandas pt. 2

> Unit 2, Activity 23

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity | Structured Jupyter notebook with activity requirements and prompts | [Link](./sql-with-pandas-pt2.ipynb)|
| Data | EuroMart List of Orders | [Link](./datasets/csv/EuroMart-ListOfOrders.csv)|
|      | EuroMart Order Breakdown | [Link](./datasets/csv/EuroMart-OrderBreakdown.csv)|
|      | EuroMart Sales Targets | [Link](./datasets/csv/EuroMart-SalesTargets.csv)|
| Solutions | Sample solutions to notebook | [Link](./solution-code/sql-with-pandas-pt2-solutions.ipynb)|

> Dataset(s) description: The three CSVs included have sales data that students will explore using Pandas and turn into a SQL database. There is a SQL folder containing a file called `EuroMart.db.sqlite`. This file can be ignored as it is something that students are expected to create in the lab.

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:

- Perform basic SQL queries
- Explore datasets using the Pandas library

---

## Objectives

<!--- This section lists the learning objectives of the activity or lab.  --->

This lab is meant to give students the opportunity to practice SQL queries.

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  --->

### Requirements and Suggested Timing

> Total Time Required: 90 mins.

1. Read in the `EuroMart` `.csv` data (<1 min.)
2. Rename columns to remove any spaces (5 mins.)
3. Remove dollar signs from the `sales` and `profit` columns in the `order breakdown` DataFrame. (5 mins.)
4. Create a SQL database called `EuroMart` and save the three DataFrames as SQL tables. (5 mins.)
5. Answer: How many orders has each customer placed? (5 mins.)
6. Create a query to return a table containing only geographic features from the `list of orders` table (5 mins.)
7. Create a query to return a table containing all orders that had a negative profit from the `order breakdown` table. (5 mins.)
8. Construct a query to return a table containing `customer_name` and `product_name`. (5 mins.)
9. Answer: How many orders for "office supplies" (category) has Sweden made? (5 mins.)
10. Answer: What were total sales for discontinued products? (5 mins.)
11. Answer: What is the total quantity of objects sold for each country? (5 mins.)
12. Answer: In what countries were profits lowest? (Report the lowest 5-10) (5 mins.)
13. Answer: What counties have the best and worst sales-to-profit ratios? (5 mins.)
14. Answer: What shipping method is most commonly used for "bookcases" (sub-category)? (5 mins.)
15. Answer: Which city in the `orders` table generated the highest net sales? (List all cities and countries in descending order by net sales). (5 mins.)

<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

### Bonus

16. Create a column called `shipping_delay` in the `orders` table that contains the difference in days between `order_date` and `ship_date`. (5 mins.)
17. Update your `orders` table in your SQLite3 DB to include the `shipping_delay` feature. (5 mins.)
18. Answer: Which product category has the highest average `shipping_delay`? (5 mins.)
19. Answer: In which months and categories were sales targets exceeded? (5 mins.)

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

- [Mode Analytics: SQL tutorials](https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/)