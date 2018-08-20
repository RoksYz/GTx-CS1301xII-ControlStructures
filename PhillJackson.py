def is_a_contender(test_team_name,test_wins,test_losses):
    if test_wins >= 40 and test_losses < 20:
        return "The {} are a contender!".format(test_team_name)
    elif test_wins < 40 and test_losses >= 20:
        return "The {} are not a contender!".format(test_team_name)
    else:
        return "The {} might be a contender!".format(test_team_name)

test_team_name = "Hawks"
test_wins = 18
test_losses = 40

print(is_a_contender(test_team_name, test_wins, test_losses))
