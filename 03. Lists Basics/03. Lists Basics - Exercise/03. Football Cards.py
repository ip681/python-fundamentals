team_a_count = 11
team_b_count = 11
cards_list = input().split(" ")
cards_list = list(dict.fromkeys(cards_list))
game_was_terminated = False
for i in range(len(cards_list)):
    current_player = cards_list[i]
    if current_player[0] == "A":
        team_a_count -= 1
    elif current_player[0] == "B":
        team_b_count -= 1
    if team_a_count < 7 or team_b_count < 7:
        game_was_terminated = True
        break
print(f"Team A - {team_a_count}; Team B - {team_b_count}")
if game_was_terminated:
    print("Game was terminated")


