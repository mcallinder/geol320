import dash
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div([
    html.H3('Links to Information and Data Sources'),
    html.Hr(),
    dcc.Markdown('''
    #### Journal Articles

    - 20th to 21st Century Relative Sea and Land Level Changes in Northern California
    - Assessing Potential Links between Climate Variability and Sea Levels along the Coasts of North America
    - Dynamic flood modeling essential to assess the coastal impacts of climate change
    - Reading between the tides: 200 years of measuring global sea level

    #### Other Useful Information

    - SeaLevelRise.org - California
    - California Coastal Commission - Sea Level Rise

    - City of San Francisco - Sea Level Rise Adaptation
    - Delta Stewardship Council - Climate Change

    - California Ocean Protection Council
        - Rising Seas in California: An Update On Sea-Level Rise Science - PDF, 2017
        - State of California Sea-Level Rise Guidance - PDF, 2018

    - California's Fourth Climate Change Assessment
        - California's Coast and Ocean Summary Report - PDF, 2018

    - NOAA Office For Coastal Management - California
        - National Coastal Population Report: Population Trends from 1970 to 2020 - 2013

    - Pacific Institute - The Impacts of Sea-Level Rise on the California Coast - 2009
    - CA Legislative Analyst's Office - What Threat Does Sea-Level Rise Pose to California? - 2020

    #### Tide Gauge Data

    - University of Hawaii Sea Level Center (UHSLC)
    - UHSLC Research Quality Data Portal
        - Crescent City Data Meta
        - San Francisco Data Meta
        - Los Angeles Data Meta
        - La Jolla Data Meta

    - Permanent Service for Mean Sea Level (PSMSL)
        - Crescent City Data  -  Revised Local Reference and Datum Info
        - North Spit Data  -  Revised Local Reference and Datum Info
        - San Fransisco Data  -  Revised Local Reference and Datum Info
        - Port Chicago Data  -  Revised Local Reference and Datum Info
        - Los Angeles Data  -  Revised Local Reference and Datum Info
        - La Jolla Data  -  Revised Local Reference and Datum Info

    - Global Sea Level Observing System (GLOSS)
    - GLOSS Station Handbook - See GLOSS number: 158 for SF, 159 for La Jolla

    - National Ocean Service - Tide and Water Levels - Overview of the newer tide measuring system.
    - NOAA's Next Generation Tide Gauges - PSMSL Training Document
    - NOAA Tide & Current Stations - California Region

    #### CO2 Concentration Data

    - Scripps CO2 Program - Primary Mauna Loa CO2 Record
    - NOAA Global Monitoring Laboratory Trends in Atmospheric Carbon Dioxide - Muana Loa
    - NOAA Global Monitoring Laboratory Data Finder

    #### Global Temperature Anomaly Data

    - NASA GISS Surface Temperature Analysis

    ''')
])
