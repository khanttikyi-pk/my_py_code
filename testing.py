import json
common_pw = "asdf"
###data = '''
###{
  ###  "mmk": {
###        "pos1": {
###            "andsk": "",
###            "andskpw": "",
 ###           "adminpw": common_pw
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
    "mmk": {
        "pos1": {
            "andsk": "1234",
            "andskpw": "",
            "adminpw": ""
        }
    }
}
'''
data_load = json.loads(new)
print(data_load['mmk']['pos1']['andsk'])
                

