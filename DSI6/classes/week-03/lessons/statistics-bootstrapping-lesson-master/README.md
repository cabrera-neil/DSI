<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to bootstrapping

> Unit 2, Lesson 19

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Interactive Jupyter notebook prompts for codealong lesson | [Link](./introduction-to-bootstrapping.ipynb)|
| Data | Local copy of any dataset used | [Link](./datasets/Starcraft_sample.csv)|
| Solutions | Solution code to lesson notebook | [Link](./solution-code/introduction-to-bootstrapping-solution.ipynb)|
| Archive | Older versions & source materials, when applicable  | [Link](./archive/) |

> **Dataset description:** CSV with data on Starcraft game interactions. A more detailed description can be found [here](./datasets/description.txt).

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

*After this lessons, students will be able to:*

- Understand the concept of the parametric bootstrap.
- Code the parametric bootstrap by hand.
- Apply the parametric bootstrap to calculate confidence intervals for statistics.
- Understand when bootstrapping is useful.
- Practice bootstrapping.

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

*Before this lesson(s), students should already be able to:*

- Explain what confidence intervals are
- Use the Pandas library

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> **Total Time: 180 mins**

- The Bootstrapping Procedure (30 mins.)
- Coding the Nonparametric Bootstrap: Starcraft Data (40 mins.)
  - Load Starcraft data (5 mins.)
  - Extract APM vector (5 mins.)
  - Plot distribution of APM with a histogram (5 mins.)
  - Write a function for nonparametric bootstrap (independent) (15 mins.)
  - Use bootstrapping function on APM vector (10 mins.)
- Comparing Bootstrapped to Standard Confidence Intervals (15 mins.)
- Bootstrapping the Median
  - Motivation (20 mins.)
  - Plot distribution of APM (5 mins.)
  - Calculate 99% confidence interval for median using formula (10 mins.)
  - Bootstrap 99% confidence interval for medain (10 mins.)
  - How does bootstrapping affect the distribution?
- The Theory Behind the Bootstrap (20 mins.)
- Independent Practice: Confidence Intervals of Correlations (30 mins.)

---

<!--- If a repo contains any additional practice files or supplementary resources (PDFs, etc) describe them here  --->
<!---
> OPTIONAL: Practice/Resources
- Item 1 description
- Item 2 description

---
--->

## Additional Resources

<!--- This section lists useful reference materials that can inform, extend, or deepen a student's understanding of the material. While this may seem like a "nice to have" feature, we normally see a range of advanced and remedial students in our classes. Curating these resources allows us to provide targeted materials and suggestions that instructors can use to support different student needs. --->

*For more information on this topic, check out the following resources:*

- [MIT Paper on Bootstrapping](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading24.pdf)
- [Youtube Explanation of Bootstrapping](https://www.youtube.com/watch?v=ZCXg64l9R_4)

---