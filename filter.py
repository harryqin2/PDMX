import pandas as pd

# Load the metadata
df = pd.read_csv('PDMX.csv')

# Apply our "Gold Standard" filters
# Note: Ensure column names match exactly (they are usually lowercase in PDMX)
filtered_df = df[
    (df['rating'] >= 4) & 
    (df['genres'].str.contains('jazz|classical', case=False, na=False)) &
    (df['is_public_domain'] == True)
].sort_values(by='rating', ascending=False)

# Grab the first 100 as a pilot batch
pilot_batch = filtered_df.head(100)
pilot_batch.to_csv('pilot_targets.csv', index=False)

print(f"Found {len(filtered_df)} total candidates. Pilot batch of 100 saved.")