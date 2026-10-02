#!/usr/bin/env python3
"""Summarize one week of clinic encounters and save the two report files."""

from pathlib import Path

from vitals_tools import (
    count_patients,
    mean_systolic,
    patients_at_or_above,
    systolic_readings,
)


DATA_PATH = Path("data") / "clinic_encounters.csv"
OUTPUT_DIR = Path("output")

def read_encounters(data_path):
    """
    Read through the CSV file, skipping the header.
    Keep rows with 3 fields, an integer systolic value, and a realistic value.
    Print a message for every skipped row.
    Return the encounters list and number of skipped rows.
    """

    encounters = []
    skipped = 0
    
    with open(data_path, "r") as file:
        lines = file.readlines()

        for line in lines[1:]:
            fields = line.strip().split(",")

            #check if fields is 3
            if len(fields) != 3:
                skipped += 1
                print(f"Skipped row:{fields}")

                continue
            else:
            #check if third value is integer
                try:
                    systolic = int(fields[2])
                except ValueError:
                    skipped += 1
                    print("Not integer, skipping")
                    continue

                #check if systolic is okay range
                if systolic < 60 or systolic > 250:
                    skipped += 1
                    print(f"Skipping out of range systolic value: {systolic}.")
                    continue
                else:
                    encounters.append((fields[0], fields[1], systolic))
        return encounters, skipped



def main():
    #TODO: describe the two artifacts this writes.
    """
    read_ecounters() give us the rows of info in the csv file given they meet the 3 requirements
     and tells us how many csv rows were skipped
    
    """
    encounters, skipped = read_encounters(DATA_PATH)


    # TODO: build the six report lines and write them to output/vitals_report.txt.
    # TODO: read the file back and print it, so you can see what was saved.
    # TODO: choose your follow-up cutoff, then write output/followup_list.txt
    #       with the Cutoff line, the Reason line, and one patient ID per line.
    readings = systolic_readings(encounters)

    with open(OUTPUT_DIR / "vitals_report.txt", "w") as file:
        file.write(f"Usable encounters: {len(encounters)}\n")
        file.write(f"Skipped rows: {skipped}\n")
        file.write(f"Patients seen: {count_patients(encounters)}\n")
        file.write(f"Mean systolic: {mean_systolic(readings):.1f} mmHg\n")
        file.write(f"Highest systolic: {max(readings)} mmHg\n")
        file.write(f"Lowest systolic: {min(readings)} mmHg\n")

    cutoff = 165
    reason = "The clinic has a limited number of callbacks. We should prioritize those with higher systolic readings."
    with open(OUTPUT_DIR / "followup_list.txt", "w") as file:
        file.write(f"Cutoff: {cutoff} mmHg\n")
        file.write(f"Reason: {reason}\n")
        
        followup_patients = patients_at_or_above(encounters, cutoff)

        for patient in followup_patients:
            file.write(f"{patient}\n")

if __name__ == "__main__":
    main()

