import pandas as pd
import tobii_research as tr
import winsound
import time

# Function to play the start and end beeps
def play_beeps(start=True):
    if start:
        winsound.Beep(500, 500)  # Lower pitch beep for start
        time.sleep(0.5)
        winsound.Beep(700, 500)  # Higher pitch beep for start
    else:
        winsound.Beep(700, 500)  # Higher pitch beep for end
        time.sleep(0.5)
        winsound.Beep(500, 500)  # Lower pitch beep for end

# Function to record eye tracking data
def record_eye_data(duration=10):
    # Find and connect to the eye tracker
    found_eyetrackers = tr.find_all_eyetrackers()
    if not found_eyetrackers:
        print("No eye tracker found.")
        return
    eye_tracker = found_eyetrackers[0]
    print(f"Connected to {eye_tracker.model} with serial number {eye_tracker.serial_number}")

    # Initialize list to store data
    data = []

    # Callback function to capture data
    def gaze_data_callback(gaze_data):
        # Extract relevant information from gaze data
        timestamp = gaze_data['system_time_stamp']
        left_gaze_point = gaze_data['left_gaze_point_on_display_area']
        right_gaze_point = gaze_data['right_gaze_point_on_display_area']
        # Append to data list
        data.append([timestamp, left_gaze_point, right_gaze_point])

    # Subscribe to gaze data
    eye_tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

    # Play start beeps
    play_beeps(start=True)

    # Record data for the specified duration
    print(f"Recording for {duration} seconds...")
    time.sleep(duration)

    # Play end beeps
    play_beeps(start=False)

    # Unsubscribe from gaze data
    eye_tracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=['Timestamp', 'LeftGazePoint', 'RightGazePoint'])

    # Save DataFrame to CSV
    csv_filename = 'eye_tracking_data.csv'
    df.to_csv(csv_filename, index=False)
    print(f"Data saved to {csv_filename}")

# Run the eye tracking recording for 10 seconds
record_eye_data(duration=10)
