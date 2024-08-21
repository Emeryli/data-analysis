<h1 align="center">Data Analysis Portfolio</h1> 

### \| Table of Content📖 
  - [Introduction](#intro)
  - [IMDB Data Analysis](#Movies)
  - [Data Professional Survey Analysis](#ProfessionalSuvey)
  - [Bike Buyer Excel Analysis](#bikebuyer)
  - [Covid-19 Data R Analysis](#covid)
  - [Identify Commonalities](#ic) 

---

<a id="intro"></a>
### \| Introduction :star:
Here is the manual to make this portfolio more readable. Feel free to jump to the sections you like by clicking the titles under the Table of Content, whose order is ranked by the date the projects were added to the portfolio. Each section contains the title, the goals of the project, and the steps that I took to achieve the results. All the source scripts/files can be found and downloaded from the panel on the left by clicking the title. Thanks for reading!

---
 <!-- headings -->
 <a id="Movies"></a>
### \| IMDB Data Analysis :movie_camera:
This project was to find out what factors had high correlation to the **gross**. In conclusion, the **budget** has a high correlation (> 0.7). 
First, the project used matplotlib to plot the scatter dots of gross and budget. From there, we can see when budget increases, the gross increases relatively. 
![1](https://github.com/Emeryli/DataAnalysis/assets/71569536/453a884a-a269-4bb1-962c-87b055c9e546)

Secondly, in order to visualize their relation better. Regression line was drawn to indicate the positive correlation.
![2](https://github.com/Emeryli/DataAnalysis/assets/71569536/87cc2c2f-808f-4483-ae38-38fa60ab601d)

Third, Heatmap was used to show the numbers of correlation.
![3](https://github.com/Emeryli/DataAnalysis/assets/71569536/6c4a3535-e4b2-4557-9332-442001bc3308)

Lastly, The correlations were sorted ascendantly.

---

<a id="ProfessionalSuvey"></a>
### \| Data Professional Survey Analysis :pencil:
This project created visuals in Power BI based on the data from the survey. The report shows the average salaries, happiness and age, as well as the most used programming language. The viewers can click the country they like to view the corresponding data. 
![dataSurvey](https://github.com/Emeryli/DataAnalysis/assets/71569536/55be7fd0-6e70-4a37-85eb-6a491c064c2a)

---

<a id="bikebuyer"></a>
### \| Bike Buyers Excel Dashboard 🚲
In order to find out what traits of the survey takers would be more likely to respond to the survey, a dashboard was created to answer the question. After analyzing, people with age between 31 to 55 are the major survey respondents. Besides, the dashboard also reflected the relationship between income and education level. Such information can be used by the business to make selling strategies targeted at specific age groups with certain education level.  
![bike](https://github.com/Emeryli/DataAnalysis/assets/71569536/20b1d1c2-9def-4dd8-a4a2-4746e76bed95)

---

<a id="covid"></a>
### \| Covid-19 Data Analysis in R Language 🦠
Determining what factors were statistically significantly related to death was the main goal of this analysis. However, the original raw data was not ready to be used as some columns format were not standardized, which means they needed to be cleaned up first. Next step, in order to find out the factors mentioned, both age and gender were hypothesized to be related to death. Finally, after performing Welch's Two Sample t-test, the p-values of those were less than 0.05, meaning we can reject the null hypothesis, concluding that both age and gender are statistically significant.<br />
![covid1](https://github.com/Emeryli/DataAnalysis/assets/71569536/ebe32233-c721-48bf-b06b-34c3e8794eb5) <br />Age Welch's Two Sample t-test
<br />
![covid2](https://github.com/Emeryli/DataAnalysis/assets/71569536/8dea01af-4a69-451f-b293-9827cd87b628)
<br />Gender Welch's Two Sample t-test

---

<a id="ic"></a>
### \| Identify Commonalities 
This Python script takes text documents, which contain the group name at the first line, and elements in the following rows, and outputs the common elements across different groups. 
<br />Input:
![thumbnail_image001](https://github.com/user-attachments/assets/bf4d5241-0a4c-43ec-8c16-beb54e4d4178)
<br />Output:
![thumbnail_image002](https://github.com/user-attachments/assets/2eb24f0d-dccc-496b-9fc7-9cace5d7a86f)





