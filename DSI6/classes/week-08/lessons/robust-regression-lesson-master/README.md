# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Robust Regression

> Unit X, Lesson Y

<!--- This template is an instructor-facing description of lesson contents. Students who fork these repos may also be able to view. --->

---

## Materials We Provide
<!--- This section is a table of contents for the lesson. The table structure breaks down typical lesson resources into types, distinguishing between lesson notebooks and other supporting materials. Note that the table below demonstrates the total possible range of materials; most lessons won't require all of the categories below. Also note that every item in the repo should get its own line and link, like the example shown for data. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Interactive jupyter notebook with structured lesson content | [Link](./robust-regression.ipynb)|
| Data | Local copy of any dataset used | [Link](./lemonade-stand.csv)|

> Dataset description: Lemonade stand is a data set of lemonade sales and their relationship to temperature and humidity.

> Note that this lesson has some hands-on physical activities. You might want to check whether there is a large open
> space available. If you can organise to buy a ball of string and a large number of numbered counters that can make
> for a more enjoyable experience (and a faster one too).


---

## Learning Objectives
<!--- This section lists the learning objectives of the lesson. For information on how to write clear learning objectives, see: http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/ --->

- **Revise** the limitations and short-comings of OLS and the $R^2$ scoring function
- **Define** when to use robust regression methods instead of OLS
- **Demonstrate** how Theil-Sen, RANSAC and Huber work, and what they are optimising for
- **Explain** the advantages of using median absolute error as a scoring function
- **Create** a scoring function appropriate for different business scenarios

---

## Student Requirements
<!--- This section explains the relevant prerequisites; in other words, what do students need to know to be able to benefit and perform the tasks required in this lesson? This includes lists of skills or prior learning objectives --->

**Before this lesson(s), students should already be able to**:
- Split a dataset into train and test parts
- Create a linear model using `sklearn.linear_model.LinearRegression`
- Create a scatter plot using Matplotlib
- Understand the concept of error in a prediction

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection --->

> Total Time: 72 min. 

- **Introduction**
  - Motivational speech about how a lot of what data scientists do, they've learned now? (5 min)
- **Review of ordinary least squares** (22 min)
    - Review (10 min)
	- Why we like R^2 (4 min)
	- Problems with R^2 (5 min)
	- Alternatives (3 min)
- **Robust Regression** (35 min)
	- Theil-Sen (15 min including activity)
	- RANSAC (15 mins including activity)
	- Huber (5 min)
- **Median Absolute Error** (5 min)
- **Scenario-specific scoring functions** (5 min)
	- Qiqi's Lemonade Stand (5 min)
- Lesson Review

---

## Additional Resources
<!--- This section lists useful reference materials that can inform, extend, or deepen a student's understanding of the material. While this may seem like a "nice to have" feature, we normally see a range of advanced and remedial students in our classes. Curating these resources allows us to provide targeted materials and suggestions that instructors can use to support different student needs. --->

For more information on this topic, check out the following resources:
- [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/)
- [The more advanced book: Elements of Statistical Learning](http://web.stanford.edu/~hastie/ElemStatLearn/)
- [Spurious Correlations](http://www.tylervigen.com/spurious-correlations)
- Wikipedia pages on [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance), [Welch's t-test](https://en.wikipedia.org/wiki/Welch's_t-test), [Mann-Whitney test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)
- The [RANSAC song is an amusing video](http://danielwedge.com/ransac/)
