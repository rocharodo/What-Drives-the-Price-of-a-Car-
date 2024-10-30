<div style="margin: 20px; background-color:#FFFFF0; ">
<h1>Table of content</h1>
<ul>
    <li><a href="#DataProblemDefinition">Data Problem Definition</a></li>
    <li><a href="#DataUndestanding">Data Understanding Steps</a></li>
    <li><a href="#HistogramDistribution">Histogram and Distribution</a></li>
    <li><a href="#DataPreparation">Data Preparation</a></li>
    <li><a href="#ModelSelection">Selecting the model</a></li>
    <li><a href="#ExecutiveSummary">Executive Summary</a></li>
</ul>
<div id="DataProblemDefinition">
    <h1>Data Problem Definition:</h1>
    <p>
        Identify the key predictive factors that influence the sale price of used cars using a dataset of 426,000 vehicle records.
        Specifically, develop a regression model that explains the variation in sale price based on various attributes such as manufacturer, model, year, odometer, condition, and other relevant features.
        <br />
        The goal is to extract insights on the relationships between these attributes and sale price, ultimately informing feature importance and driving business recommendations for the used car dealership.<br />
    </p>
    <h2>Key Objectives:</h2>
    <ul>
        <li>
            Identify significant predictors of used car sale price.
        </li>
        <li>
            Quantify the relationships between predictors and sale price.
        </li>
        <li>
            Rank features by importance to inform business decisions.
        </li>
    </ul>
    <h2>Technical Requirements:</h2>
    <ul>
        <li>
            Data preprocessing and feature engineering
        </li>
        <li>
            Regression modeling (e.g. linear)
        </li>
        <li>
            Feature selection and importance analysis
        </li>
        <li>
            Model evaluation and validation
        </li>
    </ul>
    <p>
        This reframed definition provides a clear direction for the data analysis task, focusing on identifying key drivers of used car prices using regression modeling and feature importance analysis.
    </p>
</div>

<div id="DataUndestanding">
    <h1>Data Understanding Steps</h1>
    <p>
        I will use the following steps to get familiar with the dataset and identify quality issues: <br />
    </p>
    <ul>
        <li>
            Step 1: Initial Data Review
            <ul>
                <li>
                    Check the dataset's dimensions (number of rows, columns)
                </li>
                <li>
                    Review the data types for each column (numeric, categorical, date, etc.)
                </li>
            </ul>
        </li>
        <li>
            Step 2: Summary Statistics
            <ul>
                <li>
                    Calculate summary statistics for numeric columns (mean, median, mode, min, max, std dev)
                </li>
                <li>
                    Generate frequency distributions for categorical columns
                </li>
            </ul>
        </li>
        <li>
            Step 3: Data Visualization
            <ul>
                <li>
                    Plot histograms or density plots for numeric columns
                </li>
                <li>
                    Create bar charts for categorical columns
                </li>
                <li>
                    Use scatter plots or correlation matrices to explore relationships between columns
                </li>
            </ul>
        </li>
        <li>
            Step 4: Missing Value Analysis
            <ul>
                <li>
                    Identify columns with missing values
                </li>
                <li>
                    Calculate the percentage of missing values for each column
                </li>
            </ul>
        </li>
        <li>
            Step 5: Data Quality Checks
            <ul>
                <li>
                    Check for invalid or inconsistent values
                </li>
                <li>
                    Identify duplicates or redundant records
                </li>
                <li>
                    Verify data formats (e.g., date, time, categorical)
                </li>
            </ul>
        </li>
        <li>
            Step 6: Data Profiling
            <ul>
                <li>
                    Create a data profile report summarizing the findings
                </li>
                <li>
                    Document data quality issues, inconsistencies, and areas for improvement        <ul>
                </li>
            </ul>
        </li>
    </ul>
    <br />
    <p>Here is the information of the raw data:</p>
    <br />
    <div style="display: block; overflow-x: auto; min-height: 150px; width: 100%;margin-right:auto;">
        <table style="border-collapse: collapse; width: 50%; border-radius: 10px; overflow: hidden;margin:auto;background-color:white;">
            <thead style="background-color: #f0f0f0; border-bottom: 1px solid #ddd;">
                <tr style="text-align: right;">
                    <th style="padding: 10px; border-right: 1px solid #ddd;">Column</th>
                    <th style="padding: 10px;">Non-Null Count</th>
                    <th style="padding: 10px;">Null Counts</th>
                    <th style="padding: 10px;">Percent</th>
                    <th style="padding: 10px;">Dtype</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">id</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">426880</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0.000000</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">int64</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">region</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">426880</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0.000000</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">price</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">426880</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0.000000</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">int64</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">year</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">425675</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">1205</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0.282281</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">float64</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">manufacturer</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">409234</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">17646</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">4.133714</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">model</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">421603</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">5277</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">1.236179</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">condition</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">252776</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">174104</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">40.785232</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">cylinders</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">249202</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">177678</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">41.622470</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">fuel</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">423867</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">3013</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0.705819</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">odometer</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">422480</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">4400</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">1.030735</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">float64</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">title_status</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">418638</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">8242</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">1.930753</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">transmission</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">424324</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">2556</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0.598763</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">VIN</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">265838</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">161042</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">37.725356</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">drive</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">296313</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">130567</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">30.586347</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">size</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">120519</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">306361</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">71.767476</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">type</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">334022</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">92858</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">21.752717</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">paint_color</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">296677</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">130203</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">30.501078</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
                <tr>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">state</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">426880</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">0.000000</td>
                    <td style="padding:10px;border-top:none;border-bottom:1px solid #ddd;border-right:1px solid #ddd;">object</td>
                </tr>
            </tbody>
        </table>

    </div>
    <div>
        <p>
            Based on the table above, it is clear that some features contain null values. Notably, some of these null values exceed the actual non-null values, such as in the case of the "size" feature. As a result, these null values are not worth retaining, as they will skew the data.
            <br />
            As a general guideline, we will retain features with fewer than 50% null values. Later, we will decide whether to fill in the null values with the highest value for each feature, or with a placeholder such as "missing" or "unknown".
        </p>
    </div>

</div>


<div id="HistogramDistribution">
    <h2>Histogram and Distribution</h2>
    <p>
        The following graphs are presented in two separate categories: <br />
        <h3>Numerical Features: Histograms</h3>
        These graphs display the distribution of numerical features through histograms, providing a visual representation of the data's central tendency, dispersion, and shape.
        <br />
        <h3>Categorical Features: Grouped Distributions</h3>
        These graphs illustrate the relationship between categorical features and the target variable (price) by showing the grouped distribution of the feature versus the price. This allows for an examination of how different categories impact the price, enabling insights into potential outliers and patterns.
        <br />
        By visualizing the grouped distribution, we can identify:
        <ol>
            <li>
                Categories with exceptionally high or low prices
            </li>
            <li>
                Categories with limited or excessive price variability
            </li>
        </ol>
        This analysis facilitates a deeper understanding of the complex relationships between categorical features and the target variable, ultimately supporting more informed decision-making.
    </p>
    <div style="text-align:center;">
        <img width="1100" src="histo.png" />
    </div>

    <h2>Initial Observations and Data Quality Concerns</h2>
    <p>
        Upon examining the grouped distributions, it is readily apparent that the data contains:
        <ol>
            <li>
                Outliers and erroneous information - like the 10 digit chevrolet or the 1234567890 volvo -, which can significantly compromise the accuracy and reliability of any subsequent analysis
            </li>
            <li>
                A significantly uneven distribution between manufacturers, with some having a disproportionately large or small number of data points
            </li>
        </ol>
        <h3>
            Need for Data Cleansing
        </h3>
        To ensure the integrity of our analysis, it is essential to perform a thorough data cleansing exercise to:
        <ol>
            <li>
                Identify and remove outliers that may skew the results
            </li>
            <li>
                Correct or eliminate erroneous or invalid data points
            </li>
            <li>
                Handle missing values or inconsistencies
            </li>
            <li>
                Eliminate duplicates
            </li>
        </ol>
        By doing so, we can enhance the quality and reliability of the data, thereby supporting more robust and meaningful insights. This crucial step will enable us to build a stronger foundation for our analysis and mitigate potential risks associated with flawed data.
    </p>
</div>

<div id="DataPreparation">
    <h1>Data Preparation</h1>
    <p>
        Following an in-depth analysis of the data, I identified several initiatives to cleanse and preprocess the data for further analysis. The steps I took are outlined below:
        <h4>Feature Selection and Removal</h4>
        I dropped the following features to minimize redundancy and optimize the dataset:
        <ol>
            <li>
                id
            </li>
            <li>
                VIN
            </li>
            <li>
                size
            </li>
            <li>
                region
            </li>
        </ol>
        <h4>Handling Missing Values</h4>
        To ensure data quality, I removed rows with null values in the following critical features:
        <ol>
            <li>
                year
            </li>
            <li>
                manufacturer
            </li>
        </ol>
        <h4>Imputation of Missing Values</h4>
        For the remaining features with null values, I applied the following imputation strategies:
        <ol>
            <li>
                Fuel: replaced with "gas"
            </li>
            <li>
                title_status: replaced with "missing"
            </li>
            <li>
                drive: replaced with "unknown"
            </li>
            <li>
                paint_color: replaced with "unknown"
            </li>
            <li>
                condition: replaced with "unknown"
            </li>
            <li>
                type: replaced with "unknown"
            </li>
            <li>
                model: replaced with "missing"
            </li>
        </ol>
        <h4>Outlier Removal</h4>
    <p>
        To prevent skewness and ensure robust analysis, I removed the bottom 10% and top 5% of values in the price feature, effectively eliminating outliers.
    </p>

    <h4>
        Concatenation
    </h4>
    <p>
        Analyses revealed that separate manufacturer and model features can introduce errors due to shared models across manufacturers.
        <br />
        To resolve this issue, I concatenated these features, creating unique combined values and ultimately enhancing the model's performance.
    </p>
    <br />
    <p>
        These data preparation steps enabled me to create a cleaner, more reliable dataset for subsequent analysis and modeling.
        The results can be seen in the following graphs:
    </p>
    <br />
    <div style="text-align:center;">
        <img width="1100" src="histo_cleansed.png" />
    </div>
    <h2>Result Analysis</h2>
    <p>
        <h3>Improved Data Distribution</h3>
        As evident from the graphs, our data now exhibits a more even distribution. This is consistently observed across all graphs, with the manufacturer vs. price graph serving as a prime example. Here, we can see that the prices for each manufacturer are now more evenly distributed, indicating the removal of the most prominent outliers.
        <h3>Enhanced Price Analysis</h3>
        The price graph is now displaying different information. Previously, it displayed a simple price histogram. Now, it showcases a price vs. year distribution, revealing the average prices across all years. This new representation uncovers a cyclical pattern and a discernible trend, offering valuable insights into price fluctuations over time.
        <h3>Comparative Analysis</h3>
        The graph below provides a direct comparison between the original data price vs. year and the cleansed data price vs. year. At a glance, we can appreciate the significant improvement in data distribution. The cleansed data, now more evenly distributed, will serve as the foundation for further analysis, enabling more accurate and reliable conclusions.
    </p>
    <div style="text-align:center;">
        <img width="1100" src="pricevsyear.png" />
    </div>

    <h2>Data Preparation</h2>
    Now that we have thoroughly cleansed the data, we can proceed to prepare it for further analysis, focusing particularly on the categorical features.
    <h3>Encoding Categorical Features</h3>
    To facilitate analysis, I applied the following encoding techniques:
    <ol>
        <li>
            One Hot Encoding: For the features with multiple categories, I used One Hot Encoding to create binary vectors:
            <ol>
                <li>
                    model
                </li>
                <li>
                    Transmission
                </li>
                <li>
                    paint_color
                </li>
                <li>
                    state
                </li>
                <li>
                    fuel
                </li>
                <li>
                    title_status
                </li>
                <li>
                    drive
                </li>
                <li>
                    type
                </li>
                <li>
                    condition
                </li>
            </ol>
        </li>
    </ol>

    <h3>Data Preparation and Encoding</h3>
    <p>
        The data preparation and encoding process was successfully executed utilizing the make_column_transformer function, capable of handling multiple encoding schemes concurrently.
    </p>


    <h3>Next Steps</h3>
    With the transformed data, we can now proceed to select a suitable algorithm and forecast the price with increased accuracy.
