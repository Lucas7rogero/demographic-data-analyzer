import pandas as pd


def calculate_demographic_data(print_data=True):
    # le o arquivo csv
    df = pd.read_csv("adult.data.csv")

    # conta as pessoas por raça
    race_count = df["race"].value_counts()

    # media de idade dos homens com uma casa decimal
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # % de pessoas com bacharelado com uma casa decimal
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # separa por nivel de educacao
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # % de ricos por nivel de educacao
    higher_education_rich = round(
        (higher_education["salary"] == ">50K").mean() * 100, 1
    )
    lower_education_rich = round(
        (lower_education["salary"] == ">50K").mean() * 100, 1
    )

    # menor carga horaria semanal
    min_work_hours = df["hours-per-week"].min()

    # % de ricos entre os que trabalham menos horas
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((num_min_workers["salary"] == ">50K").mean() * 100, 1)

    # pais com maior % de ricos
    country_rich_pct = (
        df.groupby("native-country")["salary"]
        .apply(lambda s: (s == ">50K").mean() * 100)
        .dropna()
    )
    highest_earning_country = country_rich_pct.idxmax()
    highest_earning_country_percentage = round(country_rich_pct.max(), 1)

    # ocupacao de ricos na Índia
    india_rich = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
