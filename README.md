# LP Cost Optimization Project

## Project Overview

The **Lp-Cost-Optimization-Project** is a cost optimization tool designed to support partnerships between companies and EMBRAPII (Brazilian Agency for Research and Industrial Innovation) following the guidelines for conventional partnerships. The goal is to minimize the total project cost (CT) by efficiently distributing resources across cost units, human resources, and support rates, while accounting for EMBRAPII’s funding contribution. Once the core structure is built, the project aims to expand support to other types of partnerships.

## Features

- Calculates the total project cost (CT) based on user-defined cost units and human resource allocations.
- Incorporates operational support and infrastructure rates to provide an adjusted project cost.
- Includes EMBRAPII funding calculation, allowing for up to 1/3 of the total cost to be covered by non-reimbursable funding.
- Displays exact EMBRAPII funding percentage over the total project cost.

## Usage

### Prerequisites

To run this project, you'll need:

- Python 3.x
- `pulp` library for linear programming (`pip install pulp`)

## Running the Program

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Lp-Cost-Optimization-Project.git
   cd Lp-Cost-
2. **Run the main script**:
    ```bash
    python main.py

## Project Structure 
    ```bash
    Lp-Cost-Optimization-Project/
    ├── main.py              # Main script for running the cost optimization
    ├── README.md            # Project documentation
    └── requirements.txt     # List of dependencies

## Example

When running the program, you will be prompted to enter each cost unit value and the human resources economic value (RHE). The program will calculate the total cost (CT), adjusted cost, EMBRAPII funding, and funding percentage.

## Future Goals

Expand to support other types of EMBRAPII partnerships.
Implement a user interface for easier input and display of cost optimization results.
Add more advanced cost modeling options.
Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, create a new branch for your feature or bug fix, and submit a pull request.

> **Note**: This project follows EMBRAPII's guidelines for conventional partnerships. For more information, visit the [EMBRAPII website](https://embrapii.org.br/).
