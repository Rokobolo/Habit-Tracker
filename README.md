# Habit-Tracker
First major personal project: Habit Tracker with Interface

# What is it?
So this project is actually from day 37 of my python course. The original project was to simply write codes to see how to use API further.
The project was fun to build, but the original final product required me to go back to the code and make edits everytime I needed to use a different function.<br />
With this in mind, I decided to build a simple UI for it and readjust the code so everything fits.
It's simple and a bit redundant in some places, but the main goal was to put knowledge together and makes something that works.

# What does it do?
- Obviously, it will track your habits.

# How does it do it?
- The project is containing 3 files:
     - main.py: Which just consolidates the rest
     -  pixela.py: Where the magic operates
     -  ui.py: Where the interface is built
<br />
- When launching the app, you will have 3 different options. If it's the first time you use the app, you will need to create an account.

![image](https://github.com/Rokobolo/Habit-Tracker/assets/139471568/a6ca3734-5ee7-483c-829b-68e916d06677)

## Step 1: Create an account:
- This first menu looks like this:

![image](https://github.com/Rokobolo/Habit-Tracker/assets/139471568/05a5b138-eba3-44cc-a5fa-4decc6e9e9d6)

- Enter a valid user name and password, then click on Create.
- If your data isn't valid, a pop-up window will appear:

![image](https://github.com/Rokobolo/Habit-Tracker/assets/139471568/ff3609a6-d4f8-4ea3-a8a4-b95272fdbca7)

- There are several error messages based on the response, the box just use the server response text as its content.
- If you successfuly enter valid data, the pop up will open with a link to your profile as well as opening the page directly in your browser.
     - The app doesn't save data for you (username, password)

![image](https://github.com/Rokobolo/Habit-Tracker/assets/139471568/3d3d4cd6-006f-455c-b494-ec8a0044ded5)

## Step 2: Create a Graph:

![image](https://github.com/Rokobolo/Habit-Tracker/assets/139471568/031b04d0-39d1-4385-8d9d-87de241c7209)

To create a graph you will need to have an account first, if it is not done, be sure to go back and create one.

- Unique ID: this is an ID that you will need to re-use to update the graph (it will be visible on the graph page)
- Graph name: Pick a name for the graph
- Unit measure: Choose a unit measure, can be anything
