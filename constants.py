from plotly.colors import qualitative

# If True, will pull data from sources' website, else use local data previously downloaded from same source.
use_remote = False

# Website title
title = "GEOL 320 - Sea-Level Rise in California"

# Plotly graph configuration options
config = {
    'displaylogo': False,
    'displayModeBar': False,
    # 'modeBarButtonsToRemove': ['zoom', 'pan', 'select', 'zoomIn', 'zoomOut', 'autoScale', 'resetScale'],
    'scrollZoom': True,
    # 'staticPlot': True,
}

# California tide gauge station names
name_cresc = 'Crescent City'
name_humbo = 'Humboldt Bay'
name_arena = 'Arena Cove'
name_reyes = 'Port Reyes'
name_sanfr = 'San Francisco'
name_portc = 'Port Chicago'
name_alame = 'Alameda'
name_redwo = 'Redwood City'
name_monte = 'Monterey'
name_ports = 'Port San Luis'
name_oilpl = 'Oil Platform'
name_santb = 'Santa Barbara'
name_santm = 'Santa Monica'
name_losan = 'Los Angeles'
name_lajol = 'La Jolla'
name_sandi = 'San Diego'

# California tide gauge station GPS coordinates
coord_cresc = [41.745, -124.183]
coord_humbo = [40.767, -124.217]
coord_arena = [38.913, -123.708]
coord_reyes = [37.995, -122.977]
coord_sanfr = [37.807, -122.465]
coord_portc = [38.055, -122.040]
coord_alame = [37.772, -122.299]
coord_redwo = [37.507, -122.212]
coord_monte = [36.605, -121.888]
coord_ports = [35.177, -120.760]
coord_oilpl = [34.468, -120.673]
coord_santb = [34.408, -119.685]
coord_santm = [34.008, -118.500]
coord_losan = [33.720, -118.272]
coord_lajol = [32.867, -117.257]
coord_sandi = [32.713, -117.173]

# CO2 concentration data sources
co2_data1 = "https://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/in_situ_co2/monthly/monthly_in_situ_co2_mlo.csv" if use_remote else "data/monthly_in_situ_co2_mlo.csv"
co2_data2 = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_gl.csv" if use_remote else "data/co2_mm_gl.csv"

# UHSLC tide gauge daily research quality data sources
uhslc_cresc = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d556a.csv" if use_remote else "data/d556a.csv"
uhslc_humbo = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d576a.csv" if use_remote else "data/d576a.csv"
uhslc_arena = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d573a.csv" if use_remote else "data/d573a.csv"
uhslc_sanfr = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d551a.csv" if use_remote else "data/d551a.csv"
uhslc_monte = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d555a.csv" if use_remote else "data/d555a.csv"
uhslc_ports = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d565a.csv" if use_remote else "data/d565a.csv"
uhslc_oilpl = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d594a.csv" if use_remote else "data/d594a.csv"
uhslc_santb = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d577a.csv" if use_remote else "data/d577a.csv"
uhslc_santm = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d578a.csv" if use_remote else "data/d578a.csv"
uhslc_losan = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d567a.csv" if use_remote else "data/d567a.csv"
uhslc_lajol = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d554a.csv" if use_remote else "data/d554a.csv"
uhslc_sandi = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d569a.csv" if use_remote else "data/d569a.csv"

# PSMSL tide gauge monthly data sources
psmsl_cresc_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/378.rlrdata"  if use_remote else "data/378.rlrdata"
psmsl_humbo_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/1639.rlrdata" if use_remote else "data/1639.rlrdata"
psmsl_arena_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/2125.rlrdata" if use_remote else "data/2125.rlrdata"
psmsl_reyes_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/1394.rlrdata" if use_remote else "data/1394.rlrdata"
psmsl_sanfr_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/10.rlrdata"   if use_remote else "data/10.rlrdata"
psmsl_portc_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/2330.rlrdata" if use_remote else "data/2330.rlrdata"
psmsl_alame_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/437.rlrdata"  if use_remote else "data/437.rlrdata"
psmsl_redwo_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/2329.rlrdata" if use_remote else "data/2329.rlrdata"
psmsl_monte_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/1352.rlrdata" if use_remote else "data/1352.rlrdata"
psmsl_ports_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/508.rlrdata"  if use_remote else "data/508.rlrdata"
psmsl_santb_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/2126.rlrdata" if use_remote else "data/2126.rlrdata"
psmsl_santm_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/377.rlrdata"  if use_remote else "data/377.rlrdata"
psmsl_losan_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/245.rlrdata"  if use_remote else "data/245.rlrdata"
psmsl_lajol_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/256.rlrdata"  if use_remote else "data/256.rlrdata"
psmsl_sandi_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/158.rlrdata"  if use_remote else "data/158.rlrdata"

