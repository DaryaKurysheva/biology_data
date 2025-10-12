import requests
import pandas as pd

def get_data(p_url, p_species_component):
    try:
        response = requests.get(
            url=p_url,
            params={"species": p_species_component},
        )
        print(f"Ответ {response.status_code} для {p_species_component} получен")
        return response.json()
    except Exception as e:
        print(f"Ошибка при запросе для {p_species_component}: {e}")
        return None

def work_with_ans_api(p_url, p_species_list):
    data_list = []
    for species in p_species_list:
        data = get_data(p_url, species)
        if data:
            data_list.append(data)
    return data_list

def generate_csv(p_data_list, p_name_csv):
    if not p_data_list:
        print("Нет данных для сохранения.")
        return None
    ans_df = pd.DataFrame(p_data_list)

    int_columns = ['key', 'nubKey', 'taxonKey', 'confidence']
    for col in int_columns:
        if col in ans_df.columns:
            ans_df[col] = pd.to_numeric(ans_df[col], errors='coerce', downcast='integer')

    str_columns = ['scientificName', 'canonicalName', 'rank', 'taxonomicStatus',
                   'kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species', 'matchType', 'status']
    for col in str_columns:
        if col in ans_df.columns:
            ans_df[col] = ans_df[col].astype('string', errors='ignore')

    bool_columns = ['synonym']
    for col in bool_columns:
        if col in ans_df.columns:
            ans_df[col] = ans_df[col].astype('boolean', errors='ignore')

    ans_df.to_csv(p_name_csv, index=False)
    print(f"Данные сохранены в {p_name_csv} ({len(ans_df)} записей).")
    return ans_df



def main():
    url = "https://api.gbif.org/v1/species/match/"
    species_list = [
        "Homo sapiens", "Canis lupus", "Felis catus", "Ursus arctos", "Panthera leo",
        "Elephas maximus", "Delphinus delphis", "Aquila chrysaetos", "Rosa canina",
        "Quercus robur", "Drosophila melanogaster", "Escherichia coli"
    ]
    data_list = work_with_ans_api(url, species_list)
    print("Полученный список записей")
    print(data_list)
    df = generate_csv(data_list, "species.csv")
    print(df.head(5))
    print(df.info())


if __name__ == "__main__":
    main()
