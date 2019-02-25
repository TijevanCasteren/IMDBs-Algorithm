def ml():
    """Function tasked with running the machine learning alglorythm

    """
    import numpy 
    from sklearn import linear_model
    from sklearn.metrics import mean_squared_error, r2_score
    import statsmodels.api as sm
    from sklearn.model_selection import train_test_split
    
    resp=[] #define response list
    
    def convert(): # convert the dataset into a final dataset file by removing the lines containing empty ratings
        out=open("data/new_dataoutput.txt","w")
        f = open("data/testoutput.txt")
        for line in f:         
            li=line.split("|")
            if li[2]=='' or li[0]=='':
                continue
            else:
                out.write(line) # write new dataset
                resp.append(float(li[2])) # import response into list
        f.close()
        out.close()        
    
    convert()
    
    #export features from new (final) dataset file
    data=numpy.loadtxt("data/new_dataoutput.txt",delimiter="|", usecols = (3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40))
    
    train_Y=[]
    test_Y=[]
    
    
    #Random split using built-in function:
    train_X, test_X, train_Y, test_Y = train_test_split(data, resp, test_size=0.5, random_state=42)
    
    #Ordinary Least Squares:
    reg = linear_model.LinearRegression()
    reg.fit(train_X,train_Y) #Fit the model
    pred_Y = reg.predict(test_X) #Make predictions
    print("\nOrdinary Least Squares prediction:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y)) #Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y)) #Calculates R2 of predictions
    
    # Analysis of the linear coefficients significance (least squares regression):
    X2 = sm.add_constant(train_X)
    est = sm.OLS(train_Y, X2)#Define the model
    est2 = est.fit()#Fit the model
    print(est2.summary())
    
    #Ridge regression
    reg = linear_model.Ridge(alpha=.5)
    reg.fit(train_X,train_Y)#Fit the model
    pred_Y = reg.predict(test_X)#Make predictions
    print("\nRidge Regression prediction:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
    
    reg = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0], cv=3)
    reg.fit(train_X,train_Y)#Fit the model
    pred_Y = reg.predict(test_X)#Make predictions
    print("\nRidge Regression with Generalized Cross-Validation prediction:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
    
    reg = linear_model.Lasso(alpha=0.1)
    reg.fit(train_X,train_Y)#Fit the model
    pred_Y = reg.predict(test_X)#Make predictions
    print("\nLasso Model:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
    
    reg = linear_model.Lars(n_nonzero_coefs=1)
    reg.fit(train_X,train_Y)#Fit the model
    pred_Y = reg.predict(test_X)#Make predictions
    print("\nLeast Angle Regression (LARS) Model:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
    
    reg = linear_model.LassoLars(alpha=.1)
    reg.fit(train_X,train_Y)#Fit the model
    pred_Y = reg.predict(test_X)#Make predictions
    print("\nLARS Lasso Model:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
    
    reg = linear_model.BayesianRidge()
    reg.fit(train_X,train_Y)#Fit the model
    pred_Y = reg.predict(test_X)#Make predictions
    print("\nBayesian Ridge Regressor predictions:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
    
    #SVR:
    from sklearn.svm import SVR
    reg = SVR(kernel='rbf', C=1e3, gamma=0.1)
    reg.fit(train_X,train_Y)#Fit the model
    pred_Y = reg.predict(test_X)#Make predictions
    print("\nSupported Vector Machine Regressor predictions:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
    
    from sklearn import tree
    reg=tree.DecisionTreeRegressor()
    reg.fit(train_X,train_Y)#Fit the model
    pred_Y = reg.predict(test_X)#Make predictions
    #print(pred_Y,resp)
    print("\nDecision Tree Regressor predictions:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
    
    from sklearn.ensemble import AdaBoostRegressor
    from sklearn.tree import DecisionTreeRegressor
    
    rng = numpy.random.RandomState(1)
    reg = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),n_estimators=300, random_state=rng)
    reg.fit(train_X,train_Y)#Fit the model
    pred_Y = reg.predict(test_X)#Make predictions
    print("\nAda Boost Regressor predictions:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
    
    #Dimensionality reduction with PCA and then linear regression
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    pca_data=pca.fit_transform(data) #Do PCA dimensional reduction
     #Random split using built-in function:
    pca_train_X, pca_test_X, train_Y, test_Y = train_test_split(pca_data, resp, test_size=0.5, random_state=42)
    reg = linear_model.LinearRegression() # Do least squares
    reg.fit(pca_train_X,train_Y) #Fit the model
    pred_Y = reg.predict(pca_test_X)#Make predictions
    print("\nLeast squares with features compressed into 2 principal components:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
    
    #Add polynomial feautres
    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures(degree=3)
    a=poly.fit_transform(train_X) #add polynomial feautures to training set
    b=poly.fit_transform(test_X) #add polynomial features to testing set
    reg = linear_model.LinearRegression() #Least squares
    reg.fit(a,train_Y)#Fit the model
    pred_Y = reg.predict(b)#Make predictions
    print("\nLeast squares with polynomial features:")
    print("Mean squared error: %.2f" % mean_squared_error(test_Y, pred_Y))#Calculates MSE of predictions
    print('Variance score: %.2f' % r2_score(test_Y, pred_Y))#Calculates R2 of predictions
