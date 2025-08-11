# Traits modeled:
# -Growth mindset (continuous learning, resilience)
# -Collaboration (team play: code review, pair/mob programming, shared ownership)
# -Systematic thinking (design first, testing/observability, iterative refinement)

from abc import ABC, abstractmethod

# Product
class DeveloperProfile:
    def __init__(self):
        self.traits = []
        self.team_practices = []

    def add_trait(self, t: str):
        self.traits.append(t)

    def add_practice(self, p: str):
        self.team_practices.append(p)

    def __str__(self):
        traits_str = ", ".join(self.traits) if self.traits else "None"
        practices_str = ", ".join(self.team_practices) if self.team_practices else "None"
        return (f"DeveloperProfile(traits=[{traits_str}]; "
                f"teamPractices=[{practices_str}])")

# Interface
class Builder(ABC):
    @abstractmethod
    def reset(self): ...
    @abstractmethod
    def addGrowthMindset(self): ...
    @abstractmethod
    def addCollaboration(self): ...
    @abstractmethod
    def addSystematicThinking(self): ...
    @abstractmethod
    def addTeamPractices(self): ...
    @abstractmethod
    def getResult(self) -> DeveloperProfile: ...

# Concrete Builder
class DeveloperProfileBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.profile = DeveloperProfile()
        self.steps = ["reset()"]

    def addGrowthMindset(self):
        self.profile.add_trait("Growth Mindset")
        self.steps.append("addGrowthMindset()")

    def addCollaboration(self):
        self.profile.add_trait("Collaboration")
        self.steps.append("addCollaboration()")

    def addSystematicThinking(self):
        self.profile.add_trait("Systematic Thinking")
        self.steps.append("addSystematicThinking()")

    def addTeamPractices(self):
        # concrete examples that reinforce teamwork effectiveness
        for practice in ("Code Reviews", "Pair Programming", "Blameless Postmortems"):
            self.profile.add_practice(practice)
        self.steps.append("addTeamPractices()")

    def getResult(self) -> DeveloperProfile:
        self.steps.append("getResult()")
        return self.profile

    def getSteps(self):
        return list(self.steps)

# Director
class Director:
    def constructFullProfile(self, builder: Builder):
        builder.reset()
        builder.addGrowthMindset()
        builder.addCollaboration()
        builder.addSystematicThinking()
        builder.addTeamPractices()
        return builder.getResult()

if __name__ == "__main__":
    print("Program Description:")
    print("This program uses the Builder pattern to assemble a DeveloperProfile\n"
          "highlighting three common traits of effective developers—Growth Mindset,\n"
          "Collaboration, and Systematic Thinking—plus concrete team practices.")

    director = Director()
    builder = DeveloperProfileBuilder()
    profile = director.constructFullProfile(builder)

    steps = builder.getSteps()
    print("\nImportant Steps (in order):")
    for i, s in enumerate(steps, start=1):
        print(f"{i}. {s}")
    print(f"\nNumber of Steps: {len(steps)}")

    print("\nResulting Profile:")
    print(profile)
