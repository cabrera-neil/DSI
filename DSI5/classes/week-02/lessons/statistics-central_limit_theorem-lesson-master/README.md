<!--
Questions? Comments?:
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the data team on Slack and share your thoughts!
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to the Central Limit Theorem

> Unit 1, Lesson 13

<!--- Unit and Lesson or sequence information. This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide

<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Lecture Jupyter notebook with code to visualize distributions | [Link](./central-limit-theorem.ipynb)|
| Data | CSV file with a variety of data on today's highest paid athletes | [Link](./datasets/Athletes.csv)|
| Solutions | Jupyter notebook with coding and conceptual questions answered | [Link](./solution-code/central-limit-theorem-solution.ipynb)|
| Resources | Code designed to give a working example of a gaussian fit with 1,2,3 sigma lines | [Link](./code/extra_norm_code_eah.py) |

> **Dataset description:** The athletes dataset contains salary info on many high-paid athletes. Many of the features are highly skewed, so this dataset is used to show how we can create a normal distribution using the Central Limit Theorem, even when sampling from a distribution that is definitely not normal.

---

## Learning Objectives

<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

*After this lessons, students will be able to:*

- **Explain** the Normal distribution and the concept of normality.
- **Visualize** the normal distribution.
- **Explain** the uses of the 68-95-99.7 rule and the z-score.
- **Visualize** the 68-95-99.7 rule.
- **Apply** z-scoring to data.
- **Explain** and apply the Central Limit Theorem.
- **Visualize** the Central Limit Theorem.

---

## Student Requirements

<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

*Before this lesson(s), students should already be able to:*

1. Iterate and write functions in Python
2. Explain difference between statistics and parameters

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> **Total Time: 120 mins**

- Opening: Review of Sample Statistics and Parameters (10 mins)
- The Normal Distribution (20 mins)
  - Example: IQ (10 mins)
  - Plotting IQ with `scipy` (10 mins)
- The 68-95-99.7 Rule (20 mins)
  - **Check:** What percentage of individuals have an IQ between 85 and 115? (5 mins)
  - **Check:** What percentage of individuals have an IQ above 100? (5 mins)
  - **Check:** What percentage of individuals have an IQ between 85 and 130? (5 mins)
  - Visual representation of 68-95-99.7 rule on the IQ distribution (5 mins)
- The Z-Score (20 mins)
  - Formula for z statistic (5 mins)
  - Calculate the z-scores for a simple vector of values (5 mins)
  - **Check:** Describe how the scipy.stats.zscore function converts the vector of values (5 mins)
  - **Check:** If  XX  is not normal, but we calculate  ZZ  by standardizing  XX  using the mean and standard deviation of  XX  as above, is Z ~ N(0,1)? (5 mins)
- The Central Limit Theorem (20 mins)
- Visualizing the Central Limit Theorem (30 mins)
  - Overview of data (5 mins)
  - Clean data (5 mins)
  - Plot the salary information (5 mins)
  - Practice: Students write a function to sample from data (15 mins)

---

<!--- If a repo contains any additional practice files or supplementary resources (PDFs, etc) describe them here  --->

## Additional Resources

<!--- This section lists useful reference materials that can inform, extend, or deepen a student's understanding of the material. While this may seem like a "nice to have" feature, we normally see a range of advanced and remedial students in our classes. Curating these resources allows us to provide targeted materials and suggestions that instructors can use to support different student needs. --->

*For more information on this topic, check out the following resources:*

- [The Central Limt Theorem animation](http://blog.vctr.me/posts/central-limit-theorem.html)
- [Another, short explanation of the CLT](http://www.usablestats.com/lessons/central_limit)
- [Explaining the Central Limit Theorem with Bunnies & Dragons](http://blog.minitab.com/blog/michelle-paret/explaining-the-central-limit-theorem-with-bunnies-and-dragons-v2)

---