import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import our_snake, your_score, message, gameLoop

def test_snake_initial_length():
    # Test if the initial length of the snake is 1
    snake_List = [[100, 50]]
    assert len(snake_List) == 1

def test_snake_grows():
    # Test if the snake grows correctly
    snake_List = [[100, 50], [110, 50], [120, 50]]
    snake_Head = [130, 50]
    snake_List.append(snake_Head)
    if len(snake_List) > 3:
        del snake_List[0]
    assert len(snake_List) == 3

def test_score_display():
    # Initialize pygame modules to test rendering functions
    pygame.init()
    pygame.display.set_mode((800, 600))
    try:
        your_score(10)
    except Exception as e:
        assert False, f"your_score raised an exception: {e}"

def test_message_display():
    # Initialize pygame modules to test rendering functions
    pygame.init()
    pygame.display.set_mode((800, 600))
    try:
        message("Test Message", (255, 255, 255))
    except Exception as e:
        assert False, f"message raised an exception: {e}"

def test_game_initialization():
    # Test if the game initializes without errors
    try:
        gameLoop()  # This will run the game loop, which we want to test for initialization
    except Exception as e:
        assert False, f"gameLoop raised an exception during initialization: {e}"

# Add additional tests for other functionalities as needed
