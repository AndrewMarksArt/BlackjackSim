# Blackjack Simulator

Blackjack Simulator is a Python-based simulation tool for testing out different blackjack strategies. Blackjack is a popular casino game where players aim to get cards totaling as close to 21 as possible without going over. With this simulator, you can explore different strategies in the game and gain insights into their performance over time.

## Installation

The project requires Python 3.10 or higher. Additional dependencies include pandas, numpy, and matplotlib. After cloning the repository, install the required packages with:

pip install -r requirements.txt


## Usage

You can run the simulation using the main.py script. The script allows you to configure various parameters for the simulation, such as the number of decks used, the penetration point, the betting strategy, and the play strategy. For example:

python main.py --decks=6 --penetration=0.75 --betting=basic --play=basic

This command will run a simulation using 6 decks, a penetration point of 75% (the point at which the shoe ends and is reshuffled), and both basic betting and play strategies.

The output of the simulation includes metrics such as the total winnings/losses, the number of hands won/lost, and more. This can help you understand how different strategies perform under different conditions.

## Contributing

Currently, the project is not open for contributions. Please check back in the future.

## License

This project is licensed under the Apache License 2.0. See the 'LICENSE' file for more information.

## Project Status

This project is in the early stages of development, and I are actively working on adding more features and capabilities. Stay tuned for updates!

