
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Santa's Christmas Adventure
## CS110 B1 Final Project  1st Semester, 2024

## Team Members
Jyotirmoy Dasroy
Sanju Chacko

***

## Project Description
This Christmas-inspired 2D present collecter reimagines Pac-Man with a festive twist. 
Players act as santa collecting presents while the Grinch chases santa determined to steal holiday cheer. 
***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. start screen
2. moveable character
3. collision
4. score
5. game over screen

### Classes

GameObject
The GameObject class is the base for all objects in the game. It handles loading images, positioning, and collision detection.
Attributes:
image_file - Path to the object's image.
x, y - Position of the object.
image - Loaded image for display.
rect - Rectangle for position and collision.
Methods:
update_position(x, y) - Changes the object's position.

Santa
The Santa class represents the player's character. It extends GameObject and adds movement.
Attributes:
speed - How fast Santa moves.
Methods:
move(direction) - Moves Santa in a given direction (UP, DOWN, LEFT, or RIGHT), keeping him on screen.

Grinch
The Grinch class represents enemies in the game. It extends GameObject and includes movement properties.
Attributes:
dx, dy - Speed of movement in the x and y directions.
Behavior:
The Grinch image is resized to 50x50 pixels.

Present
The Present class represents collectible items. It extends GameObject and resizes the image.
Behavior:
The Present image is resized to 30x30 pixels.
***

## ATP


| Step | Procedure                          | Expected Results                              |
|------|------------------------------------|-----------------------------------------------|
| 1    | Start the game.                    | The game begins, and Santa is visible.        |
| 2    | Press the UP arrow key.            | Santa moves up.                               |
| 3    | Press the DOWN arrow key.          | Santa moves down.                             |
| 4    | Press the LEFT arrow key.          | Santa moves left.                             |
| 5    | Press the RIGHT arrow key.         | Santa moves right.                            |

| Step | Procedure                          | Expected Results                              |
|------|------------------------------------|-----------------------------------------------|
| 1    | Start the game.                    | The game begins, and presents are visible.    |
| 2    | Move Santa to the position of a present. | Santa collides with the present.        |
| 3    | Verify the present disappears.     | The present is removed from the game world.   |
| 4    | Verify the game registers the collection. | The collection is recorded appropriately.|


| Step | Procedure                          | Expected Results                              |
|------|------------------------------------|-----------------------------------------------|
| 1    | Start the game.                    | The game begins, and Grinches are visible.    |
| 2    | Move Santa into the path of a Grinch. | Santa collides with the Grinch.            |
| 3    | Verify the game behavior.          | A "Game Over" message or similar response appears.|

| Step | Procedure                          | Expected Results                              |
|------|------------------------------------|-----------------------------------------------|
| 1    | Start the game.                    | The game begins, and Grinches are visible.    |
| 2    | Observe Grinch movement.           | Grinches move randomly in the game world.     |
| 3    | Verify movement randomness.        | Grinch movement appears erratic and unpredictable.|

| Step | Procedure                          | Expected Results                              |
|------|------------------------------------|-----------------------------------------------|
| 1    | Start the game.                    | The game begins without any issues.           |
| 2    | Press random keys or invalid keys (e.g., letters, numbers). | The game ignores the invalid input.|
| 3    | Observe if the game crashes or freezes.  | The game continues to run smoothly      |
| 4    | Ensure the game doesn't exhibit unexpected behavior. | The game remains functional, and no errors occur.|
| 5    | Check for any error message.       | If necessary, an appropriate error message is displayed or the input is ignored.|

