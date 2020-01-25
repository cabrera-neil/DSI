<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Review python iteration, control flows, and functions

> Unit 1, Lesson 4

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Jupyter Notebook with instructions and empty cells for codealong | [Link](./iteration-control-flows-functions.ipynb)|
| Data | Coffee Preferences | [Link](./datasets/coffee-preferences.csv)|
| Solutions | Sample solutions to codealong | [Link](./solution-code/iteration-control-flows-functions-solutions.ipynb)|

<!---
| Slides | Slide decks & PDFs, if applicable | [Link](./xyz)|
| Extra Resources | Other files, if applicable | [Link](./xyz) |
| Source Materials | Older content, if applicable | [Link](./xyz) |
--->

> Dataset description: Small, unclean dataset of individuals' numbers of orders from different coffee shops. Used for control flow practice.

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

- Explore `Python` control flow and conditional programming.
- Implement `For` and `While` loops to iterate through data structures.
- Apply `if, else` conditional statements.
- Create functions to perform repetitive actions.
- Demonstrate error-handling using `try, except` statements.
- Combine control flow and conditional statements to solve the classic "FizzBuzz" code challenge.
- Use `Python` control flow and functions to help us parse, clean, edit and analyze the Coffee Preferences dataset.

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

**Before this lesson(s), students should already be able to**:

- Know python data types: string, int, float, boolean, tuple, list, dictionary

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> Total Time: 90 min

- If Else Statement (10 min)
  - Write an if-else statement to check whether the suitcase is over 50lb.
  - Write an if-else statement for multiple conditions.
- Iterating With For Loops (15 min)
  - Write a for-loop that iterates from the number 1 to the number 15.
  - Iterate from 1 to 15, printing whether the number is odd or even.
  - Iterate from 1 to 30 with the various instructions.
  - Iterate through a list of animals, and print each one in all caps.
  - Iterate through the animals list. Capitalize the first letter and append the modified animals to a new list.
  - Iterate through the animals. Print out the animal name and the number of vowels in the name.
- Functions (20 min)
  - Write a function that takes word as an argument and returns the number of vowels in the word.
  - Write a function to calculate the area of a triangle using its height and width.
- While Loops (15 min)
  - While loops and strings
  - Try to convert elements in a list to floats
- Practice control flow on Coffee Preference dataset (30 min)
  - Load coffee preference data from file and print
  - Remove the remaining newline `'\n'` characters with a for-loop
  - Split the lines into "header" and "data" variables.
  - Split the header and the data strings on commas.
  - Remove the "Timestamp" column.
  - Convert numeric columns to floats and empty fields to `None`.
  - Count the `None` values per person, and put counts in a dictionary.
  - Calculate average rating per coffee brand.
  - Create a list containing only the people's names.
  - Picking a name at random. What are the odds of choosing the same name three times in a row?
  - Construct a while loop to run the choosing function until it returns True.

---

## Additional Resources

<!--- This section lists useful reference materials that can inform, extend, or deepen a student's understanding of the material. While this may seem like a "nice to have" feature, we normally see a range of advanced and remedial students in our classes. Curating these resources allows us to provide targeted materials and suggestions that instructors can use to support different student needs. --->

For more information on this topic, check out the following resources:

- [Control Flow - A Byte of Python](https://python.swaroopch.com/control_flow.html)

---