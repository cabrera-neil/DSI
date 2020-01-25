<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Review CLT, confidence intervals, and hypothesis testing

> Unit 2, Activity 18

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity |  Structured Jupyter notebook with activity requirements and prompts | [Link](./practice-clt-confidence-intervals.ipynb)|
| Data | Housing data | [Link](./datasets/housing.data)|
| Solutions | Sample solutions to lab notebook | [Link](./solution-code/practice-clt-confidence-intervals-solution.ipynb)|

> Dataset(s) description: The data is the boston housing data delimited with whitespace. Students will calculate confidence intervals for statistics using the dataset.

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:

- Perform simple statistical analysis in Pandas
- Explain and caclulate confidence intervals
- Explain and implement hypothesis tests
- Understand and evaluate p-values

---

## Objectives

<!--- This section lists the learning objectives of the activity or lab.  --->

This lab will have students practice creating and evaluating confidence intervals and hypothesis tests.

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  --->

### Requirements and Suggested Timing

> Total Time Required: 90 min

1. Find the mean, standard deviation, and standard error of the mean for the `AGE` variable. (10 mins.)
2. Generate a 90%, 95%, and 99% confidence interval for `AGE`. (10 mins.)
    - Interpret the results from all three confidence intervals.
3. Answer: Did you rely on the central limit theorem in Question 2? Why or why not? Explain. (10 mins.)
4. For the `NOX` variable, generate a 95% confidence interval and interpret it. (10 mins.)
5. For the `NOX` variable, test the hypothesis that the mean is equal to the median. (20 mins.)
6. Answer: What do you notice about the results from Questions 4 and 5? (10 mins.)
7. For the `NOX` variable, test the hypothesis that the mean is greater than or equal to the median. (10 mins.)
8. Answer: Compare the p-values from Questions 5 and 7. What do you notice? (10 mins.)

<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

<!---
### Bonus

4. Objective 4
5. Objective 5

---

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

- [Confidence Intervals Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval)