<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center"> Prediction of French electricity consumption using 4 ML models </h3>

  <p align="center">
    Here is a project of my own, in which I tried to predict the French electricity consumption over 2 days with different models of Machine Learning.
    <br />
    <a href="https://github.com/Zebho/Prediction_Consumption_French_Electricity"><strong> Explore the docs </strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#the-data">The Data</a></li>
      </ul>
      <ul>
        <li><a href="#the-preprocessing">The Preprocessing</a></li>
      </ul>
      <ul>
        <li><a href="#the-models">The Models</a></li>
      </ul>
      <ul>
        <li><a href="#the-metrics">The Metrics</a></li>
      </ul>
      <ul>
        <li><a href="#improvementsh">Improvements</a></li>
      </ul>
    </li>
    <li>
      <a href="#built-with">Built With</a>
    </li>
     <li>
      <a href="#licence">Licence</a>
    </li>
     <li>
      <a href="#contacts">Contacts</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The aim of this project is to set up a prediction of French electricity consumption over 2 days using data available on the Internet. I've chosen this example because, firstly, it's a sector that particularly appeals to me and, secondly, all the data (former consumption or associated characteristics) are easily and freely accessible on the Internet.


The project therefore comprises 4 phases:
* A phase of recovering the data needed for this modelling from various public sites,
* A pre-processing phase is required to make the data usable for the different models,
* Simple training on 4 types of model,
* More complex training in order to compare the models in a more stable way.

The training was carried out so that I could familiarise myself with them and then compare their effectiveness in a practical project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### The Data
All the data was retrieved from sites that make it freely and publicly available. It has been retrieved in the form of files and not in the form of API requests. The notebook therefore retrieves the most recent data from the following sites:

* The French electricity consumption in real time

  For example : [Eco2mix En Cours](https://eco2mix.rte-france.com/download/eco2mix/eCO2mix_RTE_En-cours-TR.zip )

* The data which corresponds to half-hourly national temperature values (normal and actual) and actual pseudo-radiation values used by Enedis to establish and control regulatory energy balances (flow reconstitution) used for the production/consumption balance essential for maintaining the electricity network

  [Data.gouv Temperature Dataset](https://www.data.gouv.fr/fr/datasets/donnees-de-temperature-et-de-pseudo-rayonnement-en-j-2/ )
* The Tempo value for each day, on the ECO2Mix website [ECO2Mix Indicators Website](https://www.rte-france.com/en/eco2mix/download-indicators )

  For example : [ECO2MIX_Tempo_2022-2023](https://eco2mix.rte-france.com/curves/downloadCalendrierTempo?season=22-23)


### The Preprocessing
The preprocessing is a classic one : one preprocess each dataset on his own and then merge the 3 in order to get one final big dataset, which is saved in a folder named "Data_Final".

We add the number of the weekday (0-6), if it is a schoolday or a public holday (0-1). Finally, one transform some variable into circulars ones in order to take into account the cyclical aspect of minutes/hours/days/months over the year.

I've added the lagged values of the consumption and the temperature in order to stabilise the model. We have 48 lagged values (24h of lagged) and 25 lagges values of temperature (12h), related to the 30-min steptime.

Finally, a robust scaler is used over all the numeric values and the Tempo values in OneHotEncoded.

### The Models
I have chosen 4 models :
* The HistGradientBoostingRegressor
* The LinearBoostRegressor
* The GradientBoostingRegressor
* The XGBOOST

### The Metrics
To compare them, I did 3 training sessions and compare their MAE and MAPE.
1) Training between 2022-06-02 and 2024-03-08, which is 498 days. And comparison over 2 days following the train set.
2) Comparison of results predictions over 2 days over 1 month apart (always stritcly 1 year's train)
3) Comparison of results predictions over 2 days with 1 year and the previous days of the month (increasing the size of the train dataset each day)

### Improvements
Here is some improvments for this projects :
* Add a Request directly on API,
* Add others features which can be useful for the prediction,
* Modify the scalers used,
* Use others ML models,
* Apply this projet on a Deep Learning point of view, with maybe a mix ML and DL.


## Built With

This section list any major frameworks/libraries used :

* SKLearn
* vacances_scolaires_france
* [https://github.com/cerlymarco/linear-tree][Lineartree]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Arthur DUBOIS - [@zebh0](https://twitter.com/zebh0) - arthurdubsm@gmail.com

Project Link: [https://github.com/Zebho/Prediction_Consumption_French_Electricity?tab=readme-ov-file](https://github.com/Zebho/Prediction_Consumption_French_Electricity?tab=readme-ov-file)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
