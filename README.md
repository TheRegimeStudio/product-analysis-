# Beauty Recommendation System
: *Mapping hair products based on their ingredients similarities and giving content-based filtering recommendation*

*This document details the purpose, methodology, and application of data science within the Beauty Recommendation system. Section 1 outlines the business objective addressed by the data science work, and defines the scope of the effort. Section 2 describes the data collected and utilized during analysis. Sections 3, 4, and 5 detail the methodologies employed, why they were selected, and how they are used and tuned (Section 4), trained (Section 5), and tested (Section 6). Finally, an interactive visualization with Bokeh *
<br>

## ***1. Textured Hair: Users are having a hard time finding products that work.***

For the longest time, textured hair people have been underrepresented, so there was not understanding of hair hair. Just had to use what was available. The natural hair movement startin ~ 2008 brought to light the need and demand for products that caters to textured hair. 

Since then, there have been plethora or products on the market for JUST textured hair. This ranges from shampoo, condition, styling gel, co-wash. Some products we didnt even know we need! Well the issue now is that we dont know what will work for us :thinking:. We are not one size fits all. It's becoming difficult when trying new products; it's a lot of research from social media, friends and family and in the case where it doesnt work <this happens a lot> we have now wasted a lot of time and money. 

I know many of you can relate to this experience but for us textured people, this is new territory for us. But we can do something about it! We know that the products we use have everything to do with chemistry and the compounds that make up this product. You have heard it before, - and if you haven't - newsflash! there are some terrible compounds in our products that doesnt work well for our hair. For some of us we might be allergic to some of ingredients. But we aren't all chemist and sometimes ***ain't no body got time*** to analyze every bottle :woozy_face:.


***A user will go to this dashboard for information on products they will like to try based on like ingredients, saving them time and money***


<br/>

# No need to worry, I decided to build a simple recommendation system :wink:

## ***2. Data: Perform extensive Exploratory Data Analysis(EDA) on Dataset.***

**Phase 1**

First thing! We need data... The issue is, because textured hair has been underrepresented, there isn't any available data. So we have to web=scrape. We will be scraping target because they have this pre classification mechanism and more access to data type and products. 


* Currently, www.target.com and www.sallybeauty.com is the only platform that has segmentation for textured hair   

**Phase 2**

* **Applied skills:** Web scraping with Selenium. Text mining and word embedding. Natural Language Processing. Content-based Recommendation Filtering using Cosine similarities of chemical compositions. Interactive Visualization/dashboard.


Data wrangling: The recorded data for each brand and each category should be read and data for each brand should be scraped individually.

* Categories to consider: Brand, name, ingredients, beauty purpose
<br/>

## ***3. Visualization***

**Key insights found**

* Clustering and classification

* Type of products

<br/>

## ***4. Modeling: Train***
: *Build an appropriate Machine Learning Model that will help user select products based on certain features*

## ***5. Modeling: Test***
