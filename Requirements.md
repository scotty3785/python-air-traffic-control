## CORE REQUIREMENTS ##
This section details the required functionality of the ATC project that will be implemented for the initial software release.

### 1.1	Deliverable ###

The delivered product shall be a single-player computer game.
### 1.2	Game objective ###
The game shall run for 3 minutes.
The objective for the player of the game shall be to maximise his or her score within the time limit, using the scoring system below.
### 1.3	Display contents ###
The screen shall be split into a square aerial view on the left side of the screen, and an information/control pane on the right side of the screen.
The square left hand pane shall contain a top-down view of an air space in a “wireframe” format – i.e. textured backgrounds are not required.
The 2D airspace shall contain 6-8 randomly placed destination points which shall be represented by circles, one of which shall be the airport and will have “AIRPORT” in small letters next to it.
The information/control pane shall be split into 2 parts:- the upper 1/6th will contain a panel displaying the game time remaining, and the player’s current score. The bottom panel shall contain a list of flight strips.
The 2D airspace shall contain a number of the following various obstacles arranged in random positions on the screen:- no fly zones, weather patterns and mountains.
The number and placement of obstacles shall be appropriate to ensure the game is challenging enough but solvable.
Aircraft shall be represented by wireframe icons.
Obstacles shall be represented by wireframe polygons.
### 1.4	Aircraft characteristics ###
Aircraft will appear on the display at points around the edge.
Each aircraft will have an identifier e.g. “A”, “B” etc and this shall be displayed in small characters next to the aircraft icon.
Each aircraft’s heading shall initially be towards its intended destination, regardless of any obstacles that might be in the way.
Each aircraft’s speed shall initially be randomly selected between 200 knots and 400 knots.
Each aircraft will have a destination that is near the furthest side of the airspace from its initial starting point, to avoid aircraft reaching destinations too quickly.
Each aircraft shall have a minimum separation distance with other aircraft, represented as a circle around the aircraft – its minimum separation radius. This circle shall either be drawn on the screen or invisible depending on a configuration option.
Each aircraft shall have a corresponding flight strip in the flight strip pane.
Each aircraft’s corresponding flight strip shall have that aircraft’s identifier within it.
### 1.5	Controlling aircraft ###
The user shall select aircraft by either clicking its icon, or clicking its corresponding flight strip.
Once an aircraft is selected, it and its flight strip shall change colour to signify to the user that it is selected.
Once an aircraft is selected, its flight path shall appear as a line on the 2D aerial view.
The user will be able to click on the line to create a waypoint, and then drag and drop that waypoint to change the flight path of the selected aircraft.
To deselect an aircraft, the user shall either select another aircraft by clicking it or its flight strip, or click an empty area of the 2D view.
If an aircraft is deselected, its flight path line shall be invisible and its colour shall return to the default colour.
### 1.6	Scoring system ###
The player shall be awarded 100 points for each correctly routed aircraft.
The player shall be penalised 50 points for routing an aircraft to an incorrect destination.
The player shall be penalised 25 points each time an aircraft is routed through an obstacle or comes within the minimum separation radius of another aircraft.

## 2.	EXTENDED REQUIREMENTS ##
This section details the features of the software that will be implemented if and only if time allows. Implementation of the features in this section is also subject to agreement by the ATC software team.
### 2.1	Variable speed ###
The user shall be able to control the speed of regular aircraft, between bounds of 200 knots and 500 knots, in discrete steps of 50 knots.
### 2.2	Variable altitude ###
The user shall be able to control the altitude of regular aircraft between predetermined bounds. The selectable altitudes shall be at discrete intervals (e.g. 1000 feet)
### 2.3	Score notification ###
On reaching a destination point, the aircraft shall disappear and a small notice shall pop up next to the destination for a few seconds notifying the user of the amount of points they have scored (e.g. +100).
### 2.4	Military aircraft ###
Military aircraft are not under control of the player.
Military aircraft shall be displayed using a distinct icon to regular aircraft.
The user shall be able to view the waypoints and speed of military aircraft in the usual way, but not alter them.
The player shall not lose points for military aircraft flying through obstacles, but shall still lose points if the minimum separation constraint is violated between a regular aircraft and a military aircraft.
Military aircraft shall appear less frequently than regular aircraft – an ideal proportion is 1 military aircraft for every 5 regular aircraft appearing.
### 2.5	Fuel consumption ###
The points that the user gains for correctly routing an aircraft to its destination shall be relative to the distance travelled by the aircraft en route to the destination. I.e. if an aircraft travels further en route to its destination, the player shall gain fewer points.
### 2.6	Textured graphics ###
The 2D aerial view shall have a coloured textured background representing a normal aerial photograph.
The aircraft shall be represented by bitmap icons.
The obstacles shall be represented by various bitmap graphics.
### 2.7	Sound ###
Sounds of air traffic control communication shall be played as background noise.
When an event occurs (such as the player gives a command to an aircraft, or one aircraft enters another’s minimum separation radius) a corresponding sound shall be played.