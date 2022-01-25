import pyinputplus as pyip

def sandwichMaker():

    Menu = {
        'bread' :   {   'wheat'     :   1.00,
                        'white'     :   1.00,
                        'sourdough' :   1.50    },

        'protein' : {   'chicken'   :   1.50,
                        'turkey'    :   2.00,
                        'ham'       :   1.50,
                        'tofu'      :   1.00    },
        
        'cheese' : {   'cheddar'    :   1.50,
                        'Swiss'     :   1.50,
                        'mozzarella':   1.00  },

        'toppings' : {  'mayo'      :   0.20, 
                        'mustard'   :   0.20, 
                        'lettuce'   :   0.50, 
                        'tomato'    :   1.00  }
    }

    orderPrice = 0

    prompt1 = 'Choose bread type:\n'
    orderPrice += Menu['bread'][pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt1)] 
    
    prompt2 = 'Choose protein type:\n'
    orderPrice += Menu['protein'] [pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt2)]
    
    if pyip.inputYesNo("Cheese?") == 'yes':
        orderPrice += Menu['cheese'][pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])]
    
    for topping in ['mayo', 'mustard', 'lettuce', 'tomato']:
        if pyip.inputYesNo('%s?' % (topping.capitalize())) == 'yes':
            orderPrice += Menu['toppings'][topping]
    
    prompt3 = 'How many Sandwiches?\n'
    orderPrice *= pyip.inputInt(prompt3, min=1)

    print('Total cost: %s$' % (round(orderPrice, 2)))

sandwichMaker()
