# BiancaClass for displaying the key waterfall elements
class BiancaClass:
    def __init__(self, communication, planning, modeling, construction, deployment):
        self.communication = communication
        self.planning = planning
        self.modeling = modeling
        self.construction = construction
        self.deployment = deployment
    # function to display
    def display_elements(self):
        print("\nWaterfall Model Key Elements:")
        print(f"1. {self.communication}")
        print(f"2. {self.planning}")
        print(f"3. {self.modeling}")
        print(f"4. {self.construction}")
        print(f"5. {self.deployment}")

# user input
print("Enter the description for each Waterfall model phase (or press Enter to keep the default):")

comm = input("Step 1 [default: Communication]: ") or "Communication"
plan = input("Step 2 [default: Planning]: ") or "Planning"
model = input("Step 3 [default: Modeling]: ") or "Modeling"
construct = input("Step 4 [default: Construction]: ") or "Construction"
deploy = input("Step 5 [default: Deployment]: ") or "Deployment"

# create an object of BiancaClass
waterfall_model = BiancaClass(comm, plan, model, construct, deploy)

# display the formatted output
waterfall_model.display_elements()