# Urban Rental Price Analysis:  
***Berlin’s WG-Gesucht Market***  

## **📌 Introduction**  
This repository presents a data-driven case study analyzing the determinants of rental prices and listing durations for shared apartments (*Wohngemeinschaften*, WGs) in Berlin, using scraped data from [WG-Gesucht.de](https://www.wg-gesucht.de/). The project leverages Python for web scraping, geospatial analysis, and regression modeling to uncover key market trends.  

**Key Objectives**:  
1. **Price Determinants**: Identify factors (e.g., size, location, amenities) influencing WG rental prices.  
2. **Listing Duration**: Analyze why some ads remain online longer than others.  

---

## **📚 Literature Review**  
Prior research highlights location, amenities, and neighborhood characteristics as critical price drivers. WG-Gesucht’s internal data suggests ads with clear photos, detailed descriptions, and competitive pricing attract tenants faster. This study tests these hypotheses empirically.  

---

## **⚙️ Methodology**  
### **1. Data Collection**  
- **Scraping Tool**: Python script (`scraper.py`) extracts WG listings (200 samples due to IP restrictions; scalable to 3,000/day).  
- **Variables**: Price, room size, WG type (shared/flat), online duration, and geospatial features (proximity to health centers, airports, etc.).  

### **2. Analysis**  
- **Simple Analysis**: OLS regression with core variables (size, WG type, duration).  
- **In-Depth Analysis**: Enhanced with geospatial dummy variables (e.g., low-crime areas, transport hubs).  
- **Airport Proximity**: Categorized distance impact on prices.  

**Regression Models**:  
#### **Price Determinants**  
**Simple**:  

$$  
Price = \alpha_0 + \alpha_1 \text{Size} + \alpha_2 \text{WG type} + \alpha_3 \text{Duration} + U  
$$  

**In-Depth**:  

$$  
Price = \alpha_0 + \sum_{i=1}^8 \alpha_i X_i + U  
$$  

*(See full equation in [Results](#-results))*  

#### **Listing Duration**  
**Simple**:  

$$  
\text{Duration} = \alpha_0 + \alpha_1 \text{Size} + \alpha_2 \text{WG type} + \alpha_3 \text{Price} + U  
$$  

---

## **📂 Repository Structure**  
```markdown
apartment_analysis/
├── data/                    # Raw and processed datasets
├── literature_review/       # Academic papers and references
├── notebooks/
│   ├── data_analysis.ipynb  # Core regression analysis
│   └── in_depth_analysis.ipynb  # Geospatial modeling
├── scraper.py               # Web scraping script
├── results/
│   ├── regression_results.csv  # Regression outputs
│   └── visualizations/      # Graphs and charts
└── README.md                # Project overview
```

---

## **📊 Results**  
### **Key Findings**  
1. **Price Drivers**:  
   - **Size**: +€X per m² (*p < 0.01*).  
   - **Location**: Proximity to Hauptbahnhof ↑ prices by Y%.  
   - **Airport**: Ads near airport ↓ duration by Z days.  

2. **Listing Duration**:  
   - Higher-priced WGs stay online longer (*p < 0.05*).  
   - Ads near cinemas/health centers rent faster.  

**Limitations**:  
- Sample size constraints due to scraping limits.  
- Geospatial proxies (e.g., "low-crime") may not capture granularity.  

Full results in [`results/README.md`](./results/README.md) and Jupyter notebooks.  

---

## **🚀 How to Reproduce**  
1. **Scrape Data**: Run `scraper.py` (adjust `max_ads` in code).  
2. **Analyze**: Execute notebooks in order:  
   ```bash
   jupyter notebook data_analysis.ipynb
   ```  
3. **Dependencies**: See `requirements.txt` for Python libraries.  

---

## **💡 Ethical Considerations**  
- **Data Use**: WG-Gesucht’s [robots.txt](https://www.wg-gesucht.de/robots.txt) permits scraping for research.  
- **Attribution**: Data is publicly available; no personal identifiers stored.  

---

**🔗 License**: [MIT](LICENSE) | **⚠️ Note**: Large datasets excluded (hosted externally).  

--- 
**📌 Copyright & Code Usage:**

© 2025 tezamo. All rights reserved.

The source code in this repository is provided for educational purposes as part of my coursework.
You may view and reference the code, but copying, modifying, or redistributing it in any form without explicit permission is prohibited.

If you wish to reuse any part of the code, please contact me to request permission.

---  

[![pages-build-deployment](https://github.com/tezamo/shared-apartment-market-study/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/tezamo/shared-apartment-market-study/actions/workflows/pages/pages-build-deployment)
[![contributors](https://img.shields.io/github/contributors/tezamo/shared-apartment-market-study.svg)](https://github.com/tezamo/shared-apartment-market-study/graphs/contributors)
[![GitHub release](https://img.shields.io/github/v/release/tezamo/shared-apartment-market-study.svg)](https://GitHub.com/tezamo/shared-apartment-market-study/releases/)
[![GitHub license](https://img.shields.io/github/license/tezamo/shared-apartment-market-study.svg)](https://github.com/tezamo/shared-apartment-market-study/blob/main/LICENSE)
