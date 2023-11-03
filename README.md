# Habit-Tracker
First major personal project: Habit Tracker with Interface

# What is it?
So this project is actually from day 37 of my python course. The original project was to simply write codes to see how to use API further.
The project uses the [PIXELA API](https://docs.pixe.la/) to track habits into a graph similar to the one used on Github. 
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

![image](https://github.com/Rokobolo/Habit-Tracker/assets/139471568/ef58e0d4-5ade-4540-8126-a4b2c23cfc61)

To create a graph you will need to have an account first, if it is not done, be sure to go back and create one.

- Unique ID: this is an ID that you will need to re-use to update the graph (it will be visible on the graph page)
- Graph name: Pick a name for the graph
- Unit measure: Choose a unit measure, can be anything
- Weight: Choose if you want it to be integer or decimals (based on your Unit measure)
- Color: Pick a color from the drop down list.
<br />
Same as the first menu, pop-ups will appear if something is missing or wrong with details. Once all the correct data are entered you will be redirected to the newly created graph in the browser.

## Step 3: Update the graph:

![image](https://github.com/Rokobolo/Habit-Tracker/assets/139471568/16519100-8221-4bb9-b171-e4e32b67b041)

To fill the graph with data you will now need to Update the pixel:

- User Name and Password: The one you used when creating your account.
- Unique ID: The ID you chose for the graph you want to update.
- Date: The date is prepopulated with today's date, but you can edit it to update the graph on another day. (format: YYYYMMDD).
- Quantity: Enter the amount you want to update the graph with.

Same as the others, pop-ups will appear based on the result. <br />
It is important to note that if you update an already existing pixel, it will overwrite it. You can reset a pixel by inputing "0" for that date.

![image](https://github.com/Rokobolo/Habit-Tracker/assets/139471568/2fdeda43-16f4-4789-8253-745d5d598b97)

# Testing the software
While building the software, I wanted to ensure that everything was working. To ensure nothing was amiss, I made sure to build a test case on the fly as I was typing my code. I ran the test case few times at important moments of the process to make sure the code was working (or not) as intended.

![image](https://github.com/Rokobolo/Habit-Tracker/assets/139471568/a916a345-3039-4146-8030-02e501d2bee8)