</div>

<div id="ModelSelection">
    <h1>Selecting the model</h1>

    <h2>Model Selection and Evaluation</h2>
    <p>
        To identify the most accurate model, I evaluated three distinct regression models, each with its strengths and weaknesses. The selected models were:
    </p>
    <ol>
        <li>
            Ridge Regression: A linear regression model that uses L2 regularization to reduce overfitting by minimizing the magnitude of model coefficients.
        </li>
        <li>
            Lasso Linear regression with L1 regularization for feature selection and reduced multicollinearity.
        </li>
        <li>
            Linear Regression Basic linear regression for simple relationships and initial analysis.
        </li>
        <li>
            Elastic Net Hybrid linear regression combining L1 and L2 regularization for balanced regularization.
        </li>
    </ol>
    <p>
        The objective of this evaluation was twofold:
    </p>
    <ul>
        <li>
            Achieve a balance between Mean Squared Error (MSE), ensuring accurate predictions while minimizing overfitting.
        </li>
        <li>
            Identify the coefficients of each feature, enabling the analysis of their impact on car prices.
        </li>
    </ul>
    <p>
        By comparing the performance of these models, we can determine which one provides the most insightful and accurate predictions, ultimately informing data-driven decisions.
    </p>
    <p>
        The result of the evaluation can be found in the following table:
    </p>

    <div style="display: block; overflow-x: auto; min-height: 150px; width: 100%;margin-right:auto;">
        <table style="border-collapse: collapse; width: 50%; border-radius: 10px; overflow: hidden; margin: auto; background-color: white;">
            <thead style="background-color: #f0f0f0; border-bottom: 1px solid #ddd;">
                <tr>
                    <th>Model</th>
                    <th>Best Score</th>
                    <th>Mean Squared Error (MSE)</th>
                    <th>Elapsed Time</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background-color:lightgreen;">
                    <td>Ridge</td>
                    <td>0.561262</td>
                    <td>40,246,517.02</td>
                    <td>30 seconds</td>
                </tr>
                <tr>
                    <td>Linear Regression</td>
                    <td>0.552364</td>
                    <td>41,062,787.54</td>
                    <td>50 seconds</td>
                </tr>
                <tr>
                    <td>Lasso</td>
                    <td>0.541976</td>
                    <td>42,015,664.01</td>
                    <td>2 hours 56 minutes</td>
                </tr>
                <tr>
                    <td>Elastic Net</td>
                    <td>0.382332</td>
                    <td>56,660,232.62</td>
                    <td>15 minutes</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h1>Conclusions</h1>

    <h2>Model Performance Comparison</h2>
    <ul>
        <li>Ridge Regression outperforms Linear Regression, Lasso and Elastic Net in terms of Best Score (0.561262) and Mean Squared Error (MSE) (40,246,517.02).</li>
        <li>
            Linear regression comes second with a score of 0.552364 an MSE of 41062787.54 and 50 seconds
        </li>
        <li>Lasso Regression has the longest training time (2 hours 56 minutes), despite its relatively poor performance.</li>
        <li>Elastic Net Regression has the worst performance among the three models, with the lowest Best Score (0.382332) and highest MSE (56,660,232.62).</li>
    </ul>

    <h2>Time-Efficiency Tradeoff</h2>
    <ul>
        <li>Ridge Regression: Best performance and fastest training time (30 seconds).</li>
        <li>Linear Regression has a very good performance (50 seconds) but is not better than Ridge Regression</li>
        <li>Elastic Net Regression: Relatively slow training time (15 minutes) considering its poor performance.</li>
        <li>Lasso Regression: Longest training time (2 hours 56 minutes), making it the least efficient.</li>
    </ul>

    <h2>Error Analysis</h2>
    <p>All models struggle with large errors, as indicated by Mean Squared Error (MSE) values.</p>
    <p>Ridge Regression has the lowest MSE (40,246,517.02).</p>

