# voiceAssistant


|Title       |Voice Assictant|
|-----------|---------------|
|**Team**       |Nguyễn Kim Long nguyenkimlong95@gmail.com|
|**Predicting**| I will build a model to answer and support users by voice|
|**Data**| Data link :https://github.com/nguyenkimlong/voiceAssistant/blob/master/intents.json , https://github.com/nguyenkimlong/voiceAssistant/blob/master/data/dialog_talk_agent.xlsx |
|**Features**| 1. Features currently available: tag, patterns, responses. <br /> 2. Regarding tag : Classify the question group. <br /> 3. With the remaining 2 features about patterns and responses : Summary of questions and answers |
|**Models**| We have our training data ready, now we will build a deep neural network that has 3 layers. We use the Keras sequential API for this. After training the model for 200 epochs, we achieved 100% accuracy on our model |
|**Discussion**|We will load the trained model and then use a graphical user interface that will predict the response from the bot. The model will only tell us the class it belongs to, so we will implement some functions which will identify the class and then retrieve us a random response from the list of responses.|
|**Future**|Expand the data further ,expand other missions(ex: auto play music, auto send mail, auto search ...)|
|**References**|https://towardsdatascience.com/gentle-start-to-natural-language-processing-using-python-6e46c07addf3  , https://docs.google.com/presentation/d/1jW5MWBBC9TJsFsOyGMSABtR48ctbVYindQMpYGkPK7I/edit#slide=id.p2 |

          
