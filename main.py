from PyQt5.QtGui import *
from PyQt5.QtWidgets import * #QApplication, QWidget, QLabel, QSlider, QPushButton, QVBoxLayout,
from PyQt5.QtCore import Qt

class RecommenderGUI(QWidget):
    def __init__(self, parent=None):
        super(RecommenderGUI, self).__init__(parent)
        self.setFixedSize(360, 540)

        self.setWindowTitle('Food Recommender')
        layout = QVBoxLayout()

        #label for sweetness slider
        self.sweetLabel = QLabel('Preference for Sweetness')
        self.sweetLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.sweetLabel)

        #sweetness slider & label showing slider's current value
        sweetness = QHBoxLayout()
        self.sweetSlider = QSlider(Qt.Horizontal)
        self.sweetSlider.setMinimum(1)
        self.sweetSlider.setMaximum(10)
        self.sweetSlider.setSingleStep(1)
        self.sweetSlider.setTickPosition(QSlider.TicksBelow)
        self.sweetSlider.valueChanged.connect(self.updateSweetValue)

        self.sweetValue = QLabel('1')
        self.sweetValue.setAlignment(Qt.AlignCenter)

        sweetness.addWidget(self.sweetSlider)
        sweetness.addWidget(self.sweetValue)
        layout.addLayout(sweetness)

        #label for saltiness slider
        self.saltLabel = QLabel('Preference for Saltiness')
        self.saltLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.saltLabel)

        #saltiness slider & label showing slider's current value
        saltiness = QHBoxLayout()
        self.saltSlider = QSlider(Qt.Horizontal)
        self.saltSlider.setMinimum(1)
        self.saltSlider.setMaximum(10)
        self.saltSlider.setSingleStep(1)
        self.saltSlider.setTickPosition(QSlider.TicksBelow)
        self.saltSlider.valueChanged.connect(self.updateSaltValue)

        self.saltValue = QLabel('1')
        self.saltValue.setAlignment(Qt.AlignCenter)

        saltiness.addWidget(self.saltSlider)
        saltiness.addWidget(self.saltValue)
        layout.addLayout(saltiness)

        #label for savoury slider
        self.savouryLabel = QLabel('Preference for Savouriness')
        self.savouryLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.savouryLabel)

        #savouriness slider & label showing slider's current value
        savouriness = QHBoxLayout()
        self.savourySlider = QSlider(Qt.Horizontal)
        self.savourySlider.setMinimum(1)
        self.savourySlider.setMaximum(10)
        self.savourySlider.setSingleStep(1)
        self.savourySlider.setTickPosition(QSlider.TicksBelow)
        self.savourySlider.valueChanged.connect(self.updateSavouryValue)

        self.savouryValue = QLabel('1')
        self.savouryValue.setAlignment(Qt.AlignCenter)

        savouriness.addWidget(self.savourySlider)
        savouriness.addWidget(self.savouryValue)
        layout.addLayout(savouriness)

        self.setLayout(layout)

        #label for meat slider
        self.meatLabel = QLabel('Preference for Meatiness')
        self.meatLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.meatLabel)

        #meatiness slider & label showing slider's current value
        meatiness = QHBoxLayout()
        self.meatSlider = QSlider(Qt.Horizontal)
        self.meatSlider.setMinimum(1)
        self.meatSlider.setMaximum(10)
        self.meatSlider.setSingleStep(1)
        self.meatSlider.setTickPosition(QSlider.TicksBelow)
        self.meatSlider.valueChanged.connect(self.updateMeatValue)

        self.meatValue = QLabel('1')
        self.meatValue.setAlignment(Qt.AlignCenter)

        meatiness.addWidget(self.meatSlider)
        meatiness.addWidget(self.meatValue)
        layout.addLayout(meatiness)

        #label for veg slider
        self.vegLabel = QLabel('Preference for Vegginess')
        self.vegLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.vegLabel)

        #vegginess slider & label showing slider's current value
        vegginess = QHBoxLayout()
        self.vegSlider = QSlider(Qt.Horizontal)
        self.vegSlider.setMinimum(1)
        self.vegSlider.setMaximum(10)
        self.vegSlider.setSingleStep(1)
        self.vegSlider.setTickPosition(QSlider.TicksBelow)
        self.vegSlider.valueChanged.connect(self.updateVegValue)

        self.vegValue = QLabel('1')
        self.vegValue.setAlignment(Qt.AlignCenter)

        vegginess.addWidget(self.vegSlider)
        vegginess.addWidget(self.vegValue)
        layout.addLayout(vegginess)

        #label for crunchiness slider
        self.crunchLabel = QLabel('Preference for Crunchiness')
        self.crunchLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.crunchLabel)

        #crunchiness slider & label showing slider's current value
        crunchiness = QHBoxLayout()
        self.crunchSlider = QSlider(Qt.Horizontal)
        self.crunchSlider.setMinimum(1)
        self.crunchSlider.setMaximum(10)
        self.crunchSlider.setSingleStep(1)
        self.crunchSlider.setTickPosition(QSlider.TicksBelow)
        self.crunchSlider.valueChanged.connect(self.updateCrunchValue)

        self.crunchValue = QLabel('1')
        self.crunchValue.setAlignment(Qt.AlignCenter)

        crunchiness.addWidget(self.crunchSlider)
        crunchiness.addWidget(self.crunchValue)
        layout.addLayout(crunchiness)

        #label for slider spiciness
        self.spiceLabel = QLabel('Preference for Spiciness')
        self.spiceLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.spiceLabel)

        #crunchiness slider & label showing slider's current value
        spiciness = QHBoxLayout()
        self.spiceSlider = QSlider(Qt.Horizontal)
        self.spiceSlider.setMinimum(1)
        self.spiceSlider.setMaximum(10)
        self.spiceSlider.setSingleStep(1)
        self.spiceSlider.setTickPosition(QSlider.TicksBelow)
        self.spiceSlider.valueChanged.connect(self.updateSpiceValue)

        self.spiceValue = QLabel('1')
        self.spiceValue.setAlignment(Qt.AlignCenter)

        spiciness.addWidget(self.spiceSlider)
        spiciness.addWidget(self.spiceValue)
        layout.addLayout(spiciness)

        #submit button
        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.onSubmit)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    # The following are update functions for the different preference metrics
    def updateSweetValue(self):
        newVal = self.sweetSlider.value()
        self.sweetValue.setText(str(newVal))

    def updateSaltValue(self):
        newVal = self.saltSlider.value()
        self.saltValue.setText(str(newVal))

    def updateSavouryValue(self):
        newVal = self.savourySlider.value()
        self.savouryValue.setText(str(newVal))

    def updateMeatValue(self):
        newVal = self.meatSlider.value()
        self.meatValue.setText(str(newVal))

    def updateVegValue(self):
        newVal = self.vegSlider.value()
        self.vegValue.setText(str(newVal))

    def updateCrunchValue(self):
        newVal = self.crunchSlider.value()
        self.crunchValue.setText(str(newVal))

    def updateSpiceValue(self):
        newVal = self.spiceSlider.value()
        self.spiceValue.setText(str(newVal))

    # As we submit, we perform the evaluation based on the inputted values from the frontend
    def onSubmit(self):
        perform_eval_from_gui({
            "Sweetness": self.sweetSlider.value(),
            "Saltiness": self.saltSlider.value(),
            "Savouriness": self.savourySlider.value(),
            "Meat": self.meatSlider.value(),
            "Vegetarian": self.vegSlider.value(),
            "Crunchiness": self.crunchSlider.value(),
            "Spiciness": self.spiceSlider.value()
         })

    def updateResultLabel(self, dish, value):
        self.resultLabel.setText('Based on user preference, the best dish is:', dish)

