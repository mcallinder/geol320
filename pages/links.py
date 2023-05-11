from constants import title
from dash import html, dcc, register_page

register_page(__name__, title=f'{title} - Links')

layout = html.Div([
    html.H3('Links to Information and Data Sources'),
    html.Hr(style={'margin': '32px 0'}),
    dcc.Markdown('''
        #### Project Specific
         - [Source Code](https://github.com/mcallinder?tab=repositories) - GitHub repositories for web application and notebooks
        ##### Jupyter Notebooks
        ###### Notebook Viewers:
        - [nbviewer](https://nbviewer.org/github/mcallinder/notebooks/) - Static Notebook viewer
        - [binder](https://mybinder.org/v2/gh/mcallinder/notebooks/HEAD) - Dynamic Notebook viewer
        ###### Static HTML Pages: (Backup in case viewers above don't work)
        - [Tide gauges along California](http://mcallinder.com/notebook_sealevel_ca.html)
        - [CO2 concentrations](http://mcallinder.com/notebook_co2.html)
        #### Journal Articles
        - [20th to 21st Century Relative Sea and Land Level Changes in Northern California](https://tektonika.online/index.php/home/article/view/6)
        - [Assessing Potential Links between Climate Variability and Sea Levels along the Coasts of North America](https://www.mdpi.com/2225-1154/11/4/80/htm)
        - [Dynamic flood modeling essential to assess the coastal impacts of climate change](https://www.nature.com/articles/s41598-019-40742-z/)
        - [Reading between the tides: 200 years of measuring global sea level](https://www.climate.gov/news-features/climate-tech/reading-between-tides-200-years-measuring-global-sea-level)
        #### Other Useful Information
        ###### CA Sea-Level Rise Guidance and Action Plans:
        - [California Coastal Commission - Sea Level Rise](https://www.coastal.ca.gov/climate/slr/)
        - [City of San Francisco - Sea Level Rise Adaptation](https://sfplanning.org/sea-level-rise-action-plan#info)
        - [Delta Stewardship Council - Climate Change](https://deltacouncil.ca.gov/delta-plan/climate-change)
        - [California Ocean Protection Council](https://www.opc.ca.gov/)
            - [Rising Seas in California: An Update On Sea-Level Rise Science](https://www.opc.ca.gov/webmaster/ftp/pdf/docs/rising-seas-in-california-an-update-on-sea-level-rise-science.pdf) - PDF, 2017
            - [State of California Sea-Level Rise Guidance](https://www.opc.ca.gov/webmaster/ftp/pdf/agenda_items/20180314/Item3_Exhibit-A_OPC_SLR_Guidance-rd3.pdf) - PDF, 2018
        ###### Other:
        - [SeaLevelRise.org - California](https://sealevelrise.org/states/california/)
        - [Pacific Institute - The Impacts of Sea-Level Rise on the California Coast](https://pacinst.org/publication/the-impacts-of-sea-level-rise-on-the-california-coast/) - 2009
        - [CA Legislative Analyst's Office - What Threat Does Sea-Level Rise Pose to California?](https://lao.ca.gov/Publications/Report/4261) - 2020
        - [California's Fourth Climate Change Assessment](https://www.climateassessment.ca.gov/)
            - [California's Coast and Ocean Summary Report](https://www.energy.ca.gov/sites/default/files/2019-11/Statewide_Reports-SUM-CCCA4-2018-011_OceanCoastSummary_ADA.pdf) - PDF, 2018
        - [NOAA Office For Coastal Management - California](https://coast.noaa.gov/states/california.html)
            - [National Coastal Population Report: Population Trends from 1970 to 2020](https://aambpublicoceanservice.blob.core.windows.net/oceanserviceprod/facts/coastal-population-report.pdf) - 2013
        #### Tide Gauge Data
        - [Permanent Service for Mean Sea Level (PSMSL)]()
            - [Crescent City Data](https://psmsl.org/data/obtaining/stations/378.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/378.php)
            - [Humboldt Bay Data](https://psmsl.org/data/obtaining/stations/1639.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/1639.php)
            - [Arena Cove Data](https://psmsl.org/data/obtaining/stations/2125.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/2125.php)
            - [Point Reyes Data](https://psmsl.org/data/obtaining/stations/1394.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/1394.php)
            - [San Fransisco Data](https://psmsl.org/data/obtaining/stations/10.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/10.php)
            - [Port Chicago Data](https://psmsl.org/data/obtaining/stations/2330.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/2330.php)
            - [Alameda Data](https://psmsl.org/data/obtaining/stations/437.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/437.php)
            - [Redwood City Data](https://psmsl.org/data/obtaining/stations/2329.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/2329.php)
            - [Monterey Data](https://psmsl.org/data/obtaining/stations/1352.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/1352.php)
            - [Port San Luis Data](https://psmsl.org/data/obtaining/stations/508.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/508.php)
            - [Santa Barbara Data](https://psmsl.org/data/obtaining/stations/2126.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/2126.php)
            - [Santa Monica Data](https://psmsl.org/data/obtaining/stations/377.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/377.php)
            - [Los Angeles Data](https://psmsl.org/data/obtaining/stations/245.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/245.php)
            - [La Jolla Data](https://psmsl.org/data/obtaining/stations/256.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/256.php)
            - [San Diego Data](https://psmsl.org/data/obtaining/stations/158.php) - [Revised Local Reference and Datum Info](https://psmsl.org/data/obtaining/rlr.diagrams/158.php)
        - [University of Hawaii Sea Level Center (UHSLC)](https://uhslc.soest.hawaii.edu/)
        - [UHSLC Research Quality Data Portal](https://uhslc.soest.hawaii.edu/data/?rq)
            - [Crescent City Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa556a.dmt)
            - [Humboldt Bay Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa576a.dmt)
            - [Arena Cove Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa573a.dmt)
            - [San Francisco Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa551a.dmt)
            - [Monterey Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa555a.dmt)
            - [Port San Luis Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa565a.dmt)
            - [Oil Platform Harvest Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa594a.dmt)
            - [Santa Barbara Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa577a.dmt)
            - [Santa Monica Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa578a.dmt)
            - [Los Angeles Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa567a.dmt)
            - [La Jolla Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa554a.dmt)
            - [San Diego Data Meta](https://uhslc.soest.hawaii.edu/rqds/pacific/doc/qa569a.dmt)
        - [Global Sea Level Observing System (GLOSS)](https://gloss-sealevel.org/)
        - [GLOSS Station Handbook](https://gloss-sealevel.org/gloss-station-handbook) - See GLOSS number: 158 for SF, 159 for La Jolla
        - [National Ocean Service - Tide and Water Levels](https://oceanservice.noaa.gov/education/tutorial_tides/tides11_newmeasure.html) - Overview of the newer tide measuring system.
        - [NOAA's Next Generation Tide Gauges](https://psmsl.org/train_and_info/training/gloss/gb/gb1/noaa.html) - PSMSL Training Document
        - [NOAA Tide & Current Stations](https://tidesandcurrents.noaa.gov/map/index.html?type=active&region=California) - California Region
        #### CO2 Concentration Data
        - [Scripps CO2 Program - Primary Mauna Loa CO2 Record](https://scrippsco2.ucsd.edu/data/atmospheric_co2/primary_mlo_co2_record.html)
        - [NOAA Global Monitoring Laboratory Trends in Atmospheric Carbon Dioxide - Muana Loa](https://gml.noaa.gov/ccgg/trends/mlo.html)
        #### Technologies Used
        ##### Languages
        - [Python](https://www.python.org/) - Version 3.11.2, used as the primary programming language
        - [Markdown](https://www.markdownguide.org/) - Simple markup language used to add formatting to plain text
        - [HTML](https://html.spec.whatwg.org/multipage/) - HyperText Markup Language, used to structure webpages
        - [CSS](https://www.w3.org/Style/CSS/) - Cascading Style Sheets, used to style webpages
        ##### Libraries
        - [Plotly](https://plotly.com/python/) - Data visualization
        - [Pandas](https://pandas.pydata.org/) - Data analysis and manipulation
        - [Statsmodels](https://www.statsmodels.org/stable/index.html) - Statistical modeling
        ##### Web App
        - [Dash](https://dash.plotly.com/) - Web framework meets dashboard from Plotly, built on Flask 
        - [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) - A third party component library
        - [Digital Ocean](https://www.digitalocean.com/) - Hosting Service
        ##### Other Tools
        - [Git](https://git-scm.com/) - A version control system
        - [Github](https://github.com/) - A software development service built around Git
        - [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE from JetBrains
    ''', link_target="_blank", className="markdown links")
])
