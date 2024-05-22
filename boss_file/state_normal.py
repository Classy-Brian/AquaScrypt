from boss_file import boss_state, state_power

class StateNormal(boss_state.BossState):

    def plays(self, boss):
        """
        Returns a string describing
        the boss reaction.
        """
        return "\n The Boss is attacking you, you're slowly falling apart\nhave you giving up?"

    def mechanic(self, boss):
        """
        Returns a string describing
        the boss reaction.
        """
        boss.change_state(state_power.StatePower())
        return "\nYou made the Boss angry, its now using its power on you"
    
        
