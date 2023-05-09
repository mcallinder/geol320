from plotly.colors import qualitative

use_remote = False

colors = {
    'Crescent City' : qualitative.Light24[0],
    'Humboldt Bay'  : qualitative.Light24[1],
    'Arena Cove'    : qualitative.Light24[2],
    'Port Reyes'    : qualitative.Light24[3],
    'San Francisco' : qualitative.Light24[4],
    'Port Chicago'  : qualitative.Light24[5],
    'Alameda'       : qualitative.Light24[6],
    'Redwood City'  : qualitative.Light24[7],
    'Monterey'      : qualitative.Light24[8],
    'Port San Luis' : qualitative.Light24[9],
    'Santa Barbara' : qualitative.Light24[10],
    'Santa Monica'  : qualitative.Light24[11],
    'Los Angeles'   : qualitative.Light24[12],
    'La Jolla'      : qualitative.Light24[13],
    'San Diego'     : qualitative.Light24[14],
    'Oil Platform'  : qualitative.Light24[16]
}

# CO2 concentration data
co2_data1 = "https://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/in_situ_co2/monthly/monthly_in_situ_co2_mlo.csv" if use_remote else "data/monthly_in_situ_co2_mlo.csv"
co2_data2 = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_gl.csv" if use_remote else "data/co2_mm_gl.csv"

# UHSLC daily tide gauge research quality data
uhslc_cresc = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d556a.csv" if use_remote else "data/d556a.csv"
uhslc_humbo = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d576a.csv" if use_remote else "data/d576a.csv"
uhslc_arena = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d573a.csv" if use_remote else "data/d573a.csv"
uhslc_sanfr = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d551a.csv" if use_remote else "data/d551a.csv"
uhslc_monte = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d555a.csv" if use_remote else "data/d555a.csv"
uhslc_ports = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d565a.csv" if use_remote else "data/d565a.csv"
uhslc_losan = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d567a.csv" if use_remote else "data/d567a.csv"
uhslc_santm = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d578a.csv" if use_remote else "data/d578a.csv"
uhslc_santb = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d577a.csv" if use_remote else "data/d577a.csv"
uhslc_lajol = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d554a.csv" if use_remote else "data/d554a.csv"
uhslc_sandi = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d569a.csv" if use_remote else "data/d569a.csv"
uhslc_oilpl = "https://uhslc.soest.hawaii.edu/data/csv/rqds/pacific/daily/d594a.csv" if use_remote else "data/d594a.csv"

uhslc_list = [
    # id, location,         daily,          [latitude, longitude]
    [556, 'Crescent City',  uhslc_cresc,    [41.74500, -124.18300]],
    [576, 'Humboldt Bay',   uhslc_humbo,    [40.76700, -124.21700]],
    [573, 'Arena Cove',     uhslc_arena,    [38.91300, -123.70800]],
    [551, 'San Francisco',  uhslc_sanfr,    [37.80700, -122.46500]],
    [555, 'Monterey',       uhslc_monte,    [36.60500, -121.88800]],
    [565, 'Port San Luis',  uhslc_ports,    [35.17700, -120.76000]],
    [594, 'Oil Platform',   uhslc_oilpl,    [34.46800, -120.67300]],
    [577, 'Santa Barbara',  uhslc_santb,    [34.40800, -119.68500]],
    [578, 'Santa Monica',   uhslc_santm,    [34.00800, -118.50000]],
    [567, 'Los Angeles',    uhslc_losan,    [33.72000, -118.27200]],
    [554, 'La Jolla',       uhslc_lajol,    [32.86700, -117.25700]],
    [569, 'San Diego',      uhslc_sandi,    [32.71300, -117.17300]]
]

