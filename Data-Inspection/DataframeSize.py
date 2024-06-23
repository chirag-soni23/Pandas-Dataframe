import pandas as pd
# get dataframe size
data = {
    'player_id': [1, 2, 3, 4],
    'name': ['Virat Kohli', 'Rohit Sharma', 'MS Dhoni', 'Jasprit Bumrah'],
    'age': [34, 36, 42, 30],
    'position': ['Batsman', 'Batsman', 'Wicketkeeper', 'Bowler'],
    'team': ['RCB', 'MI', 'CSK', 'MI']
}

df = pd.DataFrame(data)
# print(df)

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return [players.shape[0], players.shape[1]]

print(getDataframeSize(df))
