# Route Shortest Path

This project implements a solution to find the shortest path between two locations using various algorithms. It provides a user-friendly interface for both text-based and voice-based inputs.

## Features

- **Shortest Path Calculation**: Find the shortest route between source and destination.
- **Voice Command Input**: Users can input source and destination via voice using speech recognition.
- **CSV Input**: The project reads location data from a CSV file that contains source-destination pairs with distances.
- **Multiple Algorithms**: Supports different shortest path algorithms (e.g., Dijkstra's algorithm).
- **Error Handling & Validation**: Ensures that user inputs are valid and provides error messages where needed.
  
## Technologies Used

- Python
- SpeechRecognition (for voice input)
- Google Speech-to-Text (for speech recognition)
- Dijkstra's Algorithm (for shortest path calculation)

## Requirements

1. Python 3.x
2. Libraries:
   - `speechrecognition`
   - `pyaudio`
   - `csv`
   - `heapq` (or other libraries as needed)

You can install the necessary libraries using pip:

```bash
pip install speechrecognition pyaudio




Getting Started

Ensure Python 3.x is installed on your machine.
Install the necessary libraries using pip.
Running the Project
Clone the repository:
git clone https://github.com/KaranDubey400/Route-shortest-path-.git

Navigate to the project directory:
cd Route-shortest-path-

Run the script:

python app.py

Voice Input Usage
To use voice input, run the script and speak the source and destination clearly when prompted.

Example CSV File (cities.csv)
Here is an example format for the cities.csv file:

Copy
Edit
Source,Destination,Distance
Mumbai,Delhi,1400
Delhi,Bangalore,2100
Chennai,Kolkata,1500
Directory Structure
bash
Copy
Edit
/Route-shortest-path
│
├── main.py               # Main script for pathfinding
├── cities.csv            # Sample input file with source, destination, and distance
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
Contributing
Feel free to fork this repository and create pull requests for new features or bug fixes. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
SpeechRecognition library for voice-to-text functionality
Dijkstra's algorithm for finding the shortest path
vbnet
Copy
Edit
