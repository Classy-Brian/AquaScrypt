from boss_file import boss_state, state_normal

class StatePower(boss_state.BossState):

    def plays(self, boss):
        """
        Returns a string describing
        the boss reaction.
        """
        boss.change_state(state_normal.StateNormal())
        return "\n The Boss is attacking you again, but has loss its power, will it be able to defeat it?"

    def mechanic(self, boss):
        """
        Returns a string describing
        the boss reaction.
        """
        return "\nThe Boss has use its power on you, Now it gonna be hard for you to defeat it."