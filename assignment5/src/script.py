
"""
Assignment 5  - Evaluating environmental impact of your exam portfolio
Author: Katrine Munkholm Hygebjerg-Hansen
Elective: Language Analytics, Cultural Data Science spring 2024
Teacher: Ross Deans Kristensen-McLachlan
"""

#Importing neccessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define functions
def read_csv_files():
    """Read CSV files."""
    a1_df = pd.read_csv("in/emissions_A1.csv")
    a2_logreg_df = pd.read_csv("in/emissions_A2logreg.csv")
    a2_mlp_df = pd.read_csv("in/emissions_A2MLP.csv")
    a3_df = pd.read_csv("in/emissions_A3.csv")
    a4_df = pd.read_csv("in/emissions_A4.csv")
    return a1_df, a2_logreg_df, a2_mlp_df, a3_df, a4_df

def calculate_total_emissions(a1_df, a2_logreg_df, a2_mlp_df, a3_df, a4_df):
    """Calculate total emissions for each assignment."""
    total_emissions = {
        "Assignment 1": a1_df["emissions"].sum(),
        "Assignment 2 - logreg": a2_logreg_df["emissions"].sum(),
        "Assignment 2 - mlp": a2_mlp_df["emissions"].sum(),
        "Assignment 3": a3_df["emissions"].sum(),
        "Assignment 4": a4_df["emissions"].sum()
    }
    return total_emissions

def plot_total_emissions(assignments, emissions):
    """Plot total emissions for each assignment."""
    total_emissions_sum = sum(emissions)
    percentages = [emission / total_emissions_sum * 100 for emission in emissions]

    plt.figure(figsize=(10, 8))
    bars = plt.bar(assignments, emissions, color=['skyblue', 'red', 'green', 'royalblue', 'gold'])
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height + 0.0001,
                 f'{emissions[i]:.5f}\n({percentages[i]:.2f}%)', ha='center', va='bottom', fontsize=10)
    plt.title('Total Emissions for Each Assignment', fontsize=14, fontweight='bold')
    plt.xlabel('Assignment')
    plt.ylabel('Total Emissions (CO₂eq)')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout(rect=[0, 0.05, 1, 1])  # Adjust layout to make room for text below bars
    plt.savefig("out/total_emissions.png")

def group_and_plot_task_emissions(a1_df, a2_logreg_df, a2_mlp_df, a3_df, a4_df):
    """Group tasks by name and sum their emissions for each assignment."""
    assignments = {
        "Assignment 1": a1_df,
        "Assignment 2 - logreg": a2_logreg_df,
        "Assignment 2 - mlp": a2_mlp_df,
        "Assignment 3": a3_df,
        "Assignment 4": a4_df
    }
    
    task_emissions = {}
    for assignment_name, df in assignments.items():
        if assignment_name == "Assignment 1":
            task_emissions[assignment_name] = pd.Series({"Total": df["emissions"].sum()})
        else:
            task_emissions[assignment_name] = df.groupby("task_name")["emissions"].sum()
    
    total_emissions_sum = sum([df["emissions"].sum() for df in assignments.values()])
    
    plt.figure(figsize=(12, 8))
    
    for assignment_name, task_emission in task_emissions.items():
        color = 'c' if assignment_name == "Assignment 1" else 'r' if 'logreg' in assignment_name else 'g' if 'mlp' in assignment_name else 'b' if '3' in assignment_name else 'y'
        for i, (task, emission) in enumerate(zip(task_emission.index, task_emission.values)):
            percentage = emission / total_emissions_sum * 100
            plt.stem([task], [emission], markerfmt='o', linefmt=f'{color}-', basefmt=' ', label=assignment_name if i == 0 else None)
            plt.text(task, emission, f'{emission:.5f}\n({percentage:.2f}%)', ha='right' if color != 'red' else 'left', va='bottom', fontsize=10, color=color)
    
    plt.title('Emissions for Each Task in Each Assignment', fontsize=14, fontweight='bold')
    plt.xlabel('Task')
    plt.ylabel('Total Emissions (CO₂eq)')
    plt.xticks(rotation=90)
    plt.yscale('log')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout(rect=[0, 0.05, 1, 1])  
    plt.savefig("out/task_emissions.png")

# Main function to run tasks
def main():
    a1_df, a2_logreg_df, a2_mlp_df, a3_df, a4_df = read_csv_files()
    
    # Print the columns of each DataFrame to inspect the raw data
    print("Assignment 1 columns:", a1_df.columns)
    print("Assignment 2 - logreg columns:", a2_logreg_df.columns)
    print("Assignment 2 - mlp columns:", a2_mlp_df.columns)
    print("Assignment 3 columns:", a3_df.columns)
    print("Assignment 4 columns:", a4_df.columns)
    
    total_emissions = calculate_total_emissions(a1_df, a2_logreg_df, a2_mlp_df, a3_df, a4_df)
    
    # Print the total emissions for each assignment
    print("Total Emissions for Each Assignment (CO₂eq):")
    for assignment, emission in total_emissions.items():
        print(f"{assignment}: {emission:.5f} kg CO₂eq")
    
    assignments = list(total_emissions.keys())
    emissions = list(total_emissions.values())
    plot_total_emissions(assignments, emissions)
    group_and_plot_task_emissions(a1_df, a2_logreg_df, a2_mlp_df, a3_df, a4_df)

if __name__ == "__main__":
    main()
