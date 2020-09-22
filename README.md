### **Sentiment Analysis**
The aim of this project is to analyses the sentiment of social media twitter data which help to improve the user experience over a social network or system interface. The learning algorithm will learn what are the emotions of the news data present in social media. Using sentiment analysis, we aim to provide excellent performance for real time news data on social media and also provide better results in terms of accuracy.

**Technology Used:**
Machine Learning Algorithm and Natural language processing

**Problem Statement**

The problem at hand consists of two subtasks:

- Sentiment Analysis in Twitter:

_Given a message containing a marked instance of a word or a phrase, determine whether that instance is positive, negative or neutral in that context._

-  Sentence Level Sentiment Analysis :

_Given a message, decide whether the message is of positive, negative, or neutral sentiment. For messages conveying both a positive and negative sentiment, whichever is the stronger sentiment should be chosen._


**GUI** 

![Picture2](https://user-images.githubusercontent.com/32463263/93847300-34eda300-fcc4-11ea-8c9f-e4b0e91ba993.png)

![Picture3](https://user-images.githubusercontent.com/32463263/93847314-3ae38400-fcc4-11ea-9248-f0f53f41ac4d.png)

![Picture4](https://user-images.githubusercontent.com/32463263/93847404-71210380-fcc4-11ea-8da7-ca7e40316187.png)

![Picture5](https://user-images.githubusercontent.com/32463263/93847408-754d2100-fcc4-11ea-990c-a92dcc48bd10.png)

![Picture6](https://user-images.githubusercontent.com/32463263/93847479-a3326580-fcc4-11ea-8c43-c96aca455a8c.png)

![Picture7](https://user-images.githubusercontent.com/32463263/93847486-a9c0dd00-fcc4-11ea-953c-54def10c22b8.png)

![Picture8](https://user-images.githubusercontent.com/32463263/93847538-c78e4200-fcc4-11ea-9abc-0ab2e2b592bf.png)

![Picture9](https://user-images.githubusercontent.com/32463263/93847544-cbba5f80-fcc4-11ea-8363-1bc8fa2b2748.png)

![Picture10](https://user-images.githubusercontent.com/32463263/93847560-d83eb800-fcc4-11ea-8973-2a6dcf135a8b.png)



**Code Snippet**

*Importing various Libraries and other Project Files such as Listed Below*

![image](https://user-images.githubusercontent.com/32463263/93846826-cbb96000-fcc2-11ea-93f6-49b5d6a816b7.png)

*Making A Splash Screen to Introduce the Application Name*

class Splash(Toplevel):
        def __init__(self, parent):
            Toplevel.__init__(self, parent)
            self.title("Welcome")
            self.geometry("500x500+450+100")
            lblwelcome=Label(self, text ="Sentiment Analysis", font = ('arial', 20, 'bold'))
            lblwelcome1=Label(self, text =" Using ", font = ('arial', 20, 'bold'))
            lblwelcome2=Label(self, text =" Machine Learning Algorithm", font = ('arial', 20, 'bold'))
        
            lblwelcome.pack(pady = 1)
            lblwelcome1.pack(pady = 1)
            lblwelcome2.pack(pady = 1)
            
            self.update()

*Building a Root Window (container) as a Base Window*

![Picture11](https://user-images.githubusercontent.com/32463263/93847789-8f3b3380-fcc5-11ea-924d-05212e764a93.png)

*Extracting Tweets From Twitter*

![Picture12](https://user-images.githubusercontent.com/32463263/93847838-b7c32d80-fcc5-11ea-9942-11b19654ba44.png)

*Naive bayes Classifier Implementation.*

![Picture13](https://user-images.githubusercontent.com/32463263/93847879-d9241980-fcc5-11ea-90b3-381cf5320af8.png)


*Plotting A Graph From Classifier Results*

![Picture14](https://user-images.githubusercontent.com/32463263/93847922-ef31da00-fcc5-11ea-873a-3751ec619707.png)


