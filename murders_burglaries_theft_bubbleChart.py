import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('wazzdude', 'nGRjNtJ4d4MiiUjvP0dv')
trace1 = {
  "x": [8.2, 4.8, 7.5, 6.7, 6.9, 3.7, 2.9, 4.4, 5.0, 6.2, 1.9, 2.4, 6.0, 5.7, 1.3, 3.7, 4.6, 9.9, 1.4, 9.9, 2.7, 6.1, 2.2, 7.3, 6.9, 1.9, 2.5, 8.5, 1.4, 4.8, 7.4, 4.5, 6.7, 1.1, 5.1, 5.3, 2.2, 6.1, 3.2, 7.4, 2.3, 7.2, 6.2, 2.3, 1.3, 6.1, 3.3, 4.4, 3.5, 2.7], 
  "y": [953.8, 622.5, 948.4, 1084.6, 693.3, 744.8, 437.1, 688.9, 926.3, 931.0, 767.9, 564.4, 606.9, 697.6, 606.4, 689.2, 634.0, 870.6, 478.5, 641.4, 541.1, 696.8, 578.9, 919.7, 738.3, 389.2, 532.4, 972.4, 317.0, 447.1, 1093.9, 353.3, 1201.1, 311.9, 872.8, 1006.0, 758.6, 451.6, 494.2, 1000.9, 324.4, 1026.9, 961.6, 606.2, 491.8, 392.1, 959.7, 621.2, 440.8, 476.3], 
  "marker": {
    "color": ["rgba(255,229,0,0.75)", "rgba(237,255,8,0.75)", "rgba(255,77,0,0.75)", "rgba(255,200,0,0.75)", "rgba(0,168,255,0.75)", "rgba(255,189,0,0.75)", "rgba(0,120,255,0.75)", "rgba(47,255,199,0.75)", "rgba(255,226,0,0.75)", "rgba(255,181,0,0.75)", "rgba(127,0,0,0.75)", "rgba(0,176,255,0.75)", "rgba(54,255,192,0.75)", "rgba(160,255,86,0.75)", "rgba(5,236,241,0.75)", "rgba(255,177,0,0.75)", "rgba(0,48,255,0.75)", "rgba(192,255,54,0.75)", "rgba(0,124,255,0.75)", "rgba(108,255,137,0.75)", "rgba(0,0,232,0.75)", "rgba(0,168,255,0.75)", "rgba(83,255,163,0.75)", "rgba(21,255,225,0.75)", "rgba(255,185,0,0.75)", "rgba(215,255,31,0.75)", "rgba(228,255,18,0.75)", "rgba(50,255,195,0.75)", "rgba(0,0,145,0.75)", "rgba(0,0,255,0.75)", "rgba(254,237,0,0.75)", "rgba(0,0,255,0.75)", "rgba(215,255,31,0.75)", "rgba(0,0,218,0.75)", "rgba(166,255,79,0.75)", "rgba(255,233,0,0.75)", "rgba(241,7,0,0.75)", "rgba(0,72,255,0.75)", "rgba(0,116,255,0.75)", "rgba(255,85,0,0.75)", "rgba(0,0,127,0.75)", "rgba(255,144,0,0.75)", "rgba(255,81,0,0.75)", "rgba(255,100,0,0.75)", "rgba(0,48,255,0.75)", "rgba(2,232,244,0.75)", "rgba(218,0,0,0.75)", "rgba(0,104,255,0.75)", "rgba(0,208,255,0.75)", "rgba(212,255,34,0.75)"], 
    "colorsrc": "wazzdude:25:3959e3", 
    "line": {
      "color": ["rgba(255,229,0,0.75)", "rgba(237,255,8,0.75)", "rgba(255,77,0,0.75)", "rgba(255,200,0,0.75)", "rgba(0,168,255,0.75)", "rgba(255,189,0,0.75)", "rgba(0,120,255,0.75)", "rgba(47,255,199,0.75)", "rgba(255,226,0,0.75)", "rgba(255,181,0,0.75)", "rgba(127,0,0,0.75)", "rgba(0,176,255,0.75)", "rgba(54,255,192,0.75)", "rgba(160,255,86,0.75)", "rgba(5,236,241,0.75)", "rgba(255,177,0,0.75)", "rgba(0,48,255,0.75)", "rgba(192,255,54,0.75)", "rgba(0,124,255,0.75)", "rgba(108,255,137,0.75)", "rgba(0,0,232,0.75)", "rgba(0,168,255,0.75)", "rgba(83,255,163,0.75)", "rgba(21,255,225,0.75)", "rgba(255,185,0,0.75)", "rgba(215,255,31,0.75)", "rgba(228,255,18,0.75)", "rgba(50,255,195,0.75)", "rgba(0,0,145,0.75)", "rgba(0,0,255,0.75)", "rgba(254,237,0,0.75)", "rgba(0,0,255,0.75)", "rgba(215,255,31,0.75)", "rgba(0,0,218,0.75)", "rgba(166,255,79,0.75)", "rgba(255,233,0,0.75)", "rgba(241,7,0,0.75)", "rgba(0,72,255,0.75)", "rgba(0,116,255,0.75)", "rgba(255,85,0,0.75)", "rgba(0,0,127,0.75)", "rgba(255,144,0,0.75)", "rgba(255,81,0,0.75)", "rgba(255,100,0,0.75)", "rgba(0,48,255,0.75)", "rgba(2,232,244,0.75)", "rgba(218,0,0,0.75)", "rgba(0,104,255,0.75)", "rgba(0,208,255,0.75)", "rgba(212,255,34,0.75)"], 
      "colorsrc": "wazzdude:25:3959e3", 
      "width": 2
    }, 
    "size": [46.17263315639515, 28.604588157092504, 49.440341388969046, 40.819107877058634, 77.34929597531402, 46.463792042237, 43.18313440808221, 30.273154053587305, 64.93914353630238, 54.919889756117655, 33.54427887762138, 34.55567444162507, 59.66673831298549, 50.00623883221204, 41.44148024718812, 40.691883704554066, 45.22240069503854, 46.0518841873926, 33.841758202669276, 48.6079798235629, 50.40120710156516, 56.36100812805722, 47.537037137275234, 41.26708973291903, 49.088663344022805, 31.094228955943088, 36.38029648785935, 39.395840087, 33.77566838549589, 54.18760445762959, 37.20740303712634, 66.30754794718023, 54.26226420006762, 28.23292158089986, 58.20236772520623, 43.35396375591953, 43.612723627817324, 59.36279236656359, 32.12449287531771, 45.4208734318148, 29.71907873720085, 49.483549317867634, 69.10235596684717, 39.762092943379145, 28.047233662986937, 52.442846702447355, 50.02254874204053, 36.64834088649052, 48.51831587355984, 26.67408577043877], 
    "sizesrc": "wazzdude:25:82e2ef", 
    "symbol": "circle"
  }, 
  "mode": "markers", 
  "type": "scatter", 
  "uid": "97c1f07b-3f06-4562-a38a-3c8dd7bd8af0", 
  "xaxis": "x", 
  "xsrc": "wazzdude:25:190648", 
  "yaxis": "y", 
  "ysrc": "wazzdude:25:95d33c"
}
data = Data([trace1])
layout = {
  "annotations": [
    {
      "x": 8.2, 
      "y": 953.8, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "AK", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 4.799980447851102, 
      "y": 610.277793493635, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "AL", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 7.5, 
      "y": 948.4, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "AR", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 6.7, 
      "y": 1084.6, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "AZ", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 6.900041193572974, 
      "y": 681.081188118812, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "CA", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 3.7, 
      "y": 744.8, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "CO", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 2.9, 
      "y": 437.1, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "CT", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 4.4, 
      "y": 688.9, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "DE", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 5, 
      "y": 926.3, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "FL", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 6.2, 
      "y": 931, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "GA", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 1.8999845606313925, 
      "y": 755.6729844413013, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "HI", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 2.4, 
      "y": 564.4, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "IA", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 6, 
      "y": 606.9, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "ID", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 5.699953681894178, 
      "y": 685.3736916548798, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "IL", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 1.3, 
      "y": 606.4, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "IN", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 3.7, 
      "y": 689.2, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "KS", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 4.6, 
      "y": 634, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "KY", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 9.899951973716561, 
      "y": 858.3722772277229, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "LA", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 1.400040497147915, 
      "y": 464.7451202263083, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "MA", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 9.899951973716561, 
      "y": 629.1739745403112, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "MD", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 2.7, 
      "y": 541.1, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "ME", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 6.099982852453777, 
      "y": 684.5793493635078, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "MI", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 2.2, 
      "y": 578.9, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "MN", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 7.3, 
      "y": 919.7, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "MO", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 6.900041193572974, 
      "y": 732.1940594059406, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "MS", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 1.9, 
      "y": 389.2, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "MT", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 2.5, 
      "y": 532.4, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "NC", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 8.5, 
      "y": 972.4, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "ND", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 1.4, 
      "y": 317, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "NE", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 4.799980447851102, 
      "y": 434.88090523338053, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "NH", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 7.4, 
      "y": 1093.9, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "NJ", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 4.499989369836743, 
      "y": 341.07213578500716, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "NM", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 6.7, 
      "y": 1201.1, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "NV", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 1.1, 
      "y": 311.9, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "NY", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 5.1, 
      "y": 872.8, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "OH", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 5.3, 
      "y": 1006, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "OK", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 2.199975638645751, 
      "y": 746.3852899575672, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "OR", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 6.099982852453777, 
      "y": 439.3719943422915, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "PA", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 3.2, 
      "y": 494.2, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "RI", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 7.4, 
      "y": 1000.9, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "SC", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 2.3, 
      "y": 324.4, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "SD", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 7.2, 
      "y": 1026.9, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "TN", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 6.2, 
      "y": 961.6, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "TX", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 2.300013731190991, 
      "y": 606.1991513437059, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "UT", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 1.3, 
      "y": 491.8, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "VA", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 6.099982852453777, 
      "y": 379.8727015558699, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "VT", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 3.3, 
      "y": 959.7, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "WA", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 4.399951277291502, 
      "y": 608.9793493635078, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "WI", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 3.5, 
      "y": 440.8, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "WV", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 2.7, 
      "y": 476.3, 
      "align": "center", 
      "font": {
        "color": "#000000", 
        "size": 9
      }, 
      "opacity": 1, 
      "showarrow": False, 
      "text": "WY", 
      "xanchor": "center", 
      "xref": "x", 
      "yanchor": "bottom", 
      "yref": "y"
    }, 
    {
      "x": 0.4536585365853659, 
      "y": 1.0165205091937763, 
      "font": {
        "color": "#000000", 
        "size": 12
      }, 
      "showarrow": False, 
      "text": "United States Murders, Burglaries, and Theft in 2005", 
      "xanchor": "center", 
      "xref": "paper", 
      "yanchor": "bottom", 
      "yref": "paper"
    }
  ], 
  "autosize": False, 
  "height": 936, 
  "hovermode": "closest", 
  "images": [
    {
      "x": 1, 
      "y": 0.5, 
      "layer": "below", 
      "sizex": 1, 
      "sizey": 1, 
      "source": "data:image/png;base64,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", 
      "xanchor": "right", 
      "xref": "paper", 
      "yanchor": "middle"
    }
  ], 
  "legend": {"orientation": "v"}, 
  "margin": {
    "r": 276, 
    "t": 112, 
    "b": 117, 
    "l": 180, 
    "pad": 0
  }, 
  "showlegend": False, 
  "width": 1440, 
  "xaxis": {
    "anchor": "y", 
    "domain": [0, 0.9073779338858093], 
    "mirror": "ticks", 
    "nticks": 7, 
    "range": [0, 11], 
    "showgrid": False, 
    "showline": True, 
    "side": "bottom", 
    "tickfont": {"size": 10}, 
    "ticks": "inside", 
    "title": {
      "font": {
        "size": 10, 
        "color": "#000000"
      }, 
      "text": "Murders (per 100,000 population)"
    }, 
    "type": "linear", 
    "zeroline": False
  }, 
  "xaxis2": {
    "anchor": "y2", 
    "domain": [0.9640890547536726, 1], 
    "mirror": False, 
    "nticks": 0, 
    "range": [1343.7, 3308.4], 
    "showgrid": False, 
    "showline": False, 
    "side": "bottom", 
    "ticks": "inside", 
    "type": "linear", 
    "zeroline": False
  }, 
  "yaxis": {
    "anchor": "x", 
    "domain": [0, 1], 
    "mirror": "ticks", 
    "nticks": 7, 
    "range": [200, 1280], 
    "showgrid": False, 
    "showline": True, 
    "side": "left", 
    "tickfont": {"size": 10}, 
    "ticks": "inside", 
    "title": {
      "font": {
        "size": 10, 
        "color": "#000000"
      }, 
      "text": "Burglaries (per 100,000 population)"
    }, 
    "type": "linear", 
    "zeroline": False
  }, 
  "yaxis2": {
    "anchor": "x2", 
    "domain": [1.4704940723512008e-16, 1], 
    "mirror": False, 
    "nticks": 8, 
    "range": [1343.7, 3308.4], 
    "showgrid": False, 
    "showline": False, 
    "side": "right", 
    "tickfont": {"size": 10}, 
    "ticks": "inside", 
    "title": {
      "font": {
        "size": 10, 
        "color": "#000000"
      }, 
      "text": "Larceny Theft"
    }, 
    "type": "linear", 
    "zeroline": False
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
