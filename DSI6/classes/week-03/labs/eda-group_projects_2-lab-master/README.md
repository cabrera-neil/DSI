<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Group EDA projects pt. 2

> Unit 2, Activity 24

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity | Jupyter notebook with overview of lab | [Link](./group-eda-projects-overview.ipynb)|
|      | Adult education team notebook | [Link](./team-adult-education.ipynb)|
|      | Fifa team notebook | [Link](./team-fifa.ipynb)|
|      | Marathon team notebook | [Link](./team-marathon.ipynb)|
|      | Mobile Madness team notebook | [Link](./team-mobile-madness.ipynb)|
| Data | Adult CSV | [Link](./datasets/adult.csv)|
|      | Churn Dataset | [Link](./datasets/churn-bigml-20.csv)|
|      | Fifa goals dataset | [Link](./datasets/fifa_goals.csv)|
|      | Marathon winners dataset | [Link](./datasets/Winners.csv)|

### Dataset(s) description:

The Adult CSV is a dataset of personal and economic information on many adults.

The Fifa dataset contains info on soccer players in FIFA and how many goals they score.

The Marathon dataset contains information on Marathon winners.

The Churn dataset contains information on phone usage.

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:

- Explore data in pandas.
- Make visualizations using Pandas, matplotlib, or any other visualization library in Python

---

## Objectives and Requirements

<!--- This section lists the learning objectives of the activity or lab.  --->

### Team Adult Education

You are a member of the data science department at a private school. The marketing department has approached us to help write a series of blog posts that can help sell the value proposition of the school. Secondarily, business development is very interested in developing online products in emerging markets.

#### The goals are:

- Describe the areas of highest value within the dataset.
- Describe characteristics that you believe target value.
- Identify possible markets and demographic characteristics for business development.

#### Presentation requirements:

- At least 50% of presentation must address a non-technical audience.
- Someone who hasn't presented in class yet must take lead on presentation.

### Team FIFA

You are working for an advertising analytics consulting company. Your client, a name brand television network, needs to re-formulate their pricing structure for advertisement slots during soccer matches for new customers. They also want this new structure to incentivize existing customers to create new partnerships/sponsors with teams and players.

#### Goals

- Determine a reasonable metric to decide how exciting a game is.
- Engineer this feature using existing data.
- Suggest a pricing structure tied to the overall value associated with "game excitement".

#### Presentation requirements

- At least 50% of presentation must address a non-technical audience.
- Someone who hasn't presented in class yet must take lead on presentation.

### Team Mobile Madness

You are on the data science department of a mobile device company. In an effort to extend account lifetime of existing customers, we need to develop targeted A/B experiments. In order to do that efficiently, we need to have a better degree of certainty about which customers are likely to to "churn" and why.

#### Goals

- Research the concept of "churn" and A/B testing.
- Identify behaviors strongly correlated with churn in this dataset.
- Suggest what we should develop A/B tests for going forward.

#### Presentation requirements

- Concisely explain churn and A/B testing to the audience.
- At least 50% of presentation must address a non-technical audience.
- Someone who hasn't presented in class yet must take lead on presentation.

### Team Marathon

The overlords at the Marathon Planning Committee have petitioned a group of DSI students to help decide the best future sites to host marathons. The committee believes that people who choose to attend the events are drawn to the challenge and competitive aspects as the core value (harder marathons == better value). However, a small contingency within the group believe that the "spirit" of the event-its potential for spectatorship-determines the value (better spectacle == better value).

#### Goals

- Suggest qualities of high performing events.
    - Engineer new features / metrics to evaluate high performance.
    - Keep in mind the goal of the committee is to use these metrics to decide future sites for events.
- Settle the dispute within the committee about the value of challenge vs popularity.
    - Which is more important?
    - Are they valuable for different reasons?

#### Presentation requirements

- At least 75% of the presentation must address a non-technical audience.
- Someone who hasn't presented yet must take lead on presentation.

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  --->
<!---

### Requirements

1. Objective 1
2. Objective 2
3. Objective 3

--->
<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

<!---

### Bonus

4. Objective 4
5. Objective 5

--->
---

## Suggested Timing

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each section --->

> Total Time Required: Full day

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

- [Medium Blog: Exploratory Data Analysis: the Best way to Start a Data Science Project](https://medium.com/@InDataLabs/why-start-a-data-science-project-with-exploratory-data-analysis-f90c0efcbe49)