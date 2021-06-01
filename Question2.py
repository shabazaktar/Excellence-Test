# 2 Question

def maxValue(d2):
    key = max(d2, key=d2.get)
    d3={key : d2[key]}
    return d3

    

d1= {
            "1" : "Shahbaz",
            "2" : "Kamran",
            "3" : "Tayyab"
        }

d2= {
           "1" : 50,
           "2" : 60,
           "3" :70
        }
print(maxValue(d2))
