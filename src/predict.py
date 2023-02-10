from sklearn.tree import DecisionTreeRegressor
import pickle
loaded_model = pickle.load(open('src/model_VAR', 'rb'))
def graph(steplen):
    model_fit = loaded_model.fit(trend='n')
    pred = model_fit.forecast(model_fit.endog, steps=steplen)
    return pred