from flask import Flask, render_template, request, url_for
from pandas import DataFrame
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
loaded_model = joblib.load('C:\\Users\\lg\Desktop\\AirBnb\\AirbnbPricePrediction\\SeoulModel.pkl')

app = Flask(__name__, static_url_path='/static')

## GET 방식으로 값을 전달받음. 
## num이라는 이름을 가진 integer variable를 넘겨받는다고 생각하면 됨. 
## 아무 값도 넘겨받지 않는 경우도 있으므로 비어 있는 url도 함께 mapping해주는 것이 필요함
@app.route('/')
def main_get(num=None):
    return render_template('index.html', num=num)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        ## 넘겨받은 숫자 
        temp = request.args.get('num')
        temp2 = request.args.get('bed')
        temp3 = request.args.get('bath')
        temp4 = request.args.get('min')
        temp5 = request.args.get('long')
        temp6 = request.args.get('lat')
        temp7 = request.args.get('entire')
        temp8 = request.args.get('private')
        temp9 = request.args.get('share')

        data_df = [[temp,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9]]
        arr = DataFrame(data_df)
        q = arr.iloc[:, 0:9].values
        answer = f'{loaded_model.predict(q)}'
        print(answer)
        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        return render_template('index.html', num=temp,bed=temp2,bath=temp3,min=temp4,long=temp5,lat=temp6,entire=temp7,private=temp8,share=temp9,answer=answer)
    ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, threaded=True)