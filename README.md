# Beauty Recommendation System
: *Mapping hair products based on their ingredients similarities and giving content-based filtering recommendation*

*This document details the purpose, methodology, and application of data science within the Beauty Recommendation system. Section 1 outlines the business objective addressed by the data science work, and defines the scope of the effort. Section 2 describes the data collected and utilized during analysis. Sections 3, 4, and 5 detail the methodologies employed, why they were selected, and how they are used and tuned (Section 4), trained (Section 5), and tested (Section 6). Finally, an interactive visualization with Bokeh *
<br>

## ***1. Textured Hair: Users are spread thin with trying to figure out which products work for them.***

The consumers in the natural hair care industry relies on users ratings and reviews on products all over the US. Additionally, these consumers focus on the reviews from users who are similar to them. 

We will use the real time data set with various features a user would look into regarding a hair product (ie. ingredients, hair type, reviews, sentiments, ratings). We will be considering widely used products in the natural hair community.

The basic idea of analyzing this dataset is to get a fair idea about the factors affecting the products of different brands in the market, aggregate ratings of each brand. The average brand has over 10 products serving the US market.

With new products coming to the market every day, the industry is saturated. In spite of increasing demand for hair products, users are having a difficult time finding the right one. With such an overwhelming demand of hair products it has become important to study the hair parameters in connection with products on the market.
What kind of products are more popular for a specific hair type. Do the entire 4c - fine hair hair community love light products? If yes, then are these products being widely used by 4c - hair naturals? These kind of analysis can be done using the data, by studying the factors such as:
<br>

* Ingredients

* Approx Price of product

* Is a particular brand famous for its own kind of product

* Brands that sells eco-friendly products
<br/>

## ***2. Data: Perform extensive Exploratory Data Analysis(EDA) on Dataset.***

**Phase 1**

* Option 1: Scrape from brands website  
* Option 2: Find a company that sell these brand, ie target 

**Phase 2**

Data wrangling: The recorded data for each brand and each category should be read and data for each brand should be scraped individually. How many  variables were scraped in this phase? 
<br/>

## ***3. Visualization***

**Key insights found**

* Popular brands in the market

* Sentiment analysis

* Whether brand  recommend products based on hair type

* Ratings distributions (histogram) - what are the insights

* Type of products

* Distribution of cost of products  

* Most liked product type ( conditioner, shampoo) - See what people spend most of their money on.
<br/>

## ***4. Modeling: Train***
: *Build an appropriate Machine Learning Model that will help user select products based on certain features*

## ***5. Modeling: Test***
