def decimal_to_sexagesimal(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes = int((decimal_degrees - degrees) * 60)
    seconds = (decimal_degrees - degrees - minutes / 60) * 3600
    return f"{degrees}h{minutes}m{seconds:.2f}s"

import numpy as np

# Constante de Stefan-Boltzmann (W/m^2K^4)
sigma = 5.67e-8  

# Função para calcular a luminosidade da estrela em termos de luminosidade solar
def calculate_luminosity(stellar_radius, stellar_temperature):
    return 4 * np.pi * (stellar_radius ** 2) * sigma * (stellar_temperature ** 4)

# Function to calculate stellar distance in parsecs
def calculate_stellar_distance(luminosity, insolation_flux):
    return np.sqrt(luminosity / (4 * np.pi * insolation_flux))

def transit_depth(planet_radius, star_radius):
    """
    Calculates the transit depth of an exoplanet.

    Args:
    planet_radius (float): Radius of the planet in Earth radii.
    star_radius (float): Radius of the star in Solar radii.

    Returns:
    float: Transit depth.
    """
    depth = (planet_radius / star_radius) ** 2 * 1e6
    return depth

def impute_random(df, column_name):
    # Calcula quartis inferiores e superiores
    q1 = df[column_name].quantile(0.25)
    q3 = df[column_name].quantile(0.75)
    
    # Calcula a amplitude interquartil
    iqr = q3 - q1
    
    # Calcula os limites para valores dentro do intervalo interquartil
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Filtra os valores não nulos dentro do intervalo interquartil
    non_null_values = df[column_name].loc[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]
    
    # Impute os valores faltantes com valores aleatórios homogêneos
    missing_count = df[column_name].isnull().sum()
    imputed_values = np.random.uniform(q1, q3, missing_count)
    dfx = df.copy()
    # Atualiza os valores faltantes no DataFrame
    dfx.loc[dfx[column_name].isnull(), column_name] = imputed_values
    
    return dfx