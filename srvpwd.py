import pyperclip
import json
common_pw = "cdsg@123456"
#print(parsed['person']['address']['city']),

data = '''
{
    "mmk": {
        "pos1": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "pos2": { ,
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "om": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "wh": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "srvr": {
            "andsk": "",
            "andskpw": "$8$@#$CREL_SrMMK_IT$#@$8$",
            "adminpw": ""
        }
    }
    "ttm": {
        "pos1": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "pos2": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        } ,
        "om": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "wh": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "srvr": {
            "andsk": "",
            "andskpw": "$8$@#$CREL_SrMMK_IT$#@$8$",
            "adminpw": ""
        }
    }
    "spt1": {
        "pos1": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "pos2": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "om": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "wh": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "srvr": {
            "andsk": "",
            "andskpw": "$8$@#$CREL_SrMMK_IT$#@$8$",
            "adminpw": ""
        }
    }
    "hty": {
        "pos1": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "pos2": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "om": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "wh": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "srvr": {
            "andsk": "",
            "andskpw": "$8$@#$CREL_SrMMK_IT$#@$8$",
            "adminpw": ""
        }
    }
    "nok1": {
        "pos1": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "pos2": { ,
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "om": { ,
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "wh": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "srvr": {
            "andsk": "",
            "andskpw": "$8$@#$CREL_SrMMK_IT$#@$8$",
            "adminpw": ""
        }
    }
    "ndg1": {
        "pos1": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "pos2": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "om": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "wh": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "srvr": {
            "andsk": "289080368",
            "andskpw": "$8$@#$CREL_SrNDG1_IT$#@$8$",
            "adminpw": "" 
        }
    }
    "ndg2": {
        "pos1": {
            "andsk": "1108809585",
            "andskpw": "!@#4CREL_NDG2_IT4!@#",
            "adminpw": "" 
        }
        "pos2": {
            "andsk": "356160204",
            "andskpw": "!@#4CREL_NDG2_IT4!@#",
            "adminpw": "" 
        }
        "om": {
            "andsk": "462365748",
            "andskpw": "#$%6CREL_NDG2_IT6#$%",
            "adminpw": "CD$G_NDG2_IT%%",
        }
        "wh": {
            "andsk": "1532798783",
            "andskpw": "#$%6CREL_NDG2_IT6#$%",
            "adminpw": "CD$G_NDG2_IT%%",
        }
        "srvr": {
            "andsk": "746217709",
            "andskpw": "$8$@#$CREL_SrNDG2_IT$#@$8$",
            "adminpw": "" 
        }
    }
    "hyp": {
        "pos1": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "pos2": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "pos3": {
            "andsk": "",
            "andskpw": "",
            "adminpw": ""
        }
        "pos4": {
            "andsk": "779367540",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos5": {
            "andsk": "225691030",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos6": {
            "andsk": "272765831",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos7": {
            "andsk": "797705093",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos8": {
            "andsk": "593835890",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos9": {
            "andsk": "611121037",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos10": {
            "andsk": "783903419",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos11": {
            "andsk": "938436189",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos12": {
            "andsk": "349897151",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos17": {
            "andsk": "766376719",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos18": {
            "andsk": "772623003",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
,
        "pos21": {
            "andsk": "595660614",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos22": {
            "andsk": "1045419710",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos23": {
            "andsk": "542005701",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos24": {
            "andsk": "403695946",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "pos25": {
            "andsk": "351331432",
            "andskpw": "%^&CREL_HYP_IT%^&",
            "adminpw": "" 
        }
        "srvr": {
            "andsk": "889846980",
            "andskpw": "$8$@#$CREL_SrHYP_IT$#@$8$,
            "adminpw": "" 
        }
    }
    "w2": {
        "pos1": {
            "andsk": "690374321",
            "andskpw": "!@#4CREL_W002_IT4!@#",
            "adminpw": "" 
        }
        "pos2": {
            "andsk": "736671046",
            "andskpw": "!@#4CREL_W002_IT4!@#",
            "adminpw": "" 
        }
        "om": {
            "andsk": "1427278554",
            "andskpw": "#$%6CREL_W002_IT6#$%",
            "adminpw": "CD$G_W002_IT%%",
        }
        "wh": {
            "andsk": "831759908",
            "andskpw": "#$%6CREL_W002_IT6#$%",
            "adminpw": "CD$G_W002_IT%%",
        }
        "srvr": {
            "andsk": "1204531063",
            "andskpw": "$8$@#$CREL_SrW002_IT$#@$8$",
            "adminpw": "" 
        }
    }
    "w4": {
        "pos1": {
            "andsk": "1933640546",
            "andskpw": "!@#4CREL_W004_IT4!@#",
            "adminpw": "" 
        }
        "om": {
            "andsk": "1994203235",
            "andskpw": "!@#4CREL_W004_IT4!@#",
            "adminpw": "CD$G_W004_IT%%",
        }
    }
    "w5": {
        "pos1": {
            "andsk": "341080437",
            "andskpw": "!@#4CREL_W005_IT4!@#",
            "adminpw": "" 
        }
        "om": {
            "andsk": "1695380862",
            "andskpw": "!@#4CREL_W005_IT4!@#",
            "adminpw": "CD$G_W004_IT%%",
        }
    }
    "spt2": {
        "pos1": {
            "andsk": "659794137",
            "andskpw": "!@#4CREL_SPT3_IT4!@#",
            "adminpw": "" 
        }
        "pos2": {
            ,
            "andsk": "1660063208",
            "andskpw":!@#4CREL_SPT2_IT4!@#,
            "adminpw": "" 
        }
        "om": {
            "andsk": "932019964",
            "andskpw": "#$%6CREL_SPT2_IT6#$",
            "adminpw": "CD$G_SPT2_IT%%",
        }
        "wh": {
            "andsk": "852022516",
            "andskpw": "#$%6CREL_SPT2_IT6#$%",
            "adminpw": "CD$G_SPT2_IT%%",
        }
        "srvr": {
            "andsk": "117681771",
            "andskpw": "$8$@#$CREL_SrSPT2_IT$#@$8$",
            "adminpw": "" 
        }
    }
    "spt3": {
        "pos1": {
            "andsk": "659794137",
            "andskpw": "!@#4CREL_SPT3_IT4!@#",
            "adminpw": "" 
        }
        "pos2": {
            "andsk": "1 136 845 930",
            "andskpw": "!@#4CREL_SPT3_IT4!@#",
            "adminpw": "" 
        }
        "om": {
            "andsk": "124764774",
            "andskpw": "#$%6CREL_SPT3_IT6#$%",
            "adminpw": "CD$G_SPT3_IT%%",
        }
        "wh": {
            "andsk": "162366292",
            "andskpw": "#$%6CREL_SPT3_IT6#$%",
            "adminpw": "CD$G_SPT3_IT%%",
        }
        "srvr": {
            "andsk": "724549835",
            "andskpw": "$8$@#$CREL_SrSPT3_IT$#@$8$",
            "adminpw": "" 
        }
    }
    "sch": {
        "pos1": {
            "andsk": "659672766",
            "andskpw": "!@#4CREL_SCH_IT4!@#",
            "adminpw": "" 
        }
        "pos2": {
            "andsk": "336767761",
            "andskpw": "!@#4CREL_SCH_IT4!@#",
            "adminpw": "" 
        }
        "om1": {
            "andsk": "1578367886",
            "andskpw": "#$%6CREL_SCH_IT6#$%",
            "adminpw": "CD$G_SCH_IT%%",
        }
        "om2": {
            "andsk": "1441870833",
            "andskpw": 
            "adminpw": "CD$G_SCH_IT%%",
        }
        "op": {
            "andsk": "222872410",
            "andskpw": "#$%6CREL_SCH_IT6#$%",
            "adminpw": "CD$G_SCH_IT%%",
        }
        "adm1": {
            "andsk": "920944759",
            "andskpw": 
            "adminpw": "CD$G_SCH_IT%%",
        }
        "adm2": {
            "andsk": "920944759",
            "andskpw": 
            "adminpw": "CD$G_SCH_IT%%",
        }
        "mne": {
            "andsk": "1817213757",
            "andskpw": "#$%6CREL_SCH_IT6#$%",
            "adminpw": "CD$G_SCH_IT%%",
        }
        "wh": {
            "andsk": "614015665",
            "andskpw": "#$%6CREL_SCH_IT6#$%",
            "adminpw": "CD$G_SCH_IT%%",
        }
        "srvr": {
            "andsk": "518170492",
            "andskpw": "$8$@#$CREL_SrSCH_IT$#@$8$",
            "adminpw": "" 
        }
    }
    "bgo": {
        "pos1": {
            "andsk": "314692023",
            "andskpw": "!@#4CREL_BGO_IT4!@#",
            "adminpw": "" 
        }
        "pos2": {
            "andsk": "300045541",
            "andskpw": "!@#4CREL_BGO_IT4!@#",
            "adminpw": "" 
        }
        "om": {
            "andsk": "1962935624",
            "andskpw": "#$%6CREL_BGO_IT6#$%",
            "adminpw": "CD$G_BGO_IT%%",
        }
        "wh": {
            "andsk": "921700245",
            "andskpw": "#$%6CREL_BGO_IT6#$%",
            "adminpw": "CD$G_BGO_IT%%",
        }
        "srvr": {
            "andsk": "376078466",
            "andskpw": "$8$@#$CREL_SrBGO_IT$#@$8$",
            "adminpw": "" 
        }
    }
    "nok2": {
        "pos1": {
            "andsk": "1804981712",
            "andskpw": "!@#4CREL_NOK2_IT4!@#",
            "adminpw": "" 
        }
        "pos2": {
            "andsk": "1877270647",
            "andskpw": "!@#4CREL_NOK2_IT4!@#",
            "adminpw": "" 
        }
        "om": {
            "andsk": "1388070860",
            "andskpw": "#$%6CREL_NOK2_IT6#$%",
            "adminpw": "CD$G_NOK2_IT%%",
        }
        "wh": {
            "andsk": "1308408896",
            "andskpw": "#$%6CREL_NOK2_IT6#$%",
            "adminpw": "CD$G_NOK2_IT%%",
        }
        "srvr": {
            "andsk": "1962900274",
            "andskpw": "$8$@#$CREL_SrNOK2_IT$#@$8$",
            "adminpw": "" 
        }
    }
    "byn": {
        "pos1": {
            "andsk": "1044358686",
            "andskpw": "!@#4CREL_BYN_IT4!@#",
            "adminpw": "" 
        }
        "pos2": {
            "andsk": "1160860646",
            "andskpw": "!@#4CREL_BYN_IT4!@#",
            "adminpw": "" 
        }
        "om": {
            "andsk": "1861850730",
            "andskpw": "#$%6CREL_BYN_IT6#$%",
            "adminpw": "CD$G_BYN_IT%%",
        }
        "wh": {
            "andsk": "1273340798",
            "andskpw": "#$%6CREL_BYN_IT6#$%",
            "adminpw": "CD$G_BYN_IT%%",
        }
        "srvr": {
            "andsk": "751536280",
            "andskpw": "$8$@#$CREL_SrBYN_IT$#@$8$",
            "adminpw": "" 
        }
    }
    "sdg": {
        "pos1": {
            "andsk": "1658904931",
            "andskpw": "!@#4CREL_SDG_IT4!@#",
            "adminpw": "" 
        }
        "pos2": {
            "andsk": "417805711",
            "andskpw": "!@#4CREL_SDG_IT4!@#",
            "adminpw": "" 
        }
        "om": {
            "andsk": "1486529238",
            "andskpw": "#$%6CREL_SDG_IT6#$%",
            "adminpw": "CD$G_SDG_IT%%",
        }
        "wh": {
            "andsk": "1701852948",
            "andskpw": "#$%6CREL_SDG_IT6#$%",
            "adminpw": "CD$G_SDG_IT%%",
        }
        "srvr": {
            "andsk": "764398187",
            "andskpw": "$8$@#$CREL_SrMMK_IT$#@$8$",
            "adminpw": "" 
        }
    }
    "ndg3": {
        "pos1": {
            "andsk": "1778565292",
            "andskpw": "!@#4CREL_NDG3_IT4!@#",
            "adminpw": common
        }
        "pos2": {
            "andsk": "1222439062",
            "andskpw": "!@#4CREL_NDG3_IT4!@#",
            "adminpw": common_pw
        }
        "om": {
            "andsk": "1 319 258 147",
            "andskpw": "#$%6CREL_NDG3_IT6#$%",
            "adminpw": "CD$G_NDG3_IT%%"
        }
        "wh": {
            "andsk": "1 466 323 497",
            "andskpw": "#$%6CREL_NDG3_IT6#$%",
            "adminpw": "CD$G_NDG3_IT%%"
        }
        "srvr": {
            "andsk": "1404479513",
            "andskpw": 
            "adminpw": common_pw
        }
    }
    "dsk": {
        "pos1": {
            "andsk": "1178492445",
            "andskpw": "!@#4CREL_DSK_T4!@#",
            "adminpw": common_pw
        }
        "pos2": {
            "andsk": "1583376905",
            "andskpw": "!@#4CREL_DSK_T4!@#",
            "adminpw": common_pw
        }
        "om": {
            "andsk": "1816283591",
            "andskpw": "#$%6crel_dsk_it6#$%",
            "adminpw": "CD$G_DSK_IT%%"
        }
        "wh": {
            "andsk": "1887888903",
            "andskpw": "#$%6CREL_DSK_IT6#$%",
            "adminpw": "CD$G_DSK_IT%%"
        }
        "srvr": {
            "andsk": "1052261552",
            "andskpw": common_pw,
            "adminpw": common_pw
        }
    }
    "ymn": {
        "pos1": {
            "andsk": "1081207791",
            "andskpw": "!@#4CREL_YMN_T4!@#",
            "adminpw": common_pw 
        }
        "pos2": {
            "andsk": "804618561",
            "andskpw": "!@#4CREL_YMN_T4!@#",
            "adminpw": common_pw
        }
        "om": {
            "andsk": "1639222165",
            "andskpw": "#$%6CREL_YMN_IT6#$%",
            "adminpw": "CD$G_YMN_IT%%"
        }
        "wh": {
            "andsk": "1142981784",
            "andskpw": "#$%6CREL_YMN_IT6#$%",
            "adminpw": "CD$G_YMN_IT%%"
        }
        "srvr": {
            "andsk": "610917877",
            "andskpw": common_pw,
            "adminpw": common_pw 
        }
    }
}
'''

