# Twitter-API-Visualization

This project uses a Twitter API to retrieve data from tweets associated with a particular keyword. It then plots and saves a figure depiciting the length of each tweet vs the number of retweets, using Plotly on Python. In order to access tweet data using the Twitter API, you will need to setup a Twitter Developer account. Save your credentials associated with your Twitter app by running the save_credentials.py file.

To run the main file, use: (We search for tweets containing the keyword --Elon Musk, for example)
python main.py --keyword ElonMusk --count 20

The resulting figure is:
![newplot](https://user-images.githubusercontent.com/61554410/189499491-fe6eaa97-9540-4a5a-aad3-8ec60aa5d390.png)
