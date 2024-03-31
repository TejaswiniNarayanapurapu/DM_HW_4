# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in English prose
    answers["(a) explain"] = "For example, a person can be both a homeowner and he can have a low annual income, which says rules 1 and 3 can apply simultaneously"
    answers["(b) explain"] = "There are also combinations of different attribute values not covered by any rule, such as that a person with a medium annual income and not being currently employed."
    answers["(c) explain"] = "It is because the outcome for a given person may change depending on the order in which the rule is applied. For Instance, rules 5 and 7 might  conflict depending on the person's attributes."
    answers["(d) explain"] = "The default class is needed for instances where none of the provided rules apply to a person's situation."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in English prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "yes"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "because each rule defines the  unique combination of attributes that classify vertebrates into distinct categories."
    answers["(b) example"] = "The rules appear to be exhaustive for the given dataset as they cover all possible combinations of the provided attributes."
    answers["(c) example"] = "ordering is not necessary because  the rules for vertebrate classification, as described as mutually exclusive and exhaustive, each rule applies to distinct set of conditions without overlap"

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = "True"
    answers["(b)"] = "True"
    answers["(c)"] = "False"
    answers["(d)"] = "True"

    # explain_string: explanation in English prose
    answers["(a) explain"] = "In the back-propagation algorithm, the gradients of the weights at layer k+1 can indeed be computed using the gradients at layer k. This is because the error derivative with respect to a weight in layer k depends on the derivative of the error with respect to the neuron outputs in layer k+1."
    answers["(b) explain"] = "The activations at nodes in layer k+1 are computed using the outputs (activations) of nodes in layer k as inputs. This is a fundamental aspect of how neural networks propagate information forward from input to output."
    answers["(c) explain"] = "The vanishing gradient problem refers to the issue where gradients become increasingly small as the error is backpropagated through the layers. This makes the weights in the earlier layers change very slowly, if at all, which slows down training or leads to poor convergence. It does not refer to the training errors vanishing to zero while test errors remain large; that scenario is more indicative of overfitting."
    answers["(d) explain"] = "If the ANN model perfectly classifies all training instances at a given iteration, it means the predicted output matches the expected output for every instance, resulting in a zero loss gradient. Consequently, the gradients of loss with respect to weights at all layers will be zero, indicating no error to propagate back through the network."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = "+"
    answers["(d) Row 2"] = "-"
    answers["(d) Row 3"] = "-"
    answers["(d) Row 4"] = "-"

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "Th data points are separated by well, this is why k = 1 or 5 fits well"
    answers["(b) explain"] = "Due to lot of overlap in data points, we have to select a modest k value which could result in a induced misclassification"
    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.4
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.6
    answers["(a) P(A=1|-)"] = 0.2
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "This probability is calculated as the fraction of positive instances where A=1 over all positive instances."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1 
    answers["(b) P(R|+)"] = 0.096
    answers["(b) P(R|-)"] = 0

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "The class label '+' has a higher normalized probability for the given sample R, indicating it's more likely to be positive."
  
    # float
    answers["(c) P(A=1)"] = 0.4
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "yes"
  
    # type: float
    answers["(d) P(A=1)"] = 0.3
    answers["(d) P(B=0)"] = 0.2
    answers["(d) P(A=1,B=0)"] = 0.1

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "no"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.4
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "Since P(A=1,B=1|+) does not equal the product of P(A=1|+) and P(B=1|+), A and B are not conditionally independent given the class +."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
