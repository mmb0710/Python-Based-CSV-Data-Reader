# DatasetVisualizer.py

# Author: Meet Maheta

import matplotlib
matplotlib.use('TkAgg')

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as e:
    print(f"Error importing module: {e}")
    print("Please ensure you have installed pandas and matplotlib.")
    exit(1)

class DatasetVisualizer:
    """
    This class provides functionality to load a dataset from a CSV file, 
    allow the user to select a column, and visualize the data in a vertical bar chart.
    """

    def __init__(self, file_path):
        """
        Initialize the DatasetVisualizer with the file path.
        Load the dataset.
        """
        self.file_path = file_path
        self.df = self.load_dataset()

    def load_dataset(self): 

        """
        Load the dataset from a CSV file.
        Return the DataFrame.
        """
        try:
            df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Error: The file at '{self.file_path}' was not found.")
            exit(1)
        return df

    def parse_dataset(self, column_name): 
        """
        Parse the dataset to get value counts of the selected column.
        Return the data as a Series.
        """
        if column_name not in self.df.columns:
            print(f"Error: The column '{column_name}' is not found in the dataset.")
            exit(1)
        data = self.df[column_name].value_counts()
        return data

    def create_vertical_bar_chart(self, data, title, xlabel, ylabel): 
        """
        Create and display a vertical bar chart.
        """
        fig, ax = plt.subplots(figsize=(24, 12)) 
        data.plot(kind='bar', ax=ax)
        ax.set_title(f"{title} - Meet Maheta")
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.xticks(rotation=90, ha='right')  

        n = max(1, len(data) // 50)
        [label.set_visible(False) for (i, label) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]

        plt.tight_layout()  
        plt.show()

    def user_select_column(self): 
        """
        Display available columns and prompt the user to select one.
        Return the selected column name.
        """
        print("Available columns:")
        for i, column in enumerate(self.df.columns):
            print(f"{i + 1}. {column}")
        while True:
            try:
                column_index = int(input("Select a column number to visualize (or enter 0 to exit): ")) - 1
                if column_index == -1:
                    return None
                if 0 <= column_index < len(self.df.columns):
                    return self.df.columns[column_index]
                else:
                    print("Invalid column number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def main_menu(self): 
        """
        Display the main menu and handle user choices.
        """
        while True:
            print("\n--- Main Menu (Meet Maheta) ---")
            print("1. Visualize a column")
            print("0. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    column_name = self.user_select_column()
                    if column_name is None:
                        print("Exiting the program. Goodbye!")
                        break
                    data = self.parse_dataset(column_name)
                    self.create_vertical_bar_chart(data, f"Vertical Bar Chart of {column_name}", column_name, "Frequency")
                elif choice == 0:
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def main():
    """
    Main function to create an instance of DatasetVisualizer and start the main menu.
    """
    file_path = '/Users/mmb0702/Desktop/PLRP/Phase 4/Practical Project Part 4/CST8333_Project4_By_Meet_Maheta/Traffic_Volumes_-_Provincial_Highway_System.csv' 
    visualizer = DatasetVisualizer(file_path)
    visualizer.main_menu()

if __name__ == "__main__":
    main()
