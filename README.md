<center><img src="https://www.invest4land.com/wp-content/uploads/2021/05/Invest4Land-Investment-Agricultural-Real-Estate-Agroforestry-Secondary-Income-Generation-Eggs-Livestock-Farmlands-Investment-Agriculture-0-1.jpg" height="400"/></center>

# **Exploratory data analysis of socially responsible investment opportunities into real estate of King County (WA, USA)**
The names and personalities below are fictional.

[<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>](https://colab.research.google.com/github/eburakova/eda-kc-housing/blob/main/eda_notebook.ipynb)


### ❗️👷🏼‍♂️ Under construction ( |||||||||||------| 80% )
## The challenge
Ms. Erin Robinson - The Client of Nova Piscibus Consulting GmbH - is a socially responsible investor in the real estate. She wishes to improve living conditions in King County (WA, USA) by investing into the development of poor neighborhoods. 
Our goal at Nova Piscibus is to determing the factors that affect potential returns and are aligned with the Client's. 

## The dataset
The dataset consists of Price of Houses in King County, Washington 
from sales **between May 2014 and May 2015** and was provided by [@neuefische](https://github.com/neuefische). 
Along with house price it consists of information on 18 house features, 
date of sale and ID of sale (see full description inside).

The present dataset is based on the [`house_data`](https://www.kaggle.com/datasets/arathipraj/house-data) 
and [`house_sales`](https://www.kaggle.com/datasets/andykrause/kingcountysales) datasets on Kaggle.

## Result summary

|High risk / high reward | Conservative |
|---|---|
|Central houses in bad condition. They may be still expensive, they would require a lot of resources to renovate. However, there is a large potential for price increase. 	| Houses on the outskirts in average condition. Only minor renovations would be needed (rather, construction works), but the price will never be comparable to the central houses |
| White center, Rainer Valley and generally the area around the Boeing Field seems in the most dire need of improvement! | A few objects in Carnation and the houses in Fall City can be interest.  |
| Areas in the north (like Maple Leaf and Lake City) can form a secondary interest. ||

## Setup the local environment

### **`macOS`** type the following commands : 

- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :

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
