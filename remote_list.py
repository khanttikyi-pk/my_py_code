
import pyperclip
import json
common_pw = "cdsg@123456"
###data = '''
###{
  ###  "mmk": {
###        "pos1": {
###            "andsk": "",
###            "andskpw": "",
 ###           "adminpw": "'''+common_pw+'''"
 ###       }
   ###     "pos2": { 
     ###       "andsk": "",
       ###     "andskpw": "",
         ###   "adminpw": ""
        ###}
###}
###'''
###parsed = json.loads(data)
#print(parsed['mmk']['pos1']['adminpw'])

new = '''
{
    "ttm": {
        "pos1": {
            "andsk": "1 474 636 989",
            "andskpw": "!@#4CREL_TTM_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "pos2": {
            "andsk": "1548785288",
            "andskpw": "!@#4CREL_TTM_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "om": {
            "andsk": "936432510",
            "andskpw": "#$%6CREL_TTM_IT6#$%",
            "adminpw": "CD$G_TTM_IT%%"
        },
        "wh": {
            "andsk": "840644603",
            "andskpw": "#$%6CREL_TTM_IT6#$%",
            "adminpw": "CD$G_TTM_IT%%"
        },
        "srvr": {
            "andsk": "840644603",
            "andskpw": "$8$@#$CREL_SrTTM_IT$#@$8$",
            "adminpw": "'''+common_pw+'''"
        }
    },
    "mmk": {
        "pos1": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        },
        "pos2": { 
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        },
        "om": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        },
        "wh": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        },
        "srvr": {
            "andsk": "",
            "andskpw": "$8$@#$CREL_SrMMK_IT$#@$8$",
            "adminpw": ""
        }
    },
    "nok1": {
        "pos1": {
            "andsk": "1 804 981 712",
            "andskpw": "!@#4CREL_NOK1_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "pos2": {
            "andsk": "1 497 098 469",
            "andskpw": "!@#4CREL_NOK1_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "om": {
            "andsk": "335774342",
            "andskpw": "CREL_NOK_IT%%",
            "adminpw": "CD$G_NOK_IT%%"
        },
        "om1": {
            "andsk": "821542220",
            "andskpw": "CREL_NOK_IT%%",
            "adminpw": "CD$G_NOK_IT%%"
        },
        "wh": {
            "andsk": "484883840",
            "andskpw": "#%CREL_NOK_IT#%",
            "adminpw": "CD$G_NOK_IT%%"
        },
        "srvr": {
            "andsk": "599207039",
            "andskpw": "$8$@#$CREL_SrNOK_IT$#@$8$",
            "adminpw": "'''+common_pw+'''"
        }
    },
    "ndg1": {
        "pos1": {
            "andsk": "1282451821",
            "andskpw": "!@#4CREL_NDG1_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "pos2": {
            "andsk": "1824642196",
            "andskpw": "!@#4CREL_NDG1_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "pos3": {
            "andsk": "1962790685",
            "andskpw": "!@#4CREL_NDG1_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "om": {
            "andsk": "1086613659",
            "andskpw": "#$%6CREL_NDG1_IT6#$%",
            "adminpw": "CD$G_NDG_IT%%"
        },
        "om1": {
            "andsk": "1564043377",
            "andskpw": "#$%6CREL_NDG1_IT6#$%",
            "adminpw": "CD$G_NDG_IT%%"
        },
        "wh": {
            "andsk": "741705573",
            "andskpw": "#$%6CREL_NDG1_IT6#$%",
            "adminpw": "CD$G_NDG_IT%%"
        },
        "wh1": {
            "andsk": "288349106",
            "andskpw": "#$%6CREL_NDG1_IT6#$%",
            "adminpw": "CD$G_NDG_IT@@"
        },
        "srvr": {
            "andsk": "289080368",
            "andskpw": "!@#4CREL_NDG1_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        }
    },
    "ndg2": {
        "pos1": {
            "andsk": "1108809585",
            "andskpw": "!@#4CREL_NDG2_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "pos2": {
            "andsk": "356160204",
            "andskpw": "!@#4CREL_NDG2_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "om": {
            "andsk": "462365748",
            "andskpw": "#$%6CREL_NDG2_IT6#$%",
            "adminpw": "CD$G_NDG2_IT%%"
        },
        "wh": {
            "andsk": "1532798783",
            "andskpw": "#$%6CREL_NDG2_IT6#$%",
            "adminpw": "CD$G_NDG2_IT%%"
        },
        "srvr": {
            "andsk": "746217709",
            "andskpw": "$8$@#$CREL_SrNDG2_IT$#@$8$",
            "adminpw": "'''+common_pw+'''"
        }
    },
    "hyp": {
        "pos1": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        },
        "pos2": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        },
        "pos3": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        },
        "pos4": {
            "andsk": "779367540",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos5": {
            "andsk": "225691030",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos6": {
            "andsk": "272765831",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos7": {
            "andsk": "797705093",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos8": {
            "andsk": "593835890",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos9": {
            "andsk": "611121037",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos10": {
            "andsk": "783903419",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos11": {
            "andsk": "938436189",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos12": {
            "andsk": "349897151",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos17": {
            "andsk": "766376719",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos18": {
            "andsk": "772623003",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos21": {
            "andsk": "595660614",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos22": {
            "andsk": "1045419710",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos23": {
            "andsk": "542005701",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos24": {
            "andsk": "403695946",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "pos25": {
            "andsk": "351331432",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "'''+common_pw+'''"
        },
        "srvr": {
            "andsk": "889846980",
            "andskpw": "$8$@#$CREL_SrHYP_IT$#@$8$",
            "adminpw": "'''+common_pw+'''"
        }
    },
    "w2": {
        "pos1": {
            "andsk": "690374321",
            "andskpw": "!@#4CREL_W002_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "pos2": {
            "andsk": "736671046",
            "andskpw": "!@#4CREL_W002_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "om": {
            "andsk": "1427278554",
            "andskpw": "#$%6CREL_W002_IT6#$%",
            "adminpw": "CD$G_W002_IT%%"
        },
        "wh": {
            "andsk": "831759908",
            "andskpw": "#$%6CREL_W002_IT6#$%",
            "adminpw": "CD$G_W002_IT%%"
        },
        "srvr": {
            "andsk": "1204531063",
            "andskpw": "$8$@#$CREL_SrW002_IT$#@$8$",
            "adminpw": "'''+common_pw+'''"
        }
    },
    "w4": {
        "pos1": {
            "andsk": "1933640546",
            "andskpw": "!@#4CREL_W004_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "om": {
            "andsk": "1994203235",
            "andskpw": "!@#4CREL_W004_IT4!@#",
            "adminpw": "CD$G_W004_IT%%"
        }
    },
    "w5": {
        "pos1": {
            "andsk": "341080437",
            "andskpw": "!@#4CREL_W005_IT4!@#",
            "adminpw": "'''+common_pw+'''"
        },
        "om": {
            "andsk": "1695380862",
            "andskpw": "!@#4CREL_W005_IT4!@#",
            "adminpw": "CD$G_W004_IT%%"
        }
    }
}
'''
data_load = json.loads(new)
while True:
    try:
        where = input('Store: ')
        which = input('Node: ')
        what = input('Require: ')
        param = data_load[where][which][what]
        copy_data = pyperclip.copy(param)
    except KeyError:
        continue
    except KeyboardInterrupt:
        break

        """"wh": {
            "andsk": "484883840",
            "andskpw": "#%CREL_NOK_IT#%",
            "adminpw": "'''+common_pw+'''"
        },"""
