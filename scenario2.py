from beamngpy import BeamNGpy, Scenario, Vehicle

# Instantiate BeamNGpy instance
bng = BeamNGpy('localhost', 64256, home=r'C:\Users\ziggy\Desktop\beamng\BeamNG.tech.v0.31.2.0', user=r'C:\Users\ziggy\Desktop\beamng\BeamNG.tech.v0.31.2.0\tech\max')

# Launch BeamNG.tech
bng.open()

# Create a scenario in west_coast_usa
scenario = Scenario('west_coast_usa', 'RISE and TOBII Scenario 01')

# Create the first vehicle (ETK800)
vehicle1 = Vehicle('ego_vehicle', model='etk800', license='RISE')
# Add the first vehicle to the scenario
scenario.add_vehicle(vehicle1, pos=(-717, 101, 118), rot_quat=(0, 0, 0.3826834, 0.9238795))

# Create a second vehicle (for example, a Pickup)
vehicle2 = Vehicle('npc_vehicle', model='pickup', license='MEETUP')
# Add the second vehicle to the scenario at a different position
scenario.add_vehicle(vehicle2, pos=(-720, 150, 118), rot_quat=(0, 0, -0.3826834, 0.9238795))

# Place files defining our scenario for the simulator to read
scenario.make(bng)

# Load and start our scenario
bng.scenario.load(scenario)
bng.scenario.start()

# Set the AI mode for both vehicles
vehicle1.ai.set_mode('span')
vehicle2.ai.set_mode('span')

# Optionally, you can define waypoints or specific behaviors for each vehicle
# For example, making them drive to a specific location or follow a route

input('Hit enter when done...')