</div>

<div id="ExecutiveSummary">
    <h1 style="text-align:center;">Used Car Price Prediction Report</h1>
    <h1>Executive Summary</h1>
    <p>
        This report presents the findings of a data analysis aimed at identifying key factors influencing used car prices. Using Ridge model, we determined the most relevant features and their coefficients. Our results provide actionable insights for used car dealers to fine-tune their inventory and pricing strategies.
    </p>
    <h2>Methodology</h2>
    <p>
        This predictive modeling project employed a structured approach to analyze the vehicle dataset and estimate car prices.
    </p>
    <h3>Dataset</h3>
    <p>
        The dataset utilized in this study consisted of 426,000 vehicle records, containing a mix of numerical and categorical features:
    </p>
    <ul>
        <li>
            Numerical features: price, year, odometer
        </li>
        <li>
            Categorical features: region, manufacturer, model, condition, cylinders, fuel, transmission, drive, size, type, paint_color, state
        </li>
        <li>
            Identifier: id, VIN
        </li>
    </ul>


    <h3>Data Preprocessing</h3>
    <p>
        The dataset underwent rigorous data cleansing and preparation:
    </p>
    <ul>
        <li>
            Handling missing values and outliers
        </li>
        <li>
            Data normalization and feature scaling
        </li>
        <li>
            Encoding categorical variables
        </li>
        <li>
            Transforming numerical features
        </li>
    </ul>


    <h3>Model</h3>
    To predict car prices, the following models were evaluated:
    <ul>
        <li>
            Ridge Regression:
            Ridge Regression is a regularized linear regression technique that minimizes overfitting by adding a penalty term to the cost function.
        </li>

        <li>
            Lasso (Least Absolute Shrinkage and Selection Operator):
            Lasso is another regularized linear regression technique.
        </li>

        <li>
            Linear Regression:
            Linear Regression is a basic linear regression model.
        </li>
        <li>
            Elastic Net:
            Elastic Net is a hybrid regularized linear regression technique that combines Ridge and Lasso.
        </li>
    </ul>
    <h3>Evaluation Metrics</h3>
    <p>
        Model performance was assessed using:
    </p>
    <ul>
        <li>
            Mean Squared Error (MSE): measures prediction accuracy
        </li>
        <li>
            Score: Evaluates the model's ability to make accurate predictions.
        </li>
        <li>
            Time/Performance: Measures the computational efficiency and speed of the model.
        </li>
    </ul>


    <h1>Model Selection and Insights</h1>

    <p>Following a thorough evaluation, we selected the Ridge model as the most suitable algorithm due to its accuracy and performance. To glean actionable insights, we examined two key characteristics: permutation importance and coefficients. These metrics enabled us to determine vital information from the model, which informed the subsequent benefits for car dealerships, categorised into low-end, mid-range, and high-end.</p>

    <h2>Permutation Importance Insights</h2>
    <p>Permutation importance measures the contribution of each feature to a model's predictions. It calculates the decrease in model performance when a feature is randomly shuffled, indicating its relative importance.</p>
    <p><strong>Permutation Importance:</strong> Which features matter most?</p>

    <div style="text-align:center;">
        <img src="permutation.png" />
    </div>
    <ul>
        <li>
            The number of cylinders (5 cylinders) and the car's condition (excellent) are the most important features, influencing 89.5% of the model's predictions.
        </li>
        <li>
            The condition of the car (fair, unknown, new, like new, good) has a significant impact on the prediction, indicating that the model is sensitive to the car's state.
        </li>
        <li>
            The number of cylinders (10, 4, 12, 3) has a relatively lower importance score, suggesting that the model is less sensitive to these features.
        </li>
    </ul>

    <h2>Coefficients Insights</h2>
    <p>Coefficients represent the change in the predicted outcome for a one-unit change in the feature, while holding all other features constant. They indicate:</p>
    <p>
        <strong>Coefficients:</strong> How much do individual features impact the prediction?
    </p>
    <div style="text-align:center;">
        <img src="coefficients.png" />
    </div>

    <ul>
        <li><strong>Luxury brands</strong>: Negative coefficients (e.g., Ferrari -11165.953304, Audi -11055.727044) signify lower prices or reduced demand, indicating a niche market.</li>
        <li><strong>Classic Ford models</strong>: High positive coefficients (e.g., Ford_Roadster 43548.884763) suggest elevated demand and prices, presenting lucrative opportunities.</li>
        <li><strong>Mid-range models</strong>: Moderate coefficients (e.g., Chevrolet_Coupe 32694.947709) indicate stable demand and prices, ensuring a consistent revenue stream.</li>
    </ul>

    <h2>Benefits for Car Dealerships</h2>

    <h3>High-End Car Dealers</h3>

    <ul>
        <li>Stock high-performance vehicles: Focus on 5-cylinder models from luxury brands.</li>
        <li>Emphasise condition: Highlight excellent condition to command premium prices.</li>
        <li>Target luxury buyers: Focus marketing on affluent customers seeking high-end features.</li>
        <li>Potential profit margins increase by $32,000-$43,000 per luxury unit sold.</li>
    </ul>

    <h3>Mid-Range Car Dealers</h3>

    <ul>
        <li>Focus on 5-cylinder models, which have high importance scores (cylinders_5 cylinders: 0.51755).</li>
        <li>Focus on selling Chevrolet Coupe and Ford Convertible, highlighting value-for-money.</li>
        <li>
            Emphasize the value of mid-range models like Ford F-350 SD Lariat and GMC Sierra SLT 6.2L Crew Cab, considering their negative coefficients (-11575.422905 and -11442.310872).
        </li>
        <li>
            Highlight excellent condition and maintenance to appeal to practical buyers (condition_excellent importance score: 0.37687).
        </li>
    </ul>

    <h3>Low-End Car Dealers</h3>

    <ul>
        <li>Target budget-conscious buyers: Emphasise affordability, fuel efficiency, and reliability.</li>
        <li>
            Focus on affordable models with fewer cylinders (3 or 4), which have lower importance scores (cylinders_3 cylinders: 0.00614, cylinders_4 cylinders: 0.02032).
        </li>
        <li>
            Highlight good condition and maintenance to appeal to budget-conscious buyers (condition_good importance score: 0.00598).
        </li>
        <li>Price competitively: Set prices considering low-end coefficients and market demand.</li>
    </ul>

    <h3>Common Benefits</h3>

    <ul>
        <li>Data-driven pricing: Utilise coefficients to inform pricing strategies.</li>
        <li>Inventory optimisation: Stock vehicles with in-demand features.</li>
        <li>Targeted marketing: Focus on specific customer segments.</li>
    </ul>

    <h3>Luxury and Classic Models</h3>

    <p>Ford's iconic models (Roadster, Coupe, T, T-Bucket, Tudor, Model A) increase prices by $32,000-$43,000. Chevrolet's Coupe increases prices by $32,694.</p>

    <h3>Commercial and Heavy-Duty Vehicles</h3>

    <p>Models like Audi Q8, Ferrari California T, and GMC Sierra SLT 6.2L Crew Cab reduce prices by $11,000-$15,000.</p>

    <p>By leveraging these insights, car dealerships can refine their business strategies, enhance customer satisfaction, and boost profitability.</p>

    <h2>Action Items:</h2>
    <ul>
        <li>Review inventory and pricing strategies.</li>
        <li>Develop targeted marketing campaigns.</li>
        <li>Adjust sales training to emphasize value propositions.</li>
    </ul>
    <h2>Conclusion</h2>
    <p>
        This analysis provides valuable insights for used car dealers to refine their pricing strategies and inventory management. By understanding the impact of key features on car prices, dealers can make informed decisions to optimize their business.
    </p>
</div>
</div>