class Rule():

   # the init sets the structure of each rule that will be used for the inference system.
   # The antecedents will be used to capture the user preference membershipsl, while the consequent
   # the preference of a specific meal, such as low preference for burger for a specific rule. The
   # set name will be used to describe the meal that the rule belongs to for categorization purposes of software
   def __init__(self, antecedent, consequent, set_name = ""):
      self.antecedents = antecedent
      self.consequent = consequent
      self.set_name = set_name

# This class will be used to describe the graph of each antecedent and consequent, along with calculations
# for determining the membership values of the specific graph and the area average of the specific graph
class Graph_Details():

   # initiate x and y axis of the graph, along with the type of graph that it is, such as low, medium and high. This
   # will be used to describe the graph for either the antecedent or consequent
   def __init__(self, x_axis, y_axis, set_name = "", type = ""):
      self.x_axis = x_axis
      self.y_axis = y_axis
      self.set_name = set_name

      # depending on what type of graph it is, calculate the area average based on height of membership
      if type == "Low":
         self.graph_classifier = self.lowGraphCalc
      elif type == "Medium":
         self.graph_classifier = self.medGraphCalc
      else:
         self.graph_classifier = self.highGraphCalc

   def lowGraphCalc(self, height):
      x_axis = self.x_axis

      rect_area = (x_axis[1] - x_axis[0]) * height
      rect_center_point = (x_axis[0] + x_axis[1]) / 2
      triangle_area = (x_axis[2] - x_axis[1]) * height / 2
      triangle_center_point = x_axis[1] + (x_axis[2] - x_axis[1]) / 3

      return get_area_avg( [(rect_center_point, rect_area), (triangle_center_point, triangle_area)])

   def highGraphCalc(self, height):
      x_axis = self.x_axis

      rect_area = (x_axis[3] - x_axis[2]) * height
      rect_center_point = (x_axis[2] + x_axis[3]) / 2
      triangle_area = (x_axis[2] - x_axis[1]) * height / 2
      triangle_center_point = x_axis[1] + (x_axis[2] - x_axis[1]) * 2 / 3

      return get_area_avg( [(rect_center_point, rect_area), (triangle_center_point, triangle_area)])


   def medGraphCalc(self, height):
      x_axis = self.x_axis

      left_triangle_area = (x_axis[2]-x_axis[1]) * height / 2
      left_tri_center_point = x_axis[1] + (x_axis[2]-x_axis[1]) * 2 / 3
      rect_area = (x_axis[3] - x_axis[2]) * height
      rect_center_point = (x_axis[3] + x_axis[2]) / 2
      right_triangle_area = (x_axis[4] - x_axis[3]) * height / 2
      right_triangle_center_point = x_axis[3] + (x_axis[4]-x_axis[3]) / 3

      return get_area_avg( [(left_triangle_area, left_tri_center_point), (rect_center_point, rect_area), (right_triangle_center_point, right_triangle_area)] )

   # determine the membership of the current graph based on the point of the graph
   def membership(self, point_on_graph):
      x_axis = self.x_axis
      y_axis = self.y_axis

      pos = 1
      for i in range(1, len(x_axis)):
        if x_axis[i] >= point_on_graph:
            pos = i
            break

      if pos == 1:
        pos = len(x_axis) - 1

      slope = (y_axis[pos] - y_axis[pos - 1]) / (x_axis[pos] - x_axis[pos - 1])
      return y_axis[pos - 1] + slope*(point_on_graph - x_axis[pos - 1])