###server_pwds = {
#    "mmk": "$8$@#$CREL_SrMMK_IT$#@$8$",,
#    "ttm": "$8$@#$CREL_SrTTM_IT$#@$8$",,
#    "spt1": "$8$@#$CREL_SrSPT1_IT$#@$8$",,
#    "hty": "$8$@#$CREL_SrHTY_IT$#@$8$",,
#    "nok1": "$8$@#$CREL_SrNOK1_IT$#@$8$",,
#    "ndg1": "$8$@#$CREL_SrNDG1_IT$#@$8$",,
#    "ndg2": "$8$@#$CREL_SrNDG2_IT$#@$8$",,
#    "hyp": "$8$@#$CREL_SrHYP_IT$#@$8$",,
#    "w2": "$8$@#$CREL_SrW002_IT$#@$8$",,
#    "w3": "$8$@#$CREL_SrW003_IT$#@$8$",,
#    "spt2": "$8$@#$CREL_SrSPT2_IT$#@$8$",,
#    "spt3": "$8$@#$CREL_SrSPT3_IT$#@$8$",,
#    "sch": "$8$@#$CREL_SrSCH_IT$#@$8$",,
#        "bgo": "$8$@#$CREL_SrBGO_IT$#@$8$",,
#        "nok2": "$8$@#$CREL_SrNOK2_IT$#@$8$",,
#        "byn": "$8$@#$CREL_SrBYN_IT$#@$8$",,
#        "sdg": "cdsg@12345678",,
#        "ndg3": "cdsg@12345678",,
#        "dsk": "cdsg@123456",,
#        "ymn": "cdsg@123456",,
#        }
parsed = json.loads(data)
while True:
    try:
        storename = input("choose storename: ")
        copy_stname = pyperclip.copy(storename)
    except KeyError:
        continue
    except KeyboardInterrupt:
        break
    
