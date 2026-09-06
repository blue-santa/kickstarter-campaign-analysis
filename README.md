# Kickstarter Campaign Analysis

## Springboard Academy \- Capstone 3

Over the last few years, entrepreneurs have invented some truly unusual ideas, such as edible picnic cups, pirate-themed pancakes, and even a bluetooth-enabled lunchbox. To bring these types of concepts to fruition, entrepreneurs can turn to a popular crowdsourcing platform called Kickstarter. Only \~40% of campaigns are successful, and this data essay seeks to learn why. This essay uses popular statistical and machine-learning techniques to analyze campaigns with a few key questions in mind: 

- How can we categorize a potential Kickstarter campaign?  
- What do successful and unsuccessful campaigns have in common?  
- Can we predict whether a campaign will be successful, based on its descriptive data?

The basic idea of Kickstarter is that a candidate can present a rough outline of any potential creation on the website, state how much money they believe they would need to complete the work, and viewers can choose to support by pledging funds. There is a catch: the money is only charged if there is enough audience support to exceed the entrepreneur’s stated target. Otherwise, the crowdsourcing attempt fails and the candidate is left empty handed.

This project first engages in several analytical methods to categorize campaigns and create a predictive model. Kickstarter campaign datasets are available on Web Robots platform.


The datasets are wrangled to create a clean, unified dataset that can support exploratory data analysis. This work is performed in Jupyter Notebook. Common visualization techniques, such as bar plots, scatterplots, and word clusters are created to generate a sense for the overall nature of Kickstarter campaigns. Machine-learning techniques follow, using the popular Scikit-learn library tools such as Logistic Regression. In addition, taking into account categorical data both from the raw dataset and from metadata, the essay breaks the campaigns into groups using K-Means Clustering.

At a future date, as a final step, this project may also develope a presentation that includes a graph visualization of the campaigns. This visualization will show limited sets of campaign clusters, their relationship to each other, and their relationship to various forms of metadata. The essay will use tools such as FalkorDB, Redis, and [Cytoscape.js](http://Cytoscape.js) to create this browsable static visualization. The findings will be communicated on the author’s personal web portfolio.

In summary, this essay uses data from Kickstarter campaigns and their unusual entrepreneurial ideas to analyze and predict campaign outcomes. Foundational data-science techniques take place first in Jupyter Notebook using Scikit-Learn, Logistic Regression, and K-Means Clustering. The findings are communicated in an overall presentation that includes a pdf report, model parameters, jupyter notebook files, and .png file visualizations using matplotlib and seabor. 

# Model Parameters

## Classification Model

### Library

Scikit-Learn

### Type

LogisticRegression

### R^2 Score

`0.92`

## Scaler

### Library

Scikit-Learn

### Type

StandardScaler
~                 

## Clustering Model

### Library

Scikit-Learn

### Type

KMeans

### Hyperparameters

`n_clusters=2500`
`init=k-means++`
