# Group-Organizer

Group-Organizer is a Python program designed to organize individuals from an Excel sheet into groups with an equal number of male and female members (if possible). It ensures a balanced distribution of genders across the groups and saves the grouped data into a new Excel file.

## Features

- **Randomized Grouping**: Randomly shuffles individuals to ensure unbiased group formation.
- **Gender Balancing**: Attempts to balance the number of male and female members in each group.
- **Customizable Groups**: User-defined number of groups to accommodate different needs.
- **Excel Output**: Outputs the grouped data into a well-structured Excel file.

## Installation

### Prerequisites

- Python 3.x
- Pandas library

### Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/Jibin-Gigi/Group-Organizer.git
   ```

2. **Navigate to the Project Directory**

   ```sh
   cd Group-Organizer
   ```

3. **Install Dependencies**

   Ensure you have `pip` installed. Then run:

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Program**

   Execute the script with:

   ```sh
   python main.py
   ```

## Usage

1. **Prepare Your Excel File**

   - The input Excel file should contain a sheet with individual data, including a "Gender" column.
   - Ensure the sheet name matches the one specified in the code (default is `Sheet1`).

2. **Run the Script**

   - After running `main.py`, enter the number of groups you want to create when prompted.

3. **Output**

   - The program generates an Excel file named `output.xlsx`, containing separate sheets for each group with balanced gender representation, if possible.

## Example

1. **Input File**: An Excel sheet with columns like Name, Gender, Contact Number, etc.
2. **Output File**: `output.xlsx` with sheets named `Group 1`, `Group 2`, etc., containing the grouped individuals.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
