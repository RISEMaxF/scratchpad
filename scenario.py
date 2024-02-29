from beamngpy import BeamNGpy, Scenario, Vehicle, setup_logging
from beamngpy.sensors import Electrics
from beamngpy.beamngcommon import BNGValueError

def main():
    # Initialize BeamNGpy instance to interface with the BeamNG.tech game
    beamng = BeamNGpy('localhost', 64256)
    scenario = Scenario('east_coast_usa', 'RISE TOBII inToxEye')

    # Create a vehicle for the player
    vehicle = Vehicle('ego_vehicle', model='etk800', license_plate='RISE')
    vehicle.attach_sensor('electrics', Electrics())

    # Set the spawn point for the player's vehicle
    scenario.add_vehicle(vehicle, pos=(-717, 101, 118), rot=(0, 0, 45))

    # Define AI vehicle and its behavior
    ai_vehicle = Vehicle('ai_vehicle', model='etk800', license_plate='RISE')
    scenario.add_vehicle(ai_vehicle, pos=(-750, 150, 118), rot=(0, 0, -135))  # Adjust pos and rot for oncoming direction

    # Create the scenario
    scenario.make(beamng)

    # Load and start BeamNG.tech
    bng = beamng.open(launch=True)
    bng.load_scenario(scenario)
    bng.start_scenario()

    # Set AI vehicle to drive according to traffic rules
    try:
        bng.set_ai_mode(ai_vehicle, mode='span', target='ego_vehicle')
        bng.ai_drive_in_lane(ai_vehicle, True)
        bng.ai_set_speed(ai_vehicle, speed=16, mode='limit')  # Speed in m/s. Adjust as necessary.
    except BNGValueError as e:
        print(f"Error setting AI behavior: {e}")

    # Keep the script running until you manually stop it, so you can interact with the scenario
    input("Press Enter to end the scenario and close BeamNG.tech...")

    bng.close()

if __name__ == "__main__":
    setup_logging()
    main()
