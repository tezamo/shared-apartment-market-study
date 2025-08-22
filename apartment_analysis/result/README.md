# Regression Analysis and Reports
## Section 1: Factors Affecting Rental Prices
The purpose of this investigation is to determine the variables affecting Berlin, Germany's rental costs for apartments and shared flats (WG). Numerous studies have shown, as mentioned in the literature, that location, facilities, and other factors have a big impact on rental pricing. In order to achieve this, we took certain variables from the information gathered by web scraping from WG-Gesucht, such as room size, number of rooms (WG type), and location. Through basic data analysis, these factors were used to investigate their association with rental prices. The in-depth analysis and airport proximation analysis are carried out utilizing the Geopy module to assess different factors. For the basic analysis and the in-depth analysis and airport proximation analysis, OLS regression analyses were carried out. These studies' conclusions and interpretations are recorded in the corresponding Jupyter notebooks.


The equation for **simple analysis** as follows:

$$
Price = \alpha_0 + \alpha_1 \text{Size} + \alpha_2 \text{WG type} + \alpha_3 \text{Online Duration} + U
$$

where:
```
Price: The rental price in €.
Size : Size of the WG room in m².
WG type: Number of rooms in the WG
Online duration: The duration that WG ads are online in minutes
```

---
The equation for **extendedvars analysis** as follows:

$$
\begin{aligned}
Price = & \alpha_0 + \alpha_1 \text{Size} + \alpha_2 \text{WG type} + \alpha_3 \text{Online Duration} + \alpha_4 \text{Health Centers Proximity} \\
& + \alpha_5 \text{Low Crime Areas Proximity} + \alpha_6 \text{Berlin Hauptbahnhof Proximity} + \alpha_7 \text{Berlin Brandenburg Airport Proximity} + \alpha_8 \text{Cinemas Proximity} + U
\end{aligned}
$$


where:
```
Price: The rental price in €.
Size : Size of the WG room in m².
WG type: Number of rooms in the WG
Online duration: The duration that WG ads are online in minutes
Health Centers Proximityi: Dummy variable if the location of apartment is near to health centers in Berlin 1, otherwise 0.
Low-crime Areas Proximityt: Dummy variable if the location of apartment is near to low-crime areas un Berlin 1, otherwise 0.
Berlin Hauptbahnhof Proximityf: Dummy variable if the location of apartment is near to the Berlin Hauptbahnhof 1, otherwise 0.
Berlin Brandenburg Airport Proximity: Dummy variable if the location of apartment is near to the Berlin Brandenburg Airport 1, otherwise 0.
Cinemas Proximity: Dummy variable if the location of the apartment is near to cinemas 1, otherwise 0.
```
The equation for **airport_proximation_analysis** as follows:

$$
Price = \alpha_0 + \alpha_1 \text{Distance Category Very Close} + \alpha_2 \text{Distance Category Moderately Close} + \alpha_3 \text{Distance Category Very Far} + U
$$

---
## Section 2: Determinants of WG Listing Duration
In the second section, we used mostly the same variables to investigate the length of time an advertisement remains online. Here, the dependent variable was the duration in minutes. Additionally, the rental price was included as another influencing variable.

---
The equation for **simple analysis** as follows:

$$
\text{Online Duration} = \alpha_0 + \alpha_1 \text{Size} + \alpha_2 \text{WG type} + \alpha_3 \text{Price} + U
$$


where:
```
Online duration: The duration that WG ads are online in minutes
Size : Size of the WG room in m².
WG type: Number of rooms in the WG
Price: The rental price in €.
```
---

The equation for **extendedvars analysis** as follows:

$$
\begin{aligned}
\text{Online Duration} = & \alpha_0 + \alpha_1 \text{Size} + \alpha_2 \text{WG type} + \alpha_3 \text{Price} + \alpha_4 \text{Health Centers Proximity} \\
& + \alpha_5 \text{Low Crime Areas Proximity} + \alpha_6 \text{Berlin Hauptbahnhof Proximity} + \alpha_7 \text{Berlin Brandenburg Airport Proximity} + \alpha_8 \text{Cinemas Proximity} + U
\end{aligned}
$$



where:
```
Online duration: The duration that WG ads are online in minutes
Size : Size of the WG room in m².
WG type: Number of rooms in the WG
Price: The rental price in €.
Health Centers Proximityi: Dummy variable if the location of apartment is near to health centers in Berlin 1, otherwise 0.
Low-crime Areas Proximityt: Dummy variable if the location of apartment is near to low-crime areas un Berlin 1, otherwise 0.
Berlin Hauptbahnhof Proximityf: Dummy variable if the location of apartment is near to the Berlin Hauptbahnhof 1, otherwise 0.
Berlin Brandenburg Airport Proximity: Dummy variable if the location of apartment is near to the Berlin Brandenburg Airport 1, otherwise 0.
Cinemas Proximity: Dummy variable if the location of the apartment is near to cinemas 1, otherwise 0.
```
The results of the regressions can be found in `data_analysis.ipynb` , `MultiVarRegression.ipynb` and  `airport_proximation_analysis.ipynb` and CSV files in the `result` folder.
