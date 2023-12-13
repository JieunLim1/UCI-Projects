- The game has 4 controls:

w - move the sprite up
s - move the sprite down
a - move the sprite left
d - move the sprite right
q - quit the game
space - reset the board

- The sprite (i) can move in empty spaces of the board, but cannot pass through walls (+). It can push a single box (!) into an empty or target (o) space, but cannot push more than one at a time. In other words, boxes cannot be pushed into other boxes or walls. Pushing the box right:

- 
The game ends when a win is detected or the user quits the program

Quitting prints the message: "Goodbye"
Winning prints the message: "You Win!"

- General Structure of the Program
When boiled down, most simple games have the same repeated set of actions:

the program provides information about the current game state to the player
the user takes action through input
the program reacts
the program identifies the input
the program updates the game state
repeat forever, or until the user wins or loses
This loop is often referred to as the game loop, and is where the bulk of the game's code lives. Generally, there are things the program must do before the game starts and after it ends:



SAMPLE GAME
+ + + + + + + +
+   .         +
+ i   !   o   +
+       !   o +
+             +
+ + + + + + + +

d (Player moves right)
+ + + + + + + +
+   .         +
+   i !   o   +
+       !   o +
+             +
+ + + + + + + +

d
+ + + + + + + +
+   .         +
+     i ! o   +
+       !   o +
+             +
+ + + + + + + +

d (Player pushes the box onto the target, converting the BOX_NS into BOX_S)
+ + + + + + + +
+   .         +
+       i .   +
+       !   o +
+             +
+ + + + + + + +

d (Player pushes the box off the target, converting BOX_S to BOX_NS, and steps onto the target, converting SPRITE into SPRITE_T)
+ + + + + + + +
+   .         +
+         I ! +
+       !   o +
+             +
+ + + + + + + +

  (Player resets the game)
+ + + + + + + +
+   .         +
+ i   !   o   +
+       !   o +
+             +
+ + + + + + + +

d
+ + + + + + + +
+   .         +
+   i !   o   +
+       !   o +
+             +
+ + + + + + + +

d
+ + + + + + + +
+   .         +
+     i ! o   +
+       !   o +
+             +
+ + + + + + + +

w
+ + + + + + + +
+   . i       +
+       ! o   +
+       !   o +
+             +
+ + + + + + + +

d
+ + + + + + + +
+   .   i     +
+       ! o   +
+       !   o +
+             +
+ + + + + + + +

s (Player attempts to push more than one box)
+ + + + + + + +
+   .   i     +
+       ! o   +
+       !   o +
+             +
+ + + + + + + +

a
+ + + + + + + +
+   . i       +
+       ! o   +
+       !   o +
+             +
+ + + + + + + +

s
+ + + + + + + +
+   .         +
+     i ! o   +
+       !   o +
+             +
+ + + + + + + +

d
+ + + + + + + +
+   .         +
+       i .   +
+       !   o +
+             +
+ + + + + + + +

a
+ + + + + + + +
+   .         +
+     i   .   +
+       !   o +
+             +
+ + + + + + + +

s
+ + + + + + + +
+   .         +
+         .   +
+     i !   o +
+             +
+ + + + + + + +

d
+ + + + + + + +
+   .         +
+         .   +
+       i ! o +
+             +
+ + + + + + + +

d  (Player satisfies last box, satisfying the win condition and terminating the game)
+ + + + + + + +
+   .         +
+         .   +
+         i . +
+             +
+ + + + + + + +
You Win!





*Test Case 15
Test case #15 tests your project using a more intricate game board. 
It is common for students to successfully pass test cases 1-14, which utilize a simpler board, 
but encounter difficulties with test case #15, which may expose unforeseen scenarios. 
The game board utilized for this test case is available in the game_settings.py file, 
specifically labeled as TEST_CASE_15_BOARD. If you encounter challenges with test case #15, 
we recommend replacing your current game board with TEST_CASE_15_BOARD and run with the provided 
input below. With the input below, your game should end as the inputs lead to a win. 
This approach can aid in identifying and resolving any errors in your project.

addddwdsaasd dwddssssasdwwwwaaadsdsdssaasaawwsd