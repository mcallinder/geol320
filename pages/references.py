from constants import title
from dash import dcc, html, register_page

register_page(__name__, title=f'{title} - References')

layout = html.Div([
    html.H3('References and Data Sources'),
    html.Hr(style={'margin-top': '32px'}),
    dcc.Markdown('''
        #### GEOL 320 Project
        
        Caldwell, P. C., Merrifield, M. A., & Thompson, P. R. (2015). *Sea level measured by tide gauges from global oceans — the Joint Archive for Sea Level holdings* (NCEI Accession 0019568, Version 5.5) Dataset. NOAA National Centers for Environmental Information. https://doi.org/10.7289/V5V40S7W.
        
        Keeling, C. D., Piper, S. C., Bacastow, R. B., Wahlen, M., Whorf, T. P., Heimann, M., & Meijer, H. A. (2001). Exchanges of atmospheric CO2 and 13CO2 with the terrestrial biosphere and oceans from 1978 to 2000 Dataset. Scripps Institution of Oceanography. Retrieved 2023 from https://scrippsco2.ucsd.edu/data/atmospheric_co2/primary_mlo_co2_record.html
        
        Lan, X., Tans, P., & Thoning, K.W. (2023). *Trends in globally-averaged CO2 determined from NOAA Global Monitoring Laboratory measurements* (Version 2023-04) Dataset. https://doi.org/10.15138/9N0H-ZH07
        
        Permanent Service for Mean Sea Level (PSMSL) (2023). Tide Gauge Data Dataset. Retrieved 2023 from http://www.psmsl.org/data/obtaining/
        
        #### GEOL 330 Paper
        
        Barnard, P. L., Erikson, L. H., Foxgrover, A. C., Finzi Hart, J. A., Limber, P. W., O'Neill, A. C., . . . Jones, J. M. (2019). Dynamic flood modeling essential to assess the coastal impacts of climate change. *Scientific Reports* (9), 4309. https://doi.org/10.1038/s41598-019-40742-z
        
        Caldwell, P. C., Merrifield, M. A., & Thompson, P. R. (2015). *Sea level measured by tide gauges from global oceans — the Joint Archive for Sea Level holdings* (NCEI Accession 0019568, Version 5.5) Dataset. NOAA National Centers for Environmental Information. https://doi.org/10.7289/V5V40S7W
        
        *California*. (n.d.). Office For Coastal Management. Retrieved from https://coast.noaa.gov/states/california.html
        
        City and County of San Francisco. (2016). *San Francisco Sea Level Rise Action Plan*. Retrieved from San Francisco Planning: https://sfplanning.org/sea-level-rise-action-plan
        
        Dusto, A. (2014, August 4). *Reading between the tides: 200 years of measuring global sea level*. Climate.gov. Retrieved from https://www.climate.gov/news-features/climate-tech/reading-between-tides-200-years-measuring-global-sea-level
        
        Ehlers, R. (2020, August 10). *What Threat Does Sea-Level Rise Pose to California?* California Legislative Analyst's Office. Retrieved from https://lao.ca.gov/Publications/Report/4261
        
        Giovannettone, J., Paredes-Trejo, F., Amaro, V. E., & Santos, C. A. (2023). Assessing Potential Links between Climate Variability and Sea Levels along the Coasts of North America. *Climate*, 11(4), 80. https://doi.org/10.3390/cli11040080
        
        Griggs, G., Árvai, J., DeConto, R., Fox, J., Fricker, H. A., Kopp, R. E., . . . Whiteman, L. (2017). *Rising Seas in California: An Update on Sea-Level Rise Science. California Ocean Science Trust, April 2017*. California Ocean Protection Council Science Advisory Team Working Group. Retrieved from https://www.opc.ca.gov/webmaster/ftp/pdf/docs/rising-seas-in-california-an-update-on-sea-level-rise-science.pdf
        
        NOAA. (2013). *National Coastal Population Report: Population Trends from 1970 to 2020*. Retrieved from https://coast.noaa.gov/digitalcoast/training/population-report.html
        
        Patton, J. R., Williams, T. B., Anderson, J. K., Hemphill-Haley, M., J.Burgette, R., II, R. W., . . . Leroy, T. H. (2023). 20th to 21st Century Relative Sea and Land Level Changes in Northern California. *Tektonika*. https://doi.org/10.55575/tektonika2023.1.1.6 
        
        Permanent Service for Mean Sea Level (PSMSL). (2023). *Tide Gauge Data* Dataset. Retrieved 2023 from http://www.psmsl.org/data/obtaining/

        Sea-Level Rise Leadership Team. (2022). *State Agency Sea-Level Rise Action Plan For California*. Ocean Protection Council. Retrieved from https://www.opc.ca.gov/webmaster/_media_library/2022/08/SLR-Action-Plan-2022-508.pdf
    ''', link_target="_blank", className="markdown ref")
])