def evaluate_rule(expression, user_inputs):
    # if the left part of the expression is a rule, get its weighted average with the user input, else if it is another expression then recursively call evaluate_rule
    left = expression[1]
    if isinstance(left, Graph_Details):
        left_membership = left.membership(user_inputs[left.set_name])
    else:
       left_membership =  evaluate_rule(left, user_inputs)
    
    # if the right part of the expression is a rule, get its weighted average with the user input, else if it is another expression then recursively call evaluate_rule
    right = expression[2]
    if isinstance(right, Graph_Details):
        right_membership = right.membership(user_inputs[right.set_name])
    else:
        right_membership =  evaluate_rule(right, user_inputs)
   
   # if the expression is a conjunction (AND) take the min of left and right weighted average, if it's a disjunction (OR) take the max
    result = min(left_membership, right_membership) if expression[0] == 'AND' else max(left_membership, right_membership)
    return result

def get_area_avg(area_arr):
   weight = 0
   values = 0

   for tuple in area_arr:
      values += tuple[0] * tuple[1]
      weight += tuple[1]

   if weight == 0:
      return (0,0)
   else:
      return (values / weight, weight)

# determines the centroid value based on the rules array. For an instance,
# determine the centroid of low and high burger preference to establish the
# final score of burger
def final_output(rule_arr, height_caps):
   results = []
   for i in range(len(rule_arr)):
      results.append(rule_arr[i].consequent.graph_classifier(height_caps[i]))

   return get_area_avg(results)

