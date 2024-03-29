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

    # explain-string: explanation in english prose
    answers["(a) explain"] = "For example, a person can be both a homeowner and have a low annual income, which means rules 1 and 3 can apply simultaneously"
    answers["(b) explain"] = "There are combinations of attribute values not covered by any rule, such as a person with a medium annual income and not currently employed."
    answers["(c) explain"] = "Because the outcome for a given person could change depending on the order in which the rules are applied. For instance, rules 5 and 7 could potentially conflict depending on the person's attributes."
    answers["(d) explain"] = "a default class is needed for situations where none of the provided rules apply to a person's situation."

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

    # explain_string: explanation in english prose
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
    answers["(c)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) example"] = "because each rule defines a unique combination of attributes that classify vertebrates into distinct categories."
    answers["(b) example"] = "The rules appear to be exhaustive for the given dataset as they cover all possible combinations of the provided attributes."
    answers["(c) example"] = "ordering is necessary because it ensures that the correct classification is applied based on the specific combinations of attributes before any more general rules"

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = "True"
    answers["(b)"] = "True"
    answers["(c)"] = "False"
    answers["(d)"] = "True"

    # explain_string: explanation in english prose
    answers["(a) explain"] = "In the back-propagation algorithm, the gradients of the weights at layer k+1 can indeed be computed using the gradients at layer k. This is because the error derivative with respect to a weight in layer k depends on the derivative of the error with respect to the neuron outputs in layer k+1."
    answers["(b) explain"] = "The activations at nodes in layer k+1 are computed using the outputs (activations) of nodes in layer k as inputs. This is a fundamental aspect of how neural networks propagate information forward from input to output."
    answers["(c) explain"] = "The vanishing gradient problem refers to the issue where gradients become increasingly small as the error is backpropagated through the layers. This makes the weights in the earlier layers change very slowly, if at all, which slows down training or leads to poor convergence. It does not refer to the training errors vanishing to zero while test errors remain large; that scenario is more indicative of overfitting."
    answers["(d) explain"] = "If the ANN model perfectly classifies all training instances at a given iteration, it means the predicted output matches the expected output for every instance, resulting in a zero loss gradient. Consequently, the gradients of loss with respect to weights at all layers will be zero, indicating no error to propagate back through the network."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.72
    answers["(a) P(X_2=1)"] = 0.58
    answers["(a) P(X_1=1,X_2=1)"] = 0.4

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "no"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.5
    answers["(c) P(X_3=1 | -)"] = 0.5

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = "+"
    answers["(d) Row 2"] = "+"
    answers["(d) Row 3"] = "-"
    answers["(d) Row 4"] = "-"

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.0

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "A K of 5 is chosen as it typically offers a good balance between bias and variance, making the model robust to noise and outliers without overfitting or underfitting. It considers enough neighbors to make a reasonable prediction while smoothing out local variations and noise."
    answers["(b) explain"] = "Similar to scenario (a), a K of 5 provides a balanced approach for most datasets capturing the underlying trends without being too sensitive to noise.It's a good starting point that can be adjusted based on cross-validation to achieve better performance specific to the dataset characteristics."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "This probability is calculated as the fraction of positive instances where A=1 over all positive instances."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.657 
    answers["(b) P(R|+)"] = 0.192
    answers["(b) P(R|-)"] = 0.032

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
    answers["(d) P(A=1)"] = 0.4
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.2

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.4
    answers["(e) P(A=1|+)"] = 0.6
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
