import streamlit as st

# AWG to mm² mapping (approximate values)
awg_to_mm2_table = {
    0: 53.5,
    1: 42.4,
    2: 33.6,
    3: 26.7,
    4: 21.1,
    5: 16.8,
    6: 13.3,
    7: 10.5,
    8: 8.37,
    9: 6.63,
    10: 5.26,
    11: 4.17,
    12: 3.31,
    13: 2.63,
    14: 2.08,
    15: 1.65,
    16: 1.31,
    17: 1.04,
    18: 0.823,
    19: 0.653,
    20: 0.518,
    21: 0.412,
    22: 0.326,
    23: 0.258,
    24: 0.205,
    25: 0.162,
    26: 0.129,
    27: 0.102,
    28: 0.081,
    29: 0.064,
    30: 0.051,
    31: 0.040,
    32: 0.032,
    33: 0.025,
    34: 0.020,
    35: 0.016,
    36: 0.013,
    37: 0.010,
    38: 0.008,
    39: 0.006,
    40: 0.005
}

def awg_to_mm2(awg):
    return awg_to_mm2_table.get(awg, "Invalid AWG")

def mm2_to_awg(mm2):
    closest_awg = min(awg_to_mm2_table, key=lambda x: abs(awg_to_mm2_table[x] - mm2))
    return closest_awg

# Streamlit UI
st.title("🔁 Cable Size Converter")

conversion_type = st.radio("Choose conversion type:", ["AWG ➜ mm²", "mm² ➜ AWG"])

if conversion_type == "AWG ➜ mm²":
    awg_input = st.number_input("Enter AWG value (0 to 40)", min_value=0, max_value=40, value=10)
    mm2_result = awg_to_mm2(awg_input)
    st.success(f"{awg_input} AWG is approximately {mm2_result} mm²")

elif conversion_type == "mm² ➜ AWG":
    mm2_input = st.number_input("Enter Cable Size in mm²", min_value=0.001, value=2.5)
    awg_result = mm2_to_awg(mm2_input)
    approx_mm2 = awg_to_mm2(awg_result)
    st.success(f"{mm2_input} mm² is approximately AWG {awg_result} (≈ {approx_mm2} mm²)")
