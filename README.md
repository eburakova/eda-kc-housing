<center><img src="https://www.invest4land.com/wp-content/uploads/2021/05/Invest4Land-Investment-Agricultural-Real-Estate-Agroforestry-Secondary-Income-Generation-Eggs-Livestock-Farmlands-Investment-Agriculture-0-1.jpg" height="400"/></center>

# **Exploratory data analysis of socially responsible investment opportunities into real estate of King County (WA, USA)**
The names and personalities below are fictional.

[<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Read In Colab"/>](https://colab.research.google.com/github/eburakova/eda-kc-housing/blob/main/eda_notebook.ipynb)

## The challenge
Ms. Erin Robinson - The Client of Nova Piscibus Consulting GmbH - is a socially responsible investor in the real estate. She wishes to improve living conditions in King County (WA, USA) by investing into the development of poor neighborhoods. 
Our goal at Nova Piscibus is to determing the factors that affect potential returns and are aligned with the Client's. 

## The dataset
The dataset consists of Price of Houses in King County, Washington 
from sales **between May 2014 and May 2015** and was provided by [@neuefische](https://github.com/neuefische). 
Along with house price it consists of information on 18 house features, 
date of sale and ID of sale (see full description inside).

## Navigation
* [Data cleaning](cleaning.ipynb) 
* [Analysis](eda-notebook.ipynb)

>❗️**The notebooks will not run without the file `data/houses.csv`**. The dataset used here can be reconstructed from the 
> the [`house_data`](https://www.kaggle.com/datasets/arathipraj/house-data) 
> and [`house_sales`](https://www.kaggle.com/datasets/andykrause/kingcountysales) datasets on Kaggle - with a little bit of
> effort and no guarantee of reproducibility.

## Result summary

Nothing affects the price more than
* the proximity to Seattle downtown 
* the living area in the house.

Based on extensive data exploration, I suggest the following three objects: 

<img width="686" alt="image" src="https://github.com/eburakova/eda-kc-housing/assets/132762399/a4b4fcb9-3a20-4c88-8c6a-c7bff7786508">

|    |         id |   bedrooms |   bathrooms |   m2_living |   m2_lot |   floors |   waterfront |   view |   condition |   grade |   m2_above |   m2_basement |   yr_built |   yr_renovated |   zipcode |     lat |     long |   m2_living15 |   m2_lot15 | sale_date   |   price |   basement_share |   age |   yrs_since_renovation |   p_per_m2 |   dist_from_center | zone   |   poor_neighborhood_id |
|---:|-----------:|-----------:|------------:|------------:|---------:|---------:|-------------:|-------:|------------:|--------:|-----------:|--------------:|-----------:|---------------:|----------:|--------:|---------:|--------------:|-----------:|:------------|--------:|-----------------:|------:|-----------------------:|-----------:|-------------------:|:-------|-----------------------:|
| 69 | 2648500030 |          1 |           1 |     100.334 |  300.074 |        1 |            0 |      0 |           3 |       6 |    100.334 |        0      |       1963 |            nan |     98002 | 47.3075 | -122.217 |       112.412 |    535.117 | 2014-07-25  |  112000 |         0        |    52 |                    nan |     1116.3 |            61.3488 | rural  |                      0 |
| 24 | 2781250750 |          2 |           2 |     126.347 |  306.577 |        2 |            0 |      0 |           3 |       6 |    126.347 |        0      |       2004 |            nan |     98038 | 47.3489 | -122.022 |       121.702 |    306.577 | 2014-08-28  |  222000 |         0        |    11 |                    nan |     1757.1 |            53.9958 | rural  |                     13 |
| 91 | 5560000650 |          3 |           1 |     141.211 |  785.024 |        1 |            0 |      0 |           2 |       6 |    104.051 |       37.1609 |       1961 |            nan |     98023 | 47.328  | -122.337 |       122.631 |    785.024 | 2014-12-02  |  135000 |         0.263158 |    54 |                    nan |      956   |            57.5993 | rural  |                     20 |


----
# For development
## Setup the local environment

### **`macOS` or `Linux`**:

- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`Windows`**: 
- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
    ```
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