# This function takes the user inputs and then determines the best meals based on the preferences selected
def perform_eval_from_gui(user_inputs):
    dish_outcome = {}
    for dish, rule_set in all_rules.items():
        height_caps = []
        for rule in rule_set:
            height_caps.append(evaluate_rule(rule.antecedents, user_inputs))
        dish_outcome[dish] = round(final_output(rule_set, height_caps)[0], 2)

    # we then take the best 3 dishes, where higher score equals better and then display it for the user
    best_dish = sorted(dish_outcome.items(), key = lambda dish : dish[1], reverse=True)
    result = QMessageBox()
    result.setWindowTitle('Top 3 Dishes')
    result.setText('Best dish: {} - Dish ranking: {} \nSecond best dish: {} - Dish ranking: {} \nThird best dish: {} - Dish ranking: {}'.format(best_dish[0][0], best_dish[0][1], best_dish[1][0], best_dish[1][1], best_dish[2][0], best_dish[2][1]))
    result.exec_()

if __name__ == '__main__':

    #declaring the RecommenderGUI instance
    app = QApplication([])
    window = RecommenderGUI()

    # membership functions for sweetness
    x_low_sweetness = [0,1,9,10]
    y_low_sweetness = [1,1,0.1,0.1]
    sweetness_Low = Graph_Details(x_low_sweetness, y_low_sweetness, set_name = "Sweetness", type = "Low")

    x_med_sweetness = [0,1,4.5,5.5,9,10]
    y_med_sweetness = [0.1,0.1,1,1,0.1,0.1]
    sweetness_Med = Graph_Details(x_med_sweetness, y_med_sweetness, set_name = "Sweetness", type = "Medium")

    x_high_sweetness = [0,1,9,10]
    y_high_sweetness = [0.1,0.1,1,1]
    sweetness_High = Graph_Details(x_high_sweetness, y_high_sweetness, set_name = "Sweetness", type = "High")


    # membership functions for saltiness
    x_low_saltiness = [0,1,9,10]
    y_low_saltiness = [1, 1, 0.1, 0.1]
    saltiness_Low = Graph_Details(x_low_saltiness, y_low_saltiness, set_name = "Saltiness", type = "Low")

    x_med_saltiness = [0,1,4.5,5.5,9,10]
    y_med_saltiness = [0.1,0.1,1,1,0.1,0.1]
    saltiness_Med = Graph_Details(x_med_saltiness, y_med_saltiness, set_name = "Saltiness", type = "Medium")

    x_high_saltiness = [0,1,9,10]
    y_high_saltiness = [0.1, 0.1, 1, 1]
    saltiness_High = Graph_Details(x_high_saltiness, y_high_saltiness, set_name = "Saltiness", type = "High")

    # membership functions for savouriness
    x_low_savouriness = [0,1,9,10]
    y_low_savouriness = [1,1,0.1,0.1]
    savouriness_Low = Graph_Details(x_low_savouriness, y_low_savouriness, set_name = "Savouriness", type = "Low")

    x_med_savouriness = [0,1,4.5,5.5,9,10]
    y_med_savouriness = [0.1,0.1,1,1,0.1,0.1]
    savouriness_Med = Graph_Details(x_med_savouriness, y_med_savouriness, set_name = "Savouriness", type = "Medium")

    x_high_savouriness = [0,1,9,10]
    y_high_savouriness = [0.1,0.1,1,1]
    savouriness_High = Graph_Details(x_high_savouriness, y_high_savouriness, set_name = "Savouriness", type = "High")

    # membership functions for meat based preference
    x_low_meat = [0,1,9,10]
    y_low_meat = [1,1,0.1,0.1]
    meat_Low = Graph_Details(x_low_meat, y_low_meat, set_name = "Meat", type = "Low")

    x_med_meat = [0,1,4.5,5.5,9,10]
    y_med_meat = [0.1,0.1,1,1,0.1,0.1]
    meat_Med = Graph_Details(x_med_meat, y_med_meat, set_name = "Meat", type = "Medium")

    x_high_meat = [0,1,9,10]
    y_high_meat = [0.1,0.1,1,1]
    meat_High = Graph_Details(x_high_meat, y_high_meat, set_name = "Meat", type = "High")

    # membership functions for vegetarian based preference
    x_low_vegetarian = [0,1,9,10]
    y_low_vegetarian = [1,1,0.1,0.1]
    vegetarian_Low = Graph_Details(x_low_vegetarian, y_low_vegetarian, set_name = "Vegetarian", type = "Low")

    x_med_vegetarian = [0,1,4.5,5.5,9,10]
    y_med_vegetarian = [0.1,0.1,1,1,0.1,0.1]
    vegetarian_Med = Graph_Details(x_med_vegetarian, y_med_vegetarian, set_name = "Vegetarian", type = "Medium")

    x_high_vegetarian = [0,1,9,10]
    y_high_vegetarian = [0.1,0.1,1,1]
    vegetarian_High = Graph_Details(x_high_vegetarian, y_high_vegetarian, set_name = "Vegetarian", type = "High")

    # membership functions for crunchiness based preference
    x_low_crunch = [0,1,9,10]
    y_low_crunch = [1,1,0.1,0.1]
    crunch_Low = Graph_Details(x_low_crunch, y_low_crunch, set_name = "Crunchiness", type = "Low")

    x_med_crunch = [0,1,4.5,5.5,9,10]
    y_med_crunch = [0.1,0.1,1,1,0.1,0.1]
    crunch_Med = Graph_Details(x_med_crunch, y_med_crunch, set_name = "Crunchiness", type = "Medium")

    x_high_crunch = [0,1,9,10]
    y_high_crunch = [0.1,0.1,1,1]
    crunch_High = Graph_Details(x_high_crunch, y_high_crunch, set_name = "Crunchiness", type = "High")

    # membership functions for vegetarian based preference
    x_low_spice = [0,1,9,10]
    y_low_spice = [1,1,0.1,0.1]
    spice_Low = Graph_Details(x_low_spice, y_low_spice, set_name = "Spiciness", type = "Low")

    x_med_spice = [0,1,4.5,5.5,9,10]
    y_med_spice = [0.1,0.1,1,1,0.1,0.1]
    spice_Med = Graph_Details(x_med_spice, y_med_spice, set_name = "Spiciness", type = "Medium")

    x_high_spice = [0,1,9,10]
    y_high_spice = [0.1,0.1,1,1]
    spice_High = Graph_Details(x_high_spice, y_high_spice, set_name = "Spiciness", type = "High")

    # membership functions for Burger
    x_low_burger= [0,2,5,10]
    y_low_burger= [1,1,0.1,0.1]
    burger_Low = Graph_Details(x_low_burger, y_low_burger, set_name = "Burger", type = "Low")

    x_high_burger= [0,5,8,10]
    y_high_burger = [0.1,0.1,1,1]
    burger_High = Graph_Details(x_high_burger, y_high_burger, set_name = "Burger", type = "High")

    # membership functions for Fries
    max_fries = 10
    x_low_fries = [0,2,5,10]
    y_low_fries = [1,1,0.1,0.1]
    fries_Low = Graph_Details(x_low_fries, y_low_fries, set_name = "Fries", type = "Low")

    x_high_fries = [0,5,8,10]
    y_high_fries = [0.1,0.1,1,1]
    fries_High = Graph_Details(x_high_fries, y_high_fries, set_name = "Fries", type = "High")

    # membership functions for Caesar Salad
    max_caesar_salad = 10
    x_low_caesar_salad = [0,2,5,10]
    y_low_caesar_salad = [1,1,0.1,0.1]
    caesar_salad_Low = Graph_Details(x_low_caesar_salad, y_low_caesar_salad, set_name = "Caesar Salad", type = "Low")

    x_high_caesar_salad = [0,5,8,10]
    y_high_caesar_salad = [0.1,0.1,1,1]
    caesar_salad_High = Graph_Details(x_high_caesar_salad, y_high_caesar_salad, set_name = "Caesar Salad", type = "High")

    # membership functions for Waffles
    max_waffles = 10
    x_low_waffles = [0,2,5,10]
    y_low_waffles = [1,1,0.1,0.1]
    waffles_Low = Graph_Details(x_low_waffles, y_low_waffles, set_name = "Waffles",  type = "Low")

    x_high_waffles = [0,5,8,10]
    y_high_waffles = [0.1,0.1,1,1]
    waffles_High = Graph_Details(x_high_waffles, y_high_waffles, set_name = "Waffles",  type = "High")

    # membership functions for Fruit Salad
    max_fruit_salad = 10
    x_low_fruit_salad = [0,2,5,10]
    y_low_fruit_salad = [1,1,0.1,0.1]
    fruit_salad_Low = Graph_Details(x_low_fruit_salad, y_low_fruit_salad, set_name = "Fruit Salad",  type = "Low")

    x_high_fruit_salad = [0,5,8,10]
    y_high_fruit_salad = [0.1,0.1,1,1]
    fruit_salad_High = Graph_Details(x_high_fruit_salad, y_high_fruit_salad, set_name = "Fruit Salad",  type = "High")

    # membership functions for Spaghetti
    max_spaghetti = 10
    x_low_spaghetti = [0,2,5,10]
    y_low_spaghetti = [1,1,0.1,0.1]
    spaghetti_Low = Graph_Details(x_low_spaghetti, y_low_spaghetti, set_name = "Spaghetti", type = "Low")

    x_high_spaghetti = [0,5,8,10]
    y_high_spaghetti = [0.1,0.1,1,1]
    spaghetti_High = Graph_Details(x_high_spaghetti, y_high_spaghetti, set_name = "Spaghetti", type = "High")

    # membership functions for Spicy Burrito
    max_spicy_burrito = 10
    x_low_spicy_burrito = [0,2,5,10]
    y_low_spicy_burrito = [1,1,0.1,0.1]
    spicy_burrito_Low = Graph_Details(x_low_spicy_burrito, y_low_spicy_burrito, set_name = "Spicy Burrito", type = "Low")

    x_high_spicy_burrito = [0,5,8,10]
    y_high_spicy_burrito = [0.1,0.1,1,1]
    spicy_burrito_High = Graph_Details(x_high_spicy_burrito, y_high_spicy_burrito, set_name = "Spicy Burrito", type = "High")

    # membership functions for Vegetarian Sushi
    max_sushi = 10
    x_low_sushi = [0,2,5,10]
    y_low_sushi = [1,1,0.1,0.1]
    sushi_Low = Graph_Details(x_low_sushi, y_low_sushi, set_name = "Vegetarian Sushi", type = "Low")

    x_high_sushi = [0,5,8,10]
    y_high_sushi = [0.1,0.1,1,1]
    sushi_High = Graph_Details(x_high_sushi, y_high_sushi, set_name = "Vegetarian Sushi", type = "High")

    # membership functions for Curry
    max_curry = 10
    x_low_curry = [0,2,5,10]
    y_low_curry = [1,1,0.1,0.1]
    curry_Low = Graph_Details(x_low_curry, y_low_curry, set_name = "Curry", type = "Low")

    x_high_curry = [0,5,8,10]
    y_high_curry = [0.1,0.1,1,1]
    curry_High = Graph_Details(x_high_curry, y_high_curry, set_name = "Curry", type = "High")

    # antecedents are constructed using LISP syntax, i.e. ('LOGIC_OPERATOR', right_expression, left_expression)
    Burger_Low_Pref = Rule(('AND', savouriness_Low, ('AND', meat_Low, ('AND', vegetarian_High, spice_High))), burger_Low, set_name = "Burger")
    Burger_High_Pref = Rule(('AND', savouriness_High, ('AND', vegetarian_Low, ('AND', spice_Low, ('OR', meat_Med, meat_High)))), burger_High, set_name = "Burger")

    Fries_Low_Pref = Rule(('AND', sweetness_High, ('AND', saltiness_Low, ('AND', savouriness_Low, crunch_Low))), fries_Low, set_name = "Fries")
    Fries_High_Pref = Rule(('AND', savouriness_High, ('AND', sweetness_Low, ('AND', saltiness_High, ('AND', crunch_High, ('OR', meat_Low, meat_Med))))), fries_High, set_name = "Fries")

    Caesar_Salad_Low_Pref = Rule(('AND', meat_High, ('AND', vegetarian_Low, ('AND', saltiness_High, spice_High))), caesar_salad_Low, set_name = "Caesar Salad")
    Caesar_Salad_High_Pref = Rule(('AND', savouriness_Med, ('AND', vegetarian_High, ('AND', meat_Low, crunch_Med))), caesar_salad_High, set_name = "Caesar Salad")

    Waffles_Low_Pref = Rule(('AND', sweetness_Low, ('AND', saltiness_Med, ('AND', spice_High, ('OR', meat_High, meat_Med)))), waffles_Low, set_name = "Waffles")
    Waffles_High_Pref = Rule(('AND', sweetness_High, ('AND', saltiness_Low, meat_Low)), waffles_High, set_name = "Waffles")

    Fruit_Salad_Low_Pref = Rule(('AND', vegetarian_Low, ('AND', sweetness_Low, ('AND', spice_High, ('OR', meat_Med, meat_High)))), fruit_salad_Low, set_name = "Fruit Salad")
    Fruit_Salad_High_Pref = Rule(('AND', sweetness_Med, ('AND', meat_Low, vegetarian_High)), fruit_salad_High, set_name = "Fruit Salad")

    Spaghetti_Low_Pref = Rule(('AND', sweetness_High, ('AND', savouriness_Low, vegetarian_High)), spaghetti_Low, set_name = "Spicy Burrito")
    Spaghetti_High_Pref = Rule(('AND', savouriness_Med, ('AND', sweetness_Low, ('OR', meat_High, meat_Med))), spaghetti_High, set_name = "Spicy Burrito")

    Spicy_Burrito_Low_Pref = Rule(('AND', sweetness_High, ('AND', savouriness_Low, ('AND', meat_Low, ('AND', spice_Low, sweetness_High)))), spicy_burrito_Low, set_name = "Spicy Burrito")
    Spicy_Burrito_High_Pref = Rule(('AND', savouriness_High, ('AND', sweetness_Low, ('AND', spice_High, ('AND', saltiness_High, ('OR', meat_High, meat_Med))))), spicy_burrito_High, set_name = "Spicy Burrito")

    Sushi_Low_Pref = Rule(('AND', crunch_High, ('AND', sweetness_High,vegetarian_Low)), sushi_Low, set_name = "Vegetarian Sushi")
    Sushi_High_Pref = Rule(('AND', vegetarian_High, ('AND', sweetness_Low, ('AND', saltiness_Med, ('AND', crunch_Low, meat_Low)))), sushi_High, set_name = "Vegetarian Sushi")

    Curry_Low_Pref = Rule(('AND', savouriness_Low, ('AND', spice_Low, crunch_Low)), curry_Low, set_name = "Curry")
    Curry_High_Pref = Rule(('AND', savouriness_High, ('AND', spice_High, ('AND', meat_Med, vegetarian_Med))), curry_High, set_name = "Curry")

    # we then generate the rule sets of each meal in order to determine the centroid score of each dish, which
    # then allows us to rank them
    Burger_Rule_Set = [Burger_Low_Pref, Burger_High_Pref]
    Fries_Rule_Set = [Fries_Low_Pref, Fries_High_Pref]
    Caesar_Salad_Rule_Set = [Caesar_Salad_Low_Pref, Caesar_Salad_High_Pref]
    Waffles_Rule_Set = [Waffles_Low_Pref, Waffles_High_Pref]
    Fruit_Salad_Rule_Set = [Fruit_Salad_Low_Pref, Fruit_Salad_High_Pref]
    Spaghetti_Rule_Set = [Spaghetti_Low_Pref, Spaghetti_High_Pref]
    Spicy_Burrito_Rule_Set = [Spicy_Burrito_Low_Pref, Spicy_Burrito_High_Pref]
    Sushi_Rule_Set = [Sushi_Low_Pref, Sushi_High_Pref]
    Curry_Rule_Set = [Curry_Low_Pref, Curry_High_Pref]

    all_rules = {
        "Burger": Burger_Rule_Set,
        "Fries": Fries_Rule_Set,
        "Caesar Salad": Caesar_Salad_Rule_Set,
        "Waffles": Waffles_Rule_Set,
        "Fruit Salad": Fruit_Salad_Rule_Set,
        "Spaghetti": Spaghetti_Rule_Set,
        "Spicy Burrito": Spicy_Burrito_Rule_Set,
        "Vegetarian Sushi": Sushi_Rule_Set,
        "Curry": Curry_Rule_Set
        }

    window.show()
    app.exec_()
