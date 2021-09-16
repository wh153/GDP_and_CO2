import pandas as pd
import matplotlib.pyplot as plt

mortality = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
a = mortality[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

plt.scatter(
    a["GDP per capita (constant 2010 US$)"],
    a["Mortality rate, infant (per 1,000 live births)"],
    alpha=0.5,
)
plt.show()

# For excercise with Nansu
