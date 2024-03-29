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

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = None
    answers["(a) P(X_2=1)"] = None
    answers["(a) P(X_1=1,X_2=1)"] = None

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = None

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = None

    # float
    answers["(c) P(X_1=1 | +)"] = None
    answers["(c) P(X_1=1 | -)"] = None
    answers["(c) P(X_2=1 | +)"] = None
    answers["(c) P(X_2=1 | -)"] = None
    answers["(c) P(X_3=1 | +)"] = None
    answers["(c) P(X_3=1 | -)"] = None

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = None
    answers["(d) Row 2"] = None
    answers["(d) Row 3"] = None
    answers["(d) Row 4"] = None

    # float between 0 and 1
    answers["(d) Training error rate"] = None

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = None
    answers["(b) K"] = None

    # explain_string
    answers["(a) explain"] = None
    answers["(b) explain"] = None

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = None
    answers["(a) P(B=1|+)"] = None
    answers["(a) P(C=1|+)"] = None
    answers["(a) P(A=1|-)"] = None
    answers["(a) P(B=1|-)"] = None
    answers["(a) P(C=1|-)"] = None

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = None
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = None 
    answers["(b) P(R|+)"] = None
    answers["(b) P(R|-)"] = None

    # string, '+' or '-'
    answers["(b) class label"] = None

    # explain_string
    answers["(b) Explain your reasoning"] = None
  
    # float
    answers["(c) P(A=1)"] = None
    answers["(c) P(B=1)"] = None
    answers["(c) P(A=1,B=1)"] = None

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = None
  
    # type: float
    answers["(d) P(A=1)"] = None
    answers["(d) P(B=0)"] = None
    answers["(d) P(A=1,B=0)"] = None

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = None
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = None
    answers["(e) P(A=1|+)"] = None
    answers["(e) P(B=1|+)"] = None

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = None

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  None
  
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
