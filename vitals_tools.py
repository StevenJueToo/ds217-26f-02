"""Reusable helpers for summarizing clinic systolic readings."""


def systolic_readings(encounters):
    """compiles the systolic readings from read_encounters into a list"""
    readings = []
    for i in encounters:
        readings.append(i[2])
    return readings

def mean_systolic(readings):
    """gets the mean of systolic readings, if no readings, return None"""
    # TODO: return None when there is nothing to average, then sum() / len().
    if len(readings) != 0:
        return sum(readings)/len(readings)
    else:
        return None


def count_patients(encounters):
    """counts unique patients found in encounters"""
    # TODO: collect the patient IDs and keep only the distinct ones.
    all_patients = []
    for i in encounters:
        all_patients.append(i[0])
    return len(set(all_patients))


def patients_at_or_above(encounters, cutoff):
    """for each patient, check systolic readings if they are at or above cut off"""
    # TODO: keep each patient whose systolic reading is at or above cutoff.

    readings_above_cutoff = []
    for systolic in encounters:
        if systolic[2] >= cutoff:
            readings_above_cutoff.append(systolic[0])
    return list(set(readings_above_cutoff))