# PSMSL monthly tide gauge research quality data
psmsl_cresc_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/378.rlrdata" if use_remote else "data/378.rlrdata"
psmsl_humbo_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/1639.rlrdata" if use_remote else "data/1639.rlrdata"
psmsl_arena_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/2125.rlrdata" if use_remote else "data/2125.rlrdata"
psmsl_reyes_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/1394.rlrdata" if use_remote else "data/1394.rlrdata"
psmsl_sanfr_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/10.rlrdata" if use_remote else "data/10.rlrdata"
psmsl_portc_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/2330.rlrdata" if use_remote else "data/2330.rlrdata"
psmsl_alame_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/437.rlrdata" if use_remote else "data/437.rlrdata"
psmsl_redwo_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/2329.rlrdata" if use_remote else "data/2329.rlrdata"
psmsl_monte_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/1352.rlrdata" if use_remote else "data/1352.rlrdata"
psmsl_ports_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/508.rlrdata" if use_remote else "data/508.rlrdata"
psmsl_santb_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/2126.rlrdata" if use_remote else "data/2126.rlrdata"
psmsl_santm_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/377.rlrdata" if use_remote else "data/377.rlrdata"
psmsl_losan_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/245.rlrdata" if use_remote else "data/245.rlrdata"
psmsl_lajol_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/256.rlrdata" if use_remote else "data/256.rlrdata"
psmsl_sandi_mon = "https://psmsl.org/data/obtaining/rlr.monthly.data/158.rlrdata" if use_remote else "data/158.rlrdata"

# PSMSL annual tide gauge research quality data
psmsl_cresc_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/378.rlrdata" if use_remote else "data/378a.rlrdata"
psmsl_humbo_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/1639.rlrdata" if use_remote else "data/1639a.rlrdata"
psmsl_arena_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/2125.rlrdata" if use_remote else "data/2125a.rlrdata"
psmsl_reyes_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/1394.rlrdata" if use_remote else "data/1394a.rlrdata"
psmsl_sanfr_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/10.rlrdata" if use_remote else "data/10a.rlrdata"
psmsl_portc_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/2330.rlrdata" if use_remote else "data/2330a.rlrdata"
psmsl_alame_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/437.rlrdata" if use_remote else "data/437a.rlrdata"
psmsl_redwo_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/2329.rlrdata" if use_remote else "data/2329a.rlrdata"
psmsl_monte_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/1352.rlrdata" if use_remote else "data/1352a.rlrdata"
psmsl_ports_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/508.rlrdata" if use_remote else "data/508a.rlrdata"
psmsl_santb_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/2126.rlrdata" if use_remote else "data/2126a.rlrdata"
psmsl_santm_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/377.rlrdata" if use_remote else "data/377a.rlrdata"
psmsl_losan_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/245.rlrdata" if use_remote else "data/245a.rlrdata"
psmsl_lajol_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/256.rlrdata" if use_remote else "data/256a.rlrdata"
psmsl_sandi_ann = "https://psmsl.org/data/obtaining/rlr.annual.data/158.rlrdata" if use_remote else "data/158a.rlrdata"

psmsl_list = [
    # id,   location,         monthly,          annual,           [latitude, longitude]
    [378,   'Crescent City',  psmsl_cresc_mon,  psmsl_cresc_ann,  [41.745, -124.181667]],
    [1639,  'Humboldt Bay',   psmsl_humbo_mon,  psmsl_humbo_ann,  [40.766667, -124.216667]],
    [2125,  'Arena Cove',     psmsl_arena_mon,  psmsl_arena_ann,  [38.913333, -123.706667]],
    [1394,  'Port Reyes',     psmsl_reyes_mon,  psmsl_reyes_ann,  [37.995, -122.976667]],
    [10,    'San Francisco',  psmsl_sanfr_mon,  psmsl_sanfr_ann,  [37.806667, -122.465]],
    [2330,  'Port Chicago',   psmsl_portc_mon,  psmsl_portc_ann,  [38.055, -122.04]],
    [437,   'Alameda',        psmsl_alame_mon,  psmsl_alame_ann,  [37.771667, -122.298333]],
    [2329,  'Redwood City',   psmsl_redwo_mon,  psmsl_redwo_ann,  [37.506667, -122.211667]],
    [508,   'Monterey',       psmsl_monte_mon,  psmsl_monte_ann,  [36.605, -121.886667]],
    [2126,  'Port San Luis',  psmsl_ports_mon,  psmsl_ports_ann,  [35.176667, -120.76]],
    [377,   'Santa Barbara',  psmsl_santb_mon,  psmsl_santb_ann,  [34.408333, -119.685]],
    [377,   'Santa Monica',   psmsl_santm_mon,  psmsl_santm_ann,  [34.008333, -118.5]],
    [245,   'Los Angeles',    psmsl_losan_mon,  psmsl_losan_ann,  [33.72, -118.271667]],
    [256,   'La Jolla',       psmsl_lajol_mon,  psmsl_lajol_ann,  [32.866667, -117.256667]],
    [158,   'San Diego',      psmsl_sandi_mon,  psmsl_sandi_ann,  [32.713333, -117.173333]]
]
