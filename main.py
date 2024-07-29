import pandas as pd


def main():
    
    df = pd.read_excel('Google Launchpad.xlsx', sheet_name='Sheet1')
    df = df.sample(frac=1).reset_index(drop=True)
    df['Your contact number'] = df['Your contact number'].astype(str)
    
    
    no_of_groups = int(input('Enter the number of groups: '))

    
    male_df = df[df['Gender'] == 'Male']
    female_df = df[df['Gender'] == 'Female']

    
    males_per_group = len(male_df) // no_of_groups
    females_per_group = len(female_df) // no_of_groups

    
    remaining_male = len(male_df) % no_of_groups
    remaining_female = len(female_df) % no_of_groups

    
    groups = []
    male_start_index = female_start_index = 0
    for i in range(no_of_groups):
        male_end_index = male_start_index + males_per_group
        female_end_index = female_start_index + females_per_group

        if i < remaining_male:
            male_end_index += 1  
        if i < remaining_female:
            female_end_index += 1

        
        group = pd.concat([male_df.iloc[male_start_index:male_end_index], 
                           female_df.iloc[female_start_index:female_end_index]]) 
        groups.append(group)

        male_start_index = male_end_index
        female_start_index = female_end_index
    
    
    with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:
        for indx, group in enumerate(groups):
            group.to_excel(writer, sheet_name=f"Group {indx + 1}", index=False)


if __name__ == "__main__":
    main()
