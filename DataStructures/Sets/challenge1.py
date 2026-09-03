text1 = "Linear regression analysis is used to predict the value of a variable based on the value of another variable. The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable. This form of analysis estimates the"
text2 = "Logistic regression is a supervised machine learning algorithm widely used for binary classification tasks, such as identifying whether an email is spam or not and diagnosing diseases by assessing the presence or absence of specific conditions based on patient test results. This approach utilizes the logistic"


text1_set = text1.split(" ")
text1set = set(text1_set)
text2_set = text2.split(" ")
text2set = set(text2_set)

repeat ={x for x in text1set.intersection(text2set) if len(x) > 3} 
print(repeat)