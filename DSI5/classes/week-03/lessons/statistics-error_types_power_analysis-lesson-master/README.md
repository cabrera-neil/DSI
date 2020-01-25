<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Type I, II error, power analysis, and intro to split testing

> Unit 2, Lesson 21

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Interactive jupyter notebook with structured lesson content, part 1 | [Link](./split-tests-error-power-analysis.ipynb)|
| Solutions | Solution code to lessons and practice activities | [Link](./solution-code/split-tests-error-power-analysis-solutions.ipynb)|

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

*After this lessons, students will be able to:*

- Apply an understanding of statistical hypothesis testing within the context of split testing.
- Apply the chi-squared test of independence to "winner" a split test.
- Understand the relationship between p-values, alpha thresholds, and statistical significance.
- Understand the difference between a type I error, statistical power, and a type II error.
- Visualize the interaction of `alpha` and `power`.
- Understand how the components of experimental design interact.
- Learn how to calculate the statistical power of a test.
- Learn how to calculate the required sample size of a test.
- Visualize the required sample size of a test, given its other requirements.

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

*Before this lesson(s), students should already be able to:*

1. Munge data using Pandas
2. Perform hypothesis testing

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> **Total Time: 180 mins**

- Introduction to A/B Testing (10 mins.)
- Split Tests are Hypothesis Tests (10 mins.)
- Chi-Squared Test of Independence (30 mins.)
- Statistical Significance, P-Values, The Alpha Threshold, and Type I Errors (30 mins.)
  - Statistical Significance (10 mins.)
  - Type I Errors and the Alpha Threshold (10 mins.)
  - A Side Note on P-Value Thresholds (10 mins.)
- Type II Errors and Statistical Power (20 mins.)
  - Alpha and Beta (15 mins.)
  - Statistical Power (5 mins.)
- Visualizing the Interaction Between `alpha` and `power` (10 mins.)
- Power Analysis and Sample Size Calculation (40 mins.)
  - Calculation for the Statistical Power of a test (20 mins.)
  - Calculation for the required sample size of a test (20 mins.)
- Calculating the Required Sample Size Visually (10 mins.)

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

- [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/)
- [The more advanced book: Elements of Statistical Learning](http://web.stanford.edu/~hastie/ElemStatLearn/)
- [Spurious Correlations](http://www.tylervigen.com/spurious-correlations)
- [The Complete A/B testing Guide](https://vwo.com/ab-testing/)

---