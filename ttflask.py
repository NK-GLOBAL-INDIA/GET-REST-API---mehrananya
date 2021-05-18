from flask import Flask, jsonify

app = Flask(__name__)
di = {'a':'today is 18th may', 'b':'today is friday', 'c':'date is saturday 10'}
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    count = 0
    m=[]
    for k, j in di.items():
        f=0
        for i in j:
            p = len(j)
            d = di[k].index(j)
            if (i.isnumeric() and f==0):
                count = count+1
                f=f+1
                m.append(j)

            elif (d==p-1 and count==0):
                return ''
            else:
                pass

    return jsonify({'result' : m})

app.run()