# PSMSL tide gauge annual data sources
psmsl_cresc_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/378.rlrdata"  if use_remote else "data/378a.rlrdata"
psmsl_humbo_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/1639.rlrdata" if use_remote else "data/1639a.rlrdata"
psmsl_arena_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/2125.rlrdata" if use_remote else "data/2125a.rlrdata"
psmsl_reyes_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/1394.rlrdata" if use_remote else "data/1394a.rlrdata"
psmsl_sanfr_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/10.rlrdata"   if use_remote else "data/10a.rlrdata"
psmsl_portc_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/2330.rlrdata" if use_remote else "data/2330a.rlrdata"
psmsl_alame_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/437.rlrdata"  if use_remote else "data/437a.rlrdata"
psmsl_redwo_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/2329.rlrdata" if use_remote else "data/2329a.rlrdata"
psmsl_monte_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/1352.rlrdata" if use_remote else "data/1352a.rlrdata"
psmsl_ports_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/508.rlrdata"  if use_remote else "data/508a.rlrdata"
psmsl_santb_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/2126.rlrdata" if use_remote else "data/2126a.rlrdata"
psmsl_santm_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/377.rlrdata"  if use_remote else "data/377a.rlrdata"
psmsl_losan_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/245.rlrdata"  if use_remote else "data/245a.rlrdata"
psmsl_lajol_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/256.rlrdata"  if use_remote else "data/256a.rlrdata"
psmsl_sandi_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/158.rlrdata"  if use_remote else "data/158a.rlrdata"

# List of UHSLC data and information
uhslc_list = [
    # id, name,       daily,       [lat, lon]]
    [556, name_cresc, uhslc_cresc, coord_cresc],
    [576, name_humbo, uhslc_humbo, coord_humbo],
    [573, name_arena, uhslc_arena, coord_arena],
    [551, name_sanfr, uhslc_sanfr, coord_sanfr],
    [555, name_monte, uhslc_monte, coord_monte],
    [565, name_ports, uhslc_ports, coord_ports],
    [594, name_oilpl, uhslc_oilpl, coord_oilpl],
    [577, name_santb, uhslc_santb, coord_santb],
    [578, name_santm, uhslc_santm, coord_santm],
    [567, name_losan, uhslc_losan, coord_losan],
    [554, name_lajol, uhslc_lajol, coord_lajol],
    [569, name_sandi, uhslc_sandi, coord_sandi]
]

# List of PSMSL data and information
psmsl_list = [
    # id,  name,       monthly,         annual,          [lat, lon]
    [378,  name_cresc, psmsl_cresc_mon, psmsl_cresc_ann, coord_cresc],
    [1639, name_humbo, psmsl_humbo_mon, psmsl_humbo_ann, coord_humbo],
    [2125, name_arena, psmsl_arena_mon, psmsl_arena_ann, coord_arena],
    [1394, name_reyes, psmsl_reyes_mon, psmsl_reyes_ann, coord_reyes],
    [10,   name_sanfr, psmsl_sanfr_mon, psmsl_sanfr_ann, coord_sanfr],
    [2330, name_portc, psmsl_portc_mon, psmsl_portc_ann, coord_portc],
    [437,  name_alame, psmsl_alame_mon, psmsl_alame_ann, coord_alame],
    [2329, name_redwo, psmsl_redwo_mon, psmsl_redwo_ann, coord_redwo],
    [1352, name_monte, psmsl_monte_mon, psmsl_monte_ann, coord_monte],
    [508,  name_ports, psmsl_ports_mon, psmsl_ports_ann, coord_ports],
    [2126, name_santb, psmsl_santb_mon, psmsl_santb_ann, coord_santb],
    [377,  name_santm, psmsl_santm_mon, psmsl_santm_ann, coord_santm],
    [245,  name_losan, psmsl_losan_mon, psmsl_losan_ann, coord_losan],
    [256,  name_lajol, psmsl_lajol_mon, psmsl_lajol_ann, coord_lajol],
    [158,  name_sandi, psmsl_sandi_mon, psmsl_sandi_ann, coord_sandi]
]

# Assigning each location its own color, so it can be uniform across different plots.
# Dash color sequences viewable at https://plotly.com/python/discrete-color/
colors = {
    name_cresc: qualitative.Light24[0],
    name_humbo: qualitative.Light24[1],
    name_arena: qualitative.Light24[2],
    name_reyes: qualitative.Light24[3],
    name_sanfr: qualitative.Light24[4],
    name_portc: qualitative.Light24[5],
    name_alame: qualitative.Light24[6],
    name_redwo: qualitative.Light24[7],
    name_monte: qualitative.Light24[8],
    name_ports: qualitative.Light24[9],
    name_oilpl: qualitative.Light24[10],
    name_santb: qualitative.Light24[11],
    name_santm: qualitative.Light24[12],
    name_losan: qualitative.Light24[13],
    name_lajol: qualitative.Light24[14],
    name_sandi: qualitative.Light24[16]
}
