# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Kaggle Challenge: Classification

## Introduction

Welcome to your first week of work at the Center for Disease Control. Time to get to work!

Due to the recent epidemic of West Nile Virus in the Windy City, we've had Chicago's Department of Public Health set up a surveillance and control system. We're hoping it will let us learn something from the mosquito population as we collect data over time. Pesticides are a necessary evil in the fight for public health and safety, not to mention expensive. We need to derive an effective plan to deploy pesticides throughout the city, and that is **exactly** where you come in.

You and your team will need to help us track and predict the regions with the highest concentration of viral mosquito vectors. Also, see Cathy in HR about getting your benefits set up. We have a GREAT health plan!

Once again, welcome to the CDC. We have high expectations for you!

---

## Dataset

The dataset, along with description, can be found here: [https://www.kaggle.com/c/predict-west-nile-virus/](https://www.kaggle.com/c/predict-west-nile-virus/).

**This is also where you will be submitting your code for evaluation**. We will be using the Kaggle Leaderboard to keep track of your score. The leaderboard uses roughly 30% of the dataset to score an AUC (Area Under Curve) metric. [You can read more about the scoring metric here](https://www.kaggle.com/c/predict-west-nile-virus#evaluation). Despite the fact that an official Kaggle competition is closed, teams can still submit their models and get evaluated by their official metrics, which allows for us to use these competitions even though they are "over".



---

## Requirements

Here is your team's assignment:
- Set up a GitHub repository
- Create a Jupyter notebook
- Investigate the data
- Evaluate threats and outliers
- Submit notebook for automated Kaggle scoring
- Create a presentation of your findings

**Bonus:**
- Use a project management systemt to divide and document your work
- Using `np.correlate`, explore correlations in the data. Document your findings
- Commit all of your notes to the GitHub repo in a 'Research' directory

---

## Evaluation

Your Kaggle submission will be evaluated in the following 4 areas:

1. **AUC Score**: A clear winning group will be determined based on the AUC Scoring performed by the Kaggle Leaderboard. This is not to say that the winning group's work will always be the best submission. Hitting a benchmark is important but does not guarantee success. A standout project will also have:

2. **Clear Documentation**: Document the observations and decisions your team has made along the way, either by commenting in your code or by including a separate markdown/text file. Repeatability is key - would someone else be able to understand your decisions and replicate your methods? 

3. **Clean Code**: All of your models, pipelines, cleaning techniques, and transformations should be properly coded and documented. Syntax is important, as Data Scientists are often tasked with building products that will be collaborated upon or maintained by other engineers. It is also important that no mistakes were made while pipelining data. If any data points were corrupted, the results are useless.

4. **Brief Presentation**: Your presentation should be short and sweet.  Describe your data and approach as if your client is in front of you. Explain the decisions you made, which factors and metrics you used to evaluate, and include visualizations of your results. The goal is to summarize the project lifecycle and tell a story about your team's journey.

---

## Suggested Ways to Get Started

#### Roles

E.g."Roles are good. structure your teams so that you have a mixture of abilities." Explain common industry roles ahead of time (Missing content here) and have them self select.

Teams of 5*
- product owner
- documentation
- data processing
- visualization
- QA

NOTE: If bigger teams, give less time. E.g. quick weekend hackathon (get as far as possible, measure team's model performance against each other for "winner", treat winners to something nice)
Teams of 3 (benefit: avoids dead weight)
If smaller team, give longer timeline for competition (e.g. 1-2 weeks)


#### GitHub Repo

1. Create a GitHub repository for your group and add everyone as contributors.
2. Retrieve the dataset and upload it into a directory named `assets`.
3. Generate a .py or .ipynb file that imports the available data.

#### EDA

1. Ask questions to describe the data. What does it represent? What types are present? What does each data points' distribution look like?
2. What kind of cleaning is needed? Document any potential issues that will need to be resolved.
3. When describing your approach, try following the scientific method. Ask: What is our problem statement? What can we learn from the data in order to make an educated hypothesis? What is our hypothesis?

#### Project Planning

1. Define your deliverable: what is the end result?
2. Break that deliverable up into its components, and then divide further until you have actionable items.
3. Begin deciding priorities and owners for each task. 

---
