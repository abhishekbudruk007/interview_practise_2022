# Write a function which takes a dictionary of any depth and return a string (Should work for below kind of dictionaries).
#
# I/P:
# 	{
# 		'Last': {
# 			'Year': {
# 				'Was': {
# 					'Quite': {
# 						'Engaged With': 'Development.'
# 					}
# 				}
# 			}
# 		}
# 	}
#
# O/P:
# Last Year Was Quite Engaged With Development.
#
# ===
#
# I/P:
# 	{
# 		'I': {
# 			'Am': {
# 				'Fine': {
# 					'With': {
# 						'Your': {
# 							'Performance': ['Selvan!', 'How', 'Are', 'You?']
# 						}
# 					}
# 				}
# 			}
# 		}
# 	}
#
# O/P:
# I Am Fine With Your Performance Selvan! How Are You?
final_result = ''
def convert_to_string(dict):
    if type(dict) == str:
        return dict
    if type(dict) == list:
        return " ".join(dict)
    for key, values in dict.items():
        try:
            return key + " " + convert_to_string(values)
        except Exception as e:
            pass
    return final_result

# dict1 = {'Last': {'Year': { 'Was': { 'Quite': { 'Engaged With': ['Development','Program','c++']}}}}}

dict2 = {
		'I': {
			'Am': {
				'Fine': {
					'With': {
						'Your': {
							'Performance': ['Selvan!', 'How', 'Are', 'You?']
						}
					}
				}
			}
		}
	}

result = convert_to_string(dict2)
print (result)
# print (" ".join(result))