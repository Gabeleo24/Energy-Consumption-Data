import pandas as pd

# Data for the table in CSV format
data = {
    "City": [
        "Tokyo", "Shanghai", "Bombay", "Karachi", "Delhi", "New Delhi", "Manila", "Moscow", "Seoul", "São Paulo",
        "Istanbul", "Lagos", "Mexico", "Jakarta", "New York", "Kinshasa", "Cairo", "Lima", "Peking", "London",
        "Bogotá", "Dhaka", "Lahore", "Rio de Janeiro", "Baghdad", "Bangkok", "Bangalore", "Santiago", "Calcutta", "Toronto",
        "Rangoon", "Sydney", "Madras", "Wuhan", "Saint Petersburg", "Chongqing", "Xian", "Chengdu", "Los Angeles", "Alexandria",
        "Tianjin", "Melbourne", "Ahmadabad", "Abidjan", "Kano", "Casablanca", "Hyderabad", "Ibadan", "Singapore", "Ankara",
        "Shenyang", "Riyadh", "Ho Chi Minh City", "Cape Town", "Berlin", "Montreal", "Harbin", "Guangzhou", "Durban", "Madrid",
        "Nanjing", "Kabul", "Pune", "Surat", "Chicago", "Kanpur", "Umm Durman", "Luanda", "Addis Abeba", "Nairobi", "Taiyuan",
        "Jaipur", "Salvador", "Dakar", "Dar es Salaam", "Rome", "Mogadishu", "Jiddah", "Changchun", "Taipei", "Kiev", "Faisalabad",
        "Izmir", "Lakhnau", "Gizeh", "Fortaleza", "Cali", "Surabaya", "Belo Horizonte", "Mashhad", "Nagpur", "Harare", "Brasília",
        "Santo Domingo", "Nagoya", "Aleppo", "Paris", "Jinan", "Tangshan", "Dalian"
    ],
    "Country": [
        "Japan", "China", "India", "Pakistan", "India", "India", "Philippines", "Russia", "South Korea", "Brazil",
        "Turkey", "Nigeria", "Mexico", "Indonesia", "United States", "Congo (Democratic Republic)", "Egypt", "Peru",
        "China", "United Kingdom", "Colombia", "Bangladesh", "Pakistan", "Brazil", "Iraq", "Thailand", "India", "Chile",
        "India", "Canada", "Burma", "Australia", "India", "China", "Russia", "China", "China", "China", "United States",
        "Egypt", "China", "Australia", "India", "Côte d'Ivoire", "Nigeria", "Morocco", "India", "Nigeria", "Singapore",
        "Turkey", "China", "Saudi Arabia", "Vietnam", "South Africa", "Germany", "Canada", "China", "China", "South Africa",
        "Spain", "China", "Afghanistan", "India", "India", "United States", "India", "Sudan", "Angola", "Ethiopia", "Kenya",
        "China", "India", "Brazil", "Senegal", "Tanzania", "Italy", "Somalia", "Saudi Arabia", "China", "Taiwan", "Ukraine",
        "Pakistan", "Turkey", "India", "Egypt", "Brazil", "Colombia", "Indonesia", "Brazil", "Iran", "India", "Zimbabwe",
        "Brazil", "Dominican Republic", "Japan", "Syria", "France", "China", "China", "China"
    ],
    "Regional warming since 1960 (°C / century)": [
        "1.63 ± 0.29", "1.89 ± 0.23", "1.34 ± 0.38", "2.31 ± 0.39", "1.97 ± 0.34", "1.97 ± 0.34", "0.91 ± 0.29",
        "3.47 ± 0.25", "2.16 ± 0.21", "1.89 ± 0.53", "1.71 ± 0.28", "1.63 ± 0.51", "1.17 ± 0.44", "1.47 ± 0.32",
        "2.86 ± 0.23", "1.44 ± 0.46", "1.92 ± 0.20", "1.12 ± 0.56", "2.50 ± 0.35", "2.66 ± 0.23", "1.32 ± 0.21",
        "0.84 ± 0.41", "2.49 ± 0.33", "1.68 ± 0.45", "2.69 ± 0.52", "1.10 ± 0.23", "1.36 ± 0.31", "1.27 ± 0.45",
        "0.98 ± 0.39", "3.06 ± 0.18", "1.06 ± 0.40", "1.92 ± 0.24", "1.32 ± 0.35", "1.56 ± 0.30", "3.05 ± 0.35",
        "1.11 ± 0.25", "2.07 ± 0.48", "1.29 ± 0.27", "2.01 ± 0.29", "1.90 ± 0.21", "2.50 ± 0.35", "1.65 ± 0.29",
        "1.66 ± 0.39", "1.76 ± 0.31", "2.13 ± 0.54", "2.71 ± 0.39", "1.19 ± 0.47", "1.74 ± 0.46", "1.45 ± 0.22",
        "1.49 ± 0.29", "2.38 ± 0.24", "2.68 ± 0.60", "1.07 ± 0.37", "1.39 ± 0.60", "2.74 ± 0.24", "2.95 ± 0.23",
        "2.68 ± 0.38", "0.72 ± 0.20", "1.41 ± 0.34", "2.53 ± 0.30", "1.88 ± 0.28", "2.99 ± 0.48", "1.26 ± 0.39",
        "1.52 ± 0.34", "2.63 ± 0.21", "1.55 ± 0.29", "2.09 ± 0.34", "1.54 ± 0.43", "2.22 ± 0.30", "1.87 ± 0.18",
        "2.48 ± 0.43", "1.85 ± 0.29", "1.93 ± 0.38", "1.98 ± 0.42", "1.99 ± 0.32", "2.66 ± 0.35", "1.99 ± 0.58",
        "2.23 ± 0.72", "2.51 ± 0.42", "1.62 ± 0.24", "3.03 ± 0.24", "2.49 ± 0.33", "1.78 ± 0.19", "1.55 ± 0.29",
        "1.92 ± 0.20", "2.11 ± 0.32", "1.39 ± 0.20", "1.38 ± 0.24", "1.88 ± 0.32", "3.73 ± 0.29", "1.25 ± 0.29",
        "1.59 ± 0.23", "2.05 ± 0.19", "1.76 ± 0.40", "1.62 ± 0.21", "1.69 ± 0.20", "2.84 ± 0.23", "2.23 ± 0.27",
        "2.38 ± 0.34", "2.32 ± 0.34"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_path = "/Users/gabrielmancillas/Documents/GitHub/S-P-500/data/City Selection.csv"
df.to_csv(csv_path, index=False)

csv_path