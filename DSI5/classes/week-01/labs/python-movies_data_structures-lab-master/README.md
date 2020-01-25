<!---
Questions? Comments?:

1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!

--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Review with Movie Data

> Unit 1, Activity 7

<!--- Unit and sequence information. This template is an instructor-facing description for a given activity or lab. --->

---

## Materials We Provide

<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between  notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lab/Activity |  Jupyter notebook with lab prompts | [Link](./python-movies-lab.ipynb)|
| Solutions | Sample solutions to movies lab | [Link](./solution-code/python-movies-lab-solutions.ipynb)|

---

## Prerequisites

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this activity/lab? List all relevant skills or prior learning objectives --->

**Before this activity, students should already be able to**:

- Use conditional statements (`if`, `elif`, `else`) for control flow
- Understand and write list and dictionary comprehensions in Python

---

## Objectives

<!--- This section lists the learning objectives of the activity or lab.  --->

This lab is meant to give students practice with iteration, control flow, and writing list comprehensions.

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  --->

### Requirements

1. Write a function that:
    - Accepts a single movie dictionary from the `movies` list as an argument.
    - Returns True if the IMDB score is above 5.5.
2. Write a function that:
    - Accepts the list of movies and a specified imdb score.
    - Returns the sublist of movies that have a score greater than the specified score.
3. Write a function that:
    - Accepts the movies list and a category name.
    - Returns the movie names within that category (case-insensitive!)
    - If the category is not in the data, print a message that it does not exist and return None.
4. Write a function that:
    - Accepts the movies list and a "search criteria" variable.
    - If the criteria variable is numeric, return a list of movie titles with a score greater than or equal to the criteria.
    - If the criteria variable is a string, return a list of movie titles that match that category (case-insensitive!). If there is no match, return an empty list and print an informative message.

<!--- If there are any bonus objectives, list them here. Bonus objectives are items that are not officially required in order to "complete" a given activity, but are provided as suggested enrichment for students who want additional challenges.--->

### Bonus

5. Write a function that:
    - Accepts the movies list and a specified category.
    - Returns True if the average score of the category is higher than the average score of all movies.
6. Write a function that:
    - Accepts the movies list as an argument.
    - Returns the movies list sorted first by category and then by movie according to average score and individual score, respectively.
7. Write a function that:
    - Accepts the movies list and a "search string".
    - Returns a dictionary with keys `'category'` and `'title'` whose values are lists of categories that contain the search string and titles that contain the search string, respectively (case-insensitive!)
8. Write a function that:
    - Accepts the movies list and a string search criteria variable.
    - The search criteria variable can contain within it:
      - Boolean operations: `'AND'`, `'OR'`, and `'NOT'` (can have/be lowercase as well, I just capitalized for clarity).
      - Search criteria specified with syntax `score=...`, `category=...`, and/or `title=...`, where the `...` indicates what to look for.
        - If `score` is present, it means scores greater than or equal to the value.
        - For `category` and `title`, the string indicates that the category or title must _contain_ the search string (case-insensitive).
    - Returns the matches for the search criteria specified.

---

## Suggested Timing

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each section --->

> Total Time Required: 90 min

- **Objective 1** (estimated: 10 min)
- **Objective 2** (estimated: 10 min)
- **Objective 3** (estimated: 10 min)
- **Objective 4** (estimated: 15 min)
- **Objective 5** (estimated: 15 min)
- **Objective 6** (estimated: 10 min)
- **Objective 7** (estimated: 10 min)
- **Objective 8** (estimated: 10 min)

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

- [Understanding Control Flow](https://www.codeproject.com/Articles/663666/Python-Basics-Understanding-The-Flow-Control-State) This is a detailed article on control flow in Python
- [List Comprehensions in Python](http://www.pythonforbeginners.com/basics/list-comprehensions-in-python) This is a great resource for those who don't fully understand list comprehensions
- [List, dictionary, and set comprehensions](https://www.smallsurething.com/list-dict-and-set-comprehensions-by-example/) A detailed overview of all three techniques.